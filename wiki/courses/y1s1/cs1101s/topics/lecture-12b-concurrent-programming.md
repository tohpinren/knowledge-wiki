---
page_id: "y1s1-cs1101s-lecture-12b-concurrent-programming"
title: "L12B: Concurrent Programming"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Concurrent computing executes multiple computations during overlapping time periods, improving performance, responsiveness, and modular modeling. The Source language uses `concurrent_execute(f1, ..., fn)` to run nullary functions as concurrent threads, but this does not imply parallelism (simultaneous execution on m..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l12b-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l12b-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l12b-view-pdf#section-3"
  - "cs1101s-lecture-lecture-l12b-view-pdf#section-4"
  - "cs1101s-lecture-lecture-l12b-view-pdf#section-5"
topics:
  - "concurrent"
  - "can"
  - "serializers"
  - "threads"
  - "multiple"
  - "synchronization"
  - "execution"
  - "shared"
  - "computing"
  - "executes"
source_count: 1
lecture_number: 12
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# L12B: Concurrent Programming

This page introduces concurrent programming, a paradigm for executing multiple computations during overlapping time periods. It covers the fundamental concepts, explains how to implement concurrency in Source, and delves into mechanisms like serializers, mutexes, and semaphores to manage shared resources and prevent common concurrency issues such as race conditions and deadlocks.

## Introduction to Concurrent Computing

Concurrent computing involves executing several computations *concurrently*, meaning during overlapping time periods, as opposed to *sequentially*, where one computation must complete before the next one starts [source: cs1101s-lecture-lecture-l12b-view-pdf#section-1, cs1101s-lecture-lecture-l12b-view-pdf#section-2, cs1101s-lecture-lecture-l12b-view-pdf#section-5].

### Why Concurrent Computing?
Concurrent computing offers several benefits [source: cs1101s-lecture-lecture-l12b-view-pdf#section-1, cs1101s-lecture-lecture-l12b-view-pdf#section-6]:
*   **Performance**: Complex tasks can be divided into smaller subtasks and executed simultaneously on different processors, potentially improving overall performance.
*   **Responsiveness**: It enables the creation of responsive user interfaces where other tasks can execute independently without blocking the UI.
*   **Abstraction and Modularity**: It allows for a more natural and modular modeling of real-world objects that inherently act concurrently.

### Concurrency in Source
The Source language supports running concurrent threads using the primitive function `concurrent_execute` [source: cs1101s-lecture-lecture-l12b-view-pdf#section-1, cs1101s-lecture-lecture-l12b-view-pdf#section-7].
```javascript
concurrent_execute(f1, f2, ..., fn)
```
*   Each `fᵢ` must be a nullary function that returns `undefined` [source: cs1101s-lecture-lecture-l12b-view-pdf#section-7].
*   The `concurrent_execute` function sets up a separate thread `tᵢ` that executes the body of `fᵢ` [source: cs1101s-lecture-lecture-l12b-view-pdf#section-7].
*   These threads `tᵢ` all run concurrently with the main thread [source: cs1101s-lecture-lecture-l12b-view-pdf#section-7].

**Example 1: Concurrency in Source**
Consider two functions, `thread1` and `thread2`, which each perform `sum_1_to_n(5000)` twice. When run sequentially, `thread1` completes before `thread2` begins. When run concurrently using `concurrent_execute(thread1, thread2)`, the execution times of both threads overlap [source: cs1101s-lecture-lecture-l12b-view-pdf#section-8, cs1101s-lecture-lecture-l12b-view-pdf#section-9].

```javascript
function sum_1_to_n(n) {
    let sum = 0;
    for (let i = 1; i <= n; i = i + 1) { sum = sum + i; }
    return sum;
}

function thread1() {
    display(get_time() - prog_start_tm, "Thread 1 start time:");
    sum_1_to_n(5000);
    display(get_time() - prog_start_tm, "Thread 1 middle time:");
    sum_1_to_n(5000);
    display(get_time() - prog_start_tm, "Thread 1 end time:");
}

function thread2() {
    display(get_time() - prog_start_tm, "Thread 2 start time:");
    sum_1_to_n(5000);
    display(get_time() - prog_start_tm, "Thread 2 middle time:");
    sum_1_to_n(5000);
    display(get_time() - prog_start_tm, "Thread 2 end time:");
}

let prog_start_tm = 0;

// Sequential run
prog_start_tm = get_time();
display("Sequential run:");
thread1(); thread2();

// Concurrent run
prog_start_tm = get_time();
display("Concurrent run:");
concurrent_execute(thread1, thread2);
```

The sample output shows that the "Concurrent run" takes approximately the same total time as the "Sequential run" in this scenario [source: cs1101s-lecture-lecture-l12b-view-pdf#section-10]. This highlights an important distinction.

### Concurrency vs. Parallelism
*   **Concurrency**: Occurs when the execution of multiple tasks *overlaps in time*. This can happen on a single core or processor, where the system switches rapidly between tasks [source: cs1101s-lecture-lecture-l12b-view-pdf#section-10, cs1101s-lecture-lecture-l12b-view-pdf#section-11].
*   **Parallelism**: Occurs when the execution of multiple tasks *occurs simultaneously in time*. This *must* happen on multiple cores or processors [source: cs1101s-lecture-lecture-l12b-view-pdf#section-10, cs1101s-lecture-lecture-l12b-view-pdf#section-11].

Therefore, concurrency does not imply parallelism; a concurrent program might still run on a single processor, with tasks interleaving rather than executing simultaneously [source: cs1101s-lecture-lecture-l12b-view-pdf#section-10].

**Example 2: Interleaving of Threads**
When two threads (`thread_A` and `thread_B`) are executed concurrently, their individual operations (e.g., `display("A1")`, `display("B1")`) can interleave in various ways, leading to different output orders across multiple runs [source: cs1101s-lecture-lecture-l12b-view-pdf#section-12, cs1101s-lecture-lecture-l12b-view-pdf#section-13].

```javascript
function delay(ms) {
    const start_tm = get_time();
    while (get_time() - start_tm < ms) { /* do nothing */ }
}

function thread_A() {
    delay(20 * math_random());
    display("A1");
    delay(20 * math_random());
    display("A2");
    delay(20 * math_random());
    display("A3");
}

function thread_B() {
    delay(20 * math_random());
    display("B1");
    delay(20 * math_random());
    display("B2");
    delay(20 * math_random());
    display("B3");
}

// Concurrent run
concurrent_execute(thread_A, thread_B);
```

### Race Conditions and Correctness
When concurrent threads update a **shared variable**, different interleavings of operations can lead to different results. This situation is known as a **race condition** [source: cs1101s-lecture-lecture-l12b-view-pdf#section-14, cs1101s-lecture-lecture-l12b-view-pdf#section-15].

**Example 3: Interleaving of Threads with Shared Variable**
Consider two threads (`thread_A` and `thread_B`) that both read, increment/decrement, and write to a shared global variable `x` [source: cs1101s-lecture-lecture-l12b-view-pdf#section-14].

```javascript
function delay(ms) {
    const start_tm = get_time();
    while (get_time() - start_tm < ms) { /* do nothing */ }
}

let x = 0; // Shared variable

function thread_A() {
    const s = x;
    const t = s + 1;
    x = t;
}

function thread_B() {
    const s = x;
    const t = s - 1;
    x = t;
}

concurrent_execute(thread_A, thread_B);
delay(200);
display(x, "Final x:");
```
The output `Final x:` can be 0, -1, or 1, depending on the exact timing and interleaving of `thread_A` and `thread_B` operations [source: cs1101s-lecture-lecture-l12b-view-pdf#section-15].

A concurrent program is considered **correct** if it produces the same result as if the threads had run *sequentially in some order* [source: cs1101s-lecture-lecture-l12b-view-pdf#section-16]. It does not require threads to *actually* run sequentially, only that their observable behavior is consistent with some sequential execution. Due to various possible sequential orderings, there may be more than one "correct" result [source: cs1101s-lecture-lecture-l12b-view-pdf#section-16].

## Mechanisms for Controlling Concurrency: Serializers

To ensure correct program behavior by constraining the interleaving of concurrent threads, **synchronization mechanisms** are used [source: cs1101s-lecture-lecture-l12b-view-pdf#section-17]. One such mechanism is the **serializer**.

### What is Serialization?
Serialization works by creating *distinguished sets of functions*. Only one execution of a function within a serialized set is permitted to happen at a time. If a function in the set is already executing, any other thread attempting to execute a function from that same set will be forced to wait until the first execution finishes [source: cs1101s-lecture-lecture-l12b-view-pdf#section-18]. This mechanism is crucial for controlling access to **shared variables** [source: cs1101s-lecture-lecture-l12b-view-pdf#section-18].

### Serializers in Source
Serializers are constructed using the `make_serializer` function. `make_serializer` is not a primitive but is implementable with additional primitives provided by Source §3 Concurrent [source: cs1101s-lecture-lecture-l12b-view-pdf#section-19].
*   A serializer takes a function as an argument and returns a *serialized function* that behaves like the original function [source: cs1101s-lecture-lecture-l12b-view-pdf#section-19].
*   All calls to a *given* serializer (i.e., the same `make_serializer` instance) return serialized functions that belong to the *same set*. This means only one of them can execute at a time [source: cs1101s-lecture-lecture-l12b-view-pdf#section-19].

**Example 4: Using Serializers**
By wrapping the operations on the shared variable `x` from Example 3 with a serializer `s`, we ensure that only one of the lambda functions (which modify `x`) can execute at any given time. This guarantees that `x` will have a predictable final value, either 101 or 121, depending on which serialized function acquires the serializer first [source: cs1101s-lecture-lecture-l12b-view-pdf#section-20, cs1101s-lecture-lecture-l12b-view-pdf#section-21].

```javascript
let x = 10;
const s = make_serializer();

// thread_A becomes s(() => { x = x * x; })
// thread_B becomes s(() => { x = x + 1; })
concurrent_execute(s(() => { x = x * x; }),
                   s(() => { x = x + 1; }));
// Possible final x: 101 (x*x then x+1) or 121 (x+1 then x*x)
```

**Example 4 (revisited): Eliminating Race Conditions**
Applying a serializer `ser` to `thread_A` and `thread_B` functions (from Example 3) guarantees a consistent outcome, resolving the race condition. The output will always be `Final x: 0` in this specific setup, as one thread will complete its full read-modify-write cycle before the other starts [source: cs1101s-lecture-lecture-l12b-view-pdf#section-21].

```javascript
// ... (definitions of delay, make_serializer, thread_A, thread_B)

const ser = make_serializer(); // Create a serializer instance
let x = 0;

// Pass serialized versions of thread_A and thread_B
concurrent_execute(ser(thread_A), ser(thread_B));
delay(200);
display(x, "Final x:"); // Output: Final x: 0 (always)
```

**Example 5: Multiple Serializers for Multiple Shared Resources**
When dealing with multiple shared resources (e.g., `x` and `y`), distinct serializers can be used for each resource. This allows concurrent access to `x` and `y` independently, but operations on `x` will be serialized by `ser_x` and operations on `y` by `ser_y`. In this example, the final values for `x` and `y` are consistently 0 [source: cs1101s-lecture-lecture-l12b-view-pdf#section-22].

```javascript
// ... (definitions of make_serializer, delay)

const ser_x = make_serializer();
const ser_y = make_serializer();

let x = 0;
let y = 0;

function thread_A() {
    ser_y(() => { // Access y first
        const s = y;
        const t = s - 1;
        y = t;
    })();
    ser_x(() => { // Then access x
        const s = x;
        const t = s + 1;
        x = t;
    })();
}

function thread_B() {
    ser_x(() => { // Access x first
        const s = x;
        const t = s - 1;
        x = t;
    })();
    ser_y(() => { // Then access y
        const s = y;
        const t = s + 1;
        y = t;
    })();
}

concurrent_execute(thread_A, thread_B);
delay(200);
display(x, "Final x:"); // Output: Final x: 0
display(y, "Final y:"); // Output: Final y: 0
```

### Implementing Serializers with Mutexes
Serializers are often implemented using a more primitive synchronization mechanism called a **mutex** (short for **mutual exclusion**) [source: cs1101s-lecture-lecture-l12b-view-pdf#section-23].

A mutex is an object that supports two operations: `acquire` and `release` [source: cs1101s-lecture-lecture-l12b-view-pdf#section-23]. Once a mutex has been acquired by a thread, no other `acquire` operations on that mutex can proceed until the mutex is released by the acquiring thread [source: cs1101s-lecture-lecture-l12b-view-pdf#section-23]. In our implementation, each serializer has an associated mutex [source: cs1101s-lecture-lecture-l12b-view-pdf#section-23].

The `make_serializer` function in Source can be implemented as follows [source: cs1101s-lecture-lecture-l12b-view-pdf#section-24]:
```javascript
function make_serializer() {
    const mutex = make_mutex(); // Each serializer gets its own mutex
    return f => { // Returns a serialized version of function f
        function serialized_f() {
            mutex("acquire"); // Acquire the mutex before executing f
            const val = f();  // Execute the original function f
            mutex("release"); // Release the mutex after f completes
            return val;
        }
        return serialized_f;
    };
}
```

### Implementing Mutexes
Mutexes themselves can be implemented using primitive atomic functions `clear` and `test_and_set` provided in Source §3 Concurrent [source: cs1101s-lecture-lecture-l12b-view-pdf#section-25, cs1101s-lecture-lecture-l12b-view-pdf#section-26]. These functions are performed **atomically**, meaning without interruption [source: cs1101s-lecture-lecture-l12b-view-pdf#section-26].

*   `test_and_set(cell)`:
    *   If `head(cell)` is `true`, it returns `true` (meaning the mutex is locked).
    *   If `head(cell)` is `false`, it sets `head(cell)` to `true` and returns `false` (meaning the mutex was successfully acquired).
*   `clear(cell)`: Sets `head(cell)` to `false` (meaning the mutex is released).

The `make_mutex` function implementation [source: cs1101s-lecture-lecture-l12b-view-pdf#section-25]:
```javascript
function make_mutex() {
    const cell = list(false); // A list representing the mutex state (false = unlocked, true = locked)
    function the_mutex(m) {
        return m === "acquire"
               ? test_and_set(cell)
                 ? the_mutex("acquire") // If already locked, retry acquiring (spin-lock)
                 : true                  // Successfully acquired
               : m === "release"
               ? clear(cell)             // Release the mutex
               : error(m, "Unknown request -- mutex");
    }
    return the_mutex;
}
```

## Applications of Serializers

Serializers are practical for managing concurrent access to shared resources.

**Example 6: Bank Account**
Consider implementing a bank account that supports concurrent withdrawal and deposit transactions, such as a joint account accessed from multiple ATMs [source: cs1101s-lecture-lecture-l12b-view-pdf#section-28].

**Example 6a: Implementation without Serializers (Incorrect)**
Without serialization, concurrent withdrawals and deposits can lead to race conditions. If two threads try to withdraw/deposit simultaneously, the final balance can be inconsistent, as the order of read-modify-write operations is not guaranteed [source: cs1101s-lecture-lecture-l12b-view-pdf#section-29, cs1101s-lecture-lecture-l12b-view-pdf#section-30].

```javascript
// ... (delay function)

function make_account(balance) {
    function withdraw(amount) {
        if (balance >= amount) {
            balance = balance - amount;
            return balance;
        } else {
            return "Insufficient funds";
        }
    }
    function deposit(amount) {
        balance = balance + amount;
        return balance;
    }
    function dispatch(m) {
        return m === "withdraw" ? withdraw
               : m === "deposit" ? deposit
               : m === "balance" ? balance
               : error(m, "Unknown request");
    }
    return dispatch;
}

const my_account = make_account(100); // Initial balance 100

function thread_A() {
    my_account("withdraw")(50); // 100 - 50 = 50
    my_account("deposit")(100);  // 50 + 100 = 150
}

function thread_B() {
    my_account("withdraw")(50); // 150 - 50 = 100
    my_account("deposit")(100);  // 100 + 100 = 200
}

concurrent_execute(thread_A, thread_B);
delay(200);
display(my_account("balance"), "Final balance:");
```
Outputs can vary (e.g., 100, 150, 200, 250), indicating a race condition [source: cs1101s-lecture-lecture-l12b-view-pdf#section-30]. The expected final balance should be 200.

**Example 6b: Implementation with Serializers (Correct)**
By using a serializer, access to the bank account's internal state (balance) can be controlled, ensuring that transactions are processed atomically and correctly. Each `withdraw` and `deposit` operation is wrapped in a serialized function [source: cs1101s-lecture-lecture-l12b-view-pdf#section-31, cs1101s-lecture-lecture-l12b-view-pdf#section-32].

```javascript
// ... (make_serializer, delay definitions)

function make_account(balance) {
    const protect = make_serializer(); // One serializer for the account
    function withdraw(amount) { /* ... */ } // Same as before
    function deposit(amount) { /* ... */ } // Same as before

    // Wrap withdraw and deposit with the serializer
    const protected_withdraw = protect(withdraw);
    const protected_deposit = protect(deposit);

    function dispatch(m) {
        return m === "withdraw" ? protected_withdraw
               : m === "deposit" ? protected_deposit
               : m === "balance" ? balance
               : error(m, "Unknown request");
    }
    return dispatch;
}

const my_account = make_account(100);

function thread_A() {
    my_account("withdraw")(50);
    my_account("deposit")(100);
}

function thread_B() {
    my_account("withdraw")(50);
    my_account("deposit")(100);
}

concurrent_execute(thread_A, thread_B);
delay(200);
display(my_account("balance"), "Final balance:"); // Output: Final balance: 200 (always)
```
With serializers, the output is consistently `Final balance: 200`, as expected [source: cs1101s-lecture-lecture-l12b-view-pdf#section-32].

## Concurrent Programming for Multiple Shared Resources: Deadlock

When concurrent operations manipulate **multiple shared resources**, new problems can arise, such as **deadlock** [source: cs1101s-lecture-lecture-l12b-view-pdf#section-33, cs1101s-lecture-lecture-l12b-view-pdf#section-34].

**Example 7: Exchanging Account Balances**
Consider a function to `exchange` balances between two bank accounts, which must work concurrently with other withdrawal, deposit, and exchange transactions [source: cs1101s-lecture-lecture-l12b-view-pdf#section-34].

**Example 7a: Incorrect Implementation Leading to Deadlock**
If each account has its own serializer (`serializer1` for `acc1` and `serializer2` for `acc2`), and an `exchange` operation requires acquiring both serializers, a deadlock can occur if threads acquire the serializers in different orders [source: cs1101s-lecture-lecture-l12b-view-pdf#section-35, cs1101s-lecture-lecture-l12b-view-pdf#section-36].

```javascript
// ... (make_serializer, delay, make_account_and_serializer definitions, including individual serializers)

function serialized_exchange(accounts) {
    const account1 = head(accounts);
    const account2 = tail(accounts);
    const serializer1 = account1("serializer"); // Get serializer for acc1
    const serializer2 = account2("serializer"); // Get serializer for acc2

    // This order of acquiring serializers for exchange(acc1, acc2)
    // is serializer1 then serializer2
    serializer1(serializer2(exchange))(accounts); // exchange function is passed
}

const acc1 = make_account_and_serializer(100);
const acc2 = make_account_and_serializer(200);

function thread_A() {
    serialized_exchange(pair(acc1, acc2)); // acc1 then acc2
}

function thread_B() {
    serialized_exchange(pair(acc2, acc1)); // acc2 then acc1 (CHANGED HERE)
}

concurrent_execute(thread_A, thread_B);
delay(200);
display(acc1("balance"), "Acc.1 final balance:");
display(acc2("balance"), "Acc.2 final balance:");
```

In `thread_A`, the `serialized_exchange` function attempts to acquire `acc1`'s serializer, then `acc2`'s. In `thread_B`, the order is reversed: `acc2`'s serializer, then `acc1`'s [source: cs1101s-lecture-lecture-l12b-view-pdf#section-40].

If `thread_A` acquires `acc1`'s mutex and `thread_B` simultaneously acquires `acc2`'s mutex, both threads will then try to acquire the *other* mutex, leading to a **deadlock**. Neither thread can proceed, and the program halts [source: cs1101s-lecture-lecture-l12b-view-pdf#section-41, cs1101s-lecture-lecture-l12b-view-pdf#section-43, cs1101s-lecture-lecture-l12b-view-pdf#section-44]. The system will typically report a "Potential infinite loop detected" error [source: cs1101s-lecture-lecture-l12b-view-pdf#section-41].

### Deadlock Avoidance
To avoid this specific type of deadlock when dealing with multiple resources that each have a serializer (or mutex), a common strategy is to enforce an ordering:
*   Give each account a unique identification (e.g., a number) [source: cs1101s-lecture-lecture-l12b-view-pdf#section-45].
*   Each concurrent thread must then protect (acquire) the **lowest-numbered account first** [source: cs1101s-lecture-lecture-l12b-view-pdf#section-45].

This ensures that all threads attempting to acquire multiple resources will do so in the same consistent order, preventing the circular waiting condition that causes deadlock. More sophisticated deadlock-avoidance techniques exist for complex scenarios, and sometimes deadlock cannot be completely avoided [source: cs1101s-lecture-lecture-l12b-view-pdf#section-45].

## More Synchronization Mechanisms

Beyond serializers and mutexes, other synchronization mechanisms are used to manage concurrent access and coordination [source: cs1101s-lecture-lecture-l12b-view-pdf#section-46, cs1101s-lecture-lecture-l12b-view-pdf#section-47].

### Mutexes
As discussed, a mutex protects a **critical section** of a thread that accesses a **shared resource**. It guarantees **mutually exclusive access** to the shared resource at any given time. Threads that wish to access the protected resource must `acquire` the mutex and `wait` if it's currently held, then `unlock` it when finished [source: cs1101s-lecture-lecture-l12b-view-pdf#section-47].

### Semaphores
A semaphore is a more generalized synchronization mechanism, proposed by Edgar W. Dijkstra in 1965 [source: cs1101s-lecture-lecture-l12b-view-pdf#section-47, cs1101s-lecture-lecture-l12b-view-pdf#section-48].
*   A semaphore `S` contains an **integer value**, initialized to a non-negative value [source: cs1101s-lecture-lecture-l12b-view-pdf#section-49].
*   It provides two **atomic** operations [source: cs1101s-lecture-lecture-l12b-view-pdf#section-49]:
    *   **Down (P or Wait)**:
        1.  If `S <= 0`, the process/thread blocks (goes to sleep).
        2.  Otherwise, decrement `S`.
    *   **Up (V or Signal)**:
        1.  Increment `S`.
        2.  Wakes up one sleeping process/thread, if any.

Semaphores can be implemented using mutexes [source: cs1101s-lecture-lecture-l12b-view-pdf#section-50]:
```javascript
function make_semaphore(val) {
    const val_mutex = make_mutex(); // Mutex to protect the semaphore's internal value
    function semaphore(m) {
        if (m === "up") {
            val_mutex("acquire");
            val = val + 1;
            // Wake up one waiting thread if any.
            val_mutex("release");
        } else if (m === "down") {
            val_mutex("acquire");
            while (val <= 0) { // If value is 0 or less, release mutex and "sleep"
                val_mutex("release");
                // Put thread to sleep. (This would involve OS primitives)
                val_mutex("acquire"); // Re-acquire to check condition again
            }
            val = val - 1;
            val_mutex("release");
        } else {
            error(m, "Unknown request -- semaphore");
        }
    }
    return semaphore;
}
```

## Classical Synchronization Problems

Several classical problems illustrate the challenges and solutions in concurrent programming using synchronization mechanisms [source: cs1101s-lecture-lecture-l12b-view-pdf#section-51, cs1101s-lecture-lecture-l12b-view-pdf#section-52].

### The Producers-Consumers Problem
**Problem Specification**:
Threads share a **bounded circular buffer (array)** of size `N`.
*   **Producers** produce items and insert them into the buffer. They can only do so when the buffer is **not full** (< `N` items) [source: cs1101s-lecture-lecture-l12b-view-pdf#section-53].
*   **Consumers** remove items from the buffer. They can only do so when the buffer is **not empty** (> 0 items) [source: cs1101s-lecture-lecture-l12b-view-pdf#section-53].

**A Solution using Semaphores**:
This problem can be solved using three semaphores [source: cs1101s-lecture-lecture-l12b-view-pdf#section-54]:
*   `mutex`: (initialized to 1) for mutual exclusion access to the buffer itself.
*   `not_full`: (initialized to `N`) to count empty slots, blocking producers if the buffer is full.
*   `not_empty`: (initialized to 0) to count filled slots, blocking consumers if the buffer is empty.

```javascript
const N = ...;         // Buffer size
const buffer = [];     // The circular buffer
let count = 0;
let in_pos = 0;
let out_pos = 0;

const mutex = make_semaphore(1);       // Controls access to buffer
const not_full = make_semaphore(N);    // Counts empty slots
const not_empty = make_semaphore(0);   // Counts filled slots

function producer() {
    while (true) {
        const item = produce_item(...);
        not_full("down");   // Decrement empty slots; wait if buffer is full
        mutex("down");      // Acquire mutex for buffer access
        buffer[in_pos] = item;
        in_pos = (in_pos + 1) % N;
        count = count + 1;
        mutex("up");        // Release mutex
        not_empty("up");    // Increment filled slots; potentially wake a consumer
    }
}

function consumer() {
    while (true) {
        not_empty("down");  // Decrement filled slots; wait if buffer is empty
        mutex("down");      // Acquire mutex for buffer access
        const item = buffer[out_pos];
        out_pos = (out_pos + 1) % N;
        count = count - 1;
        mutex("up");        // Release mutex
        not_full("up");     // Increment empty slots; potentially wake a producer
        consume_item(item);
    }
}
```

### The Readers-Writers Problem
**Problem Specification**:
Threads share a data structure `D` [source: cs1101s-lecture-lecture-l12b-view-pdf#section-55].
*   **Readers** retrieve information from `D`. Multiple readers can access `D` concurrently [source: cs1101s-lecture-lecture-l12b-view-pdf#section-55].
*   **Writers** modify information in `D`. Each writer must have **exclusive access** to `D` (no other reader or writer can access it simultaneously) [source: cs1101s-lecture-lecture-l12b-view-pdf#section-55].

**A Solution using Semaphores and Mutex**:
This solution prioritizes writers, ensuring that once a writer wants to write, no new readers can start reading, and existing readers finish [source: cs1101s-lecture-lecture-l12b-view-pdf#section-56].
*   `mutex`: (initialized to 1) for mutual exclusion on `num_readers` variable.
*   `room_empty`: (initialized to 1) ensures writers have exclusive access.
*   `num_readers`: a shared variable tracking the number of active readers.

```javascript
const D = make_data_structure(...);
let num_readers = 0;

const mutex = make_semaphore(1);     // Controls access to num_readers
const room_empty = make_semaphore(1); // Ensures exclusive access for writers

function writer() {
    while (true) {
        room_empty("down");    // Wait until no readers/writers are present
        modify_data(D, ...);   // Perform write operation
        room_empty("up");      // Signal that room is empty again
    }
}

function reader() {
    while (true) {
        mutex("down");         // Acquire mutex for num_readers
        num_readers = num_readers + 1;
        if (num_readers === 1) { // If this is the first reader, block writers
            room_empty("down");
        }
        mutex("up");           // Release mutex for num_readers
        read_data(D, ...);     // Perform read operation

        mutex("down");         // Acquire mutex for num_readers
        num_readers = num_readers - 1;
        if (num_readers === 0) { // If this is the last reader, unblock writers
            room_empty("up");
        }
        mutex("up");           // Release mutex for num_readers
    }
}
```

### The Dining Philosophers Problem
**Problem Specification**:
*   Five philosophers are seated around a round table with a big bowl of noodles in the center [source: cs1101s-lecture-lecture-l12b-view-pdf#section-57].
*   Five single chopsticks are placed between each pair of adjacent philosophers [source: cs1101s-lecture-lecture-l12b-view-pdf#section-57].
*   Each philosopher must alternately **think** and **eat** [source: cs1101s-lecture-lecture-l12b-view-pdf#section-57].
*   A philosopher can only eat when they have **both their left and right chopsticks** [source: cs1101s-lecture-lecture-l12b-view-pdf#section-57].
*   Assume an unlimited supply of noodles and unlimited appetite [source: cs1101s-lecture-lecture-l12b-view-pdf#section-57].

**Attempt #1: Simple Grab (Leads to Deadlock)**
If each philosopher tries to pick up their left chopstick, then their right chopstick, a deadlock can occur. If all philosophers simultaneously pick up their left chopstick, no one can pick up their right chopstick (as it's another philosopher's left chopstick), and thus none can eat, leading to an impasse [source: cs1101s-lecture-lecture-l12b-view-pdf#section-58].

```javascript
function philosopher(i) { // i represents the philosopher's index
    while (true) {
        think();
        take_left_chopstick(i);
        take_right_chopstick(i);
        eat();
        put_left_chopstick(i);
        put_right_chopstick(i);
    }
}
```

**Attempt #2: Exclusive Eating (Leads to Starvation)**
Adding a global mutex to ensure only one philosopher can eat at a time prevents deadlock, but introduces another problem: **starvation**. Some philosophers might never get to eat if the mutex is continuously acquired by others [source: cs1101s-lecture-lecture-l12b-view-pdf#section-59].

```javascript
function philosopher(i) {
    while (true) {
        think();
        mutex("acquire"); // Global mutex
        take_left_chopstick(i);
        take_right_chopstick(i);
        eat();
        put_left_chopstick(i);
        put_right_chopstick(i);
        mutex("release");
    }
}
```

Finding a good solution for the Dining Philosophers Problem is a classic exercise in concurrent programming, requiring careful design to avoid both deadlock and starvation [source: cs1101s-lecture-lecture-l12b-view-pdf#section-60].

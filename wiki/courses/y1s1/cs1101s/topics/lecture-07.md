---
page_id: "y1s1-cs1101s-lecture-07"
title: "Lecture 07: Mutable Data"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 07: Mutable Data consolidates the numbered lecture materials for this module. This source, \"L7: Mutable Data,\" outlines course logistics, academic policies, module content, and introduces the concept of statef..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l7-updated-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l7-updated-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l7-updated-view-pdf#section-3"
topics:
  - "data"
  - "assignment"
  - "model"
  - "list"
  - "state"
  - "mutators"
  - "substitution"
  - "mutable"
  - "lecture"
  - "module"
source_count: 1
lecture_number: 7
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 07: Mutable Data

This lecture introduces the concepts of state and mutable data in programming, contrasting them with the functional programming paradigm covered in earlier lectures. It covers the shift to Source §3, which supports assignment and mutable data structures, and discusses the implications for program design and evaluation models [cs1101s-lecture-lecture-l7-updated-view-pdf#section-2, cs1101s-lecture-lecture-l7-updated-view-pdf#section-7, cs1101s-lecture-lecture-l7-updated-view-pdf#section-8].

## Announcements and Policies

### Robotics Missions and Competition
Robotics Missions are currently ongoing, including "Robotic Trials" (opened yesterday, to be graded in Studio S8), "Moving about on Planet Y," "Finding ELDRIC," and "PID Stop" [cs1101s-lecture-lecture-l7-updated-view-pdf#section-3].

The Sumobot Competition is scheduled for October 15, 2022, from 3 PM to 7 PM in COM1-SR1. It features two competitions: Sumobot and Robot Talent Show. Studio sign-ups and rules will be announced next week [cs1101s-lecture-lecture-l7-updated-view-pdf#section-3].

There will be no Forum Hours this week. The winners of "The Choreographer" contest will be presented by Grandmaster Sanka [cs1101s-lecture-lecture-l7-updated-view-pdf#section-4].

### Collaboration and Plagiarism Policy
Students are encouraged to discuss missions and quests with peers but must perform the actual programming themselves. Copying programs from other students or previous batches is strictly prohibited [cs1101s-lecture-lecture-l7-updated-view-pdf#section-5].

The module emphasizes individual learning and skill development. Submitting another person's work as one's own is considered plagiarism, which is an offense punishable by NUS. Offenders will be reported to the disciplinary board, and the offense will be recorded in their official university records [cs1101s-lecture-lecture-l7-updated-view-pdf#section-5].

NUS policy on plagiarism can be found at:
*   [https://www.comp.nus.edu.sg/cug/plagiarism/](https://www.comp.nus.edu.sg/cug/plagiarism/)
*   [https://www.usp.nus.edu.sg/curriculum/plagiarism/](https://www.usp.nus.edu.sg/curriculum/plagiarism/) [cs1101s-lecture-lecture-l7-updated-view-pdf#section-5]

## Module Overview

The CS1101S course is structured into four main units:
*   **Unit 1 — Functions** (Textbook Chapter 1): Focuses on functional abstraction, understanding programs with the substitution model, and applications like runes and curves [cs1101s-lecture-lecture-l7-updated-view-pdf#section-6].
*   **Unit 2 — Data** (Textbook Chapter 2): Covers data structures like pairs, lists, and trees, along with searching and sorting algorithms, and applications such as sound processing [cs1101s-lecture-lecture-l7-updated-view-pdf#section-6].
*   **Unit 3 — State** (Parts of Textbook Chapter 3): Introduced in this lecture, this unit deals with programming using **stateful abstractions** and **mutable data processing**. It includes arrays, loops, searching, sorting of arrays, and reading programs using the [[lecture-08: Lecture 08: Environment Model|environment model]]. Example applications include robotics, image, and video processing [cs1101s-lecture-lecture-l7-updated-view-pdf#section-7].
*   **Unit 4 — Beyond** (Parts of Textbook Chapters 3 and 4): Explores advanced topics such as streams, metalinguistic abstraction, computing with Register Machines, logic programming, and concurrency [cs1101s-lecture-lecture-l7-updated-view-pdf#section-7].

From this lecture onwards, the language used is **Source §3**, which supports stateful programming constructs. Documentation for Source §3 is available at [https://docs.sourceacademy.org/source_3/](https://docs.sourceacademy.org/source_3/). The Source Academy Playground is now set to use Source §3 [cs1101s-lecture-lecture-l7-updated-view-pdf#section-8].

## State (3.1)

### Functional vs. Stateful Programming
Previously, computation has been entirely **functional** [cs1101s-lecture-lecture-l7-updated-view-pdf#section-10]:
*   Given the same arguments, a function always produces the same result.
*   It is **memoryless** or **stateless**, meaning each function call is independent of past or future calls.
*   This makes reasoning about program behavior easier and allows the use of the [[lecture-02: Lecture 02: Substitution Model, Recursion|substitution model of evaluation]] [cs1101s-lecture-lecture-l7-updated-view-pdf#section-10].

Consider the `factorial(5)` function, which always returns `120`, regardless of how many times or when it's called [cs1101s-lecture-lecture-l7-updated-view-pdf#section-11].

However, some real-world scenarios require "memory." A bank account, for instance, starts with an initial balance. A `withdraw` function returns the balance if sufficient funds exist, or an error message otherwise. Subsequent identical calls to `withdraw` will produce different results because the account **remembers** its past state. This concept is called **state** [cs1101s-lecture-lecture-l7-updated-view-pdf#section-11, cs1101s-lecture-lecture-l7-updated-view-pdf#section-12]. Functional programming, by definition, does not allow programs to have state, necessitating the use of **assignment** [cs1101s-lecture-lecture-l7-updated-view-pdf#section-12].

### Simple Bank Account: Using Assignment

To implement a stateful bank account, we use assignment to modify a variable that holds the current balance.

```javascript
function make_account(initial_balance) {
    let balance = initial_balance; // Declare and initialize a variable
    function withdraw(amount) {
        if (balance >= amount) {
            balance = balance - amount; // Assignment: modifies the 'balance' variable
            return balance;
        } else {
            display("Insufficient funds");
            return balance;
        }
    }
    return withdraw;
}

const W1 = make_account(100);
W1(40); // -> 60
W1(40); // -> 20
W1(40); // -> 20 "Insufficient funds"
W1(15); // -> 5
```
[cs1101s-lecture-lecture-l7-updated-view-pdf#section-13]

In contrast, a purely functional approach would return a *new* account state for each withdrawal, as shown below:

```javascript
function fn_make_account(initial_balance) {
    const balance = initial_balance;
    function withdraw(amount) {
        if (balance >= amount) {
            return fn_make_account(balance - amount); // Returns a new account, doesn't modify existing
        } else {
            display("Insufficient funds");
            return fn_make_account(balance); // Returns current account if insufficient
        }
    }
    return withdraw;
}

const W1 = fn_make_account(100);
const W2 = W1(40); // W2 is a new account state
const W3 = W2(40); // W3 is another new account state
const W4 = W3(40); // W4 is another new account state (with insufficient funds message)
// -> W1: fn_make_account(100), W2: fn_make_account(60), W3: fn_make_account(20), W4: fn_make_account(20) "Insufficient funds"
```
[cs1101s-lecture-lecture-l7-updated-view-pdf#section-14]

### Variable Declaration and Assignment
In Source §3, we introduce `let` for variable declaration and `=` for assignment:
*   `let name = expression;`: Declares a **variable** `name` in the current scope and initializes its value to `expression`. From this point on, `name` evaluates to the value of `expression` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-15].
*   Function parameters in Source §3 are also considered variables [cs1101s-lecture-lecture-l7-updated-view-pdf#section-15].
*   `name = expression;`: This is an **assignment statement**. `name` must be a variable (not evaluated), `expression` is evaluated, and its value is then **assigned** to the variable `name`. From this point on, `name` will evaluate to the new value of `expression` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-16].

**Example:**
```javascript
let balance = 100; // balance is 100
balance;           // -> 100
balance = balance - 20; // balance is updated
balance;           // -> 80
balance = balance - 20; // balance is updated again
balance;           // -> 60
```
[cs1101s-lecture-lecture-l7-updated-view-pdf#section-17]

When creating multiple accounts using `make_account`, each account (`W1`, `W2`) maintains its own independent `balance` variable. Withdrawals from one do not affect the other [cs1101s-lecture-lecture-l7-updated-view-pdf#section-18].

### Pros and Cons of Assignment
**Pros:**
*   Assignment enables the creation of objects with **state** [cs1101s-lecture-lecture-l7-updated-view-pdf#section-19].
*   State allows objects to exhibit different behaviors over time, mimicking real-world entities more closely [cs1101s-lecture-lecture-l7-updated-view-pdf#section-19].

**Cons:**
*   Programs with assignment are harder to reason about, debug, and verify for correctness [cs1101s-lecture-lecture-l7-updated-view-pdf#section-20].
*   The [[lecture-02: Lecture 02: Substitution Model, Recursion|substitution model of evaluation]] breaks down when assignment is used [cs1101s-lecture-lecture-l7-updated-view-pdf#section-20].

### Why the Substitution Model Breaks Down
The substitution model treats a constant or variable as merely a "name for a value," assuming its value will not change. Thus, one can be substituted for the other [cs1101s-lecture-lecture-l7-updated-view-pdf#section-23].

However, assignment treats a variable as a "**container**" holding a value. The contents of this container can be **changed over time**. This container is managed within a structure called an **environment** [cs1101s-lecture-lecture-l7-updated-view-pdf#section-23].

Consider the following simplified `withdraw` function using the substitution model:

```javascript
function make_simplified_withdraw(balance) {
    return amount => {
        balance = balance - amount; // Assignment
        return balance;
    };
}

(make_simplified_withdraw(25))(20); // Intended: balance becomes 5
```
If we apply the substitution model:
1.  `make_simplified_withdraw(25)` substitutes `balance` with `25`.
2.  Returns `amount => { balance = 25 - amount; return 25; }`.
3.  Calling this with `(20)`: `balance = 25 - 20; return 25;`
4.  This incorrectly returns `25` instead of the expected `5` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-21, cs1101s-lecture-lecture-l7-updated-view-pdf#section-22].

This demonstrates that the substitution model is not powerful enough to explain state. A more sophisticated model, the [[lecture-08: Lecture 08: Environment Model|Environment Model]], is required to correctly interpret programs with assignment [cs1101s-lecture-lecture-l7-updated-view-pdf#section-20].

## Mutable Data (3.3)

Assignment provides the capability to create **mutable data**, which means data that can be modified after its creation, such as the bank account example [cs1101s-lecture-lecture-l7-updated-view-pdf#section-25]. In Source §1 and §2, all data was **immutable**, meaning once created, it could not be changed. We had constructors, selectors, predicates, and printers, but no **mutators** [cs1101s-lecture-lecture-l7-updated-view-pdf#section-25].

### Mutable Pairs
Source §3 introduces **mutators** to create mutable data structures. For pairs, these mutators are `set_head` and `set_tail` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-26]:
*   `set_head(p, x)`: Changes the `head` of pair `p` to `x` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-26].
*   `set_tail(p, x)`: Changes the `tail` of pair `p` to `x` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-26].

**Effect of `set_head(x, y)`:**
If `x` is a pair `(c, d)` pointing to `a` as its head and `b` as its tail, and `y` is another pair `(e, f)`. After `set_head(x, y)`, the head of `x` now points to `e` (the head of `y`), effectively changing the first element of `x` to the first element of `y`, while `x`'s tail `b` remains unchanged.
[cs1101s-lecture-lecture-l7-updated-view-pdf#section-27]

**Effect of `set_tail(x, y)`:**
Similar to `set_head`, if `x` is a pair `(c, d)` and `y` is `(e, f)`. After `set_tail(x, y)`, the tail of `x` now points to `e` (the head of `y`), effectively changing the second element of `x` to the first element of `y`, while `x`'s head `a` remains unchanged.
[cs1101s-lecture-lecture-l7-updated-view-pdf#section-28]

### Be Careful with Mutators!
Using mutators requires caution, as they can lead to unexpected side effects, especially when data structures are shared.

**Example: Mutation and Sharing**
Consider lists `a`, `b`, and `c`:
```javascript
const a = list(1, 3, 5); // a: (1, (3, (5, null)))
const b = list(2, 4);   // b: (2, (4, null))
const c = append(a, b); // c: (1, (3, (5, (2, (4, null)))))
```
The `append` function, being functional, creates new pairs for `a` but reuses the pairs from `b` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-30]. This means the tail of the last element of `a` in `c` points to the *original* list `b`.

If we then mutate `b`:
```javascript
set_head(b, 9); // Changes the head of list b from 2 to 9
```
Now, `b` becomes `[9, [4, null]]`. Because `c`'s tail (specifically, the last pair derived from `a`) points to `b`, mutating `b` also changes `c` indirectly:
`c; -> [1, [3, [5, [9, [4, null]]]]]` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-29, cs1101s-lecture-lecture-l7-updated-view-pdf#section-31].

This illustrates a critical point: **mutating `b` changes `c` as well** due to the sharing of underlying data structures [cs1101s-lecture-lecture-l7-updated-view-pdf#section-29].

**Example: Cyclical Structures**
Mutators can also create cyclical data structures:
```javascript
const a = list(1, 2, 3);
set_tail(tail(tail(a)), a); // Sets the tail of the last element (3) to point back to 'a' itself
```
This creates a list `a` where `1 -> 2 -> 3 -> 1 -> 2 -> 3 -> ...`. If you were to call `length(a)` on such a list, it would run into an infinite loop, never terminating [cs1101s-lecture-lecture-l7-updated-view-pdf#section-32].

### Mutable ("Destructive") List Processing

Destructive list processing involves functions that modify existing list structures rather than creating new ones. The goal is often to avoid creating new pairs, instead constructing the result list from existing pairs of input lists [cs1101s-lecture-lecture-l7-updated-view-pdf#section-33].

**Destructive Append (`d_append`)**
`d_append(xs, ys)` appends list `ys` to list `xs` by modifying the tail of the last pair in `xs` to point to `ys`. No new pairs are created for `xs` [cs1101s-lecture-lecture-l7-updated-view-pdf#section-34].

**Example:**
```javascript
const a = list(1, 3, 5);
const b = list(2, 4);
const c = d_append(a, b);
```
After `d_append(a, b)`:
*   The original list `a` is modified such that its last element's tail (which was `null`) now points to `b`.
*   `c` will be the same as `a` (since `d_append` returns the modified `xs`).
*   `c; -> [1, [3, [5, [2, [4, null]]]]]`
*   `a; -> [1, [3, [5, [2, [4, null]]]]]` (a is modified in place)
*   `b; -> [2, [4, null]]` (b remains unchanged)
[cs1101s-lecture-lecture-l7-updated-view-pdf#section-34]

**Implementation of `d_append`:**
```javascript
function d_append(xs, ys) {
    if (is_null(xs)) {
        return ys; // If xs is null, return ys (nothing to append to)
    } else {
        // Recursively find the last pair in xs, then set its tail to ys
        set_tail(xs, d_append(tail(xs), ys)); 
        return xs; // Return the modified xs
    }
}
```
The `set_tail` operation is performed on `xs` itself, making the modification "destructive" [cs1101s-lecture-lecture-l7-updated-view-pdf#section-35].

**Destructive Map (`d_map`)**
`d_map(fun, xs)` applies a function `fun` to each element of list `xs` by modifying the `head` of each pair in `xs` in place.

**Example:**
```javascript
const a = list(1, 2, 3);
d_map(x => x * 2, a); // Multiplies each element of 'a' by 2 in place
```
After `d_map`:
*   `a; -> [2, [4, [6, []]]]` (a is modified in place)
[cs1101s-lecture-lecture-l7-updated-view-pdf#section-36]

**Implementation of `d_map`:**
```javascript
function d_map(fun, xs) {
    if (!is_null(xs)) { // If xs is not null
        set_head(xs, fun(head(xs))); // Mutate the head of the current pair
        d_map(fun, tail(xs));       // Recursively call d_map on the tail
    } else {
        // Base case: do nothing if xs is null
    }
}
```
[cs1101s-lecture-lecture-l7-updated-view-pdf#section-37]

## Summary

*   **Assignment** enables the creation of **state** in programs [cs1101s-lecture-lecture-l7-updated-view-pdf#section-38].
*   Assignment allows the creation of **mutable data structures**, which can change over time [cs1101s-lecture-lecture-l7-updated-view-pdf#section-38].
*   The **substitution model** of evaluation breaks down when assignment is used, requiring a more complex model like the [[lecture-08: Lecture 08: Environment Model|environment model]] [cs1101s-lecture-lecture-l7-updated-view-pdf#section-38].
*   **`set_head`** and **`set_tail`** are mutators that modify existing pairs and lists [cs1101s-lecture-lecture-l7-updated-view-pdf#section-38].
*   It is crucial to **be careful when mutating things!** Destructive operations can lead to unintended side effects due to data sharing and can create cyclical structures [cs1101s-lecture-lecture-l7-updated-view-pdf#section-38].

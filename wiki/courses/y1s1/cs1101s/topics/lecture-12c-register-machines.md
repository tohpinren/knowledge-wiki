---
page_id: "y1s1-cs1101s-lecture-12c-register-machines"
title: "L12C: Register Machines"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "This lecture (CS1101S, Nov 2, 2022) introduces **Register Machines** as an abstract machine model for understanding how programs run on hardware. A Register Machine is an idealized computing machine defined by: * A fixed set of **storage registers** (updatable value holders). * A **program** (sequence of instruction..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l12c-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l12c-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l12c-view-pdf#section-3"
  - "cs1101s-lecture-lecture-l12c-view-pdf#section-4"
  - "cs1101s-lecture-lecture-l12c-view-pdf#section-5"
topics:
  - "register"
  - "machine"
  - "instructions"
  - "memory"
  - "machines"
  - "registers"
  - "garbage"
  - "operations"
  - "lecture"
  - "cs1101s"
source_count: 1
lecture_number: 12
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# L12C: Register Machines

This page introduces **Register Machines** as an abstract model for understanding how programs execute on computer hardware. It details their components, operations, and how they relate to higher-level programming concepts like recursion and subroutines, culminating in discussions on memory management, including stacks, heaps, and garbage collection [source:cs1101s-lecture-lecture-l12c-view-pdf#section-1].

## Our Journey So Far

In [[lecture-01: Lecture 01: Introduction; Elements of Programming]], we began with high-level functional programming and basic abstractions. We then explored [[lecture-04: Introduction to Data Abstraction]] and [[lecture-05: List and Tree Processing]] which introduced data structures [source:cs1101s-lecture-lecture-l12c-view-pdf#section-4]. Our journey continued through [[lecture-07: Mutable Data]] and [[lecture-08: Environment Model]], which addressed state and mutable state [source:cs1101s-lecture-lecture-l12c-view-pdf#section-7]. More recently, [[lecture-11: Metalinguistic Abstraction]] delved into creating new languages and interpreters [source:cs1101s-lecture-lecture-l12c-view-pdf#section-8].

This lecture marks a shift from high-level languages to understanding low-level machines. The question is whether high-level programming can explain low-level machine operations [source:cs1101s-lecture-lecture-l12c-view-pdf#section-10].

## Abstract Machines

Regardless of how many [[lecture-11: Metalinguistic Abstraction#The Meta-Circular Evaluator|meta-circular evaluators]] are implemented, programs ultimately need to run on physical hardware. To comprehend how programs function at this hardware level, a theoretical model of computer hardware, known as an **abstract machine**, is necessary [source:cs1101s-lecture-lecture-l12c-view-pdf#section-11].

## Register Machines

A **Register Machine** is an idealized computing machine characterized by [source:cs1101s-lecture-lecture-l12c-view-pdf#section-12]:
*   A fixed set of **storage registers**: these are holders for values that can be updated.
*   A set of **instructions**: these define operations on the registers.

The register machine executes instructions sequentially. A typical instruction performs a primitive operation on the contents of some registers and assigns the result to another register [source:cs1101s-lecture-lecture-l12c-view-pdf#section-12].

### Example: Greatest Common Divisor (GCD)

Consider the `gcd` function in Source [source:cs1101s-lecture-lecture-l12c-view-pdf#section-13]:

```javascript
function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b);
}
```

This simple function demonstrates several computational elements [source:cs1101s-lecture-lecture-l12c-view-pdf#section-15, cs1101s-lecture-lecture-l12c-view-pdf#section-16, cs1101s-lecture-lecture-l12c-view-pdf#section-17, cs1101s-lecture-lecture-l12c-view-pdf#section-18, cs1101s-lecture-lecture-l12c-view-pdf#section-19, cs1101s-lecture-lecture-l12c-view-pdf#section-20]:
*   **Data**: `a`, `b`
*   **Branching**: `b === 0 ? a : ...`
*   **Modulo operator**: `a % b`
*   **Recursion**: `gcd(b, a % b)`
*   **Comparison operator**: `===`
*   **Return value**: `a` or the result of the recursive call

## A Hypothetical Machine Language

To model how such a function runs on a register machine, we introduce a hypothetical machine language composed of [source:cs1101s-lecture-lecture-l12c-view-pdf#section-24, cs1101s-lecture-lecture-l12c-view-pdf#section-26]:
*   **Program**: A sequence of instructions and labels.
*   **Labels**: Named places in the instruction sequence that can be jumped to.
*   **Registers**: Holders for values that can be read and updated.
*   **Instructions**:
    *   `Test`: Checks a boolean condition and stores the result (e.g., in a `flag` register).
    *   `Branch`: Jumps to a label if the last test succeeded.
    *   `Go to`: Jumps to a label unconditionally.
    *   `Assign`: Updates the value of a register.
*   **Primitive operations**: Basic arithmetic (`=`, `+`, `-`), `print`, `remainder` (`%`), etc.

### GCD in this Hypothetical Machine Language (Iterative Version)

The iterative version of `gcd(a, b)` can be translated into the hypothetical machine language. Instead of direct recursion, it uses loops and conditional jumps [source:cs1101s-lecture-lecture-l12c-view-pdf#section-27]:

```
begin:
    check if b === 0
    if so go to done, otherwise…
    assign t to the value of a % b
    assign a to the value of b
    assign b to the value of t
    go to begin
done:
```

In a more formal representation, this might look like [source:cs1101s-lecture-lecture-l12c-view-pdf#section-28]:

```
test_gcd:
    test(op(=), reg(b), constant(0))
    branch(label(gcd_done))
    assign(t, op(%), reg(a), reg(b))
    assign(a, reg(b))
    assign(b, reg(t))
    go_to(label(test_gcd))
gcd_done:
```

This example clearly shows the role of `Labels`, `Registers`, `Instructions`, and `Primitive Operations` [source:cs1101s-lecture-lecture-l12c-view-pdf#section-29, cs1101s-lecture-lecture-l12c-view-pdf#section-30, cs1101s-lecture-lecture-l12c-view-pdf#section-31, cs1101s-lecture-lecture-l12c-view-pdf#section-32].

### Loops in this Hypothetical Machine Language

An infinite loop, such as continually prompting the user for input and displaying `gcd` results, can also be expressed. For example [source:cs1101s-lecture-lecture-l12c-view-pdf#section-34, cs1101s-lecture-lecture-l12c-view-pdf#section-35]:

```
gcd_loop:
    assign(a, op(read)) // Read input into register 'a'
    assign(b, op(read)) // Read input into register 'b'
test_gcd:
    test(op(=), reg(b), constant(0))
    branch(label(gcd_done))
    assign(t, op(%), reg(a), reg(b)) // Modulo operation
    assign(a, reg(b))
    assign(b, reg(t))
    go_to(label(test_gcd))
gcd_done:
    perform(op(print), reg(a)) // Print result
    go_to(label(gcd_loop)) // Loop indefinitely
```

### The Need for Subroutines

If a function, like a remainder (`rem`) function used within `gcd`, needs to be reusable in multiple places, we encounter challenges [source:cs1101s-lecture-lecture-l12c-view-pdf#section-43, cs1101s-lecture-lecture-l12c-view-pdf#section-45]:
1.  **Where to return?**: After `rem` completes, how does the machine know which instruction in `gcd` to return to?
2.  **Preserving register values**: Can we be sure that registers `a` and `b` (or other registers) hold the correct values for the calling function after the subroutine runs?
3.  **Duplication**: Do we need to duplicate the entire `rem` code for every place it's called?

To address these, a new idea is introduced: allow labels to be part of program data and add a dedicated **`continue` register** [source:cs1101s-lecture-lecture-l12c-view-pdf#section-46]. The `continue` register stores the label of where the computation should resume after a subroutine call.

For the `rem` subroutine, the structure would be [source:cs1101s-lecture-lecture-l12c-view-pdf#section-46]:

```
test_rem:
    test(op(<), reg(a), reg(b))
    branch(reg(continue)) // Branch to the address stored in 'continue'
    assign(a, op(-), reg(a), reg(b))
    go_to(label(test_rem))
// result in reg(a)
```

"Calling" a subroutine like `rem` from `gcd` would involve setting the `continue` register before jumping to `test_rem` [source:cs1101s-lecture-lecture-l12c-view-pdf#section-47]:

```
test_gcd1:
    test(op(=), reg(b), constant(0))
    branch(label(gcd1_done))
    assign(continue, label(gcd_cont)) // Save return address
    go_to(label(test_rem))           // Jump to rem subroutine
gcd_cont: // Execution returns here after rem finishes
    assign(t, reg(a))
    assign(a, reg(b))
    assign(b, reg(t))
    go_to(label(test_gcd1))
gcd1_done:
```

### What about Deferred Operations? (Factorial Example)

Consider the recursive `factorial` function [source:cs1101s-lecture-lecture-l12c-view-pdf#section-48]:

```javascript
function factorial(n) {
  return n === 1 ? 1 : n * factorial(n - 1);
}
```

This function involves a "deferred operation" (the multiplication `n * ...`) that must wait for the result of the recursive call `factorial(n - 1)` [source:cs1101s-lecture-lecture-l12c-view-pdf#section-49]. When calling `factorial` multiple times, we need to keep track of an unknown number of these deferred operations [source:cs1101s-lecture-lecture-l12c-view-pdf#section-51].

## Supporting Deferred Operations with a Stack

To handle an unknown number of deferred operations and manage subroutine calls effectively, a **stack data structure** is introduced [source:cs1101s-lecture-lecture-l12c-view-pdf#section-52].
*   Each **frame** in the stack can store the current value of one or more registers.
*   **When calling a function**: We `save` necessary register values (like `continue` and arguments) and push a new frame onto the stack.
*   **When returning from a function**: We `restore` necessary register values from the stack to continue the computation in the calling context.

This mechanism allows the reuse of the same machine code for recursive functions like factorial for every subproblem. A new register, `val`, is also introduced to hold return values from function calls [source:cs1101s-lecture-lecture-l12c-view-pdf#section-52].

A stack can be implemented using `pair` functions, where `stack = pair(x, stack)` pushes `x` and `head(stack)` / `tail(stack)` are used for `pop` operations [source:cs1101s-lecture-lecture-l12c-view-pdf#section-53].

### Factorial Example with a Stack

The `factorial` machine code uses `save` and `restore` operations to manage the stack [source:cs1101s-lecture-lecture-l12c-view-pdf#section-63]:

```
fac_loop:
    test(op(=), reg(a), constant(1))
    branch(label(base_case))
    save(continue) // Save current 'continue' (return address for this call)
    save(a)       // Save current 'a' (the 'n' for this deferred operation)
    assign(a, op(-), reg(a), constant(1)) // a = n - 1
    assign(continue, label(fac_done))    // Set 'continue' for the recursive call
    go_to(label(fac_loop))                // Recurse
fac_done:
    restore(a)      // Restore 'a' (the 'n' for the deferred multiplication)
    restore(continue) // Restore 'continue' for the original caller
    assign(val, op(*), reg(a), reg(val)) // val = restored_a * recursive_val
    go_to(reg(continue))                 // Return to caller
base_case:
    assign(val, constant(1)) // Base case: factorial(1) = 1
    go_to(reg(continue))     // Return 1
```

A detailed trace of `factorial(5)` shows how `continue` and `a` values are saved and restored on the stack with each recursive call and return [source:cs1101s-lecture-lecture-l12c-view-pdf#section-64, cs1101s-lecture-lecture-l12c-view-pdf#section-65, cs1101s-lecture-lecture-l12c-view-pdf#section-66, cs1101s-lecture-lecture-l12c-view-pdf#section-67, cs1101s-lecture-lecture-l12c-view-pdf#section-68, cs1101s-lecture-lecture-l12c-view-pdf#section-69, cs1101s-lecture-lecture-l12c-view-pdf#section-70, cs1101s-lecture-lecture-l12c-view-pdf#section-71, cs1101s-lecture-lecture-l12c-view-pdf#section-72, cs1101s-lecture-lecture-l12c-view-pdf#section-73].

## Simulating a Register Machine in Source

Chapter 5 of the textbook provides a register machine simulator that allows for creating and running abstract machines [source:cs1101s-lecture-lecture-l12c-view-pdf#section-74]. The process involves:
1.  **Creating the machine**: Specifying registers, primitive operations, and instructions.
2.  **Setting register values**: Initializing registers with desired inputs.
3.  **Starting the machine**: Initiating the execution.
4.  **Getting results**: Retrieving the final values from registers.

The `make_machine` function is central to this simulation. It takes a list of register names, primitive operations, and the controller text (instructions and labels) [source:cs1101s-lecture-lecture-l12c-view-pdf#section-79].

Inside `make_machine` [source:cs1101s-lecture-lecture-l12c-view-pdf#section-83]:
*   A new machine is created (`make_new_machine`).
*   Registers are allocated (`allocate_register`).
*   Primitive operations are installed (`install_operations`).
*   Controller text is assembled into machine instructions, extracting labels and binding special registers like `pc` (program counter) and `flag` (`set_instructions` with `assemble`) [source:cs1101s-lecture-lecture-l12c-view-pdf#section-86].

The `make_new_machine` function initializes built-in registers: `pc` (what to do next), `flag` (holds test results), and `stack` (to save register values) [source:cs1101s-lecture-lecture-l12c-view-pdf#section-87]. Registers themselves are implemented as procedures that respond to "get" and "set" messages (`make_register`) [source:cs1101s-lecture-lecture-l12c-view-pdf#section-88, cs1101s-lecture-lecture-l12c-view-pdf#section-89].

The machine's execution loop is handled by `execute`, which repeatedly fetches the next instruction (from `pc`), runs it, and then recursively calls itself [source:cs1101s-lecture-lecture-l12c-view-pdf#section-91]. The `dispatch` function acts as the machine's interface, handling various messages like "start", "set_instructions", "allocate_register", "get_register", etc. [source:cs1101s-lecture-lecture-l12c-view-pdf#section-92].

## Memory

Memory consumption has been previously discussed in relation to orders of growth and space complexity [source:cs1101s-lecture-lecture-l12c-view-pdf#section-101]. Deferred operations in recursive processes require significant memory, while iterative processes can often reuse space. The `pair` function, for instance, requires space to store the head and tail of newly created pairs. Memoization and tree structures also involve a memory vs. time trade-off [source:cs1101s-lecture-lecture-l12c-view-pdf#section-101].

### Computer Memory Types

A typical computer utilizes three main types of memory [source:cs1101s-lecture-lecture-l12c-view-pdf#section-102]:
*   **Registers**: Very small, very fast memory located inside processors.
*   **RAM (Random Access Memory)**: Quite small, quite fast memory shared by all running programs. It holds stacks, instructions, and data structures.
*   **Disk**: Very large, very slow memory that stores all instructions and data in a computer, even when not actively in use.

### Storing Pairs in Memory

To represent data structures like lists (which are built from pairs) in memory, a common idea is to use two arrays: one for all "heads" and one for all "tails" [source:cs1101s-lecture-lecture-l12c-view-pdf#section-103]. A `free` pointer tracks the next available memory location. For example, `list(list(1, 2), 3, 4)` would be stored by allocating sequential locations for each pair, with the "tail" possibly pointing to another pair or an empty list (represented by `e0`) [source:cs1101s-lecture-lecture-l12c-view-pdf#section-104, cs1101s-lecture-lecture-l12c-view-pdf#section-105, cs1101s-lecture-lecture-l12c-view-pdf#section-106, cs1101s-lecture-lecture-l12c-view-pdf#section-107, cs1101s-lecture-lecture-l12c-view-pdf#section-108, cs1101s-lecture-lecture-l12c-view-pdf#section-109, cs1101s-lecture-lecture-l12c-view-pdf#section-110].

### Getting Rid of Unwanted Pairs (Garbage Collection)

Programs often create temporary data structures (pairs) that are no longer needed after certain operations. For instance, in `accumulate((x, y) => x + y, 0, filter(is_odd, enum_list(0, n)))`, the `enum_list` and `filter` lists are temporary and not directly returned by `accumulate` [source:cs1101s-lecture-lecture-l12c-view-pdf#section-111].

**Garbage Collection (GC)** is a mechanism to automatically detect "garbage objects" (pairs no longer reachable or usable by the program) and reclaim their memory space. The goal is to provide the illusion of "infinite" memory to the programmer. While GC is common in modern programming languages, it incurs overhead and trade-offs. It is typically triggered when memory runs full, leading to an "allocation stall" [source:cs1101s-lecture-lecture-l12c-view-pdf#section-112].

A common GC algorithm is **Stop-and-Copy**. This method copies reachable objects from one memory space (the "old" space) to another (the "new" space). The unreachable objects are simply left behind and the entire old space is then discarded. This ensures that the new space contains only active data, compactly stored [source:cs1101s-lecture-lecture-l12c-view-pdf#section-113, cs1101s-lecture-lecture-l12c-view-pdf#section-114, cs1101s-lecture-lecture-l12c-view-pdf#section-115, cs1101s-lecture-lecture-l12c-view-pdf#section-116, cs1101s-lecture-lecture-l12c-view-pdf#section-117, cs1101s-lecture-lecture-l12c-view-pdf#section-118, cs1101s-lecture-lecture-l12c-view-pdf#section-119, cs1101s-lecture-lecture-l12c-view-pdf#section-120, cs1101s-lecture-lecture-l12c-view-pdf#section-121, cs1101s-lecture-lecture-l12c-view-pdf#section-122].

### Stacks and Heaps

The stack discussed earlier for storing register values (e.g., `continue`, `a` in factorial) is often referred to as "the stack" or "the call stack." The arrays used for storing pairs (data structures) are typically called "the heap" [source:cs1101s-lecture-lecture-l12c-view-pdf#section-123].

The call stack is generally orders of magnitude smaller than the heap. This difference in size explains why deferred operations (which consume stack space) are more costly than operations that primarily involve manipulating pairs on the heap, especially in the context of functions using accumulators or Continuation-Passing Style (CPS) transformation. The design choice to have a small stack is pragmatic, as most programs require a very small stack, making it resource-efficient [source:cs1101s-lecture-lecture-l12c-view-pdf#section-123].

## Summary

Register machines provide a fundamental model for understanding how programs run on hardware. Key components include [source:cs1101s-lecture-lecture-l12c-view-pdf#section-100, cs1101s-lecture-lecture-l12c-view-pdf#section-124]:
*   **Special Registers**:
    *   `val`: Holds the result of function calls.
    *   `continue`: Stores the return address (label) after a function call.
    *   `stack`: Manages saved and restored register values for function calls.
    *   `pc` (program counter): Points to the current instruction.
    *   `flag`: Stores the result of the last `test` instruction.
*   **Basic Instructions**: `assign`, `test`, `branch`, `go_to`, `save`, `restore`.
*   **Basic Operations**: Arithmetic (`=`, `+`, `-`, `*`), comparisons (`<`, `>`).

Complex calculations can be performed using this simple yet powerful model. Memory can be managed for pairs using array models, enabling the implementation of stacks. Furthermore, automatic **garbage collection** is possible, providing the illusion of infinite memory by reclaiming space from unreachable objects [source:cs1101s-lecture-lecture-l12c-view-pdf#section-124].

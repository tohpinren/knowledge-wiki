---
page_id: "y1s1-cs1101s-lecture-02"
title: "Lecture 02: Substitution Model, Recursion"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 02: Substitution Model, Recursion consolidates the numbered lecture materials for this module. This CS1101S lecture (Boyd Anderson, Aug 17, 2022) covered the substitution model (sections 1.1.3, 1.1.5) and intr..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l2-print-pdf#section-1"
  - "cs1101s-lecture-lecture-l2-print-pdf#section-2"
  - "cs1101s-lecture-lecture-l2-print-pdf#section-3"
  - "cs1101s-lecture-lecture-l2-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l2-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l2-view-pdf#section-3"
topics:
  - "function"
  - "recursive"
  - "factorial"
  - "substitution"
  - "model"
  - "iterative"
  - "rune"
  - "out"
  - "order"
  - "reduction"
source_count: 2
lecture_number: 2
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 02: Substitution Model, Recursion

This page consolidates the materials for CS1101S Lecture 02, delivered by Boyd Anderson on August 17, 2022. It covers the substitution model for expression evaluation and introduces recursion and iteration concepts [source: cs1101s-lecture-lecture-l2-print-pdf#section-1, cs1101s-lecture-lecture-l2-view-pdf#section-1].

## Course Logistics

CS1101S: Programming Methodology utilizes SICP JS, Source Academy, Studios, Missions, Piazza, and Paths [source: cs1101s-lecture-lecture-l2-view-pdf#section-1].

Upcoming deliverables mentioned include [source: cs1101s-lecture-lecture-l2-print-pdf#section-1, cs1101s-lecture-lecture-l2-view-pdf#section-1]:
*   **Path P2A**: Due today for completion by tomorrow.
*   **Reflection R2**: Sheets on LumiNUS, prepare for tomorrow's reflection session.
*   **Mission M2A**: Out today after lecture.
*   **Quest Q2A**: Out today evening.
*   **Mission M2B**: Out tomorrow.
*   **Quest Q2B**: Out on Friday.

**Experience Points (XP)** are earned as follows [source: cs1101s-lecture-lecture-l2-print-pdf#section-3]:
*   **Missions**: Primary source of XP.
*   **Quests**: Optional homework, supplements XP.
*   **Early Mission/Quest submission bonus**: 75 XP within 3 days; bonus decays afterward.
*   **Avengers**: Can "unsubmit" submissions within reasonable limits. For submissions less than 2 days after release, Avengers provide feedback less than 4 days after release.
*   **Paths**: XP for submission.
*   **Early Path submission**: 25 XP within 1 day; bonus decays afterward.
*   No "unsubmit" for paths.

## 1. Substitution Model (Sections 1.1.3 and 1.1.5)

The substitution model provides a mechanistic description of how expressions are evaluated in a programming language [source: cs1101s-lecture-lecture-l2-print-pdf#section-5, cs1101s-lecture-lecture-l2-view-pdf#section-5].

### 1.1.3 Evaluating Combinations

Evaluation of arithmetic expressions involves repeatedly replacing an "eligible" subexpression with its result [source: cs1101s-lecture-lecture-l2-print-pdf#section-6, cs1101s-lecture-lecture-l2-view-pdf#section-6].

**Example**:
Evaluating `1 + 2 * 3 + 4` proceeds as follows:
```
1 + 2 * 3 + 4
(1 + (2 * 3)) + 4  // Replace eligible subexpression (2 * 3)
(1 + 6) + 4        // Result of (2 * 3) is 6
7 + 4              // Replace eligible subexpression (1 + 6)
11                 // Result of (7 + 4)
```
[source: cs1101s-lecture-lecture-l2-print-pdf#section-6, cs1101s-lecture-lecture-l2-view-pdf#section-6]

### 1.1.5 Evaluating Function Application

When evaluating function applications, the substitution model replaces formal parameters with argument values [source: cs1101s-lecture-lecture-l2-print-pdf#section-5, cs1101s-lecture-lecture-l2-view-pdf#section-5].

**Example: Cost of a Circular Handrail**
**Problem**: Calculate the cost of a circular handrail given its cost per meter ($199.50) and the circle's radius (2.1 meters) [source: cs1101s-lecture-lecture-l2-print-pdf#section-7, cs1101s-lecture-lecture-l2-view-pdf#section-7].

**Solution Code**:
```javascript
const cost_per_meter = 199.95;
function circumference(radius) {
    return 2 * math_PI * radius;
}
function cost_of_circular_handrail(r) {
    return cost_per_meter * circumference(r);
}

cost_of_circular_handrail(2.1);
```
[source: cs1101s-lecture-lecture-l2-print-pdf#section-8, cs1101s-lecture-lecture-l2-view-pdf#section-8]

**Evaluation Trace**:
```
cost_of_circular_handrail(2.1)
-> 199.5 * circumference(2.1)                   // Substitute r with 2.1
-> 199.5 * ((2 * 3.141592) * 2.1)               // Substitute circumference(2.1) with its body and math_PI
-> 199.5 * (6.283185 * 2.1)                     // Evaluate (2 * 3.141592)
-> 199.5 * 13.19468                             // Evaluate (6.283185 * 2.1)
-> 2632.340                                     // Evaluate final multiplication
```
[source: cs1101s-lecture-lecture-l2-print-pdf#section-8, cs1101s-lecture-lecture-l2-view-pdf#section-8]

### Applicative vs. Normal Order Reduction (1.1.5)

There are two primary strategies for reducing (evaluating) expressions [source: cs1101s-lecture-lecture-l2-print-pdf#section-5, cs1101s-lecture-lecture-l2-view-pdf#section-5]:

1.  **Applicative Order Reduction**: Evaluates all operands before applying the function [source: cs1101s-lecture-lecture-l2-print-pdf#section-5, cs1101s-lecture-lecture-l2-view-pdf#section-5]. This is the strategy used in Source (SICP JS).
2.  **Normal Order Reduction**: Fully expands all expressions before performing any reductions [source: cs101s-lecture-lecture-l2-print-pdf#section-5, cs1101s-lecture-lecture-l2-view-pdf#section-5].

**Example Functions**:
```javascript
function sq(x) { return x * x; }
function sum_of_sqs(x, y) { return sq(x) + sq(y); }
function f(a) { return sum_of_sqs(a + 1, a * 2); }
```

**Applicative Order Reduction for `f(5)`**:
```
f(5)
-> sum_of_sqs(5 + 1, 5 * 2)  // Evaluate arguments (5 + 1) and (5 * 2)
-> sum_of_sqs(6, 10)         // Arguments are evaluated to 6 and 10
-> sq(6) + sq(10)            // Apply sum_of_sqs
-> (6 * 6) + (10 * 10)       // Apply sq functions with evaluated arguments
-> 36 + 100
-> 136
```
[source: cs1101s-lecture-lecture-l2-print-pdf#section-9, cs1101s-lecture-lecture-l2-view-pdf#section-9]

**Normal Order Reduction for `f(5)`**:
```
f(5)
-> sum_of_sqs(5 + 1, 5 * 2)  // Do not evaluate arguments yet
-> sq(5 + 1) + sq(5 * 2)    // Substitute sum_of_sqs with its body
-> ((5 + 1) * (5 + 1)) + ((5 * 2) * (5 * 2)) // Substitute sq with its body
-> (6 * 6) + (10 * 10)      // Evaluate subexpressions
-> 36 + 100
-> 136
```
[source: cs1101s-lecture-lecture-l2-print-pdf#section-10, cs1101s-lecture-lecture-l2-view-pdf#section-10]

Both orders yield the same result for pure functions. However, the number of evaluation steps can differ significantly. Applicative order usually performs fewer steps by evaluating arguments once.

### Substitution Model for Applicative-Order Languages

The rules for evaluation in applicative-order languages are [source: cs1101s-lecture-lecture-l2-print-pdf#section-11, cs1101s-lecture-lecture-l2-view-pdf#section-11]:
*   **Primitive expressions**: Take their value directly.
*   **Operator combinations**: Evaluate operands, then apply the operator.
*   **Constant declaration**: Evaluate the value expression and replace the name by value.
*   **Function application**:
    *   If the function is primitive: Apply the primitive function.
    *   If the function is compound: Evaluate component expressions and substitute argument values for parameters in the body of the declaration.

**Example with Runes (Source Module)**
Consider these rune manipulation functions [source: cs1101s-lecture-lecture-l2-print-pdf#section-12, cs1101s-lecture-lecture-l2-view-pdf#section-12]:
```javascript
function turn_upside_down(rune) {
    return quarter_turn_right(
               quarter_turn_right(rune));
}
function quarter_turn_left(rune) {
    return quarter_turn_right(
               turn_upside_down(rune));
}
```
If we call `quarter_turn_left(heart)`, the substitution model would trace the evaluation by replacing function calls with their bodies and substituting `rune` with `heart` at each step, until a primitive rune operation is reached. [source: cs1101s-lecture-lecture-l2-print-pdf#section-12, cs1101s-lecture-lecture-l2-view-pdf#section-12]

## 2. Recursion and Iteration (Sections 1.2.1 and 1.2.2)

This section introduces recursive function definitions and contrasts recursive and iterative processes using examples like `stackn`, `repeat_pattern`, factorial, and Fibonacci [source: cs1101s-lecture-lecture-l2-print-pdf#section-13, cs1101s-lecture-lecture-l2-view-pdf#section-13].

### `stackn` and `repeat_pattern`

A new predeclared combination, `stack_frac(r, heart, sail)`, splits an available bounded box such that `heart` occupies the top fraction `r` and `sail` occupies the remaining `1 - r` [source: cs1101s-lecture-lecture-l2-print-pdf#section-14, cs1101s-lecture-lecture-l2-view-pdf#section-14].

**Example: Trisection and Quadrisection of a Heart Rune**
A trisection can be represented as:
```javascript
stack_frac(1 / 3, heart,
    stack_frac(1 / 2, heart, heart));
```
[source: cs1101s-lecture-lecture-l2-print-pdf#section-16, cs1101s-lecture-lecture-l2-view-pdf#section-16]
A quadrisection (generalizing the idea) would be:
```javascript
stack_frac(1 / 4, heart,
    stack_frac(1 / 3, heart,
        stack_frac(1 / 2, heart, heart)));
```
[source: cs1101s-lecture-lecture-l2-print-pdf#section-16, cs1101s-lecture-lecture-l2-view-pdf#section-16]

**Defining `stackn` Recursively**:
A first attempt at `stackn` might be:
```javascript
function stackn(n, rune) {
    return stack_frac(1 / n, rune, stackn(n - 1, rune));
}
```
This function has a problem: it lacks a base case, meaning it would recurse infinitely [source: cs1101s-lecture-lecture-l2-print-pdf#section-17, cs1101s-lecture-lecture-l2-view-pdf#section-17].

**The Correct `stackn` Version**:
A correct recursive function needs a trivial **base case** to stop the recursion [source: cs1101s-lecture-lecture-l2-print-pdf#section-18, cs1101s-lecture-lecture-l2-view-pdf#section-18].
```javascript
function stackn(n, rune) {
    return n === 1
        ? rune
        : stack_frac(1 / n, rune, stackn(n - 1, rune));
}
```
The solution for `n` is computed using the solution for `n - 1`, and so on, until the trivial case `n === 1` is reached [source: cs1101s-lecture-lecture-l2-print-pdf#section-18, cs1101s-lecture-lecture-l2-view-pdf#section-18].

**Recipe for Recursion**:
1.  Figure out the trivial **base case**.
2.  Assume you know how to solve the problem for `n - 1`.
3.  Based on this assumption, determine how to solve the problem for `n`.
[source: cs1101s-lecture-lecture-l2-print-pdf#section-19, cs1101s-lecture-lecture-l2-view-pdf#section-19]

**`repeat_pattern` Function**:
The `repeat_pattern` function in the `rune` module [source: cs1101s-lecture-lecture-l2-print-pdf#section-20, cs1101s-lecture-lecture-l2-view-pdf#section-20]:
`repeat_pattern(3, make_cross, sail)` should lead to `make_cross(make_cross(make_cross(sail)))`.
`repeat_pattern(3, square, 2)` should lead to `square(square(square(2)))`.

**Recursive `repeat_pattern` (First Version)**:
```javascript
function repeat_pattern(n, pat, init) {
    return n === 0
        ? init
        : pat(repeat_pattern(n - 1, pat, init));
}
```
This is a **recursive process** where applications of `pat` accumulate as a result of recursive calls. These are **deferred operations** [source: cs1101s-lecture-lecture-l2-print-pdf#section-21, cs1101s-lecture-lecture-l2-view-pdf#section-21].

**Iterative `repeat_pattern` (Second Version)**:
```javascript
function repeat_pattern(n, pat, rune) {
    return n === 0
        ? rune
        : repeat_pattern(n - 1, pat, pat(rune));
}
```
This is an **iterative process**. With applicative order reduction, the `pat` function is applied *before* the recursive call, meaning there are no deferred operations. The result is "built up" as the recursion unwinds [source: cs1101s-lecture-lecture-l2-print-pdf#section-22, cs1101s-lecture-lecture-l2-view-pdf#section-22].

### Factorial (1.2.1)

The factorial function `n!` is defined as `n * (n-1) * (n-2) * ... * 1`.
*   **Grouping**: `n! = n * ((n - 1) * (n - 2) * ... * 1)`
*   **Replacement**: `n! = n * (n - 1)!`
*   **Base Case**:
    *   `n! = 1` if `n = 1`
    *   `n! = n * (n - 1)!` if `n > 1`
[source: cs1101s-lecture-lecture-l2-print-pdf#section-23, cs1101s-lecture-lecture-l2-view-pdf#section-23]

**Factorial in Source (Recursive)**:
```javascript
function factorial(n) {
    return n === 1
        ? 1
        : n * factorial(n - 1);
}
```
[source: cs1101s-lecture-lecture-l2-print-pdf#section-24, cs1101s-lecture-lecture-l2-view-pdf#section-24]

**Example Execution using Substitution Model (`factorial(4)`)**:
```
factorial(4)
-> 4 * factorial(3)
-> 4 * (3 * factorial(2))
-> 4 * (3 * (2 * factorial(1)))
-> 4 * (3 * (2 * 1))  // Base case factorial(1) returns 1
-> 4 * (3 * 2)
-> 4 * 6
-> 24
```
This demonstrates a **recursive process** because there are deferred operations (multiplications waiting to happen) [source: cs1101s-lecture-lecture-l2-print-pdf#section-25, cs1101s-lecture-lecture-l2-view-pdf#section-25].

**Performance Considerations**:
*   **Time**: How long does the program run?
*   **Space**: How much memory is needed?
[source: cs1101s-lecture-lecture-l2-print-pdf#section-26, cs1101s-lecture-lecture-l2-view-pdf#section-26]

For the recursive factorial, the number of operations (time) grows linearly proportional to `n` [source: cs1101s-lecture-lecture-l2-print-pdf#section-27, cs1101s-lecture-lecture-l2-view-pdf#section-27]. The number of deferred operations (space), which are "things to remember" on the call stack, also grows linearly proportional to `n` [source: cs1101s-lecture-lecture-l2-print-pdf#section-28, cs1101s-lecture-lecture-l2-view-pdf#section-28].

**Iterative Factorial**:
An iterative version of factorial can be written using a helper function that carries the state (product, counter) explicitly.
```javascript
function factorial(n) {
    return iter(1, 1, n);
}

function iter(product, counter, n) {
    return counter > n
        ? product
        : iter(counter * product, counter + 1, n);
}
```
This iterative approach does not accumulate deferred operations, making its space complexity constant relative to `n` [source: cs1101s-lecture-lecture-l2-print-pdf#section-29, cs1101s-lecture-lecture-l2-view-pdf#section-29].

### Fibonacci Function (1.2.2)

The Fibonacci sequence is defined as `F(n) = F(n-1) + F(n-2)`, with `F(0)=0`, `F(1)=1`.

**Recursive Fibonacci (First Attempt)**:
```javascript
function fib(n) {
    return n <= 1
        ? n
        : fib(n - 1) + fib(n - 2);
}
```
This recursive implementation explores a computation tree where the number of leaves grows proportionally to `F(n + 1)`. This results in exponential time complexity, making it very inefficient for larger `n` [source: cs1101s-lecture-lecture-l2-print-pdf#section-30, cs1101s-lecture-lecture-l2-view-pdf#section-30].

**Iterative Fibonacci**:
An efficient iterative solution can be devised by maintaining the previous two Fibonacci numbers.
```javascript
function fib(n) {
    return fib_iter(1, 0, n);
}

function fib_iter(a, b, count) {
    return count === 0
        ? b
        : fib_iter(a + b, a, count - 1);
}
```
This iterative approach's time for exploring the computation grows linearly proportional to `n`, a significant improvement over the recursive version [source: cs1101s-lecture-lecture-l2-print-pdf#section-31, cs1101s-lecture-lecture-l2-view-pdf#section-31].

## Summary

*   The **Substitution Model** allows tracing the evaluation of expressions [source: cs1101s-lecture-lecture-l2-print-pdf#section-32, cs1101s-lecture-lecture-l2-view-pdf#section-32].
*   Distinguish between **Applicative Order** (evaluate arguments before applying function) and **Normal Order** (fully expand before reducing) reduction [source: cs1101s-lecture-lecture-l2-print-pdf#section-32, cs1101s-lecture-lecture-l2-view-pdf#section-32].
*   Function applications are replaced by their return expressions [source: cs1101s-lecture-lecture-l2-print-pdf#section-32, cs1101s-lecture-lecture-l2-view-pdf#section-32].
*   Examples of recursive solutions include `stackn`, `repeat_pattern`, `factorial`, and `fib` [source: cs1101s-lecture-lecture-l2-print-pdf#section-32, cs1101s-lecture-lecture-l2-view-pdf#section-32].
*   Understanding **recursive and iterative processes** is crucial [source: cs1101s-lecture-lecture-l2-print-pdf#section-32, cs1101s-lecture-lecture-l2-view-pdf#section-32].
*   Computational processes have resource implications: **time** and **space** [source: cs1101s-lecture-lecture-l2-print-pdf#section-32, cs1101s-lecture-lecture-l2-view-pdf#section-32].
*   The Fibonacci function highlights how different implementations can lead to vastly different performance (a "bad" recursive one and a "good" iterative one) [source: cs1101s-lecture-lecture-l2-print-pdf#section-32, cs1101s-lecture-lecture-l2-view-pdf#section-32].

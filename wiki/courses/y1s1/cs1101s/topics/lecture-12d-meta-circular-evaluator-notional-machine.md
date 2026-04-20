---
page_id: "y1s1-cs1101s-lecture-12d-meta-circular-evaluator-notional-machine"
title: "L12D: Meta-Circular Evaluator II; Notional Machine for Source \u00a73"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "This lecture introduces **notional machines** as a pedagogical tool to explain program execution, particularly for modern scripting languages, citing Yuha Sorva's [2012] work. It outlines a progression of language features including Action, Calculator, conditionals, Booleans, sequences, blocks, declarations, names,... This source reviews the concept of a programming evaluator as a program that defines the meaning of a language. Evaluator complexity incrementally increases from simple calculators to include booleans, conditionals, sequences, blocks, declarations, and compound functions."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l12d-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l12d-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l12d-view-pdf#section-3"
  - "cs1101s-lecture-lecture-l12d-view-pdf#section-4"
  - "cs1101s-lecture-lecture-l12d-view-pdf#section-5"
  - "cs1101s-lecture-lecture-l12d-part-2-pdf#section-1"
  - "cs1101s-lecture-lecture-l12d-part-2-pdf#section-2"
  - "cs1101s-lecture-lecture-l12d-part-2-pdf#section-3"
  - "cs1101s-lecture-lecture-l12d-part-2-pdf#section-4"
  - "cs1101s-lecture-lecture-l12d-part-2-pdf#section-5"
topics:
  - "return"
  - "evaluator"
  - "statements"
  - "body"
  - "model"
  - "evaluation"
  - "while"
  - "loops"
  - "environment"
  - "function"
source_count: 2
lecture_number: 12
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# L12D: Meta-Circular Evaluator II; Notional Machine for Source §3

This page discusses the meta-circular evaluator, focusing on handling `return` statements and loops, and introduces **notional machines** as a pedagogical tool for understanding program execution in modern scripting languages.

### Review: Fundamental Idea of a Programming Evaluator

The fundamental idea in programming is that the **evaluator**, which defines the meaning of statements and expressions in a programming language, is itself a program [source: cs1101s-lecture-lecture-l12d-view-pdf#section-3]. The complexity of this evaluator can be incrementally increased to handle more sophisticated language features [source: cs1101s-lecture-lecture-l12d-view-pdf#section-4].

The progression of language features in building an evaluator includes:
1.  **Calculator Language:** Handles primitive operators and literals, evaluating basic expressions [source: cs1101s-lecture-lecture-l12d-view-pdf#section-4].
2.  **Booleans, Conditionals, Sequences:** Extends the evaluator to include Boolean values, `if-else` structures, and ordered execution of statements [source: cs1101s-lecture-lecture-l12d-view-pdf#section-5].
3.  **Blocks and Declarations:** Incorporates language constructs like code blocks and variable declarations (e.g., `const`, `let`) [source: cs1101s-lecture-lecture-l12d-view-pdf#section-6].
4.  **Compound Functions (excluding return statements):** Allows for the definition and application of user-defined functions without explicit `return` statements initially [source: cs1101s-lecture-lecture-l12d-view-pdf#section-7].

### Notional Machines for Program Execution

To answer questions about "what happens when a program runs," especially in modern scripting languages, **notional machines** are proposed as a valuable pedagogical tool [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-4, cs1101s-lecture-lecture-l12d-part-2-pdf#section-5]. Yuha Sorva's [2012] PhD dissertation provides a thorough treatment of their pedagogical role [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-6].

The journey through language features using notional machines mirrors the evaluator's incremental complexity:
*   Action language
*   Calculator language
*   Conditionals, Booleans, sequences
*   Blocks, declarations, names
*   Function declaration and application (simple return)
*   Restoring environments
*   Return statements [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-7]

#### Notional Machine: Calculator Language Example

A notional machine can illustrate the evaluation of a simple expression like `1 + (2 * 3 - 4)` using two components: an **Agenda** (stack of instructions to be executed) and a **Stash** (stack to store intermediate values).

1.  **Initial State**: The Agenda contains the expression `1 + (2 * 3 - 4)`. The Stash is empty. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-9, cs1101s-lecture-lecture-l12d-part-2-pdf#section-10]
2.  **Operator Combination**: The expression is broken down into its operator and operands. The operator `+` is identified. The operands `1` and `(2 * 3 - 4)` are separated. The Agenda now contains `(2 * 3 - 4)`, `1`, `+` (implicitly in order of evaluation for `+`). [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-11, cs1101s-lecture-lecture-l12d-part-2-pdf#section-12, cs1101s-lecture-lecture-l12d-part-2-pdf#section-13]
3.  **Literal Evaluation**: `1` is a literal. It's popped from the Agenda and pushed onto the Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-15, cs1101s-lecture-lecture-l12d-part-2-pdf#section-16]
4.  **Nested Expression**: The sub-expression `(2 * 3 - 4)` is further broken down. `(2 * 3)` and `4` are operands, and `-` is the operator. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-18, cs1101s-lecture-lecture-l12d-part-2-pdf#section-19]
5.  **Further Nested Expression**: `(2 * 3)` is broken into `2`, `3`, and `*`. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-21, cs1101s-lecture-lecture-l12d-part-2-pdf#section-22]
6.  **Literal `2`**: Popped from Agenda, pushed to Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-23, cs1101s-lecture-lecture-l12d-part-2-pdf#section-24]
7.  **Literal `3`**: Popped from Agenda, pushed to Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-25, cs1101s-lecture-lecture-l12d-part-2-pdf#section-26]
8.  **Operator `*`**: Popped from Agenda. Operands `3` and `2` are popped from Stash, multiplied (`2 * 3 = 6`), and the result `6` is pushed back onto the Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-28, cs1101s-lecture-lecture-l12d-part-2-pdf#section-29]
9.  **Literal `4`**: Popped from Agenda, pushed to Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-31, cs1101s-lecture-lecture-l12d-part-2-pdf#section-32]
10. **Operator `-`**: Popped from Agenda. Operands `4` and `6` are popped from Stash, subtracted (`6 - 4 = 2`), and the result `2` is pushed back onto the Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-34, cs1101s-lecture-lecture-l12d-part-2-pdf#section-35]
11. **Operator `+`**: Popped from Agenda. Operands `2` and `1` are popped from Stash, added (`1 + 2 = 3`), and the result `3` is pushed back onto the Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-36, cs1101s-lecture-lecture-l12d-part-2-pdf#section-37]
12. **Final Result**: The Agenda is empty, and the final result `3` is on top of the Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-38]

#### Notional Machine: Sequences and Conditionals

For sequences like `1 + 2; 3 * 4;`, the notional machine splits the sequence into components, inserting a `pop` instruction between each component to discard intermediate results from the Stash, except for the final expression [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-41, cs1101s-lecture-lecture-l12d-part-2-pdf#section-42, cs1101s-lecture-lecture-l12d-part-2-pdf#section-52, cs1101s-lecture-lecture-l12d-part-2-pdf#section-53].

For conditional expressions like `false ? 8 : 3 * 4;`, the notional machine operates by:
1.  Popping the conditional from the Agenda.
2.  Pushing the branches (e.g., `8` and `3 * 4`) and the predicate (`false`) onto the Agenda.
3.  Evaluating the predicate.
4.  Based on the Boolean value from the predicate, the correct alternative (branch) is pushed onto the Agenda for evaluation, and the incorrect one is discarded. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-58, cs1101s-lecture-lecture-l12d-part-2-pdf#section-59, cs1101s-lecture-lecture-l12d-part-2-pdf#section-64, cs1101s-lecture-lecture-l12d-part-2-pdf#section-65]

#### Notional Machine: Blocks, Declarations, and Names

When handling blocks with declarations, such as:
```javascript
{
  const x = 3 * 4;
  const y = x + 2;
  x * y;
}
```
The notional machine introduces an environment model:
1.  **Block Processing**: A block extends the current environment with a new frame for declared names. The current environment is set to this new frame. The block itself is popped from the Agenda, and its body is pushed onto the Agenda. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-70, cs1101s-lecture-lecture-l12d-part-2-pdf#section-71]
2.  **Assignments**: An assignment statement involves pushing the value expression onto the Agenda, followed by an "assign" instruction.
    *   The value expression is evaluated.
    *   The "assign" instruction then locates the name in the current environment, peeks the value from the Stash, binds the name to that value, and pops itself from the Agenda. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-74, cs1101s-lecture-lecture-l12d-part-2-pdf#section-75, cs1101s-lecture-lecture-l12d-part-2-pdf#section-77, cs1101s-lecture-lecture-l12d-part-2-pdf#section-78]
3.  **Name Expressions**: When a name (variable) is encountered, its value is looked up in the current environment, pushed onto the Stash, and the name expression is popped from the Agenda. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-86, cs1101s-lecture-lecture-l12d-part-2-pdf#section-87]

#### Notional Machine: Function Declaration and Application

Function declarations, such as `function fact(n) { ... }`, are processed by:
1.  **Desugaring**: A function declaration can be desugared into a constant declaration where the value assigned is a lambda expression (function value). [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-98, cs1101s-lecture-lecture-l12d-part-2-pdf#section-99]
2.  **Lambda Expression**: Creating a function value involves packaging the function's parameters and body with the *current environment* (lexical scoping). A reference to this function value is pushed onto the Stash. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-102, cs1101s-lecture-lecture-l12d-part-2-pdf#section-103]
3.  **Function Application**: A function application (e.g., `fact(4)`) triggers:
    *   Popping the function application from the Agenda.
    *   Pushing a "call" instruction (with the number of arguments), followed by the arguments and the function expression itself, onto the Agenda. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-108, cs1101s-lecture-lecture-l12d-part-2-pdf#section-109]
4.  **Call Instruction**: This instruction handles the actual function invocation:
    *   It pops the arguments and the function value from the Stash.
    *   It extends the *function's environment* (captured at declaration time) by a new frame, binding parameters to their argument values.
    *   The current environment is reassigned to this new frame.
    *   The call instruction is popped from the Agenda.
    *   The function's body is pushed onto the Agenda for evaluation. [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-114, cs1101s-lecture-lecture-l12d-part-2-pdf#section-115]

#### Restoring Environments

When a block or a function call changes the current environment, it's crucial to restore the previous environment upon exiting that scope. This is achieved by inserting a "restore environment" instruction onto the Agenda whenever the current environment changes due to a block or a function call [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-142, cs1101s-lecture-lecture-l12d-part-2-pdf#section-143, cs1101s-lecture-lecture-l12d-part-2-pdf#section-144, cs1101s-lecture-lecture-l12d-part-2-pdf#section-159, cs1101s-lecture-lecture-l12d-part-2-pdf#section-160, cs1101s-lecture-lecture-l12d-part-2-pdf#section-228, cs1101s-lecture-lecture-l12d-part-2-pdf#section-229]. The "restore instruction" simply sets the current environment back to the environment stored within that instruction [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-248, cs1101s-lecture-lecture-l12d-part-2-pdf#section-249]. This ensures that variables from outer scopes are correctly accessible after a nested block or function completes.

For example, in:
```javascript
const x = 1;
{
  const x = 42;
  display(x); // displays 42
}
display(x);   // displays 1
```
The "restore environment" instruction ensures that after the inner block finishes, the `x` from the outer scope (with value `1`) becomes accessible again [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-137, cs1101s-lecture-lecture-l12d-part-2-pdf#section-191].

Similarly, for recursive functions or functions accessing outer scope variables:
```javascript
const n = 42;
function fact(n) {
  return n === 1 ? 1 : fact(n - 1) * n;
}
fact(4) + n; // (24 + 42) = 66
```
The "restore environment" instructions are crucial for preserving the `n` of each recursive call and the global `n` after the `fact(4)` call finishes [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-138, cs1101s-lecture-lecture-l12d-part-2-pdf#section-139, cs1101s-lecture-lecture-l12d-part-2-pdf#section-140, cs1101s-lecture-lecture-l12d-part-2-pdf#section-271].

### A Small Complication: Return Statements

Handling `return` statements in an evaluator introduces specific challenges:
*   Functions in JavaScript that do not explicitly `return` a value implicitly return `undefined` [source: cs1101s-lecture-lecture-l12d-view-pdf#section-9].
*   An `return` statement immediately exits the function from anywhere within its body, returning the result of evaluating the `return` expression [source: cs1101s-lecture-lecture-l12d-view-pdf#section-10].

To address this, the evaluator is augmented:
*   A `return_statement` component is added to the language grammar.
*   Functions `eval_return_statement`, `make_return_value`, and `is_return_value` are introduced to process `return` expressions and encapsulate their results as special `return_value` objects [source: cs1101s-lecture-lecture-l12d-view-pdf#section-11, cs1101s-lecture-lecture-l12d-view-pdf#section-12, cs1101s-lecture-lecture-l12d-view-pdf#section-13].
*   `eval_sequence` is modified to check if the evaluation of a statement yields a `return_value`. If so, the sequence's evaluation immediately propagates this `return_value` and stops further execution of the sequence [source: cs1101s-lecture-lecture-l12d-view-pdf#section-14].
*   The `apply` function (for function application) is updated to check if the result of evaluating the function body is a `return_value`. If it is, the content of the `return_value` is returned. Otherwise, `undefined` is returned [source: cs1101s-lecture-lecture-l12d-view-pdf#section-15].

### While and For Loops

Loops (`while` and `for`) are integrated into the evaluator by recognizing them as distinct statement types:
*   The `evaluate` function can check for `is_while_loop(stmt)` and `is_for_loop(stmt)`, delegating to `eval_while_loop` and `eval_for_loop` respectively [source: cs1101s-lecture-lecture-l12d-view-pdf#section-17].

#### Evaluation of While Loops
A `while` loop `while (predicate) { statements }` is evaluated recursively:
```javascript
function eval_while_loop(stmt, env) {
  if (evaluate(while_loop_predicate(stmt), env)) {
    evaluate(while_loop_statements(stmt), env);
    return eval_while_loop(stmt, env); // Recursive call to continue the loop
  } else {
    return true; // Loop terminates
  }
}
```
However, this recursive definition has challenges in JavaScript:
*   JavaScript `while` loops return the result of the *last evaluation of the body* when they exit normally.
*   Handling `break` and `continue` statements within loops also adds complexity to the evaluator [source: cs1101s-lecture-lecture-l12d-view-pdf#section-18, cs1101s-lecture-lecture-l12d-view-pdf#section-19, cs1101s-lecture-lecture-l12d-view-pdf#section-20].

#### Evaluation of For Loops (First Approximation)
A `for` loop `for (E1; E2; E3) { statements }` is an abbreviation (syntactic sugar) for a combination of blocks and a `while` loop:
```javascript
{
  E1; // Initializer
  while (E2) { // Predicate
    statements;
    E3; // Finalizer (update)
  }
}
```
This can be directly implemented in the evaluator by constructing an equivalent block structure containing a `while` loop and then evaluating this `whole_block` [source: cs1101s-lecture-lecture-l12d-view-pdf#section-21, cs1101s-lecture-lecture-l12d-view-pdf#section-22].

A peculiar JavaScript design decision is that each iteration of a `for` loop's body (especially with `let` declarations) receives its own "copy" of the loop control variable. This means closures created inside a loop iteration will capture the value of the loop variable specific to that iteration, not its final value. For example, in:
```javascript
const a = [];
for (let i = 0; i < 10; i = i + 1) {
  a[i] = x => x + i;
}
a[5](100); // Result is 105 (100 + 5)
```
Each function `x => x + i` in the array `a` captures a different `i` from its respective loop iteration, not the `i` at the end of the loop. If `var i` was used, all functions would capture the *same* `i`, resulting in `109` (100 + 9, where `i` eventually becomes 10 and the loop terminates at 9). This behavior has significant implications for how `for` loops are modeled in the notional machine [source: cs1101s-lecture-lecture-l12d-view-pdf#section-23, cs1101s-lecture-lecture-l12d-view-pdf#section-24, cs1101s-lecture-lecture-l12d-view-pdf#section-25, cs1101s-lecture-lecture-l12d-view-pdf#section-26].

### Summary So Far
This lecture covered how to extend a programming evaluator to handle `return` statements and loops, building upon the fundamental idea of an evaluator as a program [source: cs1101s-lecture-lecture-l12d-view-pdf#section-28, cs1101s-lecture-lecture-l12d-view-pdf#section-29].

### Practical and Conceptual Issues with the Environment Model
*   **Practical Issues**: When a `return` is executed, where does control flow go? How are expressions evaluated in the presence of control flow changes? [source: cs1101s-lecture-lecture-l12d-view-pdf#section-31, cs1101s-lecture-lecture-l12d-view-pdf#section-32]
*   **Conceptual Issues**: The circularity of the evaluator (evaluator is a program written in the language it evaluates) and how to properly model iterative processes without unbounded stack growth in a recursive evaluator [source: cs1101s-lecture-lecture-l12d-view-pdf#section-34, cs1101s-lecture-lecture-l12d-view-pdf#section-35].

### Approaches to Evaluation
Two main approaches for understanding evaluation are highlighted:
*   The **SICP approach** from Chapter 5, focusing on register machines [source: cs1101s-lecture-lecture-l12d-view-pdf#section-37].
*   The **notional machine approach**, which is the focus of this lecture [source: cs1101s-lecture-lecture-l12d-view-pdf#section-38].

### What Next
Future directions and applications of the notional machine approach include:
*   Developing a Python implementation of the notional machine (Lego Spike).
*   Integrating an agenda and stash into an environment model visualizer (e.g., for CS3108).
*   Building tools for simpler languages, such as an Action language.
*   Extending the machine to handle event-based programming (e.g., `async/await`).
*   Potentially teaching a CS1 course that consistently utilizes this notional machine approach [source: cs1101s-lecture-lecture-l12d-part-2-pdf#section-276, cs1101s-lecture-lecture-l12d-part-2-pdf#section-277, cs1101s-lecture-lecture-l12d-part-2-pdf#section-278, cs1101s-lecture-lecture-l12d-part-2-pdf#section-279, cs1101s-lecture-lecture-l12d-part-2-pdf#section-280].

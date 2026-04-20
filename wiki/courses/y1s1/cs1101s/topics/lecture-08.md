---
page_id: "y1s1-cs1101s-lecture-08"
title: "Lecture 08: Environment Model"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 08: Environment Model consolidates the numbered lecture materials for this module. This lecture (L8) from CS1101S: Programming Methodology, authored by Low Kok Lim (Oct 5, 2022), covers State (3.1) and the Env..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l8-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l8-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l8-view-pdf#section-3"
topics:
  - "environment"
  - "function"
  - "frame"
  - "model"
  - "new"
  - "name"
  - "expression"
  - "variables"
  - "lecture"
  - "consolidates"
source_count: 1
lecture_number: 8
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 08: Environment Model

This lecture, L8: Environment Model, is part of the CS1101S: Programming Methodology course, authored by Low Kok Lim and dated October 5, 2022. It covers the concepts of State (3.1) and the Environment Model (3.2) [source:cs1101s-lecture-lecture-l8-view-pdf#section-1, cs1101s-lecture-lecture-l8-view-pdf#section-2].

### State (3.1)

#### Recap: Variable Declaration Statement
A `let name = expression;` statement declares a variable `name` within the current scope and initializes it with the value of `expression`. From this point forward, `name` will evaluate to this value. From Source §3 onwards, function parameters are also considered variables [source:cs1101s-lecture-lecture-l8-view-pdf#section-5].

#### Recap: Assignment Statement
An assignment statement `name = expression;` works as follows:
*   `name` is a variable, not an evaluated expression [source:cs1101s-lecture-lecture-l8-view-pdf#section-6].
*   `expression` is evaluated, and its value is then assigned to the variable `name` [source:cs1101s-lecture-lecture-l8-view-pdf#section-6].
*   After assignment, `name` will evaluate to the new value of `expression` [source:cs1101s-lecture-lecture-l8-view-pdf#section-6].

#### Assignment: Pros
Assignment offers significant advantages:
*   It enables the creation of objects with **state** [source:cs1101s-lecture-lecture-l8-view-pdf#section-7].
*   This state allows objects to exhibit different behavior **over time** [source:cs1101s-lecture-lecture-l8-view-pdf#section-7].

#### Assignment: Cons
However, assignment introduces complexities:
*   Programs become harder to reason about [source:cs1101s-lecture-lecture-l8-view-pdf#section-8].
*   Debugging becomes more challenging [source:cs1101s-lecture-lecture-l8-view-pdf#section-8].
*   Verifying program correctness is more difficult [source:cs1101s-lecture-lecture-l8-view-pdf#section-8].

Crucially, the [Lecture 02: Substitution Model, Recursion](y1s1-cs1101s-lecture-02) of evaluation breaks down when assignment is involved. It is not powerful enough to explain state. A more sophisticated model, the **Environment Model**, is required [source:cs1101s-lecture-lecture-l8-view-pdf#section-8].

#### Why Substitution Model Breaks Down
The substitution model treats a constant or variable merely as "just a name for a value" where its value will not change, allowing direct substitution. In contrast, assignment conceives of a variable as a "container" holding a value, where the contents of this container can change over time. This container is managed within a structure known as an **environment** [source:cs1101s-lecture-lecture-l8-view-pdf#section-11].

Consider the following simplified `make_simplified_withdraw` function [source:cs1101s-lecture-lecture-l8-view-pdf#section-9]:
```javascript
function make_simplified_withdraw(balance) {
    return amount => {
        balance = balance - amount;
        return balance;
    }
}
```
If we attempt to evaluate `(make_simplified_withdraw(25))(20);` using the substitution model, it would incorrectly return `25`, because `balance` is substituted as a constant value, not a mutable container [source:cs1101s-lecture-lecture-l8-view-pdf#section-9, cs1101s-lecture-lecture-l8-view-pdf#section-10].

### Environment Model (3.2)

An **environment** defines the context in which an expression is evaluated. Every expression is evaluated with respect to the **current environment** [source:cs1101s-lecture-lecture-l8-view-pdf#section-13].

#### Environments
An environment is a sequence of **frames**. Each frame contains **bindings** of values to names. A frame points to its **enclosing environment**, which is the next frame in the sequence, unless it is the global frame. **Extending an environment** means adding a new frame "inside" the old one [source:cs1101s-lecture-lecture-l8-view-pdf#section-14].

**Example Environments Diagram** [source:cs1101s-lecture-lecture-l8-view-pdf#section-15]:
```
+---------+        +---------+
| Frame I | <-- C--| Frame II|
| x: 3    |        | z: 6    |
| y: 5    |        | x: 7    |
+---------+        +---------+
    ^                  ^
    |                  |
    | A                | B
```
In this diagram:
*   A, B, C are environments.
*   The value of `x` in environment A is 7 (found in Frame II).
*   The value of `x` in environment B is 3 (found in Frame I, via Frame III's enclosing environment).
*   `x` in Frame II **shadows** `x` in Frame I (the local binding takes precedence).
*   The value of `m` in environment A is `unbound` (it's only in Frame III, which is not in A's enclosing chain) [source:cs1101s-lecture-lecture-l8-view-pdf#section-15].

#### Accessing an Environment
To evaluate a name:
1.  Look up its value in the **current frame**.
2.  If not found in the current frame, look in the **enclosing environment**, and so on, recursively [source:cs1101s-lecture-lecture-l8-view-pdf#section-16].
3.  If the name is still not found after traversing all enclosing environments, it is considered **unbound** in that environment [source:cs1101s-lecture-lecture-l8-view-pdf#section-16].

#### Global Environment
The global environment consists of a single frame that holds bindings for primitive and pre-declared functions and constants. The names of these functions are bound to their implementations. For clarity in diagrams:
*   `:=` is used for constants.
*   `:` is used for variables [source:cs1101s-lecture-lecture-l8-view-pdf#section-17].

Example global environment bindings [source:cs1101s-lecture-lecture-l8-view-pdf#section-17]:
```
global
environment   error  := <implementation>
              display:= <implementation>
              pair   := <implementation>
              list   := <implementation>
              math_PI:= 3.14...
              ...
```

#### Evaluation of Blocks
When a block `{ statements }` is evaluated, it extends the current environment by adding a **new frame** [source:cs1101s-lecture-lecture-l8-view-pdf#section-18].
*   This new frame contains bindings for the constants and variables declared within the block [source:cs1101s-lecture-lecture-l8-view-pdf#section-18].
*   Initially, these constants and variables do not have associated values (they are unassigned) [source:cs1101s-lecture-lecture-l8-view-pdf#section-18].
*   As the declarations are evaluated, the names are assigned their respective values [source:cs1101s-lecture-lecture-l8-view-pdf#section-18].
*   A new frame is **not** created if the block contains no constant or variable declarations, meaning there are no empty frames [source:cs1101s-lecture-lecture-l8-view-pdf#section-18].

The user program itself is treated as an implicit **program block** that directly extends the global environment, forming what is known as the **program environment** [source:cs1101s-lecture-lecture-l8-view-pdf#section-19].

**Example for Evaluating Blocks**:
Consider the following code snippet [source:cs1101s-lecture-lecture-l8-view-pdf#section-20]:
```javascript
let x = 3;
{
    const x = 5;
    let y = 8;
}
```
1.  **Initial State**: The program environment starts, extending the global environment [source:cs1101s-lecture-lecture-l8-view-pdf#section-20].
    ```
    global_env --(encloses)--> program_env
    ```
2.  **`let x = 3;`**: `x` is declared and bound to `3` in the program environment's frame [source:cs1101s-lecture-lecture-l8-view-pdf#section-21].
    ```
    global_env --(encloses)--> program_env { x: 3 }
    ```
3.  **Entering Block `{ ... }`**: A new frame is created for the block, enclosing the program environment. `x` (constant) and `y` (variable) are declared within this new frame, initially unassigned [source:cs1101s-lecture-lecture-l8-view-pdf#section-22].
    ```
    global_env --(encloses)--> program_env { x: 3 } --(encloses)--> Block_Frame { x:= ; y: }
    ```
4.  **`const x = 5;`**: `x` in the Block_Frame is assigned the value `5` [source:cs1101s-lecture-lecture-l8-view-pdf#section-23].
5.  **`let y = 8;`**: `y` in the Block_Frame is assigned the value `8` [source:cs1101s-lecture-lecture-l8-view-pdf#section-23].
    ```
    global_env --(encloses)--> program_env { x: 3 } --(encloses)--> Block_Frame { x:= 5 ; y: 8 }
    ```
Upon exiting the block, the Block_Frame is removed, and the environment reverts to the program environment.

#### Evaluation of Declarations and Assignments
*   **Constant/Variable Declaration Statements (`const name = value;`, `let name = value;`)**: These statements change the binding of `name` to `value` within the **current frame** [source:cs1101s-lecture-lecture-l8-view-pdf#section-24].
*   **Assignment Statement (`name = new_value;`)**: The system searches for `name` starting from the current frame and traversing up the enclosing environments. Once found, its binding is changed to `new_value` [source:cs1101s-lecture-lecture-l8-view-pdf#section-24].
    *   If `name` refers to a constant, an error is signaled [source:cs1101s-lecture-lecture-l8-view-pdf#section-24].
    *   If `name` is unbound or unassigned, an error is signaled [source:cs1101s-lecture-lecture-l8-view-pdf#section-24].

**Example Environments for Assignment** [source:cs1101s-lecture-lecture-l8-view-pdf#section-25, cs1101s-lecture-lecture-l8-view-pdf#section-27]:
Consider the initial environment structure:
```
+---------+        +---------+
| Frame I | <-- C--| Frame II|
| x: 3    |        | z: 6    |
| y: 5    |        | x: 7    |
+---------+        +---------+
    ^                  ^
    |                  |
    | A                | B
    w:                 m: 1
                       y: 2
```
1.  **Evaluate in A: `let w = 50;`**: A new binding for `w` with value `50` is added to Frame II (the current frame for environment A) [source:cs1101s-lecture-lecture-l8-view-pdf#section-25, cs1101s-lecture-lecture-l8-view-pdf#section-26].
    ```
    +---------+        +---------+
    | Frame I | <-- C--| Frame II|
    | x: 3    |        | z: 6    |
    | y: 5    |        | x: 7    |
    +---------+        | w: 50   |
        ^              +---------+
        |                  ^
        | A                | B
                           m: 1
                           y: 2
    ```
2.  **Evaluate in B: `x = x + 10;`**:
    *   First, `x` is looked up in environment B.
    *   Frame III is checked (`m:1, y:2` - no `x`).
    *   The enclosing environment, Frame I, is checked. `x:3` is found. The value is `3`.
    *   The expression `x + 10` evaluates to `3 + 10 = 13`.
    *   The assignment `x = 13` then updates the binding for `x` in Frame I (where it was found) [source:cs1101s-lecture-lecture-l8-view-pdf#section-27, cs1101s-lecture-lecture-l8-view-pdf#section-28].
    ```
    +---------+        +---------+
    | Frame I | <-- C--| Frame II|
    | x: 13   |        | z: 6    |
    | y: 5    |        | x: 7    |
    +---------+        | w: 50   |
        ^              +---------+
        |                  ^
        | A                | B
                           m: 1
                           y: 2
    ```
    Notice that `x` in Frame I was updated, but `x` in Frame II remains `7`.

**Block Example Walkthrough (Detailed)** [source:cs1101s-lecture-lecture-l8-view-pdf#section-29]
```javascript
let x = 3;
if (x <= 1) {
    let y = x;
    x = y + 1;
} else {
    let z = x;
    x = z * z;
}
{
    x = x + 1;
}
{
    let x = 5;
    let y = 8;
    {
        let x = 20 + y;
    }
    x = x + 1;
}
x;
```
*(The lecture slides provide a detailed step-by-step diagrammatic trace of this example, showing the creation and modification of frames and bindings for each line of code. Key steps include initial `let x = 3;` in program environment, then entering the `else` block (as `x` is 3, not `<= 1`). Inside the `else` block, a new frame is created, `let z = x;` binds `z` to the current `x` (which is `3` from the program environment), then `x = z * z;` updates the `x` in the program environment to `9`. The block `x = x + 1;` then updates the program environment `x` to `10`. A subsequent block creates its own frame, where `let x = 5; let y = 8;` define new, local `x` and `y`. A nested block for `let x = 20 + y;` creates another frame, binding `x` to `28`. Finally, `x = x + 1;` within the inner block updates its local `x` to `6`, and `y` in the same block remains `8`. The final `x;` evaluates to `10` from the program environment.)* [source:cs1101s-lecture-lecture-l8-view-pdf#section-30, cs1101s-lecture-lecture-l8-view-pdf#section-31, cs1101s-lecture-lecture-l8-view-pdf#section-32, cs1101s-lecture-lecture-l8-view-pdf#section-33, cs1101s-lecture-lecture-l8-view-pdf#section-34, cs1101s-lecture-lecture-l8-view-pdf#section-35, cs1101s-lecture-lecture-l8-view-pdf#section-36, cs1101s-lecture-lecture-l8-view-pdf#section-37, cs1101s-lecture-lecture-l8-view-pdf#section-38, cs1101s-lecture-lecture-l8-view-pdf#section-39, cs1101s-lecture-lecture-l8-view-pdf#section-40, cs1101s-lecture-lecture-l8-view-pdf#section-41, cs1101s-lecture-lecture-l8-view-pdf#section-42, cs1101s-lecture-lecture-l8-view-pdf#section-43]

#### Evaluation of Function Applications
Every function application extends the environment in which the function was created [source:cs1101s-lecture-lecture-l8-view-pdf#section-44].
*   A new frame is created for the function call. This frame contains bindings of the **parameter variables** to their corresponding **actual arguments** [source:cs1101s-lecture-lecture-l8-view-pdf#section-44].
*   If the function has no parameters, a new frame is not created [source:cs1101s-lecture-lecture-l8-view-pdf#section-44].
*   The function body block is then evaluated in this newly extended environment [source:cs1101s-lecture-lecture-l8-view-pdf#section-44].

#### Evaluation of Lambda Expressions
A lambda expression, such as `(var1, var2, ...) => { body }`, creates a **function object**. This object is conceptually represented as two interconnected parts (two circles) [source:cs1101s-lecture-lecture-l8-view-pdf#section-45]:
1.  One part points to the function's `body` (the text of the function) [source:cs1101s-lecture-lecture-l8-view-pdf#section-45].
2.  The other part points to the **environment in which the function expression was evaluated** [source:cs1101s-lecture-lecture-l8-view-pdf#section-45].
This means a function object inherently "remembers" the environment in which it was created, which is crucial for closures [source:cs1101s-lecture-lecture-l8-view-pdf#section-45].

**Example for Evaluating Lambda Expressions**:
If we declare `const square = x => x * x;` [source:cs1101s-lecture-lecture-l8-view-pdf#section-46]:
*   After evaluation, `square` in the `program_env` will bind to a function object.
*   This function object will have parameters `x` and a body `return x * x;`.
*   Its environment pointer will point back to the `program_env` (the environment in which `square` was defined) [source:cs1101s-lecture-lecture-l8-view-pdf#section-46].

**Example for Evaluating Function Declarations**:
A `function square(x) { return x * x; }` declaration is effectively equivalent to `const square = x => x * x;` for the purposes of environment modeling [source:cs1101s-lecture-lecture-l8-view-pdf#section-47].

#### Applying a Function Value to Argument Values
To evaluate a function application `fun(arg1, arg2, ..., argn);` [source:cs1101s-lecture-lecture-l8-view-pdf#section-48]:
1.  Evaluate the subexpressions (`fun`, `arg1`, `arg2`, etc.) in the current environment [source:cs1101s-lecture-lecture-l8-view-pdf#section-48].
2.  Apply the value of the function subexpression (`fun`) to the values of the argument subexpressions (`arg1`, `arg2`, ..., `argn`) [source:cs1101s-lecture-lecture-l8-view-pdf#section-48].
    This application involves these steps:
    *   Create a new frame that points to the **environment of the function** (the environment remembered by the function object when it was created) [source:cs1101s-lecture-lecture-l8-view-pdf#section-49].
    *   In this new frame, **bind the formal parameters to the actual arguments** [source:cs1101s-lecture-lecture-l8-view-pdf#section-49].
    *   Evaluate the **body block** of the function within this new environment [source:cs1101s-lecture-lecture-l8-view-pdf#section-49].

**Example: `square(5)`**
Given `const square = x => x * x;` [source:cs1101s-lecture-lecture-l8-view-pdf#section-50]:
1.  Evaluate subexpressions `square` and `5` in the program environment. `square` resolves to the function object, `5` evaluates to `5`.
2.  Create a new frame (E1) that points to the environment where `square` was created (the `program_env`).
3.  In E1, bind `x` (formal parameter) to `5` (actual argument).
4.  Evaluate the body `return x * x;` in E1. `x * x` evaluates to `5 * 5 = 25`.
5.  Return `25`. [source:cs1101s-lecture-lecture-l8-view-pdf#section-50]

#### Example with Local Declaration: `cube`
Consider `function cube(x) { const y = x * x * x; return y; }` and `cube(3);` [source:cs1101s-lecture-lecture-l8-view-pdf#section-51].
1.  After `cube` declaration, `cube` in `program_env` points to its function object, which remembers `program_env` [source:cs1101s-lecture-lecture-l8-view-pdf#section-52].
2.  When `cube(3)` is evaluated, a new frame E1 is created, pointing to `program_env`. `x` is bound to `3` in E1 [source:cs1101s-lecture-lecture-l8-view-pdf#section-53].
3.  Inside `cube`'s body, `const y = x * x * x;` is evaluated. A new frame E2 is created *within E1* (because `const y` is a declaration within the block). `y` is bound to `3 * 3 * 3 = 27` in E2 [source:cs1101s-lecture-lecture-l8-view-pdf#section-54].
4.  `return y;` evaluates `y` from E2, returning `27`. E2 and E1 are then discarded [source:cs1101s-lecture-lecture-l8-view-pdf#section-54, cs1101s-lecture-lecture-l8-view-pdf#section-55].

#### Example with Recursion: `factorial`
The recursive `function factorial(n) { return n <= 1 ? 1 : n * factorial(n - 1); }` for `factorial(2);` demonstrates how recursive calls create new frames [source:cs1101s-lecture-lecture-l8-view-pdf#section-56].
1.  `factorial` is declared in `program_env`, pointing to its function object [source:cs1101s-lecture-lecture-l8-view-pdf#section-57].
2.  `factorial(2)` is called. Frame E1 is created, `n` is bound to `2` in E1, enclosing `program_env` [source:cs1101s-lecture-lecture-l8-view-pdf#section-58].
3.  Inside E1, `factorial(n - 1)` (i.e., `factorial(1)`) is called. Frame E2 is created, `n` is bound to `1` in E2, enclosing `program_env` (the environment of the `factorial` function object) [source:cs1101s-lecture-lecture-l8-view-pdf#section-59].
4.  Inside E2, `n <= 1` is true, so `return 1;` evaluates and `1` is returned. E2 is discarded [source:cs1101s-lecture-lecture-l8-view-pdf#section-59, cs1101s-lecture-lecture-l8-view-pdf#section-60].
5.  Back in E1, `n * factorial(n - 1)` becomes `2 * 1`. This evaluates to `2`. E1 is discarded [source:cs1101s-lecture-lecture-l8-view-pdf#section-61, cs1101s-lecture-lecture-l8-view-pdf#section-62].
6.  The final result is `2`.

#### `make_withdraw` Example
This example illustrates closures and mutable state effectively [source:cs1101s-lecture-lecture-l8-view-pdf#section-63].
```javascript
function make_withdraw(balance) {
    return amount => {
        if (balance >= amount) {
            balance = balance - amount;
            return balance;
        } else {
            return "Insufficient funds";
        }
    };
}
const W1 = make_withdraw(100);
W1(40); // -> 60
```
1.  `make_withdraw` is declared in `program_env` [source:cs1101s-lecture-lecture-l8-view-pdf#section-64].
2.  `const W1 = make_withdraw(100);`
    *   `make_withdraw(100)` is called. A new frame (E_mw) is created, `balance` is bound to `100` in E_mw, enclosing `program_env` [source:cs1101s-lecture-lecture-l8-view-pdf#section-65].
    *   The `make_withdraw` body returns a new function (the `amount => ...` lambda). This new function's environment pointer will point to E_mw (where `balance` is `100`).
    *   `W1` in `program_env` is bound to this new function object [source:cs1101s-lecture-lecture-l8-view-pdf#section-66].
3.  `W1(40);`
    *   `W1` (the inner function) is called. A new frame (E_W1) is created, pointing to E_mw (the creation environment of the `W1` function object). `amount` is bound to `40` in E_W1 [source:cs1101s-lecture-lecture-l8-view-pdf#section-67].
    *   Inside E_W1, `balance` is looked up, found in E_mw as `100`. `amount` is `40`.
    *   `balance >= amount` (100 >= 40) is true.
    *   `balance = balance - amount;` updates the `balance` in E_mw from `100` to `60` [source:cs1101s-lecture-lecture-l8-view-pdf#section-67, cs1101s-lecture-lecture-l8-view-pdf#section-68].
    *   `return balance;` returns `60` from E_mw. E_W1 is discarded [source:cs1101s-lecture-lecture-l8-view-pdf#section-68, cs1101s-lecture-lecture-l8-view-pdf#section-69].
    The `balance` variable is private to the `make_withdraw` function's environment and persists across calls to `W1`.

If `const W2 = make_withdraw(100);` is then called, `W2` will have its *own* separate environment with its own `balance` variable, independent of `W1`'s `balance` [source:cs1101s-lecture-lecture-l8-view-pdf#section-70].

#### `update` Example
```javascript
function update(x) { x = x + 1; }
let y = 2;
update(y);
y; // -> 2
```
1.  `update` function and `y` variable are declared in `program_env`. `y` is `2` [source:cs1101s-lecture-lecture-l8-view-pdf#section-71, cs1101s-lecture-lecture-l8-view-pdf#section-72].
2.  `update(y)` is called. A new frame E is created, enclosing `program_env`. `x` (parameter) is bound to the *value* of `y` (which is `2`) [source:cs1101s-lecture-lecture-l8-view-pdf#section-73].
3.  Inside E, `x = x + 1;` updates the `x` in E from `2` to `3`. This `x` is local to E [source:cs1101s-lecture-lecture-l8-view-pdf#section-74].
4.  Function returns (implicitly `undefined`). E is discarded. The `y` in `program_env` remains `2` [source:cs1101s-lecture-lecture-l8-view-pdf#section-75].
This demonstrates that parameters are passed by value, and assignment to a parameter `x` inside a function does not affect the original variable `y` passed as an argument.

#### `pair_add_one` Example
This example demonstrates mutable data structures (pairs) [source:cs1101s-lecture-lecture-l8-view-pdf#section-76].
```javascript
function pair_add_one(p) {
    set_head(p, head(p) + 1);
    set_tail(p, tail(p) + 1);
}
const q = pair(2, 5);
pair_add_one(q);
q; // -> [3, 6]
```
1.  `pair_add_one` function is declared in `program_env`.
2.  `const q = pair(2, 5);` creates a pair object `[2, 5]` in memory. `q` in `program_env` points to this pair [source:cs1101s-lecture-lecture-l8-view-pdf#section-77].
3.  `pair_add_one(q);` is called. A new frame E is created, enclosing `program_env`. `p` (parameter) is bound to the *same pair object* that `q` points to [source:cs1101s-lecture-lecture-l8-view-pdf#section-78].
4.  Inside E:
    *   `set_head(p, head(p) + 1);` modifies the `head` of the shared pair object from `2` to `3`.
    *   `set_tail(p, tail(p) + 1);` modifies the `tail` of the shared pair object from `5` to `6` [source:cs1101s-lecture-lecture-l8-view-pdf#section-79].
5.  E is discarded. The original pair object, which `q` still points to, has been modified in place.
6.  `q;` now evaluates to `[3, 6]` [source:cs1101s-lecture-lecture-l8-view-pdf#section-80].
This shows that when a mutable object (like a pair) is passed as an argument, the function operates on the original object, and changes are observable outside the function. `p` and `q` are **sharing** the same pair object [source:cs1101s-lecture-lecture-l8-view-pdf#section-81].

#### Sharing and Identity
To check if two names are sharing the same object, we use the `===` operator for identity in Source §3 [source:cs1101s-lecture-lecture-l8-view-pdf#section-81, cs1101s-lecture-lecture-l8-view-pdf#section-83].
*   **Example 1 (Sharing)**:
    ```javascript
    const a = pair(2, 3);
    const b = a;
    a === b; // -> true
    ```
    Here, `a` and `b` both point to the *exact same* pair object [source:cs1101s-lecture-lecture-l8-view-pdf#section-81].
*   **Example 2 (Not Sharing)**:
    ```javascript
    const a = pair(2, 3);
    const b = pair(2, 3);
    a === b; // -> false
    ```
    Even though the contents are identical, `a` and `b` point to *two different* pair objects created independently [source:cs1101s-lecture-lecture-l8-view-pdf#section-81].

**Identity in Source §3: `===`** [source:cs1101s-lecture-lecture-l8-view-pdf#section-83]
*   `true`, `false`, `null`, `undefined`: Each is identical only to itself.
*   **Numbers**: Two numbers are identical if they have the same representation in double-precision floating-point.
*   **Strings**: Two strings are identical if they have the same characters in the same order.
*   **Functions**: Functions are created by function expressions, and their creation bestows a unique identity upon them.
*   **Pairs**: Pairs are created by the `pair` function, and their creation bestows a unique identity upon them.

**Structures Sharing Pairs Example**:
```javascript
const p = pair(3, 4);
const a = pair(2, p);
const b = pair(1, p);
tail(a) === tail(b); // -> true
```
In this case, `a` and `b` are distinct pairs, but their `tail` parts both point to the *same* `p` pair object. Hence, `tail(a)` and `tail(b)` are identical [source:cs1101s-lecture-lecture-l8-view-pdf#section-82].

#### Drawing Compound Structures
*   **Primitive values** (numbers, strings, Booleans, `null`) in bindings are drawn **inside** frames [source:cs1101s-lecture-lecture-l8-view-pdf#section-84].
*   **Compound structures** (pairs, function objects) are drawn **outside** frames, with pointers from the frame's bindings [source:cs1101s-lecture-lecture-l8-view-pdf#section-84].

**Example**:
```javascript
let n = 10;
let p = pair(2, 3);
let foo = x => x + 1;
```
This would be drawn with `n: 10` inside the frame, and `p:` and `foo:` pointing to objects `[2, 3]` and `function` respectively, which are drawn outside the frame [source:cs1101s-lecture-lecture-l8-view-pdf#section-84].

#### `curry` Example
The lecture introduces a curried function example [source:cs1101s-lecture-lecture-l8-view-pdf#section-85]:
```javascript
function curry(f) {
    return x => y => f(x, y);
}
curry(math_pow)(3)(4);
```
This example will be continued in Reflection R8 [source:cs1101s-lecture-lecture-l8-view-pdf#section-86].

### Summary
*   Assignment allows us to create objects with **state** [source:cs1101s-lecture-lecture-l8-view-pdf#section-87].
*   The Substitution Model breaks down when dealing with assignment [source:cs1101s-lecture-lecture-l8-view-pdf#section-87].
*   The **Environment Model** replaces the Substitution Model for programs with state [source:cs1101s-lecture-lecture-l8-view-pdf#section-87].
*   When a lambda expression is evaluated, it creates a **function object** that remembers its **current environment** (the environment it was created in) [source:cs1101s-lecture-lecture-l8-view-pdf#section-87].
*   To evaluate a function application:
    1.  Create a new frame in the function's environment (the environment pointed to by the function object's right pointer) [source:cs1101s-lecture-lecture-l8-view-pdf#section-87].
    2.  Bind parameters to actual arguments in this new frame [source:cs1101s-lecture-lecture-l8-view-pdf#section-87].
    3.  Evaluate the function's body block in this new environment [source:cs1101s-lecture-lecture-l8-view-pdf#section-87].

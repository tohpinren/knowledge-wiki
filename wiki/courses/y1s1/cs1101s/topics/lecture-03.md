---
page_id: "y1s1-cs1101s-lecture-03"
title: "Lecture 03: Higher-order Functions; Scope of Names"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 03: Higher-order Functions; Scope of Names consolidates the numbered lecture materials for this module. This lecture (CS1101S, Aug 24, 2022) focuses on Higher-order Functions and Scope of Names. Key recommenda..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l3-print-pdf#section-1"
  - "cs1101s-lecture-lecture-l3-print-pdf#section-2"
  - "cs1101s-lecture-lecture-l3-print-pdf#section-3"
  - "cs1101s-lecture-lecture-l3-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l3-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l3-view-pdf#section-3"
topics:
  - "function"
  - "functions"
  - "names"
  - "problem"
  - "include"
  - "can"
  - "sicp"
  - "recursion"
  - "using"
  - "nested"
source_count: 2
lecture_number: 3
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 03: Higher-order Functions; Scope of Names

This page provides a detailed overview of Lecture 03: Higher-order Functions; Scope of Names, delivered on August 24, 2022, as part of the CS1101S: Programming Methodology course [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1]. This lecture introduces advanced programming concepts such as higher-order functions and delves into the critical topic of name scope in programming. It consolidates materials from SICP JS Sections 1.2.2, 1.3.1, 1.3.2, 1.3.4, and 1.1.8 [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].

Key recommendations for students include consistently reading the textbook, utilizing the substitution model (with a stepper tool if necessary), thinking carefully before programming, and embracing the "less is more" principle [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].

## Announcements and Words of Advice

Several important announcements and pieces of advice were shared at the beginning of the lecture:
*   **Quests**: These are considered "extra homework." Students are strongly advised to avoid them if they are struggling with time management or work/life balance [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].
*   **Contests**: The "Beautiful Runes" contest opened today and concludes on August 30th. "My Room" customization also opened today and will close at the end of the semester [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].
*   **Reading Assessment 1**: Students must review the announcement from Prof Kok Lim, as sample questions have been uploaded [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].

**Words of Advice**:
*   Read the textbook thoroughly [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].
*   Use the [substitution model](y1s1-cs1101s-lecture-02#the-substitution-model) (and a stepper tool, if helpful) [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].
*   Think, then program [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].
*   "Less is more" [source:cs1101s-lecture-lecture-l3-print-pdf#section-1, cs1101s-lecture-lecture-l3-view-pdf#section-1].

## Nested Constant Declarations

Names in programming can refer to intermediate values, which improves readability and helps in breaking down complex expressions. This concept is illustrated with an example from SICP JS 1.3.2 [source:cs1101s-lecture-lecture-l3-print-pdf#section-2, cs1101s-lecture-lecture-l3-view-pdf#section-2].

Consider the mathematical function $f(x, y) = x(1 + xy)^2 + y(1 - y) + (1 + xy)(1 - y)$.
To compute $f(2, 3)$, we can define a function with nested constant declarations:

```javascript
function f(x, y) {
    const a = 1 + x * y; // Intermediate value for (1 + xy)
    const b = 1 - y;     // Intermediate value for (1 - y)
    return x * square(a) + y * b + a * b;
}
f(2, 3);
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-2, cs1101s-lecture-lecture-l3-view-pdf#section-2]

Here, `a` and `b` are local names that refer to intermediate computations, making the final return expression clearer and preventing redundant calculations.

## More Fun with Recursion

This section revisits recursion with several examples, building on concepts introduced in [[y1s1-cs1101s-lecture-02#recursion-an-elegant-pattern|Lecture 02: Substitution Model, Recursion]] [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].

### Example: Fractal Runes ("Rune Reading")

The task is to define a `fractal` function that generates fractal images, such as a pattern of hearts, given a base rune and a depth `n`. For example, `fractal(heart, 5)` [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].

#### Solution 1 (Tree Recursion)
A recursive approach (tree recursion) can generate the fractal.
```javascript
function fractal_1(rune, n) {
    return n === 1
        ? rune
        : beside(rune,
                 stack(fractal_1(rune, n - 1),
                       fractal_1(rune, n - 1)));
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]

A question posed is whether this function can be implemented with linear recursion [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]. Attempting to use a `const` declaration inside the conditional for a linear recursive call leads to a less intuitive structure:
```javascript
function fractal_2(rune, n) {
    const smaller_frac = fractal_2(rune, n - 1); // This would be called regardless of n === 1
    return n === 1
        ? rune
        : beside(rune,
                 stack(smaller_frac, smaller_frac));
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]

This `fractal_2` example is flawed because `smaller_frac` would always be evaluated, even for the base case `n === 1`, leading to infinite recursion.

#### Conditional Statements and Blocks (SICP JS 1.3.2)
To correctly handle local names within conditional branches, one can use `if-else` blocks:
```javascript
function fractal_3(rune, n) {
    if (n === 1) {
        return rune;
    } else {
        const f = fractal_3(rune, n - 1);
        return beside(rune, stack(f, f));
    }
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]
Key points about conditional statements:
*   Each branch of the conditional (`if` and `else`) is a block.
*   A block can have local names (e.g., `f`), which are only visible inside that block [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].
*   Always remember to `return` a result in each branch, otherwise `undefined` is returned [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].

#### Excursion 1: Fractals with Iterative Process
It is possible to implement fractals using an iterative process with an auxiliary function:
```javascript
function iter(rune, n, current_fractal) {
    return n === 1
        ? current_fractal
        : iter(rune, n - 1,
               beside(rune, stack(current_fractal,
                                  current_fractal)));
}

function fractal_4(rune, n) {
    return iter(rune, n, rune);
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]
This `fractal_4` function builds up the `current_fractal` iteratively.

#### Excursion 2: A "Divine" Solution
A more concise recursive solution can be achieved by applying the `fractal_5` transformation to the `stack` of runes:
```javascript
function fractal_5(rune, n) {
    return n === 1
        ? rune
        : beside(rune,
                 fractal_5(stack(rune, rune), n - 1));
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]
This solution elegantly combines the `stack` operation with the recursive call, reducing code complexity.

### Example: Rick the Rabbit
Rick the rabbit needs to climb `n` stairs. He can `hop` (1 step), `skip` (2 steps), or `jump` (3 steps) [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]. The problem is to find the number of different ways Rick can climb a flight of `n` stairs.

**Examples**:
*   For `n = 2` stairs: `hop hop`, `skip` (2 ways) [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].
*   For `n = 3` stairs: `hop hop hop`, `skip hop`, `hop skip`, `jump` (4 ways) [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].
*   What about 0 stairs? (1 way: do nothing)
*   What about -1 stairs? (0 ways: impossible)

**Recursive Structure**:
If Rick hops, `n - 1` stairs remain.
If Rick skips, `n - 2` stairs remain.
If Rick jumps, `n - 3` stairs remain [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].
This leads to a smaller problem where the number of stairs decreases.

**Source Code**:
```javascript
function rick_the_rabbit(n) {
    return n < 0
        ? 0                             // Base case: impossible to climb negative stairs
        : n === 0
        ? 1                             // Base case: one way to climb 0 stairs (do nothing)
        : rick_the_rabbit(n - 1) +      // Rick hops
          rick_the_rabbit(n - 2) +      // Rick skips
          rick_the_rabbit(n - 3);       // Rick jumps
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]

### Example: Coin Change (SICP JS 1.2.2)
The problem asks for the number of ways to change a given amount of money into coins, given different kinds of coins with unlimited supply [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].

**5-step Method of Problem Solving (CS1101S Problem Solving Method™)**:
1.  **Read the problem very carefully** [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].
2.  **Play with examples**:
    *   Amount = 10 cents, 20 cents, 5 cents, 0 cents, -1 cents.
    *   Consider different coin denominations (e.g., 5, 10, 20, 50, 100 cents) [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].
3.  **Think**: Look for existing solutions, apply divide-and-conquer, or use "wishful thinking" to break down the problem.
    *   Idea: The highest coin denomination is either used or not used. This creates two smaller subproblems [source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3].
    *   Identify base cases.
4.  **Program using Source**: Implement the solution.
5.  **Test your program**: Verify correctness with examples.

**Representing Kinds of Coins**:
An auxiliary function `first_denomination` can map a `kinds_of_coins` parameter (representing the count of available coin types) to the value of the highest denomination available:
```javascript
function first_denomination(kinds_of_coins) {
    return kinds_of_coins === 1 ? 5 :
           kinds_of_coins === 2 ? 10 :
           kinds_of_coins === 3 ? 20 :
           kinds_of_coins === 4 ? 50 :
           kinds_of_coins === 5 ? 100 : 0;
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]

**Recursive Idea and Base Cases**:
The number of ways to make change for an `amount` using `kinds_of_coins` is:
*   The number of ways to make change for `amount - first_denomination(kinds_of_coins)` using the same `kinds_of_coins` (if the highest coin is used).
*   PLUS the number of ways to make change for `amount` using `kinds_of_coins - 1` (if the highest coin is *not* used).

Base cases:
*   If `amount === 0`, there is 1 way (no coins needed).
*   If `amount < 0` or `kinds_of_coins === 0`, there are 0 ways (impossible).

**Source Code with Base Cases**:
```javascript
function cc(amount, kinds_of_coins) {
    return amount === 0
        ? 1
        : (amount < 0 || kinds_of_coins === 0)
        ? 0
        : cc(amount - first_denomination(kinds_of_coins),
             kinds_of_coins)
          +
          cc(amount, kinds_of_coins - 1);
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-3, cs1101s-lecture-lecture-l3-view-pdf#section-3]

## Higher-Order Functions

Higher-order functions are functions that can either take other functions as arguments or return functions as results [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].

### Functions as Arguments (SICP JS 1.3.1)
Functions can be passed as arguments to other functions.

**Example 1**:
```javascript
function f(g, x) {
    return g(x);
}
function g(y) {
    return y + 1;
}
f(g, 7); // Evaluates to g(7) which is 8
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

**Example 2 (More nested calls)**:
```javascript
function f(g, x) {
    return g(g(x));
}
function g(y) {
    return y + 1;
}
f(g, 7); // Evaluates to g(g(7)) which is g(8) which is 9
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

**Abstraction**: This concept is central to powerful abstractions, such as `repeat_pattern` in Rune programs or `transform_mosaic` from "Rune Trials" missions [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].
*   `repeat_pattern(4, make_cross, rcross);`
*   `function transform_mosaic(p1, p2, p3, p4, transform) { return transform(mosaic(p1, p2, p3, p4)); }`

**Sum Abstraction**:
Consider two similar summation functions:
*   `sum_integers(a, b)`: Sums integers from `a` to `b`
    ```javascript
    function sum_integers(a, b) {
        return a > b
            ? 0
            : a + sum_integers(a + 1, b);
    }
    ```
    [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]
*   `sum_skip_cubes(a, b)`: Sums cubes of numbers, skipping by 2, from `a` to `b`
    ```javascript
    function cube(x) { return x * x * x; }
    function sum_skip_cubes(a, b) {
        return a > b
            ? 0
            : cube(a) + sum_skip_cubes(a + 2, b);
    }
    ```
    [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

Both functions follow a similar pattern: a base case, an accumulation of a `term(a)`, and a recursive call with `next(a)`. This common pattern can be abstracted into a single `sum` higher-order function:

```javascript
function sum(term, a, next, b) {
    return a > b
        ? 0
        : term(a) + sum(term, next(a), next, b);
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

Now, `sum_integers` and `sum_skip_cubes` can be expressed using this `sum` abstraction:

*   `sum_integers` using `sum`:
    ```javascript
    function identity(x) { return x; }
    function plus_one(x) { return x + 1; }
    function sum_integers(a, b) {
        return sum(identity, a, plus_one, b);
    }
    ```
    [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]
*   `sum_skip_cubes` using `sum`:
    ```javascript
    function cube(x) { return x * x * x; }
    function plus_two(x) { return x + 2; }
    function sum_skip_cubes(a, b) {
        return sum(cube, a, plus_two, b);
    }
    ```
    [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

This demonstrates the power of abstraction and higher-order functions in creating reusable code patterns. The local helper functions `cube` and `plus_two` can be "hidden" inside `sum_skip_cubes` [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]:
```javascript
function sum_skip_cubes(a, b) {
    function cube(x) { return x * x * x; }
    function plus_two(x) { return x + 2; }
    return sum(cube, a, plus_two, b);
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

### Lambda Expressions (SICP JS 1.3.2)
While local function declarations work, they can be verbose. Lambda expressions (arrow functions in JavaScript) provide a more concise syntax for anonymous functions [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].

**Syntax**:
*   `(parameters) => expression`
*   If there is only one parameter, `parameter => expression` can be used (parentheses around parameters are optional) [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].

**Meaning**: A lambda expression evaluates to a function value. This function has the given `parameters` and `return expression` as its body [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].

**Alternative Syntax for Function Declaration**:
A traditional function like:
```javascript
function plus4(x) {
    return x + 4;
}
```
can be written concisely with a lambda expression:
```javascript
const plus4 = x => x + 4;
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

Using lambda expressions, `sum_skip_cubes` becomes even more compact:
```javascript
function sum_skip_cubes(a, b) {
    return sum(x => x * x * x,
               a,
               x => x + 2,
               b);
}
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

### Functions as Returned Values (SICP JS 1.3.4)
Functions can also return other functions [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].

**Example: `make_adder`**:
```javascript
function make_adder(x) {
    function adder(y) {
        return x + y;
    }
    return adder;
}
const adder_four = make_adder(4); // adder_four is now a function that adds 4
adder_four(6);                   // returns 10
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

Using lambda expressions, `make_adder` becomes more concise:
```javascript
function make_adder(x) {
    return y => x + y; // Returns a lambda function
}
const adder_four = make_adder(4); // adder_four is a function y => 4 + y
adder_four(6);                   // returns 10
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

This pattern is often seen in functional programming, enabling partial application and function composition.
You can also call it immediately: `(make_adder(4))(6);` or `make_adder(4)(6);` [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].

Multiple adders can be created, each "remembering" its `x` value:
```javascript
const adder_1 = make_adder(1);
const adder_2 = make_adder(2);
adder_1(10); // returns 11
adder_2(20); // returns 22
```
[source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4]

### Summary of New Constructs
*   Nested `const` and `function` declaration statements [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].
*   Conditional statements and blocks [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].
*   Lambda expressions [source:cs1101s-lecture-lecture-l3-print-pdf#section-4, cs1101s-lecture-lecture-l3-view-pdf#section-4].

## Scope of Names

Understanding the scope of names is crucial when dealing with nested functions and conditional statements [source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5].

### Examples of Scope
Let's examine how name occurrences refer to their declarations:

**Example 1**:
```javascript
const z = 2;
function f(g) {
    const z = 4;
    return g(z);
}
f(y => y + z);
```
Questions:
1.  What names are declared by this program? (`z`, `f`, `g`, `y`)
2.  Which declaration does each name occurrence refer to?
    *   The `z` in `const z = 2;` declares the global `z`.
    *   The `z` in `function f(g)` is a parameter to `f`.
    *   The `z` in `const z = 4;` declares a local `z` within `f`.
    *   The `z` in `return g(z);` refers to the local `z = 4`.
    *   The `z` in `y => y + z` refers to the global `z = 2` because the lambda is defined in the global environment, before `f` is called. The `g` parameter in `f` then receives this lambda.
    *   Therefore, `f(y => y + z)` with global `z=2` and `f`'s local `z=4` would result in `g(4)` (where `g` is `y => y+2`), giving `4+2 = 6`.
[source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5]

**Example 2**:
```javascript
const x = 10;
function square(x) {
    return x * x;
}
function addx(y) {
    return y + x;
}
square(x + 5) * addx(x + 20);
```
Question: Which declaration does each occurrence of `x` refer to?
*   `const x = 10;` declares the global `x`.
*   `function square(x)`: The `x` in the parameter list is local to `square`. The `x` in `return x * x;` refers to this local `x`.
*   `function addx(y)`: The `x` in `return y + x;` refers to the global `x = 10`.
*   `square(x + 5)`: The `x` in `x + 5` refers to the global `x = 10`. The result (`15`) is passed to `square`, so `square`'s local `x` becomes `15`.
*   `addx(x + 20)`: The `x` in `x + 20` refers to the global `x = 10`. The result (`30`) is passed to `addx`, so `addx`'s `y` becomes `30`.
    *   The overall evaluation is `square(15) * addx(30)` which is `(15*15) * (30+10)` = `225 * 40` = `9000`.
[source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5]

**Example 3**:
```javascript
const pi = 3.141592653589793;
function circle_area_from_radius(r) {
    const pi = 22 / 7;
    return pi * square(r);
}
```
Question: Which declaration does the occurrence of `pi` refer to?
*   `const pi = 3.14...` declares the global `pi`.
*   `function circle_area_from_radius(r)`: The `const pi = 22 / 7;` declares a local `pi` within this function.
*   The `pi` in `return pi * square(r);` refers to this local `pi` (22/7).
[source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5]

**Example 4: Hypotenuse**
```javascript
function square(x) {
    return x * x;
}
function hypotenuse(a, b) {
    function sum_of_squares() {
        return square(a) + square(b);
    }
    return math_sqrt(sum_of_squares());
}
```
Names can refer to declarations outside of the immediately surrounding function declaration [source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5]. Here, `sum_of_squares` uses `a` and `b` from its enclosing `hypotenuse` function, and `square` from the global scope.

### Overview of Scoping Rules
**Declarations are Mandatory**: All names in Source must be declared [source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5].

**Forms of Declaration**:
1.  **Pre-declared names**: Names like `math_floor` are pre-declared. Additional names can be imported from modules, e.g., `import { heart, quarter_turn_right } from "rune";` [source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5].
2.  **Constant declarations (`const`)**: The scope of a `const` declaration is the closest surrounding pair of curly braces `{}`, or the whole program if there is no surrounding block [source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5].
3.  **Parameters of function declarations and lambda expressions**: The scope of parameters is the body of the function [source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5].
4.  **Function name of function declarations**: The scope of a function name in a function declaration is as if the function was declared with `const` [source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5].

**Scoping Rule (Lexical Scoping)**: A name occurrence refers to the **closest surrounding declaration** [source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5].

**Lexical Scoping Example**:
```javascript
function f(x) {
    function g(w) {
        const x = 20; // This x is local to g
        const y = x + 1; // This x refers to g's local x (20), so y=21
        return x => w + x; // This x is a parameter to the returned lambda
    }
    return g(x); // This x refers to f's parameter x
}
```
If we call `f(10)`, the outer `x` is `10`. Inside `g`, `const x = 20` creates a new `x`. The `x` in `y = x + 1` refers to `g`'s `x` (20). The lambda `x => w + x` creates a new scope for *its* `x` parameter. The `w` in the lambda refers to `g`'s `w` parameter, which received `f`'s `x` (10). This implies `f(10)` returns a function that adds `10` to its argument.
[source:cs1101s-lecture-lecture-l3-print-pdf#section-5, cs1101s-lecture-lecture-l3-view-pdf#section-5]

## Important Ideas

*   **Hiding** can be a useful abstraction technique, preventing internal details from cluttering the outer scope [source:cs1101s-lecture-lecture-l3-print-pdf#section-6, cs1101s-lecture-lecture-l3-view-pdf#section-6].
*   **Recursion** is an elegant pattern of problem solving [source:cs1101s-lecture-lecture-l3-print-pdf#section-6, cs1101s-lecture-lecture-l3-view-pdf#section-6].
*   **Functions can be passed to functions** (functions as arguments) [source:cs1101s-lecture-lecture-l3-print-pdf#section-6, cs1101s-lecture-lecture-l3-view-pdf#section-6].
*   **Functions can be returned from functions** (functions as returned values) [source:cs1101s-lecture-lecture-l3-print-pdf#section-6, cs1101s-lecture-lecture-l3-view-pdf#section-6].
*   **Higher-order functions** are useful for building powerful abstractions [source:cs1101s-lecture-lecture-l3-print-pdf#section-6, cs1101s-lecture-lecture-l3-view-pdf#section-6].
*   With nested functions and conditional statements, it's essential to understand the **scope of names** [source:cs1101s-lecture-lecture-l3-print-pdf#section-6, cs1101s-lecture-lecture-l3-view-pdf#section-6].
*   The **CS1101S 5-step Method of Problem Solving™** provides a structured approach to tackle programming challenges [source:cs1101s-lecture-lecture-l3-print-pdf#section-6, cs1101s-lecture-lecture-l3-view-pdf#section-6].

## Concluding Unit 1

This lecture concludes Unit 1 of CS1101S, covering:
*   Textbook Chapter 1 [source:cs1101s-lecture-lecture-l3-print-pdf#section-7, cs1101s-lecture-lecture-l3-view-pdf#section-7].
*   The substitution model as a mental model for program evaluation [source:cs1101s-lecture-lecture-l3-print-pdf#section-7, cs1101s-lecture-lecture-l3-view-pdf#section-7].
*   Big ideas: iterative/recursive processes, higher-order functions, and scope [source:cs1101s-lecture-lecture-l3-print-pdf#section-7, cs1101s-lecture-lecture-l3-view-pdf#section-7].
*   Problem-solving technique: recursion ("wishful thinking") [source:cs1101s-lecture-lecture-l3-print-pdf#section-7, cs1101s-lecture-lecture-l3-view-pdf#section-7].

**Assessment in Unit 1**:
*   Reading Assessment 1 (Friday, Week 4) [source:cs1101s-lecture-lecture-l3-print-pdf#section-7, cs1101s-lecture-lecture-l3-view-pdf#section-7].
*   Mastery Check 1 (before Friday, Week 13) [source:cs1101s-lecture-lecture-l3-print-pdf#section-7, cs1101s-lecture-lecture-l3-view-pdf#section-7].
*   Missions/Quests: problem solving practice [source:cs1101s-lecture-lecture-l3-print-pdf#section-7, cs1101s-lecture-lecture-l3-view-pdf#section-7].

Unit 2, focusing on "Building Abstractions with Data," will commence with Lecture 04 [source:cs1101s-lecture-lecture-l3-print-pdf#section-7, cs1101s-lecture-lecture-l3-view-pdf#section-7].

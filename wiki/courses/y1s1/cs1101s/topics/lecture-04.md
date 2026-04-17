---
page_id: "y1s1-cs1101s-lecture-04"
title: "Lecture 04: Introduction to Data Abstraction"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 04: Introduction to Data Abstraction consolidates the numbered lecture materials for this module. This CS1101S lecture (August 31, 2022) by Low Kok Lim introduces data abstraction, focusing on case studies for..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l4-print-pdf#section-1"
  - "cs1101s-lecture-lecture-l4-print-pdf#section-2"
  - "cs1101s-lecture-lecture-l4-print-pdf#section-3"
  - "cs1101s-lecture-lecture-l4-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l4-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l4-view-pdf#section-3"
topics:
  - "list"
  - "data"
  - "using"
  - "pair"
  - "tail"
  - "lists"
  - "source"
  - "can"
  - "functions"
  - "abstraction"
source_count: 2
lecture_number: 4
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 04: Introduction to Data Abstraction

This page consolidates the materials for CS1101S Lecture 04: Introduction to Data Abstraction, delivered by Low Kok Lim on August 31, 2022. This lecture builds upon [[_pages/y1s1-cs1101s-lecture-03|functional abstraction]] by introducing data abstraction, focusing on rational numbers and constructing lists using pairs [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1].

---

## Announcements

Key announcements from this lecture included [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]:
*   **RA1**: Scheduled for Friday at 10 AM, with Zoom sessions.
*   **E-Exam Instructions**: Participants were advised to read instructions on LumiNUS.
*   **Mock Quiz**: Available to test computer setup.
*   **Zoom Session Assignment**: An announcement regarding assignments was pending.
*   **"The Choreographer" Contest**: Opened on the day of the lecture.
*   **Unit 1 Survey**: Opened on the day of the lecture and closed Saturday 23:59. Completing it via Google Form awarded 200 XP.

## Module Overview and Language Update

The course structure, following functional abstraction (SICP Chapter 1, Unit 1), now transitions to data abstraction (SICP Chapter 2, Unit 2). Subsequent units will cover State (SICP Chapter 3) and advanced topics (SICP Chapters 4 & 5) [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1].

With this unit, the course adopts **Source §2** as the new programming language. Documentation for Source §2 is available at `https://docs.sourceacademy.org/source_2/`. The Source Academy Playground is also updated to use Source §2 [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1].

## Data Structures and Pairs

Programming involves various types of values, including numbers, booleans, strings, and functions. This lecture introduces `pairs` and the `empty list` as fundamental data types in Source [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1].

### Recalling `first_denomination` as a Data Structure

The `first_denomination` function from a previous lecture (L3) can be viewed as a basic data structure. It "stores" five values and "retrieves" them based on a given index [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]:

```javascript
function first_denomination(kinds_of_coins) {
    return kinds_of_coins === 1 ? 5 :
           kinds_of_coins === 2 ? 10 :
           kinds_of_coins === 3 ? 20 :
           kinds_of_coins === 4 ? 50 :
           kinds_of_coins === 5 ? 100 : 0;
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]

This example illustrates the two key operations on data structures:
*   **Constructing** the data structure: done via function declaration/definition (e.g., `function first_denomination(kinds) { ... }`) [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1].
*   **Selecting** components from the data structure: done via function application (e.g., `first_denomination(3)`) [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1].

### The Simplest Data Structure: A Pair

Data structures are ubiquitous in mathematics (tuples, sets, matrices). The simplest possible data structure is a **pair** [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1].
*   In mathematics, pairs are constructed using tuple notation, e.g., `(0.5, 0.25)`.
*   Components are selected using pattern matching, e.g., "Let `p` be `(x, y)`, for some `x` and `y`..." [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1].

In programming, a similar concept is seen with points in "Curve Missions," where a point `p` can be constructed and its components `x` and `y` selected [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]:

```javascript
// Construct:
const p = make_point(0.5, 0.25);

// Select:
const x = x_of(p);
const y = y_of(p);
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]

A point abstraction can be defined using functions that return other functions (closures) [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]:

```javascript
function make_point(x, y) {
    return component =>
           component === 0 ? x : y;
}

function x_of(p) {
    return p(0);
}

function y_of(p) {
    return p(1);
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]

To make this more generic for any pair of values, we use the names `pair`, `head`, and `tail` [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]:

```javascript
function pair(x, y) {
    return component =>
           component === 0 ? x : y;
}

function head(p) {
    return p(0);
}

function tail(p) {
    return p(1);
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]

An alternative, more concise way to define `pair`, `head`, and `tail` uses lambda expressions [source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]:

```javascript
const pair = (x, y) => f => f(x, y);
const head = p => p((x, y) => x);
const tail = p => p((x, y) => y);
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-1, cs1101s-lecture-lecture-l4-view-pdf#section-1]

## Case Study: Rational Numbers

A **rational number** can be represented as a pair consisting of a numerator and a denominator [source:cs1101s-lecture-lecture-l4-print-pdf#section-2, cs1101s-lecture-lecture-l4-view-pdf#section-2].

### Constructor and Selectors for Rational Numbers

In Source, we can define the constructor `make_rat` and selectors `numer` and `denom` using the `pair`, `head`, and `tail` functions [source:cs1101s-lecture-lecture-l4-print-pdf#section-2, cs1101s-lecture-lecture-l4-view-pdf#section-2]:

```javascript
function make_rat(n, d) {
    return pair(n, d);
}

function numer(x) {
    return head(x);
}

function denom(x) {
    return tail(x);
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-2, cs1101s-lecture-lecture-l4-view-pdf#section-2]

### Arithmetic Operations

With these basic functions, we can implement arithmetic operations for rational numbers [source:cs1101s-lecture-lecture-l4-print-pdf#section-3, cs1101s-lecture-lecture-l4-view-pdf#section-3]:

*   **Addition**: $\frac{n_1}{d_1} + \frac{n_2}{d_2} = \frac{n_1d_2 + n_2d_1}{d_1d_2}$
    ```javascript
    function add_rat(x, y) {
        return make_rat(numer(x) * denom(y) +
                        numer(y) * denom(x),
                        denom(x) * denom(y));
    }
    ```
    [source:cs1101s-lecture-lecture-l4-print-pdf#section-3, cs1101s-lecture-lecture-l4-view-pdf#section-3]

*   **Subtraction**: $\frac{n_1}{d_1} - \frac{n_2}{d_2} = \frac{n_1d_2 - n_2d_1}{d_1d_2}$
    ```javascript
    function sub_rat(x, y) {
        return make_rat(numer(x) * denom(y) -
                        numer(y) * denom(x),
                        denom(x) * denom(y));
    }
    ```
    [source:cs1101s-lecture-lecture-l4-print-pdf#section-3, cs1101s-lecture-lecture-l4-view-pdf#section-3]

*   **Multiplication**: $\frac{n_1}{d_1} \times \frac{n_2}{d_2} = \frac{n_1n_2}{d_1d_2}$
    ```javascript
    function mul_rat(x, y) {
        return make_rat(numer(x) * numer(y),
                        denom(x) * denom(y));
    }
    ```
    [source:cs1101s-lecture-lecture-l4-print-pdf#section-3, cs1101s-lecture-lecture-l4-view-pdf#section-3]

*   **Division**: $\frac{n_1}{d_1} \div \frac{n_2}{d_2} = \frac{n_1d_2}{d_1n_2}$
    ```javascript
    function div_rat(x, y) {
        return make_rat(numer(x) * denom(y),
                        denom(x) * numer(y));
    }
    ```
    [source:cs1101s-lecture-lecture-l4-print-pdf#section-3, cs1101s-lecture-lecture-l4-view-pdf#section-3]

### Equality of Rational Numbers

Comparing rational numbers requires careful handling. A naive approach compares numerators and denominators directly [source:cs1101s-lecture-lecture-l4-print-pdf#section-3, cs1101s-lecture-lecture-l4-view-pdf#section-3]:

*   **First attempt (incorrect)**:
    ```javascript
    function equal_rat(x, y) {
        return numer(x) === numer(y) &&
               denom(x) === denom(y);
    }
    ```
    [source:cs1101s-lecture-lecture-l4-print-pdf#section-3, cs1101s-lecture-lecture-l4-view-pdf#section-3]
    This fails for equivalent rational numbers like `1/2` and `2/4`.

*   **Second attempt (correct)**: Based on cross-multiplication: $\frac{n_1}{d_1} = \frac{n_2}{d_2} \iff n_1d_2 = n_2d_1$
    ```javascript
    function equal_rat(x, y) {
        return numer(x) * denom(y) ===
               numer(y) * denom(x);
    }
    ```
    [source:cs1101s-lecture-lecture-l4-print-pdf#section-3, cs1101s-lecture-lecture-l4-view-pdf#section-3]

### Printing and Reducing Rational Numbers

To print rational numbers in a user-friendly format, a `rat_to_string` function can be used [source:cs1101s-lecture-lecture-l4-print-pdf#section-4, cs1101s-lecture-lecture-l4-view-pdf#section-4]:

```javascript
function rat_to_string(x) {
    return stringify(numer(x)) +
           " / " +
           stringify(denom(x));
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-4, cs1101s-lecture-lecture-l4-view-pdf#section-4]

Without reduction, operations might yield unsimplified fractions like `6/9`. To address this, rational numbers should be represented in their simplest form by dividing the numerator and denominator by their **greatest common divisor (GCD)** [source:cs1101s-lecture-lecture-l4-print-pdf#section-4, cs1101s-lecture-lecture-l4-view-pdf#section-4].

The GCD can be computed using **Euclid's algorithm**:
```javascript
function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-4, cs1101s-lecture-lecture-l4-view-pdf#section-4]

The `make_rat` constructor can then be modified to automatically reduce the rational number [source:cs1101s-lecture-lecture-l4-print-pdf#section-4, cs1101s-lecture-lecture-l4-view-pdf#section-4]:

```javascript
function make_rat(n, d) {
    const g = gcd(n, d);
    return pair(n / g, d / g);
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-4, cs1101s-lecture-lecture-l4-view-pdf#section-4]

This reduction ensures that equivalent rational numbers like `1/3` and `2/6` will have the same internal representation (`1/3`), making direct equality checks (like the first attempt for `equal_rat`) more effective if applied after reduction, though the cross-multiplication method remains robust.

### Summary of Rational Numbers Case Study

*   **Pairs** can be effectively used to represent complex data like rational numbers.
*   **Constructor and selector functions** (`make_rat`, `numer`, `denom`) are used to implement operations on these data structures.
*   A well-designed **library hides the internal representation** of data, allowing users to interact with a higher-level abstraction without needing to know implementation details [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5].

## Making Lists with Pairs

The lecture then extends the concept of pairs to build **lists** [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5].

### Motivation and Discipline

To represent a sequence of items, such as coin denominations (100, 50, 20, 10, 5), we can link pairs together. However, there are many ways to nest pairs, leading to different retrieval methods [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5]:

```javascript
// Example of various pair structures:
pair(pair(100, 50), pair(20, pair(10, 5)))
pair(100, pair(pair(50, 20), pair(10, 5)))
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5]

To impose order and consistency, a **discipline** is introduced for lists:
*   `head(p)` always contains the **data element**.
*   `tail(p)` always contains the **remaining elements** (which form another list) [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5].

Following this principle, a list of denominations `(100, 50, 20, 10, 5)` would be structured as [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5]:

```javascript
const denoms = pair(100, pair(50, pair(20, pair(10, 5))));

head(denoms)     // -> 100
tail(denoms)     // -> pair(50, pair(20, pair(10, 5)))
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5]

### The Empty List: `null`

A special **base case** is needed to represent the end of a list. In Source, the special value `null` is used to represent the empty list [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5].

Thus, the formal **definition of a list in Source** is:
"A list is either `null` or a pair whose tail is a list" [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5].

Using `null`, the `first_denomination` list would look like [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5]:

```javascript
const first_denomination =
    pair(100,
        pair(50,
            pair(20,
                pair(10,
                    pair(5, null)))));
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5]

### Retrieving Data from a List

Data can be retrieved by repeatedly applying `head` and `tail` [source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5]:

```javascript
const denoms = pair(100, pair(50, pair(20, pair(10, pair(5, null)))));

head(denoms)                                        // -> 100
head(tail(denoms))                                  // -> 50
head(tail(tail(denoms)))                            // -> 20
head(tail(tail(tail(denoms))))                      // -> 10
head(tail(tail(tail(tail(denoms)))))                // -> 5
tail(tail(tail(tail(tail(denoms)))))                // -> null
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-5, cs1101s-lecture-lecture-l4-view-pdf#section-5]

## LISTS Functions in Source §2

Source §2 provides built-in functions for working with pairs and lists [source:cs1101s-lecture-lecture-l4-print-pdf#section-6, cs1101s-lecture-lecture-l4-view-pdf#section-6]:

*   `pair(x, y)`: Returns a pair made of `x` and `y`.
*   `is_pair(p)`: Returns `true` if `p` is a pair, `false` otherwise.
*   `null`: Represents an empty list.
*   `is_null(xs)`: Returns `true` if `xs` is the empty list `null`, `false` otherwise.
*   `head(p)`: Returns the head (first component) of the pair `p`.
*   `tail(p)`: Returns the tail (second component) of the pair `p`.
*   `list(x1, ..., xn)`: A variadic function that returns a list whose first element is `x1`, second is `x2`, and so on, with the last element being `xn`. This simplifies list creation compared to manual `pair` and `null` nesting [source:cs1101s-lecture-lecture-l4-print-pdf#section-6, cs1101s-lecture-lecture-l4-view-pdf#section-6].

Example using `list` [source:cs1101s-lecture-lecture-l4-print-pdf#section-6, cs1101s-lecture-lecture-l4-view-pdf#section-6]:

```javascript
// Manual way:
const first_denomination_manual =
    pair(100, pair(50, pair(20, pair(10, pair(5, null)))));

// Using list function (shorter):
const first_denomination_list = list(100, 50, 20, 10, 5);
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-6, cs1101s-lecture-lecture-l4-view-pdf#section-6]

### List Notations and Diagrams

Source §2 also offers various notations for printing and visualizing list structures [source:cs1101s-lecture-lecture-l4-print-pdf#section-7, cs1101s-lecture-lecture-l4-view-pdf#section-7]:

*   **Box Notation**: `pair(x, y)` is printed as `[x, y]`. Empty lists are printed as `null`.
    *   Example: `pair(1, pair(2, pair(3, null)))` is printed as `[1, [2, [3, null]]]` [source:cs1101s-lecture-lecture-l4-print-pdf#section-7, cs1101s-lecture-lecture-l4-view-pdf#section-7].

*   **List Notation**: Similar to box notation, but any sub-structure that is a list is formatted as `list(...)`. The `display_list(x)` function can be used to show a value `x` in list notation [source:cs1101s-lecture-lecture-l4-print-pdf#section-7, cs1101s-lecture-lecture-l4-view-pdf#section-7].
    *   Example: `display_list(pair(pair(pair(7, 8), pair(1, pair(2, null))), 6))` prints `[list([7, 8], 1, 2), 6]` [source:cs1101s-lecture-lecture-l4-print-pdf#section-7, cs1101s-lecture-lecture-l4-view-pdf#section-7].

*   **Box-and-Pointer Diagrams**: These are graphical representations of data structures made of pairs. The Source Academy Playground's Data Visualizer tool can generate these diagrams using the `draw_data` pre-declared function [source:cs1101s-lecture-lecture-l4-print-pdf#section-7, cs1101s-lecture-lecture-l4-view-pdf#section-7].
    *   Example: `draw_data(pair(1, pair(2, pair(3, null))));` would produce a visual diagram of linked boxes [source:cs1101s-lecture-lecture-l4-print-pdf#section-7, cs1101s-lecture-lecture-l4-view-pdf#section-7].

### Error Reporting for List Functions

Functions like `head(xs)` and `tail(xs)` expect their argument `xs` to be a pair. If `xs` is not a pair, a descriptive error message will be printed [source:cs1101s-lecture-lecture-l4-print-pdf#section-8, cs1101s-lecture-lecture-l4-view-pdf#section-8].

## Length of a List

The **length** of a list is defined recursively [source:cs1101s-lecture-lecture-l4-print-pdf#section-8, cs1101s-lecture-lecture-l4-view-pdf#section-8]:
*   The length of the empty list (`null`) is `0`.
*   The length of a non-empty list is one more than the length of its tail.

Examples [source:cs1101s-lecture-lecture-l4-print-pdf#section-8, cs1101s-lecture-lecture-l4-view-pdf#section-8]:
*   Length of `null` is `0`.
*   Length of `pair(10, null)` is `1`.
*   Length of `pair(10, pair(20, pair(30, null)))` is `3`.

### Computing List Length

The length of a list can be computed using a **recursive process** [source:cs1101s-lecture-lecture-l4-print-pdf#section-8, cs1101s-lecture-lecture-l4-view-pdf#section-8]:

```javascript
function length(xs) {
    return is_null(xs)
           ? 0
           : 1 + length(tail(xs));
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-8, cs1101s-lecture-lecture-l4-view-pdf#section-8]

Alternatively, an **iterative process** can be used [source:cs1101s-lecture-lecture-l4-print-pdf#section-8, cs1101s-lecture-lecture-l4-view-pdf#section-8]:

```javascript
function length_iter(xs) {
    function len(ys, counted_so_far) {
        return is_null(ys)
               ? counted_so_far
               : len(tail(ys), counted_so_far + 1);
    }
    return len(xs, 0);
}
```
[source:cs1101s-lecture-lecture-l4-print-pdf#section-8, cs1101s-lecture-lecture-l4-view-pdf#section-8]

## Summary

This lecture established key concepts related to data abstraction [source:cs1101s-lecture-lecture-l4-print-pdf#section-8, cs1101s-lecture-lecture-l4-view-pdf#section-8]:
*   Data structures are fundamental in programming.
*   **Pairs** serve as the most basic building blocks for complex data.
*   The **rational numbers** case study demonstrated how to use pairs with constructor and selector functions to create a higher-level abstraction, hiding internal representations.
*   A **list discipline** was introduced, defining lists recursively using `pairs` and `null`.
*   Built-in **LISTS functions** in Source §2 (`pair`, `head`, `tail`, `list`, `is_pair`, `is_null`, `null`) simplify list manipulation.
*   Various **notations** (Box notation, List notation) and **Box-and-pointer diagrams** help visualize data structures.
*   Recursive and iterative approaches were shown for computing the **length of a list**.

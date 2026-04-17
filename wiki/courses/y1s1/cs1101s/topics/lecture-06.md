---
page_id: "y1s1-cs1101s-lecture-06"
title: "Lecture 06: Sorting and Symbolic Processing"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 06: Sorting and Symbolic Processing consolidates the numbered lecture materials for this module. This CS1101S lecture, presented by Low Kok Lim on September 14, 2022, covered Binary Search and Binary Search Tr..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l6-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l6-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l6-view-pdf#section-3"
topics:
  - "search"
  - "binary"
  - "symbolic"
  - "sort"
  - "entries"
  - "subtree"
  - "using"
  - "september"
  - "lecture"
  - "sorting"
source_count: 1
lecture_number: 6
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 06: Sorting and Symbolic Processing

This page provides a detailed overview of Lecture 06 for CS1101S: Programming Methodology, delivered by Low Kok Lim on September 14, 2022. The lecture covered fundamental topics in data structures and algorithms, including binary search, various sorting algorithms, symbolic processing, and principles of data structure design [source:cs1101s-lecture-lecture-l6-view-pdf#section-1, cs1101s-lecture-lecture-l6-view-pdf#section-2].

### Announcements

*   Next week is Recess Week [source:cs1101s-lecture-lecture-l6-view-pdf#section-3].
*   A Midterm Assessment is scheduled for Wednesday of Week 7 (September 28) at 10 AM [source:cs1101s-lecture-lecture-l6-view-pdf#section-3].
*   A remedial class is planned for Friday evening [source:cs1101s-lecture-lecture-l6-view-pdf#section-3].
*   A guest speaker from Jane Street will give a talk on Friday, with the title to be announced [source:cs1101s-lecture-lecture-l6-view-pdf#section-3].

### Update on Contests

*   The contest "Games of Tones" opened on Monday and is due on September 22 [source:cs1101s-lecture-lecture-l6-view-pdf#section-4].
*   Voting for "The Choreographer" contest concluded yesterday [source:cs1101s-lecture-lecture-l6-view-pdf#section-4].

---

### Binary Search and Binary Search Trees (2.3.3)

#### Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half. The core idea can be illustrated with a "Guess the Secret Number" game [source:cs1101s-lecture-lecture-l6-view-pdf#section-6].

**Game: Guess the Secret Number**
Imagine a secret integer in the range \[1, 100]. Your goal is to minimize the number of guesses. After each guess, you are told if your guess is "correct", "too low", or "too high" [source:cs1101s-lecture-lecture-l6-view-pdf#section-6].

**Strategy:**
1.  Guess the "middle" number (e.g., 50 for \[1, 100]).
2.  If the guess is "too low", continue searching in the "right" half (numbers larger than your guess).
3.  If the guess is "too high", continue searching in the "left" half (numbers smaller than your guess) [source:cs1101s-lecture-lecture-l6-view-pdf#section-6].
This strategy is Binary Search.

**Implementation Example:**

```javascript
const N = 100;

function guess_secret_num(start, end) {
    if (start === end) {
        return start;
    } else {
        const guess = math_floor((start + end) / 2);
        const check = check_guess(guess); // Assume check_guess is provided
        return check === "correct"
            ? guess
            : check === "too low"
            ? guess_secret_num(guess + 1, end) // when "too low", search right half
            : guess_secret_num(start, guess - 1); // when "too high", search left half
    }
}

guess_secret_num(1, N);
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-7]

**Observations:**
*   **Run time:** At each step (for a wrong guess), the search space is cut in half. If the problem size is $N = 2^k$, it reaches size 1 after $k$ steps. Therefore, the runtime is $O(\log_2 N)$, which is equivalent to $O(\log N)$ [source:cs1101s-lecture-lecture-l6-view-pdf#section-8].
*   **Why it works:** Binary Search relies on the assumption that all numbers to the "left" of the secret number are "too low," and all numbers to the "right" are "too high." This implies a total order among the elements [source:cs1101s-lecture-lecture-l6-view-pdf#section-8].

#### Binary Search for Entries

To apply binary search for a collection of entries (e.g., checking if an entry is included), two properties are necessary [source:cs1101s-lecture-lecture-l6-view-pdf#section-9]:
1.  **Total Order**: A total order must exist, meaning any two entries can be compared (one is "smaller," "larger," or "equal" to the other). Examples include numbers and strings [source:cs1101s-lecture-lecture-l6-view-pdf#section-9].
2.  **Efficiency**: The ability to reach any "middle" entry in $O(1)$ time. This often necessitates a special data structure [source:cs1101s-lecture-lecture-l6-view-pdf#section-9].

#### Binary Trees

A **binary tree** is a recursive data structure defined as either [source:cs1101s-lecture-lecture-l6-view-pdf#section-10]:
*   The empty tree.
*   A structure containing:
    *   An **entry** (the data item).
    *   A **left branch** or **left subtree** (which is itself a binary tree).
    *   A **right branch** or **right subtree** (which is also a binary tree) [source:cs1101s-lecture-lecture-l6-view-pdf#section-10].

Visually, a node contains an entry, and pointers to its left and right subtrees (branches) [source:cs1101s-lecture-lecture-l6-view-pdf#section-10].

#### Binary Search Trees (BST)

A **binary search tree (BST)** is a specific type of binary tree that maintains a crucial property:
*   All entries in the **left subtree** are **smaller than** the entry in the current node.
*   All entries in the **right subtree** are **larger than** the entry in the current node [source:cs1101s-lecture-lecture-l6-view-pdf#section-11].

A BST serves as an abstraction for binary search, allowing efficient search, insertion, and deletion operations while preserving the sorted order property [source:cs1101s-lecture-lecture-l6-view-pdf#section-11].

**Mission "Search and Rescue"**:
Given a BST of Strings, two problems are typically addressed:
1.  **Problem 1**: Check if a given String occurs in the BST, using the BST property for efficiency.
2.  **Problem 2**: Add a new string to the BST, ensuring the BST property is preserved [source:cs1101s-lecture-lecture-l6-view-pdf#section-12].

---

### Sorting

Sorting is the process of arranging elements of a list in a specific order.

#### The Problem of Sorting

*   **Given**: A list `xs` of elements from a universe `X`, and a total order on `X` [source:cs1101s-lecture-lecture-l6-view-pdf#section-14].
*   **Wanted**: A permutation of `xs` such that each element is greater than or equal to the previous one, with respect to the total order [source:cs1101s-lecture-lecture-l6-view-pdf#section-14].
*   **Operations**: The only allowed operations on elements are comparisons (e.g., `<`, `>`, `<=`, `>=`, `===`, `!==`) [source:cs1101s-lecture-lecture-l6-view-pdf#section-14].

#### How to Sort a List with `n` Elements?

The general strategy for sorting involves "wishful thinking," imagining that we can sort lists with `m` elements where `m < n` [source:cs1101s-lecture-lecture-l6-view-pdf#section-15]. Two main approaches are:
*   **Approach A**: `m = n - 1` (e.g., sorting the tail of the list).
*   **Approach B**: `m = n / 2` (e.g., splitting the list in half) [source:cs1101s-lecture-lecture-l6-view-pdf#section-15].

#### Approach A: Insertion Sort

**Idea:**
1.  Sort the tail of the given list (using wishful thinking).
2.  Insert the head of the original list into its correct sorted position within the sorted tail [source:cs1101s-lecture-lecture-l6-view-pdf#section-16].

**Implementation:**

```javascript
function insert(x, xs) {
    return is_null(xs)
        ? list(x)
        : x <= head(xs)
        ? pair(x, xs)
        : pair(head(xs), insert(x, tail(xs)));
}

function insertion_sort(xs) {
    return is_null(xs)
        ? xs
        : insert(head(xs), insertion_sort(tail(xs)));
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-17]

The order of growth in time for Insertion Sort is generally $O(N^2)$ in the worst and average cases, as inserting an element into a list of size $k$ can take $O(k)$ time, and this is done $N$ times.

#### Approach A: Selection Sort

**Idea:**
1.  Find the smallest element `x` in the list and remove it.
2.  Sort the remaining list (using wishful thinking).
3.  Put `x` in front of the sorted remaining list [source:cs1101s-lecture-lecture-l6-view-pdf#section-18].

**Implementation:**

```javascript
// find smallest element of non-empty list xs
function smallest(xs) {
    return accumulate((x, y) => x < y ? x : y,
                      head(xs), tail(xs));
}

function selection_sort(xs) {
    if (is_null(xs)) {
        return xs;
    } else {
        const x = smallest(xs);
        return pair(x, selection_sort(remove(x, xs))); // remove function not shown, assumes it removes x from xs
    }
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-19]

The order of growth in time for Selection Sort is also typically $O(N^2)$ because finding the smallest element takes $O(N)$ time, and this operation is repeated $N$ times.

#### Approach B: Merge Sort

This approach falls under the `m = n / 2` strategy, which is generally more efficient for larger lists [source:cs1101s-lecture-lecture-l6-view-pdf#section-20].

**Idea:**
1.  **Split** the list in half.
2.  **Sort** each half using wishful thinking (recursively apply Merge Sort).
3.  **Merge** the two sorted halves together into a single sorted list [source:cs1101s-lecture-lecture-l6-view-pdf#section-20, cs1101s-lecture-lecture-l6-view-pdf#section-21].

**Implementation (`merge_sort`):**

```javascript
function merge_sort(xs) {
    if (is_null(xs) || is_null(tail(xs))) {
        return xs; // Base case: empty list or single-element list is already sorted
    } else {
        const mid = middle(length(xs)); // middle, take, drop are helper functions
        return merge(merge_sort(take(xs, mid)),
                     merge_sort(drop(xs, mid)));
    }
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-21]

**Implementation (`merge` function):**
The `merge` function takes two *already sorted* lists (`xs` and `ys`) and combines them into one sorted list [source:cs1101s-lecture-lecture-l6-view-pdf#section-22].

```javascript
function merge(xs, ys) {
    if (is_null(xs)) {
        return ys;
    } else if (is_null(ys)) {
        return xs;
    } else {
        const x = head(xs);
        const y = head(ys);
        return x < y
            ? pair(x, merge(tail(xs), ys))
            : pair(y, merge(xs, tail(ys)));
    }
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-22]

**Other Helper Functions (for `merge_sort`):**
*   `middle(n)`: Returns the floor of `n / 2`.
*   `take(xs, n)`: Returns the first `n` elements of `xs`.
*   `drop(xs, n)`: Returns `xs` with the first `n` elements removed [source:cs1101s-lecture-lecture-l6-view-pdf#section-23].

The order of growth in time for Merge Sort will be discussed in Reflection R6 [source:cs1101s-lecture-lecture-l6-view-pdf#section-24]. Generally, it is $O(N \log N)$.

#### Approach B: QuickSort

QuickSort is another divide-and-conquer sorting algorithm that also uses a "splitting" and "combining" approach, different from Merge Sort. Further details are explored in Mission "Sorting Things Out" [source:cs1101s-lecture-lecture-l6-view-pdf#section-25].

---

### Symbolic Processing (2.3.2)

Symbolic processing involves representing and manipulating mathematical expressions themselves, rather than just their numerical values.

#### Representing Functions: Directly

Traditionally, functions are represented using `function` declarations or lambda expressions in Source [source:cs1101s-lecture-lecture-l6-view-pdf#section-27].

**Example:**

```javascript
function my_fun(x) {
    return x * x + 1;
}

function eval_numeric(f, x) {
    return f(x);
}

eval_numeric(my_fun, 7); // returns 50
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-27]

#### Numerical Differentiation

Numerical differentiation approximates the derivative of a function at a point using finite differences.

**Example:**

```javascript
// numerical differentiation; simplest method
function deriv_numeric(f) {
    const dx = 0.0001;
    return x => (f(x + dx) - f(x)) / dx;
}

// Example use:
const f = x => x * x + x + 4; // f(x) = x^2 + x + 4
const f_prime = deriv_numeric(f);

f(3);       // returns 16
f_prime(3); // returns 7.000100000027487 (approx. 2*3 + 1 = 7)
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-28]

#### Symbolic Evaluation

For symbolic processing, functions and expressions are represented as **data structures** instead of executable code [source:cs1101s-lecture-lecture-l6-view-pdf#section-29].

**Example Expression (representing $x \cdot x + x + 4$):**

```javascript
const my_exp = make_sum(make_product("x", "x"),
                      make_sum("x", 4));
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-29]

**Symbolic Evaluation (`eval_symbolic`):**
The `eval_symbolic` function takes a symbolic expression (`exp`), a variable name (`name`), and a value for that variable (`val`) to evaluate the expression [source:cs1101s-lecture-lecture-l6-view-pdf#section-29].

```javascript
function eval_symbolic(exp, name, val) {
    return is_number(exp)
        ? exp
        : is_variable(exp)
        ? (is_same_variable(exp, name) ? val : NaN) // if variable matches 'name', use 'val', else NaN
        : is_sum(exp)
        ? eval_symbolic(addend(exp), name, val) +
          eval_symbolic(augend(exp), name, val)
        : is_product(exp)
        ? eval_symbolic(multiplier(exp), name, val) *
          eval_symbolic(multiplicand(exp), name, val)
        : error(exp, "unknown expression type");
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-30]

For `my_exp` and `name="x"`, `val=3`, `eval_symbolic(my_exp, "x", 3)` should return 16 [source:cs1101s-lecture-lecture-l6-view-pdf#section-29].

#### Symbolic Differentiation

Symbolic differentiation computes the derivative of an expression represented as a data structure, producing another symbolic expression representing the derivative [source:cs1101s-lecture-lecture-l6-view-pdf#section-31].

**Example:**
For `f(x) = x^2 + x + 4`, its symbolic representation `my_exp` could be differentiated to produce an expression equivalent to `f'(x) = 2x + 1` [source:cs1101s-lecture-lecture-l6-view-pdf#section-31].

**Rules of Differentiation:**
The `deriv_symbolic` function applies standard differentiation rules [source:cs1101s-lecture-lecture-l6-view-pdf#section-32]:
*   $\frac{dc}{dx} = 0$ (for a constant `c` or a variable different from `x`)
*   $\frac{dx}{dx} = 1$
*   $\frac{d(u + v)}{dx} = \frac{du}{dx} + \frac{dv}{dx}$
*   $\frac{d(uv)}{dx} = u \frac{dv}{dx} + v \frac{du}{dx}$

**Definition of `deriv_symbolic`:**

```javascript
function deriv_symbolic(exp, x) {
    return is_number(exp)
        ? 0 // d/dx (constant) = 0
        : is_variable(exp)
        ? (is_same_variable(exp, x) ? 1 : 0) // d/dx (x) = 1, d/dx (y) = 0
        : is_sum(exp)
        ? make_sum(deriv_symbolic(addend(exp), x),
                   deriv_symbolic(augend(exp), x)) // d/dx (u+v) = du/dx + dv/dx
        : is_product(exp)
        ? make_sum(make_product(multiplier(exp),
                                deriv_symbolic(multiplicand(exp), x)),
                   make_product(deriv_symbolic(multiplier(exp), x),
                                multiplicand(exp))) // d/dx (uv) = u dv/dx + v du/dx
        : error(exp, "unknown expression type");
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-33]

#### Implementation of Symbolic Representation

To work with symbolic expressions as data structures, we need:

**Constructors:** Functions to build expressions [source:cs1101s-lecture-lecture-l6-view-pdf#section-34].
```javascript
function make_sum(a1, a2) {
    return list("+", a1, a2); // Represents a sum as a list starting with "+"
}

function make_product(m1, m2) {
    return list("*", m1, m2); // Represents a product as a list starting with "*"
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-34]

**Accessors / Selectors:** Functions to extract components of an expression [source:cs1101s-lecture-lecture-l6-view-pdf#section-35].
```javascript
function addend(s) {
    return head(tail(s)); // First operand of a sum
}

function augend(s) {
    return head(tail(tail(s))); // Second operand of a sum
}

function multiplier(s) {
    return head(tail(s)); // First operand of a product
}

function multiplicand(s) {
    return head(tail(tail(s))); // Second operand of a product
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-35]

**Predicates:** Functions to check the type of an expression [source:cs1101s-lecture-lecture-l6-view-pdf#section-36].
```javascript
function is_variable(x) {
    return is_string(x); // A variable is represented as a string
}

function is_same_variable(v1, v2) {
    return is_variable(v1) && is_variable(v2) && v1 === v2;
}

function is_sum(x) {
    return is_pair(x) && head(x) === "+";
}

function is_product(x) {
    return is_pair(x) && head(x) === "*";
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-36]

#### Expression Simplification

Without simplification, `deriv_symbolic` can return a verbose expression like `x * 1 + 1 * x + 1 + 0` instead of `x + x + 1` (or `2x + 1`) for the derivative of `x^2 + x + 4` [source:cs1101s-lecture-lecture-l6-view-pdf#section-37]. To produce more readable results, constructors can be enhanced with simplification rules.

**`make_sum` with Simplification:**

```javascript
function make_sum(a1, a2) {
    return number_equal(a1, 0) // If a1 is 0, sum is a2
        ? a2
        : number_equal(a2, 0) // If a2 is 0, sum is a1
        ? a1
        : is_number(a1) && is_number(a2) // If both are numbers, return their sum
        ? a1 + a2
        : list("+", a1, a2); // Otherwise, construct the sum expression
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-38]

**`make_product` with Simplification:**

```javascript
function make_product(m1, m2) {
    return number_equal(m1, 0) || number_equal(m2, 0) // If either is 0, product is 0
        ? 0
        : number_equal(m1, 1) // If m1 is 1, product is m2
        ? m2
        : number_equal(m2, 1) // If m2 is 1, product is m1
        ? m1
        : is_number(m1) && is_number(m2) // If both are numbers, return their product
        ? m1 * m2
        : list("*", m1, m2); // Otherwise, construct the product expression
}
```
[source:cs1101s-lecture-lecture-l6-view-pdf#section-39]

With these simplified constructors, `deriv_symbolic(my_exp, "x")` now returns a simplified expression equivalent to `x + x + 1`, which is much cleaner [source:cs1101s-lecture-lecture-l6-view-pdf#section-40].

---

### Designing Data Structures

The design of data structures involves a clear distinction between what a data structure does and how it does it.

#### Process of Designing Data Structures

1.  **Specification**: Describes *what* is done (the contract) [source:cs1101s-lecture-lecture-l6-view-pdf#section-44]. This defines the operations and their expected behavior.
2.  **Implementation**: Describes *how* it is done (the work) [source:cs1101s-lecture-lecture-l6-view-pdf#section-44]. This involves the actual data representation and the code for the operations.

#### Abstraction

Functions like constructors (`make_sum`), accessors (`addend`), and predicates (`is_sum`) provide an **abstraction** of the data structure [source:cs1101s-lecture-lecture-l6-view-pdf#section-43]. This abstraction "shields" the rest of the program from the specific implementation details of the data structure [source:cs1101s-lecture-lecture-l6-view-pdf#section-43]. For instance, `eval_symbolic` and `deriv_symbolic` do not need to know whether a sum is represented as `list("+", a1, a2)` or some other form, as long as the accessor functions work correctly [source:cs1101s-lecture-lecture-l6-view-pdf#section-43].

#### Example: Set Data Structure

Let's consider the design of a Set data structure, which is an unordered collection of objects (here, numbers) [source:cs1101s-lecture-lecture-l6-view-pdf#section-45].

**Set: Specification**
*   **Constructors**: `make_empty_set()`, `add(e, S)` (adds element `e` to set `S`), `remove(e, S)` (removes `e` from `S`) [source:cs1101s-lecture-lecture-l6-view-pdf#section-45].
*   **Predicates**: `find(e, S)` (checks if `e` is in `S`) [source:cs1101s-lecture-lecture-l6-view-pdf#section-45].
*   **Contract**:
    *   `find(e, add(e, S))` returns `true`.
    *   `find(e, remove(e, S))` returns `false` [source:cs1101s-lecture-lecture-l6-view-pdf#section-45].

**Set: Implementation (Different Versions)**

Different implementations have varying performance characteristics for `add`, `remove`, and `find` operations:

*   **Version 1: Unordered List**
    *   **Idea**: Represent a set by an unordered list [source:cs1101s-lecture-lecture-l6-view-pdf#section-46].
    *   **Consequences**:
        *   `add(e, S)`: May be fast if we don't check for duplicates ($O(1)$ by simply pairing), or $O(N)$ if checking for duplicates first.
        *   `remove(e, S)`: $O(N)$ (requires searching for `e`).
        *   `find(e, S)`: $O(N)$ (requires scanning the list) [source:cs1101s-lecture-lecture-l6-view-pdf#section-46].

*   **Version 2: Ordered List**
    *   **Idea**: Represent a set by an ordered list [source:cs1101s-lecture-lecture-l6-view-pdf#section-47].
    *   **Consequences**:
        *   `add(e, S)`: $O(N)$ (must find correct insertion point to maintain order).
        *   `remove(e, S)`: $O(N)$ (must find `e` and remove while maintaining order).
        *   `find(e, S)`: $O(N)$ (even with an ordered list, linear scan is often necessary, though binary search could be adapted if indexed access were $O(1)$) [source:cs1101s-lecture-lecture-l6-view-pdf#section-47].

*   **Version 3: Binary Search Tree**
    *   **Idea**: Represent a set by a binary search tree [source:cs1101s-lecture-lecture-l6-view-pdf#section-48].
    *   **Consequences (for balanced BSTs)**:
        *   `add(e, S)`: $O(\log N)$ (traverse tree to find insertion point).
        *   `remove(e, S)`: $O(\log N)$ (traverse tree to find and remove node).
        *   `find(e, S)`: $O(\log N)$ (efficient search due to BST property) [source:cs1101s-lecture-lecture-l6-view-pdf#section-48].

#### Which Implementation is Best?

There are several reasonable choices for implementing a Set. Often, some operations are fast in one implementation and slow in another. This highlights that there is frequently a **trade-off** in data structure design [source:cs1101s-lecture-lecture-l6-view-pdf#section-49]. The "best" representation ultimately depends on which operations are **most frequent** in the specific application [source:cs1101s-lecture-lecture-l6-view-pdf#section-49].

---

### Summary

This lecture covered four main areas [source:cs1101s-lecture-lecture-l6-view-pdf#section-50]:
*   **Binary Search and Binary Search Trees (BST)**: An efficient search algorithm and a data structure that leverages sorted order for logarithmic time complexity.
*   **Sorting**:
    *   **Approach A (N-1 elements)**: Insertion Sort and Selection Sort, typically with $O(N^2)$ time complexity.
    *   **Approach B (N/2 elements)**: Merge Sort and QuickSort, generally more efficient ($O(N \log N)$).
*   **Symbolic Processing**: Representing functions as data structures to perform symbolic evaluation and differentiation, with emphasis on expression simplification.
*   **Data Structure Design**: The fundamental distinction between specification (`what`) and implementation (`how`), and the concept of trade-offs in choosing the most appropriate representation based on usage patterns.

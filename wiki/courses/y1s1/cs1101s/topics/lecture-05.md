---
page_id: "y1s1-cs1101s-lecture-05"
title: "Lecture 05: List and Tree Processing"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 05: List and Tree Processing consolidates the numbered lecture materials for this module. This lecture (L5) for CS1101S, presented on September 7, 2022, covers List Processing, Higher-order List Processing, Tr..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l5-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l5-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l5-view-pdf#section-3"
topics:
  - "list"
  - "processing"
  - "elements"
  - "tree"
  - "function"
  - "data"
  - "operations"
  - "functions"
  - "lecture"
source_count: 1
lecture_number: 5
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 05: List and Tree Processing

This lecture, L5: List and Tree Processing, was presented for CS1101S: Programming Methodology on September 7, 2022. It covers fundamental data structures and programming paradigms, including List Processing, Higher-order List Processing, Trees and Tree Processing, and Continuation-Passing Style [source:cs1101s-lecture-lecture-l5-view-pdf#section-1, cs1101s-lecture-lecture-l5-view-pdf#section-2].

## Announcements and Reading Assessment 1 Review

The lecture began with an announcement regarding "The Choreographer" contest, which closed on the night of September 7, 2022, at 23:59 [source:cs1101s-lecture-lecture-l5-view-pdf#section-1].

A review of Reading Assessment 1 (RA1) statistics was also provided, showing overall performance and common misconceptions. Key points from RA1 included:
*   In Source R2L, the right operand of a binary operation is evaluated before the left operand [source:cs1101s-lecture-lecture-l5-view-pdf#section-5].
*   When there are multiple arguments in a function application in Source R2L, argument expressions are evaluated from right to left, meaning the rightmost argument is evaluated first, and the leftmost last [source:cs1101s-lecture-lecture-l5-view-pdf#section-5].
*   Examples illustrating argument evaluation order and short-circuiting in logical operations were discussed [source:cs1101s-lecture-lecture-l5-view-pdf#section-6, cs1101s-lecture-lecture-l5-view-pdf#section-7, cs1101s-lecture-lecture-l5-view-pdf#section-8].
*   General remarks emphasized the importance of individual learning, viewing the course as a marathon, utilizing resources, and maintaining a positive learning attitude [source:cs1101s-lecture-lecture-l5-view-pdf#section-10].

## List Processing

This section reviews the concept of pairs and lists, and introduces fundamental list processing functions.

### Review of Pairs

Pairs are a basic building block for lists [source:cs1101s-lecture-lecture-l5-view-pdf#section-12].
*   `pair(1, 2)`: creates a pair.
*   `head(p)`: accesses the first component of a pair `p`.
*   `tail(p)`: accesses the second component of a pair `p`.

### List Discipline

A list is defined recursively as either `null` or a pair whose tail is a list [source:cs1101s-lecture-lecture-l5-view-pdf#section-13].
*   **Examples of lists:**
    *   `null`
    *   `pair(8, null)`
    *   `pair(1, pair(2, pair(3, pair(4, null))))`
*   A shortcut `list(...)` can be used to construct lists, e.g., `list(1, 2, 3, 4)` is equivalent to the nested `pair` structure above [source:cs1101s-lecture-lecture-l5-view-pdf#section-14].
*   Lists can be displayed in "box notation" (e.g., `[1, [2, [3, [4, null]]]]`) or "list notation" (e.g., `list(1, 2, 3, 4)`) [source:cs1101s-lecture-lecture-l5-view-pdf#section-14].
*   `is_null(xs)`: tests if a list `xs` is empty [source:cs1101s-lecture-lecture-l5-view-pdf#section-15].

The list discipline can be refined to specify the type of elements within a list: a list of a certain data type is either `null` or a pair whose `head` is of that data type and whose `tail` is a list of that data type [source:cs1101s-lecture-lecture-l5-view-pdf#section-16].
*   Examples: `list(1, 2, 3)` is a list of numbers; `list("X", "Y", "Z")` is a list of strings [source:cs1101s-lecture-lecture-l5-view-pdf#section-16].

### Computing the Length of a List

The length of an empty list is 0. The length of a non-empty list is one more than the length of its tail [source:cs1101s-lecture-lecture-l5-view-pdf#section-17].

**Recursive Implementation:**
```javascript
function length(xs) {
    return is_null(xs)
           ? 0
           : 1 + length(tail(xs));
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-17]

**Iterative Implementation:**
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
[source:cs1101s-lecture-lecture-l5-view-pdf#section-18]

### Appending Two Lists

The goal is to combine two lists, `list1` and `list2`, into a single list `list1` followed by `list2` [source:cs1101s-lecture-lecture-l5-view-pdf#section-19].

**Strategy for `append(list1, list2)`:**
1.  If `list1` is empty, return `list2`.
2.  Otherwise, recursively append the `tail` of `list1` to `list2`.
3.  Form a new pair with the `head` of `list1` and the result from step 2 [source:cs1101s-lecture-lecture-l5-view-pdf#section-21].

**Implementation:**
```javascript
function append(xs, ys) {
    return is_null(xs)
           ? ys
           : pair(head(xs), append(tail(xs), ys));
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-22]

This `append` function creates new pairs for the first list, while reusing the pairs of the second list [source:cs1101s-lecture-lecture-l5-view-pdf#section-23]. The order of growth in time and space for this recursive `append` is linear, proportional to the length of the first list `xs` [source:cs1101s-lecture-lecture-l5-view-pdf#section-22].

### Reversing a List

The goal is to reverse the order of elements in a list [source:cs1101s-lecture-lecture-l5-view-pdf#section-24].

**First attempt (incorrect):**
```javascript
function reverse1(lst) {
    return is_null(lst)
           ? null
           : pair(reverse1(tail(lst)), head(lst));
}
```
This function produces a nested pair structure that is not a flat list [source:cs1101s-lecture-lecture-l5-view-pdf#section-24].

**Second attempt (correct, but inefficient):**
```javascript
function reverse2(lst) {
    return is_null(lst)
           ? null
           : append(reverse2(tail(lst)),
                    list(head(lst)));
}
```
This version correctly reverses the list, but its runtime performance is quadratic due to repeated calls to `append` [source:cs1101s-lecture-lecture-l5-view-pdf#section-25].

**Third attempt (iterative, efficient):**
```javascript
function reverse3(xs) {
    function rev(original, reversed) {
        return is_null(original)
               ? reversed
               : rev(tail(original),
                     pair(head(original), reversed));
    }
    return rev(xs, null);
}
```
This iterative approach builds the reversed list by prepending elements one by one, resulting in linear time and space complexity [source:cs1101s-lecture-lecture-l5-view-pdf#section-26].

## Higher-order List Processing

Higher-order functions like `map`, `filter`, and `accumulate` provide powerful abstractions for list processing.

### `map`

`map` applies a given function `f` element-wise to each element of a list `xs`, producing a new list consisting of the results [source:cs1101s-lecture-lecture-l5-view-pdf#section-30].

**Example: Scaling a list**
```javascript
function scale_list(xs, k) {
    return is_null(xs)
           ? null
           : pair(k * head(xs),
                  scale_list(tail(xs), k));
}
// scale_list(list(1, 2, 3), 10) => list(10, 20, 30)
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-28]

**Example: Squaring a list**
```javascript
function square_list(xs) {
    const square = x => x * x;
    return is_null(xs)
           ? null
           : pair(square(head(xs)),
                  square_list(tail(xs)));
}
// square_list(list(1, 2, 3, 4)) => list(1, 4, 9, 16)
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-29]

**Abstraction with `map`:**
```javascript
function map(f, xs) {
    return is_null(xs)
           ? null
           : pair(f(head(xs)), map(f, tail(xs)));
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-30]

Using `map`, `scale_list` and `square_list` can be rewritten concisely:
```javascript
function scale_list(xs, k) {
    return map(x => k * x, xs);
}

function square_list(xs) {
    return map(x => x * x, xs);
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-31]

`map` can also be used to create a copy of a list:
```javascript
function copy(xs) {
    return map(x => x, xs);
}
```
This creates new pairs for the copy while preserving the original list's structure [source:cs1101s-lecture-lecture-l5-view-pdf#section-32].

### `filter`

`filter` selects elements from a list based on a given predicate function `pred` [source:cs1101s-lecture-lecture-l5-view-pdf#section-34].

**Example: Taking even numbers from a list**
```javascript
function even_numbers(xs) {
    return is_null(xs)
           ? null
           : head(xs) % 2 === 0
             ? pair(head(xs), even_numbers(tail(xs)))
             : even_numbers(tail(xs));
}
// even_numbers(list(1, 2, 3, 4, 5, 6)) => list(2, 4, 6)
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-33]

**Abstraction with `filter`:**
```javascript
function filter(pred, xs) {
    return is_null(xs)
           ? null
           : pred(head(xs))
             ? pair(head(xs), filter(pred, tail(xs)))
             : filter(pred, tail(xs));
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-34]

Rewriting `even_numbers` using `filter`:
```javascript
function even_numbers(xs) {
    return filter(x => x % 2 === 0, xs);
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-34]

### `accumulate`

`accumulate` (also known as `reduce` or `fold`) combines the elements of a list using a given binary function `f` and an `initial` value [source:cs1101s-lecture-lecture-l5-view-pdf#section-36]. This process is often called "right-to-left folding" [source:cs1101s-lecture-lecture-l5-view-pdf#section-35].

**Example: Summing elements of a list**
```javascript
function list_sum(xs) {
    return is_null(xs)
           ? 0
           : head(xs) + list_sum(tail(xs));
}
// list_sum(list(1, 2, 3)) => 6
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-35]

**Abstraction with `accumulate`:**
```javascript
function accumulate(f, initial, xs) {
    return is_null(xs)
           ? initial
           : f(head(xs),
               accumulate(f, initial, tail(xs)));
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-36]

Rewriting `list_sum` using `accumulate`:
```javascript
function list_sum(xs) {
    return accumulate((x, y) => x + y, 0, xs);
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-36]

These three higher-order functions (`map`, `filter`, `accumulate`) are known as "The Trio" for their versatility in list processing [source:cs1101s-lecture-lecture-l5-view-pdf#section-37].

## Trees and Tree Processing

### Definition of a Tree

A tree is defined as a list whose elements are either data items of a certain data type, or other trees of that data type [source:cs1101s-lecture-lecture-l5-view-pdf#section-39]. This implies a recursive, self-similar structure.

*   **Examples of trees of numbers:**
    *   `list(1, 2, 3, 4)`
    *   `list(list(1, 2), list(3, 4))` (a tree whose elements are themselves trees)
    *   `list(list(1, 2), null, 3, list(4, null))`
    *   `null` can be a tree of any type [source:cs1101s-lecture-lecture-l5-view-pdf#section-39].
*   **Caveat:** `null` and `pair` cannot be considered as the "certain data type" themselves to prevent issues like trees of `null`s or `pair`s, which might break the intended structure or meaning [source:cs1101s-lecture-lecture-l5-view-pdf#section-39].

### Counting Data Items in a Tree

The goal is to count the total number of data items (non-list elements) within a given tree [source:cs1101s-lecture-lecture-l5-view-pdf#section-41].

**Idea:**
1.  Every tree is a list.
2.  If the list is empty, return 0.
3.  If the list is not empty, add the number of data items of the `head` to the number of data items of the `tail` [source:cs1101s-lecture-lecture-l5-view-pdf#section-42].
    *   If the `head` is a tree/list, recursively count its data items.
    *   If the `head` is not a tree/list (i.e., a data item), count it as 1 [source:cs1101s-lecture-lecture-l5-view-pdf#section-42].

**Implementation:**
```javascript
function count_data_items(tree) {
    return is_null(tree)
           ? 0
           : (is_list(head(tree))
              ? count_data_items(head(tree))
              : 1)
             + count_data_items(tail(tree));
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-43]

### Scaling a Tree

The objective is to create a new tree where all data items in the original tree are scaled by a factor `k` [source:cs1101s-lecture-lecture-l5-view-pdf#section-44].

**Idea:** Map over the list that represents the tree. If an element is a data item, scale it. If it's another tree, recursively scale that sub-tree [source:cs1101s-lecture-lecture-l5-view-pdf#section-45].

**Implementation:**
```javascript
function scale_tree(tree, k) {
    return map(sub_tree =>
               !is_list(sub_tree) // Check if it's a data item (not a list)
               ? k * sub_tree
               : scale_tree(sub_tree, k),
               tree);
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-45]

### Abstraction: `map_tree`

Similar to `map` for lists, `map_tree` provides a higher-order abstraction for applying a function `f` to every data item in a tree [source:cs1101s-lecture-lecture-l5-view-pdf#section-46].

```javascript
function map_tree(f, tree) {
    return map(sub_tree =>
               !is_list(sub_tree)
               ? f(sub_tree)
               : map_tree(f, sub_tree),
               tree);
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-46]

Using `map_tree`, `scale_tree` becomes even more concise:
```javascript
function scale_tree(tree, k) {
    return map_tree(data_item => data_item * k, tree);
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-47]

## Continuation-Passing Style (CPS)

Continuation-Passing Style (CPS) is a programming pattern where the "rest of the computation" (the deferred operation) is passed as a function in an extra argument, called a "continuation" [source:cs1101s-lecture-lecture-l5-view-pdf#section-53]. This allows converting any recursive function into an iterative process.

### Iterative `append` using CPS

The standard recursive `append` is not iterative because the `pair` operation is deferred until the recursive call returns [source:cs1101s-lecture-lecture-l5-view-pdf#section-49].

**Standard Recursive `append`:**
```javascript
function append(xs, ys) { // Recursive process
    return is_null(xs)
           ? ys
           : pair(head(xs), append(tail(xs), ys));
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-52]

**Iterative `append` using `reverse` (less efficient):**
An alternative iterative `append` can be constructed by reversing the first list, then appending it to the second list, and finally reversing the result. This involves multiple traversals [source:cs1101s-lecture-lecture-l5-view-pdf#section-51].

**Iterative `append` using CPS:**
```javascript
function app(current_xs, ys, c) { // Iterative process
    return is_null(current_xs)
           ? c(ys) // Apply the continuation 'c' to the final ys
           : app(tail(current_xs), ys,
                 x => c(pair(head(current_xs), x))); // New continuation
}

function append_iter(xs, ys) {
    return app(xs, ys, x => x); // Initial continuation simply returns the result
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-52]

In this CPS version, the `c` parameter is the *continuation*. It's a function that represents the "work to be done later." When `current_xs` becomes `null`, `c(ys)` is called, passing the `ys` (which has been effectively prepended with `head(current_xs)` values) back up the chain of continuations [source:cs1101s-lecture-lecture-l5-view-pdf#section-53].

### Another CPS Example: `fractal_5`

The `fractal_5` function from Lecture 3, which builds a fractal image, can also be converted to CPS to achieve an iterative process.

**Standard Recursive `fractal_5`:**
```javascript
function fractal_5(rune, n) { // Recursive process
    return n === 1
           ? rune
           : beside(rune, fractal_5(stack(rune, rune), n - 1));
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-54, cs1101s-lecture-lecture-l5-view-pdf#section-55]

**Iterative `fractal_5` using CPS:**
```javascript
function frac(rune, n, c) { // Iterative process
    return n === 1
           ? c(rune)
           : frac(stack(rune, rune), n - 1,
                  res => c(beside(rune, res)));
}

function fractal_5_iter(rune, n) {
    return frac(rune, n, rune => rune);
}
```
[source:cs1101s-lecture-lecture-l5-view-pdf#section-55]

This transformation demonstrates that any recursive function can be converted into an iterative form using Continuation-Passing Style [source:cs1101s-lecture-lecture-l5-view-pdf#section-53].

## Summary

This lecture covered:
*   **List processing** fundamentals, including `length`, `append`, and `reverse` operations [source:cs1101s-lecture-lecture-l5-view-pdf#section-56].
*   **Higher-order list processing** using powerful abstractions like `map`, `filter`, and `accumulate` [source:cs1101s-lecture-lecture-l5-view-pdf#section-56].
*   **Trees and tree processing**, defining trees as recursive list structures and illustrating how to count data items and scale trees, introducing `map_tree` as a higher-order tree processing function [source:cs1101s-lecture-lecture-l5-view-pdf#section-56].
*   **Continuation-Passing Style (CPS)** as a programming pattern to transform any recursive function into an iterative process [source:cs1101s-lecture-lecture-l5-view-pdf#section-56].

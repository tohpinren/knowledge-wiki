---
page_id: "y1s1-cs1101s-lecture-10"
title: "Lecture 10: Streams II"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 10: Streams II consolidates the numbered lecture materials for this module. This lecture reviews stream basics, defining streams as 'delayed lists' where each pair has a data item as its head and a nullary fun..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l10-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l10-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l10-view-pdf#section-3"
topics:
  - "stream"
  - "function"
  - "streams"
  - "tail"
  - "numbers"
  - "can"
  - "element"
  - "using"
  - "lecture"
  - "consolidates"
source_count: 1
lecture_number: 10
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 10: Streams II

This lecture reviews stream basics, defining streams as 'delayed lists' where each pair has a data item as its head and a nullary function as its tail. This tail function can be activated on demand to return the remainder of the stream. Stream discipline mirrors list discipline, adapted for delayed evaluation [source: cs1101s-lecture-lecture-l10-view-pdf#section-1]. The lecture covers concepts like 'wrapping around,' 'memoized streams,' and 'advanced examples' [source: cs1101s-lecture-lecture-l10-view-pdf#section-1]. The recommended reading for this topic is Textbook Section 3.5 [source: cs1101s-lecture-lecture-l10-view-pdf#section-2].

## Idea of Streams (Review of Basics)

Streams are fundamentally "delayed lists" [source: cs1101s-lecture-lecture-l10-view-pdf#section-3]. Unlike regular lists where all elements are evaluated upfront, in streams:
*   Each pair contains a data item as its head (as usual).
*   Its tail is a *function* that can be activated when needed [source: cs1101s-lecture-lecture-l10-view-pdf#section-3].

Formally, a stream of a certain type is either `null` or a pair whose head is of that type, and whose tail is a nullary function that returns a stream of that type [source: cs1101s-lecture-lecture-l10-view-pdf#section-3].

**Stream Discipline**
The way we process streams is similar to how we process lists, but adapted for delayed evaluation. This is known as "stream discipline" [source: cs1101s-lecture-lecture-l10-view-pdf#section-3].

### Examples — Finite Streams

Examples of finite streams include:
*   An empty stream: `const s1 = null;` [source: cs1101s-lecture-lecture-l10-view-pdf#section-4]
*   A stream with element 1: `const s2 = pair(1, () => null);` [source: cs1101s-lecture-lecture-l10-view-pdf#section-4]
*   A stream with elements 1, 2, 3:
    ```javascript
    const s3 = 
        pair(1, 
             () => pair(2, 
                        () => pair(3, 
                                    () => null)));
    ```
    [source: cs1101s-lecture-lecture-l10-view-pdf#section-4]

### Example — An Infinite Stream

Consider an infinite stream of ones:
```javascript
function ones_stream() {
    return pair(1, ones_stream);
}
const ones = ones_stream();
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-5]

Accessing elements:
*   `head(ones);` returns `1` [source: cs1101s-lecture-lecture-l10-view-pdf#section-5]
*   `head(tail(ones)());` returns `1` [source: cs1101s-lecture-lecture-l10-view-pdf#section-5]
*   `head(tail(tail(ones)())());` returns `1` [source: cs1101s-lecture-lecture-l10-view-pdf#section-5]

To simplify accessing the tail, a helper function `stream_tail` is often used:
```javascript
function stream_tail(stream) {
    return tail(stream)();
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-5]

Using `stream_tail`:
*   `head(ones);` returns `1` [source: cs1101s-lecture-lecture-l10-view-pdf#section-5]
*   `head(stream_tail(ones));` returns `1` [source: cs1101s-lecture-lecture-l10-view-pdf#section-5]
*   `head(stream_tail(stream_tail(ones)));` returns `1` [source: cs1101s-lecture-lecture-l10-view-pdf#section-5]

## Stream Processing

Stream processing is analogous to list processing, with one key difference:
*   We wrap the `tail` in a function.
*   We use `stream_tail` instead of `tail` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6].

Source §3 provides pre-declared functions for stream processing, such as `stream_tail`, `stream_map`, and `stream_filter` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6].

### `enum_stream` Function

The `enum_stream` function generates a stream of numbers from `low` to `hi`:
```javascript
function enum_stream(low, hi) {
    return low > hi
        ? null
        : pair(low, 
               () => enum_stream(low + 1, hi));
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

Example:
```javascript
const s = enum_stream(1, 100);
head(s);                  // => 1
head(stream_tail(s));     // => 2
head(stream_tail(stream_tail(s))); // => 3
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

### `stream_ref` Function

The `stream_ref` function accesses the element at a specific index `n` in a stream `s`:
```javascript
function stream_ref(s, n) {
    return n === 0
        ? head(s)
        : stream_ref(stream_tail(s), n - 1);
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

Example:
```javascript
const s = enum_stream(1, 100);
stream_ref(s, 0);  // => 1
stream_ref(s, 10); // => 11
stream_ref(s, 99); // => 100
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

### `stream_map` and `stream_filter`

These are higher-order functions for stream processing:

*   **`stream_map(f, s)`**: Applies a function `f` to each element of stream `s`, returning a new stream.
    ```javascript
    function stream_map(f, s) {
        return is_null(s)
            ? null
            : pair(f(head(s)),
                   () => stream_map(f, stream_tail(s)));
    }
    ```
    [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

*   **`stream_filter(p, s)`**: Filters elements from stream `s` based on a predicate `p`, returning a new stream with only elements for which `p` is true.
    ```javascript
    function stream_filter(p, s) {
        return is_null(s)
            ? null
            : p(head(s))
                ? pair(head(s),
                       () => stream_filter(p, stream_tail(s)))
                : stream_filter(p, stream_tail(s));
    }
    ```
    [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

### Extreme Example: Prime Filtering

Consider the expression to find the second prime number after 10000:
`head(stream_tail(stream_filter(is_prime, enum_stream(10000, 1000000))));` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

This works due to lazy evaluation:
1.  `enum_stream(10000, 1000000)` is called, resulting in `pair(10000, () => enum_stream(10001, 1000000))` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6].
2.  `stream_filter` receives this stream. `is_prime(10000)` is `false`, so `stream_filter` forces the evaluation of the tail to find the next element [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]. This continues until `is_prime(10007)` is found to be `true` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6].
    At this point, `stream_filter` produces `pair(10007, () => stream_filter(is_prime, pair(10008, () => enum_stream(10009, 1000000))))` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6].
3.  Then, `stream_tail` on this pair forces the tail function to evaluate, and `stream_filter` continues its process, eventually finding the next prime, 10009 [source: cs1101s-lecture-lecture-l10-view-pdf#section-6].
4.  Finally, `head` extracts this value, `10009` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6].

This demonstrates how streams only compute values *on demand*, avoiding unnecessary computations over a large range.

### More Examples

1.  **Infinite Integers**:
    ```javascript
    function integers_from(n) {
        return pair(n, () => integers_from(n + 1));
    }
    const integers = integers_from(1);
    stream_ref(integers, 0);   // => 1
    stream_ref(integers, 10);  // => 11
    stream_ref(integers, 99);  // => 100
    ```
    [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

2.  **Filtering Multiples of 4**:
    ```javascript
    function is_divisible(x, y) {
        return x % y === 0;
    }
    const no_fours = 
        stream_filter(
            x => !is_divisible(x, 4),
            integers
        );
    stream_ref(no_fours, 3);   // => 5 (1, 2, 3, 5, ... -> 4th element is 5)
    stream_ref(no_fours, 100); // => 134 (the 101st number not divisible by 4)
    ```
    [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

### From Streams to Lists

The `eval_stream` function converts a prefix of a stream into a standard list:
```javascript
function eval_stream(s, n) {
    return n === 0
        ? null
        : pair(head(s),
               eval_stream(stream_tail(s), n - 1));
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

Example with `no_fours`:
`eval_stream(no_fours, 10);`
// `[1, [2, [3, [5, [6, [7, [9, [10, [11, [13, null]]]]]]]]]]` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

### Fibonacci Numbers

An infinite stream of Fibonacci numbers can be generated using a recursive function:
```javascript
function fibgen(a, b) {
    return pair(a, () => fibgen(b, a + b));
}
const fibs = fibgen(0, 1);
eval_stream(fibs, 10);
// [0, [1, [1, [2, [3, [5, [8, [13, [21, [34, null]]]]]]]]]]
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

### More and More Stream (Nested Repeating Sequence)

To create a stream like `1, 1, 2, 1, 2, 3, 1, 2, 3, 4, ...`:
```javascript
function more(a, b) {
    return (a > b)
        ? more(1, 1 + b)
        : pair(a, () => more(a + 1, b));
}
const more_and_more = more(1, 1);
eval_stream(more_and_more, 15);
// [1, [1, [2, [1, [2, [3, [1, [2, [3, [4, [1, [2, [3, [4, [5, null]]]]]]]]]]]]]]]
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

### Replace Function

A function `replace` creates a new stream by replacing a particular value (`a`) with another (`b`) in a given stream (`s`):
```javascript
function replace(s, a, b) {
    return is_null(s)
        ? null
        : pair((head(s) === a) ? b : head(s),
               () => replace(stream_tail(s), a, b));
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

Example: `replace(more_and_more, 1, 0);` produces the stream:
`0, 0, 2, 0, 2, 3, 0, 2, 3, 4, 0, 2, 3, 4, 5, ...` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]
When evaluated:
`const s = replace(more_and_more, 1, 0);`
`eval_stream(s, 15);`
// `[0, [0, [2, [0, [2, [3, [0, [2, [3, [4, [0, [2, [3, [4, [5, null]]]]]]]]]]]]]]]` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

### List to Infinite Stream

The `list_to_inf_stream` function takes a list and returns a stream that repeats the list infinitely:
```javascript
function list_to_inf_stream(xs) { 
    function helper(ys) {
        if (is_null(ys)) { 
            return helper(xs); // If current list is exhausted, restart with original list
        } else {
            return pair(head(ys), 
                       () => helper(tail(ys))); // Continue with tail of current list
        }
    }
    return is_null(xs) ? null : helper(xs); // Start helper with the original list
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

Example: `list_to_inf_stream(list(1, 2, 3));` produces the stream:
`1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, ...` [source: cs1101s-lecture-lecture-l10-view-pdf#section-6]

## Why Do We Need Streams?

Streams offer significant advantages:
*   They allow writing programs using sequence manipulation (similar to lists) while maintaining the efficiency of incremental computation [source: cs1101s-lecture-lecture-l10-view-pdf#section-7].
*   They enable the representation of "infinite" data structures [source: cs1101s-lecture-lecture-l10-view-pdf#section-7].

Some examples of applications for streams (not necessarily relying on delayed evaluation) include:
*   **Stream editing**: Processing files in place (e.g., find and replace operations using tools like `awk`) [source: cs1101s-lecture-lecture-l10-view-pdf#section-7].
*   **Video/Audio Streaming**: Skipping to specific parts of media without loading the entire content [source: cs1101s-lecture-lecture-l10-view-pdf#section-7].

## Wrapping Around

This section reiterates the concept of recursive stream definitions.

**Stream of Ones (Alternative Version)**
An infinite stream of ones can also be defined by having its tail refer back to itself:
`const ones = pair(1, () => ones);` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

**Defining a Repeating Sequence**
A repeating sequence like `1, 2, 3, 1, 2, 3, ...` can be defined similarly:
```javascript
const rep123 = 
    pair(1, 
         () => pair(2, 
                     () => pair(3, 
                                 () => rep123))); // Tail refers back to the start
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

`eval_stream(rep123, 15);` would yield `[1, [2, [3, [1, [2, [3, [1, [2, [3, [1, [2, [3, [1, [2, [3, null]]]]]]]]]]]]]]]` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].

**Adding Two Streams**
The `add_streams` function performs element-wise summation of two streams:
```javascript
function add_streams(s1, s2) {
    if (is_null(s1)) {
        return s2;
    } else if (is_null(s2)) {
        return s1;
    } else {
        return pair(head(s1) + head(s2),
                    () => add_streams(stream_tail(s1),
                                      stream_tail(s2)));
    }
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

Example: Adding `1 2 3 4 5 6 ...` and `1 1 2 2 3 3 ...` should return `2 3 5 6 8 9 ...` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].

### Fibonacci Numbers, Again (using `add_streams`)

Fibonacci numbers can be generated using `add_streams`:
```javascript
const fibs =
    pair(0,
         () => pair(1,
                     () => add_streams(
                               stream_tail(fibs), // The stream starting from the 2nd Fib number
                               fibs)));            // The stream starting from the 0th Fib number
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
This essentially defines `fibs` as `0, 1, (1+0), (2+1), (3+2), ...`.
`eval_stream(fibs, 10);` yields `[0, [1, [1, [2, [3, [5, [8, [13, [21, [34, null]]]]]]]]]]` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].

### Integers Revisited (using `add_streams`)

The infinite stream of integers can also be defined using `ones` and `add_streams`:
```javascript
const ones = pair(1, () => ones);
const integers = 
    pair(1, () => add_streams(ones, integers));
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
This means: `integers` = `1`, `(1+1)`, `(1+2)`, `(1+3)`, ...
`eval_stream(integers, 10);` yields `[1, [2, [3, [4, [5, [6, [7, [8, [9, [10, null]]]]]]]]]]` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].

## Memoized Streams

Memoization can be applied to streams to prevent re-computation of stream tails.

The `memo_fun` function wraps a nullary function (`fun`) to memoize its result:
```javascript
function memo_fun(fun) {
    let already_run = false;
    let result = undefined;
    function mfun() {
        if (!already_run) {
            result = fun();
            already_run = true;
            return result;
        } else {
            return result;
        }
    }
    return mfun;
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

### Memoized Stream Example 1

This example compares a non-memoized stream `onesA` with a memoized stream `onesB`. A helper `ms` function is used to display when the tail is computed.

**Non-memoized `onesA`**:
```javascript
const onesA = pair(1, () => ms("A", onesA));
function ms(m, s) {
    display(m);
    return s;
}
stream_ref(onesA, 3);
```
Output:
"A"
"A"
"A"
1
Each access to a new stream_tail re-evaluates `ms("A", onesA)`. [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

**Memoized `onesB`**:
```javascript
const onesB = 
    pair(1, memo_fun(() => ms("B", onesB)));
function ms(m, s) {
    display(m);
    return s;
}
stream_ref(onesB, 3);
```
Output:
"B"
1
Here, `ms("B", onesB)` is called only once, demonstrating that the result of `memo_fun` is stored after the first evaluation. [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

### Memoized Stream Example 2

Applying memoization to `integers_from`:
```javascript
function m_integers_from(n) {
    return pair(n, 
                memo_fun(
                    () => ms("M: " + stringify(n), 
                             m_integers_from(n + 1))));
}
const m_integers = m_integers_from(1);
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

*   `stream_ref(m_integers, 0);`
    Output: `1` (no `ms` calls for the first element) [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
*   `stream_ref(m_integers, 2);`
    Output:
    "M: 1"
    "M: 2"
    `3`
    (The first evaluation of `m_integers_from(1)`'s tail, and then `m_integers_from(2)`'s tail) [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
*   `stream_ref(m_integers, 5);`
    Output:
    "M: 3"
    "M: 4"
    "M: 5"
    `6`
    (Only the tails from index 3 to 5 are evaluated and memoized.) [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
*   `stream_ref(m_integers, 5);` (again)
    Output: `6`
    (No `ms` calls, as the value is already memoized) [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

### Why Don't We Always Do This?

Functions often have an *effect* beyond the value they compute. These are known as **side effects** [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].
*   When discussing lazy evaluation, these effects are specifically called side effects [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].
*   **Pure functional programming** involves programming without side effects [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].
*   In pure functional programming, all values can be memoized, and results are not affected by memoization [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]. However, if a function has side effects (like `display` in `ms`), memoizing it changes when those effects occur.

## Advanced Examples

### Example — Generating Primes

A naive approach to generating a stream of primes using `is_prime`:
```javascript
const primes =
    pair(2, 
         () => stream_filter(is_prime,
                             integers_from(3)));
eval_stream(primes, 10);
// [2, [3, [5, [7, [11, [13, [17, [19, [23, [29, null]]]]]]]]]]
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

The question then arises: can we make a prime stream *without* using `is_prime`? [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

### Sieve of Eratosthenes

The Sieve of Eratosthenes algorithm generates primes by iteratively filtering out multiples:
1.  Start with integers beginning with 2: `2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ...` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
2.  Filter away multiples of 2 that are greater than 2: `2 3 5 7 9 11 13 15 17 ...` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
3.  The next leftover integer is 3. Filter away multiples of 3 that are greater than 3: `2 3 5 7 11 13 17 ...` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
4.  The next leftover integer is 5. Filter away multiples of 5 that are greater than 5: `2 3 5 7 11 13 17 ...` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]
5.  And so on... [source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

The stream implementation of the Sieve of Eratosthenes:
```javascript
function is_divisible(x, y) {
    return x % y === 0;
}

function sieve(s) {
    return pair(head(s),
                () => sieve(stream_filter(
                                x => !is_divisible(x, head(s)),
                                stream_tail(s))));
}

const primes = sieve(integers_from(2));
eval_stream(primes, 10);
// [2, [3, [5, [7, [11, [13, [17, [19, [23, [29, null]]]]]]]]]]
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

### Example — Square Roots by Newton's Method

Newton's method for square roots can be implemented using streams for iteration:
```javascript
function average(a, b) {
    return (a + b) / 2;
}
function improve(guess, x) {
    return average(guess, x / guess);
}

function sqrt_iter(guess, x) {
    if (good_enough(guess, x)) {
        return guess;
    } else {
        return sqrt_iter(improve(guess, x), x);
    }
}
function sqrt(x) {
    return sqrt_iter(1.0, x);
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

Using streams, we can represent the sequence of guesses:
```javascript
function sqrt_stream(x) {
    const guesses = pair(1.0, 
                         () => stream_map(
                                   guess => improve(guess, x),
                                   guesses));
    return guesses;
}
eval_stream(sqrt_stream(2), 6);
// [1, 
// [1.5, 
// [1.4166666666666665, 
// [1.4142156862745097, 
// [1.4142135623746899, 
// [1.414213562373095, 
// null]]]]]]
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

### Example — Approximating π

The Leibniz formula for π/4 is `1 - 1/3 + 1/5 - 1/7 + ...` [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].

First, a function to produce a stream of summands `(1, -1/3, 1/5, ...)`:
```javascript
function pi_summands(n) {
    return pair(1 / n,
                () => stream_map(x => -x, 
                                 pi_summands(n + 2)));
}
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

To approximate π, we need partial sums and scaling:
```javascript
// Function to scale a stream (multiplies each element by a factor f)
function scale_stream(s, f) {
    return stream_map(x => x * f, s);
}

// Assume partial_sums(s) returns a stream whose elements are s0, s0+s1, s0+s1+s2, ...
// (This function would need to be implemented, perhaps in a reflection class)
// function partial_sums(s) { ... } 

const pi_stream = 
    scale_stream(partial_sums(pi_summands(1)), 4);

eval_stream(pi_stream, 8);
// [4, 
// [2.666666666666667, 
// [3.466666666666667, 
// [2.8952380952380956, 
// [3.3396825396825403, 
// [2.9760461760461765, 
// [3.2837384837384844, 
// [3.017071817071818,
// null]]]]]]]]
```
[source: cs1101s-lecture-lecture-l10-view-pdf#section-8]

## Summary

*   In streams, functions act as "pickles" – they preserve computations, allowing you to "open the jar" (apply the function) only when you need them [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].
*   Streams can represent "infinite" data structures [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].
*   The laziness of streams helps avoid problems of non-termination for infinite sequences [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].
*   Memoization can be effectively used on streams to cache computed values and prevent redundant calculations [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].
*   Streams are valuable for expressing iterative processes and recursive definitions of sequences [source: cs1101s-lecture-lecture-l10-view-pdf#section-8].

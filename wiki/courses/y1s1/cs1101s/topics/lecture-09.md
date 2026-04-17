---
page_id: "y1s1-cs1101s-lecture-09"
title: "Lecture 09: Searching and Sorting II; Memoization"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 09: Searching and Sorting II; Memoization consolidates the numbered lecture materials for this module. This lecture covers fundamental algorithms for searching, sorting, and optimization via memoization. * **L..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l9-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l9-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l9-view-pdf#section-3"
topics:
  - "memoization"
  - "arrays"
  - "sort"
  - "search"
  - "array"
  - "sorted"
  - "function"
  - "binary"
  - "lecture"
  - "searching"
source_count: 1
lecture_number: 9
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 09: Searching and Sorting II; Memoization

Lecture 09: Searching and Sorting II; Memoization consolidates the numbered lecture materials for this module. This lecture covers fundamental algorithms for searching, sorting, and optimization via memoization [source:cs1101s-lecture-lecture-l9-view-pdf#section-1].

## Outline
This lecture is structured around three main topics:
1.  **Searching**: Exploring methods to find elements within data structures.
2.  **Sorting**: Examining algorithms to arrange elements in a specific order.
3.  **Memoization**: An optimization technique to improve the efficiency of computations [source:cs1101s-lecture-lecture-l9-view-pdf#section-2, cs1101s-lecture-lecture-l9-view-pdf#section-4].

---

## Searching

Searching algorithms aim to locate a specific element within a collection of data. This lecture covers two primary search methods: linear search and binary search [source:cs1101s-lecture-lecture-l9-view-pdf#section-4].

### Linear / Sequential Search

Linear search, also known as sequential search, involves inspecting elements one by one from the front of a list or array until the desired number is found [source:cs1101s-lecture-lecture-l9-view-pdf#section-5]. For arrays, which offer random access (retrieving any value in O(1) time), the approach is equivalent [source:cs1101s-lecture-lecture-l9-view-pdf#section-5].

**Algorithm for Arrays:**
To find a value `v` in an array `A`:

```javascript
function linear_search(A, v) {
    const len = array_length(A);
    let i = 0;
    while (i < len && A[i] !== v) {
        i = i + 1;
    }
    return (i < len); // Returns true if v is found, false otherwise
}

linear_search([1,2,3,4,5,6,7,8,9], 5); // Example usage
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-5]

**Time Complexity:**
In the worst case, linear search requires checking every element, resulting in a time complexity of O(N), where N is the number of elements in the array or list [source:cs1101s-lecture-lecture-l9-view-pdf#section-5].

### Binary Search

Binary search is a much more efficient search algorithm, but it has a crucial prerequisite: the input array must be sorted in ascending order [source:cs1101s-lecture-lecture-l9-view-pdf#section-6].

**Core Idea:**
The main idea is to repeatedly cut the search space in half by checking the middle element of the current range.
1.  If the middle element is the target, the search is successful.
2.  If the target is smaller than the middle element, the search continues in the left half.
3.  If the target is larger than the middle element, the search continues in the right half [source:cs1101s-lecture-lecture-l9-view-pdf#section-6].

This concept is similar to how [binary search trees](https://sourceacademy.org/modules/cs1101s/data-structures#binary-search-tree) work [source:cs1101s-lecture-lecture-l9-view-pdf#section-6].

**Time Complexity:**
Because the search space is halved in each step, binary search has a runtime complexity of O(log n), where n is the number of elements [source:cs1101s-lecture-lecture-l9-view-pdf#section-7].

**Implementations:**

#### 1. Recursive Binary Search
```javascript
function binary_search(A, v) {
    function search(low, high) {
        if (low > high) {
            return false; // Not found
        } else {
            const mid = math_floor((low + high) / 2);
            return (v === A[mid]) ||
                   (v < A[mid]
                    ? search(low, mid - 1) // Search left half
                    : search(mid + 1, high)); // Search right half
        }
    }
    return search(0, array_length(A) - 1);
}

binary_search([1,2,3,4,5,6,7,8,9], 8); // Example usage
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-8]

#### 2. Iterative Binary Search (using a Loop)
```javascript
function binary_search(A, v) {
    let low = 0;
    let high = array_length(A) - 1;
    while (low <= high) {
        const mid = math_floor((low + high) / 2);
        if (v === A[mid]) {
            break; // Found
        } else if (v < A[mid]) {
            high = mid - 1; // Adjust high to search left
        } else {
            low = mid + 1; // Adjust low to search right
        }
    }
    return (low <= high); // Returns true if found, false otherwise
}

binary_search([1,2,3,4,5,6,7,8,9], 8); // Example usage
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-9]

---

## Sorting

Sorting algorithms arrange elements in a list or array in a specific order (e.g., ascending or descending). This lecture explores Selection Sort, Insertion Sort, and Merge Sort [source:cs1101s-lecture-lecture-l9-view-pdf#section-10].

### Selection Sort

**Idea for Lists:**
1.  Find the smallest element `x` in the list and remove it.
2.  Recursively sort the remaining list.
3.  Place `x` at the front of the sorted remaining list [source:cs1101s-lecture-lecture-l9-view-pdf#section-11].

**Idea for Arrays:**
For arrays, the idea is to build the sorted portion from left to right.
1.  Iterate through the array from `i = 0` to `len - 2`.
2.  For each `i`, find the smallest element in the *unsorted* portion (from `i` to `len - 1`).
3.  Swap this smallest element with the element at position `i` [source:cs1101s-lecture-lecture-l9-view-pdf#section-11].

**Example:**
Imagine an array `[2, 5, 6, 8, 10, 20, 17, 12, 18, 23, 14]`. For `i = 5`, the element `20` is at `A[i]`. The smallest element in the unsorted portion `[20, 17, 12, 18, 23, 14]` is `12`. We would swap `20` and `12` [source:cs1101s-lecture-lecture-l9-view-pdf#section-11].

**Implementation for Arrays:**
```javascript
function selection_sort(A) {
    const len = array_length(A);
    for (let i = 0; i < len - 1; i = i + 1) {
        // find_min_pos finds the index of the minimum element
        // in the sub-array A[i]...A[len-1]
        let min_pos = find_min_pos(A, i, len - 1);
        swap(A, i, min_pos);
    }
}

// Helper function to swap two elements in an array
function swap(A, x, y) {
    const temp = A[x];
    A[x] = A[y];
    A[y] = temp;
}

// Helper function to find the position of the minimum element
// in a sub-array A[low...high]
function find_min_pos(A, low, high) {
    let min_pos = low;
    for (let j = low + 1; j <= high; j = j + 1) {
        if (A[j] < A[min_pos]) {
            min_pos = j;
        }
    }
    return min_pos;
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-12]

### Insertion Sort

**Idea for Lists:**
1.  Sort the tail of the given list (using wishful thinking/recursion).
2.  Insert the head element into its correct position within the sorted tail [source:cs1101s-lecture-lecture-l9-view-pdf#section-13].

**Idea for Arrays:**
For arrays, Insertion Sort maintains a sorted prefix of the array.
1.  Move a pointer `i` from left to right, starting from the second element (`i=1`).
2.  Assume the subarray to the left of `i` (`A[0...i-1]`) is already sorted.
3.  Take the element at `A[i]` and insert it into its correct position within the sorted prefix by repeatedly swapping it with its left neighbor until its left neighbor is smaller, or it reaches the beginning of the array [source:cs1101s-lecture-lecture-l9-view-pdf#section-13].

**Example:**
Consider an array `[40, 13, 20, 8]`.
-   When `i=1`, `A[1]` is `13`. `[40, 13, 20, 8]`. Compare `13` with `40`, `13 < 40`, swap. `[13, 40, 20, 8]`. The prefix `[13, 40]` is now sorted.
-   When `i=2`, `A[2]` is `20`. `[13, 40, 20, 8]`. Compare `20` with `40`, `20 < 40`, swap. `[13, 20, 40, 8]`. Compare `20` with `13`, `20 > 13`, stop. The prefix `[13, 20, 40]` is now sorted.
-   When `i=3`, `A[3]` is `8`. `[13, 20, 40, 8]`. Compare `8` with `40`, `8 < 40`, swap. `[13, 20, 8, 40]`. Compare `8` with `20`, `8 < 20`, swap. `[13, 8, 20, 40]`. Compare `8` with `13`, `8 < 13`, swap. `[8, 13, 20, 40]`. The prefix `[8, 13, 20, 40]` is now sorted [source:cs1101s-lecture-lecture-l9-view-pdf#section-13].

**Implementation for Arrays (with `swap`):**
```javascript
function insertion_sort(A) {
    const len = array_length(A);
    for (let i = 1; i < len; i = i + 1) {
        let j = i - 1;
        // Move A[i] to its correct position in A[0...i]
        while (j >= 0 && A[j] > A[j + 1]) {
            swap(A, j, j + 1);
            j = j - 1;
        }
    }
}
// Requires the swap function from Selection Sort
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-14]

**Alternative Implementation (shifting elements):**
This version replaces explicit swaps with shifting elements to the right to make space for `A[i]`.
```javascript
function insertion_sort2(A) {
    const len = array_length(A);
    for (let i = 1; i < len; i = i + 1) {
        const x = A[i]; // Element to be inserted
        let j = i - 1;
        // Shift elements greater than x to the right
        while (j >= 0 && A[j] > x) {
            A[j + 1] = A[j]; // Shift right
            j = j - 1;
        }
        A[j + 1] = x; // Insert x into its correct position
    }
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-15]

### Merge Sort

**Idea for Lists:**
1.  Split the list in half.
2.  Recursively sort each half.
3.  Merge the two sorted lists back together [source:cs1101s-lecture-lecture-l9-view-pdf#section-16].

**Idea for Arrays:**
Similar to lists, but merging sorted halves of an array typically involves using temporary arrays to facilitate the process.
1.  Recursively sort the left half.
2.  Recursively sort the right half.
3.  Merge the two sorted halves (using temporary arrays) [source:cs1101s-lecture-lecture-l9-view-pdf#section-16].

**Example:**
The process involves a recursive "splitting" phase followed by a "merging" phase. An array like `[38, 16, 27, 39, 12, 27]` is repeatedly split into two halves until individual elements are reached. Then, these single-element arrays are merged back up, pairwise, in sorted order until the entire array is sorted [source:cs1101s-lecture-lecture-l9-view-pdf#section-17].

**Implementation for Arrays:**

```javascript
function merge_sort(A) {
    // Initial call to the helper function for the entire array
    merge_sort_helper(A, 0, array_length(A) - 1);
}

// Recursive helper function to sort a sub-array A[low...high]
function merge_sort_helper(A, low, high) {
    if (low < high) { // Base case: If low >= high, sub-array has 0 or 1 element and is already sorted
        const mid = math_floor((low + high) / 2);
        merge_sort_helper(A, low, mid); // Sort left half
        merge_sort_helper(A, mid + 1, high); // Sort right half
        merge(A, low, mid, high); // Merge the two sorted halves
    }
}

// Function to merge two sorted sub-arrays A[low...mid] and A[mid+1...high]
function merge(A, low, mid, high) {
    const B = []; // Temporary array for merging
    let left = low;
    let right = mid + 1;
    let Bidx = 0;

    // Merge elements from A[low...mid] and A[mid+1...high] into B
    while (left <= mid && right <= high) {
        if (A[left] <= A[right]) {
            B[Bidx] = A[left];
            left = left + 1;
        } else {
            B[Bidx] = A[right];
            right = right + 1;
        }
        Bidx = Bidx + 1;
    }

    // Copy any remaining elements from the left half
    while (left <= mid) {
        B[Bidx] = A[left];
        Bidx = Bidx + 1;
        left = left + 1;
    }

    // Copy any remaining elements from the right half
    while (right <= high) {
        B[Bidx] = A[right];
        Bidx = Bidx + 1;
        right = right + 1;
    }

    // Copy sorted elements from B back to A
    for (let k = 0; k < high - low + 1; k = k + 1) {
        A[low + k] = B[k];
    }
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-18, cs1101s-lecture-lecture-l9-view-pdf#section-19, cs1101s-lecture-lecture-l9-view-pdf#section-20]

---

## Memoization

Memoization is an optimization technique used primarily in dynamic programming to speed up computations by caching (storing) the results of expensive function calls and returning the cached result when the same inputs occur again [source:cs1101s-lecture-lecture-l9-view-pdf#section-21, cs1101s-lecture-lecture-l9-view-pdf#section-24].

### Motivation: Naïve Fibonacci Implementation

Consider the naive recursive implementation of the Fibonacci function:
```javascript
function fib(n) {
    return n <= 1
           ? n
           : fib(n - 1) + fib(n - 2);
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-22]

**Order of Growth:** This implementation has an exponential time complexity, specifically $\Theta(\Phi^n)$, where $\Phi$ is the golden ratio [source:cs1101s-lecture-lecture-l9-view-pdf#section-22].

**Why Exponential?**
The exponential growth arises from **lots of duplicate computations**. For example, `fib(5)` calls `fib(4)` and `fib(3)`. `fib(4)` calls `fib(3)` and `fib(2)`. Notice that `fib(3)` is computed twice. This redundancy grows significantly for larger `n`, as the same subproblems (e.g., `fib(2)`, `fib(1)`, `fib(0)`) are re-evaluated multiple times throughout the call tree [source:cs1101s-lecture-lecture-l9-view-pdf#section-23].

### How to do Better? The Idea of Memoization

The core idea of memoization is to "remember what you had computed earlier!" [source:cs1101s-lecture-lecture-l9-view-pdf#section-24].
When a function `f` is called with arguments `x`, the function:
1.  Checks if `f(x)` has been computed before.
2.  If yes, it retrieves the previously computed value from a "local table" (e.g., an array or a hash map).
3.  If no, it computes `f(x)`, stores the result in the local table, and then returns it [source:cs1101s-lecture-lecture-l9-view-pdf#section-24].

### Memoized Fibonacci Function

By using an array (`mem`) as a local table to store computed results, we can optimize the Fibonacci function:
```javascript
function mfib(n) {
    // 'mem' serves as memory for already computed results of fib
    const mem = [];

    function fib(k) {
        // Test if fib(k) has been computed already
        if (mem[k] !== undefined) {
            return mem[k]; // Just access memory
        } else {
            // Compute fib and add result to memory
            const result = k <= 1
                           ? k
                           : fib(k - 1) + fib(k - 2);
            mem[k] = result;
            return result;
        }
    }
    return fib(n);
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-25]

**Order of Growth in Time:**
The memoized Fibonacci function has a time complexity of $\Theta(n)$ [source:cs1101s-lecture-lecture-l9-view-pdf#section-26].
**How come?** Each `fib(k)` for `k` from `0` to `n` is computed only once. Subsequent calls to `fib(k)` simply retrieve the value from `mem[k]` in O(1) time. Thus, the total number of distinct computations is proportional to `n` [source:cs1101s-lecture-lecture-l9-view-pdf#section-27].

### Using "Global Memory" for Memoization

Sometimes, a global `mem` array is used for memoization. This means `mem` is declared outside the `mfib` function. This changes how `mfib` is called and how `mem` is managed, but the core idea of storing and retrieving results remains [source:cs1101s-lecture-lecture-l9-view-pdf#section-28].

### Tribonacci Numbers

The concept of memoization can be applied to other similar recursive sequences, like Tribonacci numbers, where `trib(n)` is the sum of the three preceding numbers: `trib(n-1) + trib(n-2) + trib(n-3)`.

**Naïve Implementation:**
```javascript
function trib(n) {
    return n === 0
           ? 0
           : n === 1
             ? 1
             : n === 2
               ? 1
               : trib(n - 1) + trib(n - 2) + trib(n - 3);
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-29]

**Tribonacci with "Global Memory" (Memoized):**
```javascript
const mem_trib = []; // Global memory for Tribonacci

function mtrib(n) {
    if (mem_trib[n] !== undefined) {
        return mem_trib[n];
    } else {
        const result = n === 0
                       ? 0
                       : n === 1
                         ? 1
                         : n === 2
                           ? 1
                           : mtrib(n - 1) + mtrib(n - 2) + mtrib(n - 3);
        mem_trib[n] = result;
        return result;
    }
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-30]

### An Abstraction for Memoization

We can create a higher-order function, `memoize`, to abstract the memoization pattern. This function takes another function `f` as an argument and returns a memoized version of `f` [source:cs1101s-lecture-lecture-l9-view-pdf#section-31].

```javascript
function memoize(f) {
    const mem = []; // Local memory for the memoized function

    function mf(x) { // The memoized function
        if (mem[x] !== undefined) {
            return mem[x];
        } else {
            const result = f(x); // Call the original function 'f'
            mem[x] = result;
            return result;
        }
    }
    return mf; // Return the memoized function
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-31]

**Tribonacci using `memoize`: First Attempt**
A common mistake is to apply `memoize` to a function that still calls its *original* (unmemoized) recursive definition internally.

```javascript
function trib(n) { // This trib is NOT memoized
    return n === 0
           ? 0
           : n === 1
             ? 1
             : n === 2
               ? 1
               : trib(n - 1) + trib(n - 2) + trib(n - 3); // Still calls the original trib
}

const memo_trib = memoize(trib);
memo_trib(23); // Calls memoized trib for 23
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-32]

**What is the order of growth in time?**
It is **still exponential** [source:cs1101s-lecture-lecture-l9-view-pdf#section-32].
**How come?** The `f(x)` call inside `memoize`'s `mf` function invokes the *original* `trib` function. This original `trib` function is unaware of the `mem` table managed by `memoize`, so its recursive calls (`trib(n-1)`, etc.) will recompute values instead of using the cache [source:cs1101s-lecture-lecture-l9-view-pdf#section-33].

**Tribonacci using `memoize`: Second Attempt**
To correctly use the `memoize` abstraction for recursive functions, the function passed to `memoize` must call the *memoized* version of itself. This can be achieved by defining the recursive logic *within* the `memoize` function's scope, allowing it to reference the `mf` (memoized function) being created. A common pattern is to use a lambda function or an anonymous function within `memoize`.

```javascript
const mtrib = memoize(n => { // The function 'f' now refers to 'mtrib' via closure
    return n === 0
           ? 0
           : n === 1
             ? 1
             : n === 2
               ? 1
               : mtrib(n - 1) + mtrib(n - 2) + mtrib(n - 3); // Calls the memoized mtrib
});
mtrib(23);
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-34]

**What is the order of growth in time?**
This correct implementation results in a time complexity of $\Theta(n)$ [source:cs1101s-lecture-lecture-l9-view-pdf#section-34].

### The n-Choose-k Problem

The "n-Choose-k" problem asks: How many ways are there to choose `k` items out of `n` possible choices? [source:cs1101s-lecture-lecture-l9-view-pdf#section-35]

**Strategy:**
Consider one specific item, `x`. Either `x` is chosen or it is not [source:cs1101s-lecture-lecture-l9-view-pdf#section-35].
The total number of ways is the sum of:
*   **Not chosen:** Ways to choose `k` items from the remaining `n-1` items (`choose(n-1, k)`).
*   **Chosen:** Ways to choose `k-1` items from the remaining `n-1` items (`choose(n-1, k-1)`) [source:cs1101s-lecture-lecture-l9-view-pdf#section-35].

**Base Cases:**
*   If `k > n`, there are `0` ways.
*   If `k = 0` or `k = n`, there is `1` way.

**Straightforward Implementation:**
```javascript
function choose(n, k) {
    return k > n
           ? 0
           : k === 0 || k === n
             ? 1
             : choose(n - 1, k) + choose(n - 1, k - 1);
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-36]

This straightforward implementation also has an exponential order of growth in time due to redundant computations.

**How can we speed up the computation?**
Memoization! [source:cs1101s-lecture-lecture-l9-view-pdf#section-36]

### Memoization Considerations for n-Choose-k

For the n-Choose-k problem, the result depends on two inputs: `n` and `k` [source:cs1101s-lecture-lecture-l9-view-pdf#section-37]. Therefore, we need a **two-dimensional table (a 2-D array)** to record intermediate results. The result of `choose(n, k)` would be stored in `mem[n][k]` [source:cs1101s-lecture-lecture-l9-view-pdf#section-37].

**Read and Write from/to Global 2-D Array:**
Helper functions can manage reading from and writing to this 2-D array, initializing inner arrays as needed.

```javascript
const mem_nCk = []; // Global 2-D array for memoization

function read(n, k) {
    // Check if mem_nCk[n] exists and if mem_nCk[n][k] is defined
    return mem_nCk[n] === undefined
           ? undefined
           : mem_nCk[n][k];
}

function write(n, k, value) {
    if (mem_nCk[n] === undefined) {
        mem_nCk[n] = []; // Initialize the inner array if it doesn't exist
    }
    mem_nCk[n][k] = value;
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-38]

### n-Choose-k with Memoization

Using the helper `read` and `write` functions:

```javascript
function mchoose(n, k) {
    // Check if result is already memoized
    if (read(n, k) !== undefined) {
        return read(n, k);
    } else {
        const result = k > n
                       ? 0
                       : k === 0 || k === n
                         ? 1
                         : mchoose(n - 1, k) + mchoose(n - 1, k - 1); // Recursive calls use memoized mchoose
        write(n, k, result); // Store the result
        return result;
    }
}
```
[source:cs1101s-lecture-lecture-l9-view-pdf#section-39]

**Order of Growth in Time:**
The memoized `mchoose` function has a time complexity of $\Theta(nk)$. Each pair `(n, k)` is computed only once [source:cs1101s-lecture-lecture-l9-view-pdf#section-39].

**Order of Growth in Space:**
The space complexity for storing the `mem_nCk` table is also $\Theta(nk)$ in the worst case, as it may need to store results for all combinations up to `(n, k)` [source:cs1101s-lecture-lecture-l9-view-pdf#section-39].

---

## Summary

*   The idea of **binary search** effectively transfers from [binary search trees](hub:CS1101S) to sorted arrays, enabling O(log n) search time [source:cs1101s-lecture-lecture-l9-view-pdf#section-40].
*   Core ideas from **sorting algorithms for lists** can be adapted for sorting arrays. For arrays, we leverage random-access memory, loops, element swapping, and array copying (for algorithms like Merge Sort) [source:cs1101s-lecture-lecture-l9-view-pdf#section-40].
*   **Memoization** is a powerful technique that transforms inefficient ("naïve") recursive solutions with overlapping subproblems into efficient ("smart") ones by caching previously computed results [source:cs1101s-lecture-lecture-l9-view-pdf#section-40].

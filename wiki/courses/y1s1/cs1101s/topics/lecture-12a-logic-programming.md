---
page_id: "y1s1-cs1101s-lecture-12a-logic-programming"
title: "L12A: Logic Programming"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Logic programming originated from mathematical logic and A.I., with Carl Hewitt's Planner (1969) as an early foundation. Bob Kowalski's discovery of deduction for computation and Alain Colmerauer's development of Prolog in the 1970s introduced this new paradigm, influencing database research and programming language..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l12a-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l12a-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l12a-view-pdf#section-3"
  - "cs1101s-lecture-lecture-l12a-view-pdf#section-4"
  - "cs1101s-lecture-lecture-l12a-view-pdf#section-5"
topics:
  - "query"
  - "logic"
  - "system"
  - "assertions"
  - "programming"
  - "information"
  - "queries"
  - "variables"
  - "originated"
  - "mathematical"
source_count: 1
lecture_number: 12
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# L12A: Logic Programming

This page provides an introduction to logic programming, covering its history, how information is represented and queried, and the underlying mechanisms of a query system.

## History of Logic Programming

Logic programming is a programming paradigm rooted in mathematical logic and artificial intelligence (A.I.) [source: cs1101s-lecture-lecture-l12a-view-pdf#section-1].

Its early foundations include Carl Hewitt's Planner, developed in 1969. In the 1970s, significant advancements occurred simultaneously:
*   Bob Kowalski (Imperial College) discovered the use of deduction for computation [source: cs1101s-lecture-lecture-l12a-view-pdf#section-1].
*   Alain Colmerauer (Marseille) developed Prolog, a logic programming language based on unification and deduction [source: cs1101s-lecture-lecture-l12a-view-pdf#section-1].

This emergence introduced a new programming paradigm – a distinct way of describing computation – that profoundly influenced database research and programming languages [source: cs1101s-lecture-lecture-l12a-view-pdf#section-1].

## Deductive Information Retrieval

In logic programming, information is stored and retrieved deductively [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

### Representing Information with Assertions

Information is represented using **assertions** [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].
*   The first symbols in an assertion (e.g., `address`, `job`, `salary`) denote the *kind* of information.
*   The "arguments" (e.g., lists, literals) are the *data* associated with that information kind.

**Examples of Assertions:**
*   `address(list("Bitdiddle", "Ben"), list("Slumerville", list("Ridge", "Road"), 10))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]
*   `job(list("Bitdiddle", "Ben"), list("computer", "wizard"))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]
*   `salary(list("Bitdiddle", "Ben"), 60000)` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

The system can store various relationships, such as `can_do_job` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]:
*   `can_do_job(list("computer", "wizard"), list("computer", "programmer"))`
*   `can_do_job(list("computer", "wizard"), list("computer", "technician"))`
*   `can_do_job(list("computer", "programmer"), list("computer", "programmer", "trainee"))`
*   `can_do_job(list("administration", "assistant"), list("administration", "big", "wheel"))`

### Simple Queries

Queries are structured similarly to assertions but can contain **logic variables** [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]. Logic variables are typically prefixed with a dollar sign (e.g., `$x`, `$y`, `$person`, `$type`).

**Query Input Example:**
`job($x, list("computer", "programmer"))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

**Query Results Example:**
*   `job(list("Hacker", "Alyssa", "P"), list("computer", "programmer"))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]
*   `job(list("Fect", "Cy", "D"), list("computer", "programmer"))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

The core concept is **matching**: an assertion matches a query if the query's logic variables can be instantiated with data to obtain the assertion [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

**Matching Example:**
A query `job($x, list("computer", $type))` could match assertions like:
*   `job(list("Bitdiddle", "Ben"), list("computer", "wizard"))`
*   `job(list("Hacker", "Alyssa", "P"), list("computer", "programmer"))`
*   `job(list("Fect", "Cy", "D"), list("computer", "programmer"))`
*   `job(list("Tweakit", "Lem", "E"), list("computer", "technician"))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

Note that data structures matter for matching. For instance, `job($x, list("computer", $type))` would *not* match `job(list("Reasoner", "Louis"), list("computer", "programmer", "trainee"))` because the inner lists have different structures. However, if the query was `job($x, pair("computer", $type))`, it *would* match, by substituting `$type` with `list("programmer", "trainee")` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

### Query Processing

Query processing involves finding all assignments to logic variables in a query pattern that satisfy the pattern [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].
1.  The kind of information specified in the query pattern must match the kind of information in an assertion.
2.  The assertion must result from the pattern by instantiating the pattern variables with values.
3.  The system responds by listing all instantiations of the query pattern with the variable assignments that satisfy it [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

**Special case:** If a query pattern has no variables, it reduces to determining if that pattern exists in the database. The empty assignment satisfies such a pattern [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

### Compound Queries

Logic programming supports compound queries using logical operators:

#### `and` Queries
An `and(query1, query2, ..., queryN)` is satisfied by all sets of values for the pattern variables that simultaneously satisfy `query1`, `query2`, ..., `queryN` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

**Example:** Find all computer programmers and their addresses.
`and(job($person, list("computer", "programmer")), address($person, $where))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

#### `or` Queries
An `or(query1, query2, ..., queryN)` is satisfied by all sets of values for the pattern variables that satisfy *at least one* of `query1`, `query2`, ..., `queryN` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

**Example:** Find anyone supervised by Ben Bitdiddle OR Alyssa P. Hacker.
`or(supervisor($x, list("Bitdiddle", "Ben")), supervisor($x, list("Hacker", "Alyssa", "P")))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

#### `not` Queries
A `not(query1)` is satisfied by all assignments to the pattern variables that *do not* satisfy `query1` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

**Example:** Find all people supervised by Ben Bitdiddle who are *not* computer programmers.
`and(supervisor($x, list("Bitdiddle", "Ben")), not(job($x, list("computer", "programmer"))))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

#### `javascript_predicate` Queries
This allows integrating JavaScript predicates for more complex filtering. A `javascript_predicate(predicate)` is satisfied by assignments to pattern variables for which the instantiated predicate evaluates to true [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

**Example:** Find all people whose salary is greater than $30,000.
`and(salary($person, $amount), javascript_predicate($amount > 30000))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

### Rules

Rules allow defining new relationships based on existing assertions and other rules, potentially representing large or even infinite sets of assertions [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

**General Form of a Rule:**
`rule(conclusion, body)`
where `conclusion` is a pattern and `body` is any query. A rule represents all instantiations of its conclusion with variable assignments that satisfy its body [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].

**Examples of Rules:**
1.  **`lives_near` rule:** Two distinct people live near each other if they share the same town address.
    `rule(lives_near($person_1, $person_2), and(address($person_1, pair($town, $rest_1)), address($person_2, pair($town, $rest_2)), not(same($person_1, $person_2))))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]
2.  **`same` rule:** A helper rule stating that two variables are the same if they are instantiated to the same value.
    `rule(same($x, $x))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]
3.  **`wheel` rule:** Defines a "wheel" as someone who supervises a middle manager, who in turn supervises the "wheel".
    `rule(wheel($person), and(supervisor($middle_manager, $person), supervisor($x, $middle_manager)))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

Rules can be used in compound queries [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2].
**Example:** Find computer personnel who live near Ben Bitdiddle.
`and(job($x, pair("computer", something)), lives_near($x, list("Bitdiddle", "Ben")))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

### Recursive Rules

Rules can be recursive, defining relationships in terms of themselves.

**Example: `outranked_by` rule:** A `staff_person` is outranked by a `boss` if the `boss` directly supervises the `staff_person`, OR the `boss` supervises a `middle_manager` who is in turn outranked by the `boss`.
`rule(outranked_by($staff_person, $boss), or(supervisor($staff_person, $boss), and(supervisor($staff_person, $middle_manager), outranked_by($middle_manager, $boss))))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

### Logic as Programs: Appending Lists

Consider appending lists, a common operation in functional programming:

**Functional Programming (e.g., JavaScript-like):**
```javascript
function append(x, y) {
    return is_null(x)
        ? y
        : pair(head(x), append(tail(x), y));
}
```
[source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

**Logic Programming:**
In logic programming, `append($x, $y, $z)` means that lists `$x` and `$y` append to form list `$z` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]. This relationship can be defined with two rules:
1.  **Base case:** If the first list `$x` is `null`, then `$y` appends to `null` to form `$y`.
    `rule(append(null, $y, $y))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]
2.  **Recursive case:** If `$x` is `pair($u, $v)` (a list with head `$u` and tail `$v`), then `$x` and `$y` append to form `pair($u, $z)` if `$v` and `$y` append to form `$z`.
    `rule(append(pair($u, $v), $y, pair($u, $z)), append($v, $y, $z))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

These rules can be used in various ways:

*   **Forward computation (finding the result):**
    **Query Input:** `append(list("a", "b"), list("c", "d"), $z)`
    **Query Results:** `append(list("a", "b"), list("c", "d"), list("a", "b", "c", "d"))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

*   **Backward computation (finding a component):**
    **Query Input:** `append(list("a", "b"), $y, list("a", "b", "c", "d"))`
    **Query Results:** `append(list("a", "b"), list("c", "d"), list("a", "b", "c", "d"))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

*   **Finding all ways to make a given list (decomposition):**
    **Query Input:** `append($x, $y, list("a", "b", "c", "d"))`
    **Query Results:**
    *   `append(null, list("a", "b", "c", "d"), list("a", "b", "c", "d"))`
    *   `append(list("a"), list("b", "c", "d"), list("a", "b", "c", "d"))`
    *   `append(list("a", "b"), list("c", "d"), list("a", "b", "c", "d"))`
    *   `append(list("a", "b", "c"), list("d"), list("a", "b", "c", "d"))`
    *   `append(list("a", "b", "c", "d"), null, list("a", "b", "c", "d"))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-2]

This demonstrates that logic programs define relationships that can be queried in multiple directions, unlike conventional functions which compute a single output from given inputs.

## How the Query System Works

The query system relies on **frames** to manage variable bindings and processes information as **streams of frames** [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

### Frames

A **frame** keeps track of the bindings (assignments) of logic variables [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

**Example Frame:**
```
$x: ["Reasoner", ["Louis", null]]
$type: ["programmer", ["trainee", null]]
```
[source: cs1101s-lecture-lecture-l12a-view-pdf#section-3]

### Streams of Frames

The query system operates by transforming streams of frames [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3]. An "input stream of frames" goes into a query component (e.g., `job(x, y)`), which then interacts with a "stream of assertions from data base" to produce an "output stream of frames, filtered and extended" [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

#### Processing `and` Queries

For `and(A, B)` queries, the process involves a sequential flow of frames:
1.  An input stream of frames enters query component A.
2.  The output of A becomes the input for query component B.
3.  The final output of B is the result stream of frames [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

This means that for `and` queries, both components must be satisfied by the bindings.

#### Processing `or` Queries

For `or(A, B)` queries, the process is different:
1.  The input stream of frames is sent to both query component A and query component B in parallel.
2.  The results from A and B are then merged to form the output stream of frames [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

This reflects that `or` queries are satisfied if at least one component is satisfied.

### Handling Rules: Unification

Rules are handled in query processing by finding rules whose conclusions match a given query pattern [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3]. This matching is performed by a **unifier** [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

The job of a **unifier** for two patterns is to find a frame (a set of variable bindings) that makes the two patterns equal [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

**Unification Example:**
Unify `list($x, $x)` and `list(list("a", $y, "c"), list("a", "b", $z))` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

Step-by-step unification:
1.  The first arguments must unify: `$x` must unify with `list("a", $y, "c")`.
2.  The second arguments must unify: `$x` must unify with `list("a", "b", $z)`.
3.  Since `$x` must unify with both, it implies `list("a", $y, "c")` must unify with `list("a", "b", $z)`.
4.  Comparing element by element:
    *   `"a"` unifies with `"a"`.
    *   `$y` unifies with `"b"`, so `$y = "b"`.
    *   `"c"` unifies with `$z`, so `$z = "c"`.
5.  Thus, `$x` becomes `list("a", "b", "c")`.

The final binding is `$x = list("a", "b", "c")`, `$y = "b"`, `$z = "c"` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

**Another Unification Example:**
Unify `list($x, "a")` and `list(list("b", $y), $z)` [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

Step-by-step:
1.  The first arguments must unify: `$x` must unify with `list("b", $y)`. So, `$x = list("b", $y)`.
2.  The second arguments must unify: `"a"` must unify with `$z`. So, `$z = "a"`.
3.  The remaining binding is `$x` to pattern `list("b", $y)`. No conflicts, so this is a successful unification [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

### Applying Rules

Applying rules in logic programming involves two main steps:
1.  **Unify the query with the conclusion of the rule.** If successful, this forms an extension of the original frame (i.e., new variable bindings).
2.  **Relative to the extended frame, evaluate the query formed by the body of the rule.** This means using the bindings found in step 1 to satisfy the conditions of the rule [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

This process can be compared to applying functions in conventional programming:
1.  Bind the function's parameters to its arguments to form a frame that extends the original function environment.
2.  Relative to the extended environment, evaluate the expression formed by the body of the function [source: cs1101s-lecture-lecture-l12a-view-pdf#section-3].

The conceptual similarity highlights that both paradigms involve establishing a context (frame/environment) and evaluating a body based on that context.

## Implementing the Query System

The query system operates through a **driver loop** [source: cs1101s-lecture-lecture-l12a-view-pdf#section-4]. A simplified driver loop for query processing illustrates its flow:

```javascript
function query_driver_loop() {
    const input = user_read(input_prompt);
    if (is_null(input)) {
        // ... handle null input ...
    } else {
        const q = convert_to_query_syntax(parse(input));
        if (is_assertion(q)) {
            add_rule_or_assertion(assertion_body(q));
        } else {
            display_stream(
                stream_map(
                    frame => unparse(instantiate_expr(exp, frame)),
                    evaluate_query(q, singleton_stream(null))
                )
            );
        }
    }
    return query_driver_loop(); // Recursive call to continue the loop
}
```
[source: cs1101s-lecture-lecture-l12a-view-pdf#section-4]

This loop continuously reads user input:
*   If the input is an assertion or a rule, it is added to the database.
*   If the input is a query, the system evaluates it by producing a stream of matching frames and displays the results.

## Summary

*   **Assertions** are used to represent information within a database [source: cs1101s-lecture-lecture-l12a-view-pdf#section-5].
*   **Queries** enable the retrieval of this information [source: cs1101s-lecture-lecture-l12a-view-pdf#section-5].
*   **Logic variables** are fundamental for forming patterns in queries [source: cs1101s-lecture-lecture-l12a-view-pdf#section-5].
*   **Compound queries** (using `and`, `or`, `not`, `javascript_predicate`) allow for complex information requests [source: cs1101s-lecture-lecture-l12a-view-pdf#section-5].
*   **Rules** describe (potentially infinite) collections of assertions, enabling powerful deductions and defining new relationships [source: cs1101s-lecture-lecture-l12a-view-pdf#section-5].
*   Logic programming allows for **programmatic deduction** in interesting ways [source: cs1101s-lecture-lecture-l12a-view-pdf#section-5].
*   The query system itself serves as an interesting use case for **stream processing** [source: cs1101s-lecture-lecture-l12a-view-pdf#section-5].

---
page_id: "y1s1-cs1231s-lecture-05-set-operations"
title: "Lecture 05: Set Operations and Laws"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Covers fundamental set operations (union, intersection, complement, difference) and the algebraic laws that govern them, such as De Morgan's laws."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-5-sets-0-pdf#section-3"
  - "cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-3"
  - "cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-2"
  - "cs1231s-tutorial-tut03ans-post-pdf#section-1"
  - "cs1231s-tutorial-tut03qns-pdf#section-2"
topics:
  - "set"
  - "sets"
  - "elements"
  - "definition"
  - "finite"
  - "laws"
  - "example"
  - "identities"
  - "all"
  - "not"
source_count: 5
lecture_number: 5
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 05: Set Operations and Laws

This page covers fundamental set operations and the algebraic laws that govern them, essential for understanding discrete structures. We will review basic set definitions and representations, then delve into union, intersection, complement, and difference, concluding with powerful set identities like De Morgan's laws and the Principle of Inclusion-Exclusion.

---

### Introduction to Sets

A **set** is defined as an unordered collection of distinct objects, known as **members** or **elements** [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-1].
*   The notation $x \in A$ means "$x$ is an element of set $A$".
*   The notation $x \notin A$ means "$x$ is not an element of set $A$".

**Common Sets**
Several sets are commonly used in mathematics [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-1]:
*   $\mathbb{N}$: Natural numbers (e.g., 0, 1, 2, 3...)
*   $\mathbb{Z}$: Integers (e.g., ..., -1, 0, 1, 2...) (from "Zahlen")
*   $\mathbb{Q}$: Rational numbers (e.g., -1/10, 1/3) (from "quotients")
*   $\mathbb{R}$: Real numbers (e.g., $\sqrt{2}$, $\pi$)
*   $\mathbb{C}$: Complex numbers (e.g., $\sqrt{-1}$, 10)
*   $\mathbb{Z}^+$: Positive integers (e.g., 1, 2, 3...)
*   $\mathbb{Z}^-$: Negative integers (e.g., -1, -2, -3...)
*   $\mathbb{Z}_{\ge 0}$: Non-negative integers (e.g., 0, 1, 2, 3...)
    *   "Positive" means $>0$.
    *   "Negative" means $<0$.
    *   "Non-negative" means $\ge 0$.

**Specifying Sets**
Sets can be specified in two primary ways:

1.  **Roster Notation (Listing Elements)** [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-1]
    Elements are listed within curly braces.
    *   Finite sets: $\{x_1, x_2, \ldots, x_n\}$
        *   Example: $A = \{1, 5, 6, 3, 3, 3\}$ has elements 1, 5, 6, and 3. Repetition and order do not affect the elements of a set [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-0-pdf#section-8].
    *   Infinite sets: $\{x_1, x_2, x_3, \ldots\}$
        *   Example: $B = \{0, 2, 4, 6, 8, \ldots\}$ represents the non-negative even integers.

2.  **Set-Builder Notation (Describing Elements)** [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-0-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-2]
    This notation describes the properties elements must satisfy to be in the set: $\{x \in U : P(x)\}$, read as "the set of all $x$ in $U$ such that $P(x)$ is true".
    *   $U$ is the universal set from which elements are drawn.
    *   $P(x)$ is a predicate that $x$ must satisfy.
    *   Example: $C = \{x \in \mathbb{Z}_{\ge 0} : x \text{ is even}\}$ represents the non-negative even integers.

**Equality of Sets**
Two sets $A$ and $B$ are **equal**, denoted $A=B$, if and only if they contain precisely the same elements [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-0-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-2]:
$A = B \iff \forall z (z \in A \iff z \in B)$.
A key principle for set equality is that **order and repetition do not matter** when defining a set [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-0-pdf#section-8]. For instance, $\{1, 5, 6, 3, 3, 3\} = \{1, 5, 6, 3\} = \{1, 3, 5, 6\}$.

**The Empty Set**
The **empty set** is the unique set that contains no elements [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-3]. It is denoted by $\emptyset$ or {} [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-1].
*   Existence: There is a set with no elements.
*   Uniqueness: Any two sets with no elements are equal.
The proof of uniqueness is trivial: if sets A and B have no elements, then any statement like "if $z \in A$ then $z \in B$" is vacuously true because the antecedent ($z \in A$) is always false [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-1].

**Inclusion of Sets**
*   **Subset**: A set $A$ is a **subset** of set $B$, denoted $A \subseteq B$, if every element of $A$ is also an element of $B$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-3]:
    $A \subseteq B \iff \forall z (z \in A \implies z \in B)$.
    Alternatively, we say $B$ **includes** $A$, denoted $B \supseteq A$.
*   **Proper Subset**: A set $A$ is a **proper subset** (or **strict subset**) of $B$, denoted $A \subset B$, if $A \subseteq B$ and $A \neq B$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-3]. This implies that there is at least one element in $B$ that is not in $A$.
*   Important remarks [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-2]:
    *   $A \not\subseteq B \iff \exists z (z \in A \land z \notin B)$.
    *   $A = B \iff A \subseteq B \land B \subseteq A$.
    *   $\emptyset \subseteq A$ for any set $A$.
    *   $A \subseteq A$ for any set $A$.

**Membership vs. Inclusion**
It's crucial to distinguish between an element being a member of a set and a set being a subset of another set [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-3]. Sets can themselves be elements of other sets.
*   Example: Let $A = \{\emptyset\}$. This set has 1 element, which is the empty set. So, $\emptyset \in A$, but $A$ is not empty.
*   Example: Let $B = \{\{1\}, \{2\}, \{3\}\}$. This set has 3 elements: $\{1\}$, $\{2\}$, and $\{3\}$. So, $\{3\} \in B$, but $3 \notin B$.

**Power Set**
The **power set** of $A$, denoted $\mathcal{P}(A)$ (or $P(A)$), is the set of all possible subsets of $A$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-4].
*   Example:
    *   $\mathcal{P}(\emptyset) = \{\emptyset\}$. Its cardinality is $|\mathcal{P}(\emptyset)| = 1 = 2^0$.
    *   $\mathcal{P}(\{1\}) = \{\emptyset, \{1\}\}$. Its cardinality is $|\mathcal{P}(\{1\})| = 2 = 2^1$.
    *   $\mathcal{P}(\{1, 2\}) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$. Its cardinality is $|\mathcal{P}(\{1, 2\})| = 4 = 2^2$.
*   For a finite set $A$, the cardinality of its power set is $|\mathcal{P}(A)| = 2^{|A|}$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-4].

**Ordered Pairs and Cartesian Products**
*   An **ordered pair** is an expression $(x, y)$ where the order of elements matters. $(x, y) = (x', y')$ if and only if $x=x'$ and $y=y'$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-4].
    *   Note: $(1,2) \neq (2,1)$, unlike sets where $\{1,2\} = \{2,1\}$.
*   The **Cartesian product** of two sets $A$ and $B$, denoted $A \times B$ (read as "A cross B"), is the set of all possible ordered pairs where the first element is from $A$ and the second is from $B$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-4]:
    $A \times B = \{(x, y) : x \in A \text{ and } y \in B\}$.
    *   Example: $\{a, b\} \times \{1, 2, 3\} = \{(a, 1), (a, 2), (a, 3), (b, 1), (b, 2), (b, 3)\}$.
*   The cardinality of a Cartesian product of finite sets is $|A \times B| = |A| \times |B|$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-5].
*   This concept extends to **ordered $n$-tuples** $(x_1, x_2, \ldots, x_n)$ and the Cartesian product of $n$ sets $A_1 \times A_2 \times \ldots \times A_n$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-6]. If $A_1 = A_2 = \ldots = A_n = A$, we write $A^n = A \times A \times \ldots \times A$ ($n$-many times).

---

### Boolean Operations on Sets

For any sets $A$ and $B$, the fundamental Boolean operations are:

1.  **Union** ($A \cup B$) [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-5]
    The union of $A$ and $B$ is the set of all elements that are in $A$, or in $B$, or in both.
    $A \cup B = \{x : x \in A \text{ or } x \in B\}$.

2.  **Intersection** ($A \cap B$) [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-5]
    The intersection of $A$ and $B$ is the set of all elements that are common to both $A$ and $B$.
    $A \cap B = \{x : x \in A \text{ and } x \in B\}$.

3.  **Set Difference** ($A \setminus B$ or $A - B$) [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-5]
    The complement of $B$ in $A$ is the set of all elements that are in $A$ but not in $B$.
    $A \setminus B = \{x : x \in A \text{ and } x \notin B\}$.

4.  **Universal Set** ($U$) [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-5]
    In a particular context, the **universal set** $U$ is a set that contains all objects being discussed.

5.  **Complement** ($\overline{B}$ or $B^c$) [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-5]
    The complement of set $B$ (within a universal set $U$) is the set of all elements in $U$ that are not in $B$.
    $\overline{B} = U \setminus B = \{x \in U : x \notin B\}$.

**Example of Boolean Operations** [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-5]
Let $A = \{x \in \mathbb{Z} : x \le 10\}$ and $B = \{x \in \mathbb{Z} : 5 \le x \le 15\}$. Assume $\mathbb{Z}$ is the universal set.
*   $A \cup B = \{x \in \mathbb{Z} : (x \le 10) \lor (5 \le x \le 15)\} = \{x \in \mathbb{Z} : x \le 15\}$.
*   $A \cap B = \{x \in \mathbb{Z} : (x \le 10) \land (5 \le x \le 15)\} = \{x \in \mathbb{Z} : 5 \le x \le 10\}$.
*   $A \setminus B = \{x \in \mathbb{Z} : (x \le 10) \land \neg(5 \le x \le 15)\} = \{x \in \mathbb{Z} : x < 5\}$.
*   $\overline{B} = \{x \in \mathbb{Z} : \neg(5 \le x \le 15)\} = \{x \in \mathbb{Z} : (x < 5) \lor (x > 15)\}$.

---

### Set Identities and Laws

Set operations follow a number of algebraic laws, known as **set identities**, which are analogous to logical equivalences [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-6]. For all sets $A, B, C$ within a universal set $U$:

| Law                   | Union Form                                | Intersection Form                               |
| :-------------------- | :---------------------------------------- | :---------------------------------------------- |
| **Identity Laws**     | $A \cup \emptyset = A$                    | $A \cap U = A$                                  |
| **Universal Bound Laws** | $A \cup U = U$                            | $A \cap \emptyset = \emptyset$                  |
| **Idempotent Laws**   | $A \cup A = A$                            | $A \cap A = A$                                  |
| **Double Complement Law** | $\overline{(\overline{A})} = A$                  | -                                               |
| **Commutative Laws**  | $A \cup B = B \cup A$                     | $A \cap B = B \cap A$                           |
| **Associative Laws**  | $(A \cup B) \cup C = A \cup (B \cup C)$   | $(A \cap B) \cap C = A \cap (B \cap C)$         |
| **Distributive Laws** | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| **De Morgan's Laws**  | $\overline{(A \cup B)} = \overline{A} \cap \overline{B}$ | $\overline{(A \cap B)} = \overline{A} \cup \overline{B}$ |
| **Absorption Laws**   | $A \cup (A \cap B) = A$                   | $A \cap (A \cup B) = A$                         |
| **Complement Laws**   | $A \cup \overline{A} = U$                 | $A \cap \overline{A} = \emptyset$               |
| **Set Difference Law** | $A \setminus B = A \cap \overline{B}$     | -                                               |
|                       | $\overline{\emptyset} = U$                  | $\overline{U} = \emptyset$                      |

#### Proving Set Identities

Set identities can be proven using several methods:

1.  **Venn Diagrams** [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-6]
    Venn diagrams provide a visual way to demonstrate identities. By shading regions corresponding to each side of an identity, if the shaded regions match, the identity is demonstrated. This method relies on the fact that each possibility for membership in the sets is represented by a unique region in the diagram.

    *   **Example: De Morgan's Law** $\overline{(A \cup B)} = \overline{A} \cap \overline{B}$
        *   Draw Venn diagrams for $A \cup B$ and its complement, and for $\overline{A} \cap \overline{B}$.
        *   The region representing $\overline{(A \cup B)}$ (elements not in A and not in B) will be the same as the region representing $\overline{A} \cap \overline{B}$ (elements not in A AND not in B).

2.  **Truth Tables (Membership Tables)** [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-6]
    Similar to propositional logic, we can construct a truth table (or membership table) to list all possibilities for an element $x \in U$ being a member of $A$ or $B$.
    *   **Example: De Morgan's Law** $\overline{(A \cup B)} = \overline{A} \cap \overline{B}$

    | $x \in A$ | $x \in B$ | $x \in A \cup B$ | $x \in \overline{(A \cup B)}$ | $x \in \overline{A}$ | $x \in \overline{B}$ | $x \in \overline{A} \cap \overline{B}$ |
    | :-------- | :-------- | :--------------- | :------------------ | :---------- | :---------- | :----------------------- |
    | T         | T         | T                | F                   | F           | F           | F                        |
    | T         | F         | T                | F                   | F           | T           | F                        |
    | F         | T         | T                | F                   | T           | F           | F                        |
    | F         | F         | F                | T                   | T           | T           | T                        |

    Since the columns for "$x \in \overline{(A \cup B)}$" and "$x \in \overline{A} \cap \overline{B}$" are identical, the sets are equal [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8].

3.  **Direct Proofs (Element Method)** [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-7]
    To prove $X = Y$, one typically shows $X \subseteq Y$ and $Y \subseteq X$. To show $X \subseteq Y$, assume an arbitrary element $z \in X$ and use definitions and logical equivalences to show $z \in Y$.
    *   **Example: De Morgan's Law** $\overline{(A \cup B)} = \overline{A} \cap \overline{B}$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8]
        Let $z \in U$.
        1.  $z \in \overline{(A \cup B)}$
        2.  $\iff z \notin (A \cup B)$ (by definition of complement)
        3.  $\iff \neg (z \in A \lor z \in B)$ (by definition of union)
        4.  $\iff (\neg (z \in A)) \land (\neg (z \in B))$ (by [[y1s1-cs1231s-lecture-02-logical-equivalence#De Morgan's Laws for Propositions|De Morgan's Laws for propositions]])
        5.  $\iff (z \notin A) \land (z \notin B)$ (by definition of $\notin$)
        6.  $\iff (z \in \overline{A}) \land (z \in \overline{B})$ (by definition of complement)
        7.  $\iff z \in (\overline{A} \cap \overline{B})$ (by definition of intersection)
        Since $z \in \overline{(A \cup B)} \iff z \in (\overline{A} \cap \overline{B})$, it follows that $\overline{(A \cup B)} = \overline{A} \cap \overline{B}$.

    *   **Example Application**: Show $(A \cap B) \cup (A \setminus B) = A$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-7]
        1.  $(A \cap B) \cup (A \setminus B)$
        2.  $= (A \cap B) \cup (A \cap \overline{B})$ (by Set Difference Law)
        3.  $= A \cap (B \cup \overline{B})$ (by Distributive Law)
        4.  $= A \cap U$ (by Complement Law)
        5.  $= A$ (by Identity Law)

---

### Cardinality of a Union

**Disjoint Sets**
*   Two sets $A$ and $B$ are **disjoint** if their intersection is the empty set, i.e., $A \cap B = \emptyset$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-7].
*   Sets $A_1, A_2, \ldots, A_n$ are **pairwise disjoint** or **mutually disjoint** if $A_i \cap A_j = \emptyset$ for all distinct $i, j$ [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8].

**Sum Rule for Disjoint Sets**
For disjoint finite sets $A$ and $B$, the cardinality of their union is the sum of their cardinalities [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-7]:
$|A \cup B| = |A| + |B|$.
This extends to $n$ pairwise disjoint finite sets:
$|A_1 \cup A_2 \cup \ldots \cup A_n| = |A_1| + |A_2| + \ldots + |A_n|$.

**Inclusion-Exclusion Principle**
For any two finite sets $A$ and $B$ (not necessarily disjoint), the cardinality of their union is given by [source:cs1231s-cs1231s-extra-lecture-slides-5-sets-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes5-sets-pdf#section-7]:
$|A \cup B| = |A| + |B| - |A \cap B|$.
This principle accounts for elements counted twice (once in $|A|$ and once in $|B|$) by subtracting the size of their intersection.

---

### Practice Problems

1.  **Power Set Calculation**: Let $P(A)$ denote the power set of $A$. Find $P(P(P(\emptyset)))$ [source:cs1231s-tutorial-tut03ans-post-pdf#section-1].
    *   $P(\emptyset) = \{\emptyset\}$.
    *   $P(P(\emptyset)) = P(\{\emptyset\}) = \{\emptyset, \{\emptyset\}\}$.
    *   $P(P(P(\emptyset))) = P(\{\emptyset, \{\emptyset\}\}) = \{\emptyset, \{\emptyset\}, \{\{\emptyset\}\}, \{\emptyset, \{\emptyset\}\}\}$.

2.  **Set Operations**: Let $A = \{5, 6, 7, \ldots, 12\}$. Find $\{n \in A : n \text{ is even}\}$ [source:cs1231s-tutorial-tut03qns-pdf#section-2, cs1231s-tutorial-tut03ans-post-pdf#section-2].
    *   Answer: $\{6, 8, 10, 12\}$.

3.  **Set Operations**: Let $A = \{0, 1, 4, 5, 6, 9\}$ and $B = \{0, 2, 4, 6, 8\}$. Find $|A \cap B|$ and $|A \cup B|$ [source:cs1231s-tutorial-tut03qns-pdf#section-1].
    *   $A \cap B = \{0, 4, 6\}$. So, $|A \cap B| = 3$.
    *   $A \cup B = \{0, 1, 2, 4, 5, 6, 8, 9\}$. So, $|A \cup B| = 8$.

---

**Next Topic**: [[y1s1-cs1231s-lecture-06-types-functions-composition|Lecture 06: Types of Functions and Composition]]

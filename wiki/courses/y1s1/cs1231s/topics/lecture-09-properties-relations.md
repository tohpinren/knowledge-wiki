---
page_id: "y1s1-cs1231s-lecture-09-properties-relations"
title: "Lecture 09: Properties of Relations"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Examines key properties of binary relations, including reflexivity, symmetry, transitivity, and antisymmetry, which are foundational for equivalence and partial order relations."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-2"
  - "cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-1-pdf#section-2"
  - "cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2"
  - "cs1231s-tutorial-tut04ans-post-pdf#section-2"
  - "cs1231s-tutorial-tut05qns-pdf#section-1"
topics:
  - "equivalence"
  - "set"
  - "relations"
  - "relation"
  - "such"
  - "all"
  - "equality"
  - "partitions"
  - "symmetric"
  - "classes"
source_count: 5
lecture_number: 9
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 09: Properties of Relations

This page examines the foundational properties of binary relations, crucial for understanding more complex structures like equivalence relations and partial orders. We begin by defining relations and illustrating their representation, then delve into the key properties: reflexivity, symmetry, and transitivity. These properties combine to define equivalence relations, which are intrinsically linked to the concept of partitions. Finally, we introduce antisymmetry and explore partial order relations.

## Introduction to Relations

A **relation** formalizes the idea of elements being "related" in some way. Historically, the concept of relations, particularly equivalence relations, emerged from a desire to generalize the notion of "equality" into a more flexible mathematical framework, such as congruence modulo *n* [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-1-pdf#section-1].

For instance, we've encountered congruence modulo *n*:
*   $a \equiv b \pmod n$ if and only if $a \pmod n = b \pmod n$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-2].
*   Addition, multiplication, and subtraction make sense under this congruence [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-2].
*   "Division by $a$" is possible if and only if $\gcd(a, n) = 1$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-2].
*   Solving $ax \equiv c \pmod n$ for $x$ is possible when $\gcd(a, n) = 1$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-2].

The motivation is to transform such notions of "congruence" into a form of "actual equality" by identifying the essential qualities that any notion of equality should possess [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-1-pdf#section-1].

### Defining a Relation

A **relation** from a set $A$ to a set $B$ is formally defined as a subset of the Cartesian product $A \times B$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-1].
If an ordered pair $(x, y)$ is in the relation $R$, we write "$x R y$", meaning "$x$ is $R$-related to $y$" [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-1]. If $(x, y) \notin R$, we write "$x \not R y$".

**Example 1: "Is enrolled in"**
Let $S$ be the set of all NUS students and $M$ be the set of all modules offered by NUS. The relation "is enrolled in" from $S$ to $M$ is the set:
$R = \{(x, y) \in S \times M : x \text{ is enrolled in } y\}$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-1].

**Example 2: Numerical Relation**
Let $A = \{0, 1, 2\}$ and $B = \{1, 2, 3, 4\}$. Define the relation $R$ from $A$ to $B$ by setting $x R y \iff x < y$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-1].
As a set, $R = \{(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4)\}$.
In this relation, $0 R 1$ and $0 R 2$, but $2 \not R 1$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-3].

### Arrow Diagrams

Relations can be visualized using **arrow diagrams**. An arrow from element $a$ to element $b$ indicates that $a R b$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-1].

**Example:**
Let $A = \{1, 2, 3, 4\}$ and $B = \{x, y, z\}$. Consider the relation $R$ from $A$ to $B$ defined by $R = \{(1, x), (1, y), (2, x), (2, y), (2, z), (3, z), (4, z)\}$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-1].
An arrow diagram would show:
*   Arrows from 1 to x, y
*   Arrows from 2 to x, y, z
*   Arrow from 3 to z
*   Arrow from 4 to z

## Properties of Binary Relations on a Set

A **binary relation on a set $A$** is a relation from $A$ to $A$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2]. Key properties for such relations include reflexivity, symmetry, and transitivity.

### 1. Reflexivity

A relation $R$ on a set $A$ is **reflexive** if every element is related to itself [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
Formally: $\forall x \in A (x R x)$.

**Examples:**
*   **Equality relation ($=$)** on a set $A$: For all $x, y \in A$, $x R y \iff x = y$. This is reflexive because $x = x$ for all $x \in A$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Subset relation ($\subseteq$)** on a set $U$ of sets: For all $X, Y \in U$, $X R' Y \iff X \subseteq Y$. This is reflexive because $X \subseteq X$ for any set $X$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Non-strict less-than relation ($\le$)** on $\mathbb{Q}$: For all $x, y \in \mathbb{Q}$, $x R y \iff x \le y$. This is reflexive because $x \le x$ for all $x \in \mathbb{Q}$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Strict less-than relation ($<$)** on $\mathbb{Q}$: For all $x, y \in \mathbb{Q}$, $x R' y \iff x < y$. This is *not* reflexive because $x \not< x$ (e.g., $0 \not< 0$) [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Divisibility relation ($|$)** on $\mathbb{Z}$: For all $x, y \in \mathbb{Z}$, $x R y \iff x | y$. This is reflexive because $x | x$ for any integer $x$ (since $x = 1 \cdot x$) [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Congruence-mod-$n$ relation ($\equiv \pmod n$)** on $\mathbb{Z}$: For a fixed $n \in \mathbb{Z}^+$, for all $x, y \in \mathbb{Z}$, $x R' y \iff x \equiv y \pmod n$. This is reflexive because $x \equiv x \pmod n$ for all $x \in \mathbb{Z}$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Relation $R$ on $\mathbb{Z} \setminus \{0\}$ defined by $a R b \iff ab > 0$**: This is reflexive because for any $a \in \mathbb{Z} \setminus \{0\}$, $a^2 > 0$ [source:cs1231s-tutorial-tut04ans-post-pdf#section-6].

### 2. Symmetry

A relation $R$ on a set $A$ is **symmetric** if whenever $x$ is related to $y$, then $y$ is also related to $x$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
Formally: $\forall x, y \in A (x R y \implies y R x)$.

A relation $R$ is symmetric if and only if any of the following logically equivalent conditions hold [source:cs1231s-tutorial-tut04ans-post-pdf#section-2]:
*   $\forall x, y \in A (x R y \implies y R x)$ (the definition)
*   $\forall x, y \in A (x R y \iff y R x)$
*   $R = R^{-1}$ (where $R^{-1}$ is the inverse relation, i.e., $(y,x) \in R^{-1} \iff (x,y) \in R$)

**Examples:**
*   **Equality relation ($=$)** on a set $A$: If $x = y$, then $y = x$. Thus, it is symmetric [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Subset relation ($\subseteq$)** on a set $U$ of sets: This is *not* symmetric. For example, if $U = \{\{1\}, \{1,2\}\}$, then $\{1\} \subseteq \{1,2\}$, but $\{1,2\} \not\subseteq \{1\}$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Non-strict less-than relation ($\le$)** on $\mathbb{Q}$: This is *not* symmetric. For example, $0 \le 1$ but $1 \not\le 0$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Strict less-than relation ($<$)** on $\mathbb{Q}$: This is *not* symmetric. For example, $0 < 1$ but $1 \not< 0$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Divisibility relation ($|$)** on $\mathbb{Z}$: This is *not* symmetric. For example, $1 | 2$ but $2 \not| 1$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Congruence-mod-$n$ relation ($\equiv \pmod n$)** on $\mathbb{Z}$: This is symmetric because if $x \equiv y \pmod n$, then $y \equiv x \pmod n$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Relation $R$ on $\mathbb{Z} \setminus \{0\}$ defined by $a R b \iff ab > 0$**: This is symmetric because if $ab > 0$, then $ba > 0$ by the commutative law of multiplication [source:cs1231s-tutorial-tut04ans-post-pdf#section-6].

### 3. Transitivity

A relation $R$ on a set $A$ is **transitive** if whenever $x$ is related to $y$ and $y$ is related to $z$, then $x$ is also related to $z$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
Formally: $\forall x, y, z \in A (x R y \land y R z \implies x R z)$.

**Examples:**
*   **Equality relation ($=$)** on a set $A$: If $x = y$ and $y = z$, then $x = z$. Thus, it is transitive [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Subset relation ($\subseteq$)** on a set $U$ of sets: If $X \subseteq Y$ and $Y \subseteq Z$, then $X \subseteq Z$. Thus, it is transitive [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Non-strict less-than relation ($\le$)** on $\mathbb{Q}$: If $x \le y$ and $y \le z$, then $x \le z$. Thus, it is transitive [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Strict less-than relation ($<$)** on $\mathbb{Q}$: If $x < y$ and $y < z$, then $x < z$. Thus, it is transitive [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Divisibility relation ($|$)** on $\mathbb{Z}$: If $x | y$ and $y | z$, then $x | z$. Thus, it is transitive [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Congruence-mod-$n$ relation ($\equiv \pmod n$)** on $\mathbb{Z}$: This is transitive because if $x \equiv y \pmod n$ and $y \equiv z \pmod n$, then $x \equiv z \pmod n$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2].
*   **Relation $R$ on $\mathbb{Z} \setminus \{0\}$ defined by $a R b \iff ab > 0$**: If $ab > 0$ and $bc > 0$, it implies that $a,b$ have the same sign and $b,c$ have the same sign. Therefore, $a,c$ must also have the same sign, meaning $ac > 0$. Thus, it is transitive [source:cs1231s-tutorial-tut04ans-post-pdf#section-6].

### 4. Antisymmetry

A relation $R$ on a set $A$ is **antisymmetric** if the only way $x$ can be related to $y$ and $y$ related to $x$ is if $x$ and $y$ are the same element [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5, cs1231s-tutorial-tut05qns-pdf#section-2].
Formally: $\forall x, y \in A (x R y \land y R x \implies x = y)$.

**Note:** Antisymmetry is distinct from (and not the opposite of) symmetry.
*   A relation can be both symmetric and antisymmetric (e.g., the equality relation).
*   A relation can be neither symmetric nor antisymmetric (e.g., the "less than or equal to" relation on integers).
*   A relation can be symmetric but not antisymmetric (e.g., congruence mod n for n > 1).
*   A relation can be antisymmetric but not symmetric (e.g., the "less than" relation on integers).

**Examples:**
*   **Equality relation ($=$)** on a set $A$: If $x = y$ and $y = x$, then $x = y$. It is antisymmetric [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5].
*   **Subset relation ($\subseteq$)** on a set $U$ of sets: If $X \subseteq Y$ and $Y \subseteq X$, then $X = Y$. It is antisymmetric [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5].
*   **Non-strict less-than relation ($\le$)** on $\mathbb{Q}$: If $x \le y$ and $y \le x$, then $x = y$. It is antisymmetric [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5].
*   **Strict less-than relation ($<$)** on $\mathbb{Q}$: This is antisymmetric vacuously, as $x < y$ and $y < x$ can never simultaneously be true.
*   **Divisibility relation ($|$)** on $\mathbb{Z}^+$ (positive integers): If $x | y$ and $y | x$, then since $x, y$ are positive, it must be that $x = y$. It is antisymmetric on $\mathbb{Z}^+$ [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5]. However, on $\mathbb{Z}$, it is *not* antisymmetric, e.g., $2 | -2$ and $-2 | 2$, but $2 \neq -2$.
*   **Congruence-mod-$n$ relation ($\equiv \pmod n$)** on $\mathbb{Z}$: This is *not* antisymmetric for $n > 1$. For example, for $n=2$, $0 \equiv 2 \pmod 2$ and $2 \equiv 0 \pmod 2$, but $0 \neq 2$ [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5].
*   **Relation $R$ on $S$ (strings) defined by $a R b \iff \text{len}(a) \le \text{len}(b)$**: This is *not* antisymmetric. For example, if $a = \text{"s"}$ and $b = \text{"u"}$, then $\text{len}(a) = 1$ and $\text{len}(b) = 1$. So $\text{len}(a) \le \text{len}(b)$ and $\text{len}(b) \le \text{len}(a)$. Thus $a R b$ and $b R a$, but $a \ne b$ [source:cs1231s-tutorial-tut05qns-pdf#section-2].

### Asymmetry

A relation $R$ on a set $A$ is **asymmetric** if whenever $x$ is related to $y$, then $y$ is *not* related to $x$ [source:cs1231s-tutorial-tut05qns-pdf#section-1, cs1231s-tutorial-tut05qns-pdf#section-2].
Formally: $\forall x, y \in A (x R y \implies y \not R x)$.

An asymmetric relation cannot be reflexive. If $x R x$ were true, then $x R x \implies x \not R x$, which is a contradiction.
An asymmetric relation is always antisymmetric. If $(x R y \land y R x)$ were true, then by asymmetry it would imply $y \not R x$, a contradiction. Therefore, $(x R y \land y R x)$ is always false, and the implication $(x R y \land y R x \implies x = y)$ is vacuously true.

**Example:**
*   The **strict less-than relation ($<$)** on $\mathbb{Q}$: If $x < y$, then $y \not< x$. This is asymmetric.
*   An empty relation on a non-empty set is asymmetric (and symmetric, and transitive) [source:cs1231s-tutorial-tut05qns-pdf#section-1].

## Equivalence Relations

An **equivalence relation** is a binary relation that is reflexive, symmetric, and transitive [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2]. Equivalence relations capture the essential qualities of equality, allowing us to group "equivalent" elements together.

### Equivalence Classes and Quotient Sets

Let $R$ be an equivalence relation on a set $A$. For each $x \in A$, the **equivalence class of $x$ with respect to $R$**, denoted $[x]_R$, is defined as the set of all elements in $A$ that are $R$-related to $x$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2]:
$[x]_R = \{y \in A : x R y\}$.
When the relation $R$ is clear from context, the subscript can be dropped, and we simply write $[x]$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6].

The **quotient set** of $A$ by $R$, denoted $A/R$, is the set of all distinct equivalence classes [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2]:
$A/R = \{[x]_R : x \in A\}$.

**Example 1: Equality relation**
The equality relation ($=$) on a set $A$ is an equivalence relation. The equivalence classes are of the form [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-2]:
$[x] = \{y \in A : x = y\} = \{x\}$.
The quotient set is $A/R = \{\{x\} : x \in A\}$, which means each element forms its own equivalence class [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6].

**Example 2: Congruence-mod-$n$ relation**
For a fixed $n \in \mathbb{Z}^+$, the congruence-mod-$n$ relation on $\mathbb{Z}$ is an equivalence relation. The equivalence classes are of the form [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-3]:
$[x] = \{y \in \mathbb{Z} : x \equiv y \pmod n\} = \{x + nk : k \in \mathbb{Z}\}$.
The quotient set is $\mathbb{Z}/R_n = \{[0], [1], \dots, [n-1]\}$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6].
For $n=2$, there are two equivalence classes:
*   $[0] = \{2k : k \in \mathbb{Z}\}$ (even integers)
*   $[1] = \{2k+1 : k \in \mathbb{Z}\}$ (odd integers) [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6].

### Properties of Equivalence Classes

For an equivalence relation $R$ on a set $A$, the following statements are logically equivalent for all $x, y \in A$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-3]:
1.  $x R y$
2.  $[x] = [y]$
3.  $[x] \cap [y] \neq \emptyset$

**Proof Sketch:**
*   **((1) $\implies$ (2))**: Assume $x R y$. By symmetry, $y R x$. For any $z \in [x]$, $x R z$. By transitivity (from $y R x$ and $x R z$), $y R z$, so $z \in [y]$. Thus, $[x] \subseteq [y]$. By switching the roles of $x$ and $y$, we can similarly show $[y] \subseteq [x]$. Therefore, $[x] = [y]$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-3].
*   **((2) $\implies$ (3))**: Assume $[x] = [y]$. Then $[x] \cap [y] = [x]$. By reflexivity, $x R x$, so $x \in [x]$. Since $x \in [x]$, $[x]$ is non-empty, and thus $[x] \cap [y] \neq \emptyset$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-3].
*   **((3) $\implies$ (1))**: Assume $[x] \cap [y] \neq \emptyset$. Let $z$ be an element in the intersection. Then $z \in [x]$ and $z \in [y]$. By definition of equivalence class, $x R z$ and $y R z$. By symmetry, $z R y$. By transitivity (from $x R z$ and $z R y$), $x R y$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-3].

## Partitions

A **partition** of a non-empty set $A$ is a collection of non-empty subsets of $A$ (called **components**) that satisfy two conditions [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-3]:
1.  **Covering condition (at least one)**: Every element in $A$ belongs to at least one subset in the partition.
    Formally: $\forall x \in A, \exists S \in \mathcal{C} (x \in S)$.
2.  **Disjointness condition (at most one)**: Every element in $A$ belongs to at most one subset in the partition. This means that any two distinct subsets in the partition must be disjoint.
    Formally: $\forall x \in A, \forall S, S' \in \mathcal{C} ((x \in S \land x \in S') \implies S = S')$.
    This condition implies that if $S \neq S'$, then $S \cap S' = \emptyset$.

Combining these, a partition essentially divides a set into a collection of non-overlapping, non-empty subsets whose union is the original set.

**Example 1: Partitions of a small set**
Let $A = \{1, 2, 3\}$. Some possible partitions of $A$ are [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-3]:
*   $\{\{1\}, \{2\}, \{3\}\}$
*   $\{\{1\}, \{2, 3\}\}$
*   $\{\{2\}, \{1, 3\}\}$
*   $\{\{3\}, \{1, 2\}\}$
*   $\{\{1, 2, 3\}\}$

**Example 2: Partition from congruence-mod-2**
The congruence-mod-2 relation on $\mathbb{Z}$ gives rise to the partition [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-3]:
$\{\{2k : k \in \mathbb{Z}\}, \{2k+1 : k \in \mathbb{Z}\}\}$.
This partition separates all integers into two groups: even numbers and odd numbers.

## The Relationship Between Equivalence Relations and Partitions

There is a fundamental connection between equivalence relations and partitions: every equivalence relation on a set corresponds to a unique partition of that set, and vice-versa.

### Theorem 9.3.4: Equivalence Relations Induce Partitions

If $R$ is an equivalence relation on a set $A$, then the set of its equivalence classes, $A/R$, forms a partition of $A$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].

**Proof Sketch:**
We need to show that $A/R$ satisfies the two conditions of a partition:
1.  **Covering condition ($\ge 1$)**: For any $x \in A$, by reflexivity, $x R x$, so $x \in [x]$. Therefore, $x$ belongs to the equivalence class $[x] \in A/R$. Every element is in at least one class [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].
2.  **Disjointness condition ($\le 1$)**: For any two equivalence classes $[x], [y] \in A/R$, if their intersection is not empty ($[x] \cap [y] \neq \emptyset$), then by [[#Properties of Equivalence Classes|Proposition 9.2.13]], it implies that $[x] = [y]$. This means that distinct equivalence classes are disjoint. Every element is in at most one class [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].

Since both conditions are met, $A/R$ is a partition of $A$.

### Theorem 9.3.5: Partitions Induce Equivalence Relations

If $\mathcal{C}$ is a partition of a set $A$, then there exists an equivalence relation $R$ on $A$ such that $A/R = \mathcal{C}$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].

**Proof Sketch:**
1.  **Define $R$**: Define a relation $R$ on $A$ such that for all $x, y \in A$, $x R y \iff x \text{ and } y \text{ are in the same component } S \in \mathcal{C}$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].
2.  **Prove $R$ is reflexive**: For any $x \in A$, by the covering condition of a partition ($\ge 1$), there exists a component $S \in \mathcal{C}$ such that $x \in S$. Since $x$ is in the same component as itself, $x R x$. Thus, $R$ is reflexive [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].
3.  **Prove $R$ is symmetric**: Assume $x R y$. By definition of $R$, $x$ and $y$ are in the same component $S \in \mathcal{C}$. This means $y$ and $x$ are also in the same component $S$. Therefore, $y R x$. Thus, $R$ is symmetric [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].
4.  **Prove $R$ is transitive**: Assume $x R y$ and $y R z$. By definition of $R$, $x$ and $y$ are in some component $S \in \mathcal{C}$, and $y$ and $z$ are in some component $S' \in \mathcal{C}$. Since $y \in S$ and $y \in S'$, and $S, S'$ are components of a partition, by the disjointness condition ($\le 1$), it must be that $S = S'$. Therefore, $x, y, z$ are all in the same component $S$. This means $x R z$. Thus, $R$ is transitive [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].
5.  **Show $A/R = \mathcal{C}$**: This part involves showing mutual inclusion: $A/R \subseteq \mathcal{C}$ and $\mathcal{C} \subseteq A/R$. The key step is to show that for any $x \in A$, if $S \in \mathcal{C}$ contains $x$, then the equivalence class $[x]$ is equal to $S$. This relies on the properties of partitions and the definition of $R$ [source:cs1231s-cs1231s-extra-lecture-slides-9-1-equiv-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-4].

These theorems establish a powerful connection, showing that equivalence relations and partitions are two ways of looking at the same underlying structure for dividing a set into distinct, non-overlapping subsets.

## Partial Orders

While equivalence relations model generalized equality, **partial orders** model generalized "less than or equal to" or "precedence." A binary relation $R$ on a set $A$ is a **(non-strict) partial order** if it is [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5]:
1.  **Reflexive**: $\forall x \in A (x R x)$
2.  **Antisymmetric**: $\forall x, y \in A (x R y \land y R x \implies x = y)$
3.  **Transitive**: $\forall x, y, z \in A (x R y \land y R z \implies x R z)$

We often use the symbol "$\preceq$" to denote a partial order.

**Examples:**
*   The **non-strict less-than relation ($\le$)** on $\mathbb{Q}$ is a partial order [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5].
*   The **divisibility relation ($|$)** on $\mathbb{Z}^+$ (positive integers) is a partial order [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5].
*   The **subset relation ($\subseteq$)** on a power set $\mathcal{P}(A)$ is a partial order [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5].

### Comparability

For a partial order $R$ on a set $A$, two elements $x, y \in A$ are **comparable (under $R$)** if $x R y$ or $y R x$ [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5]. If neither $x R y$ nor $y R x$ holds, the elements are incomparable.

### Total Order

A relation $R$ on a set $A$ is a **(non-strict) total order** if it is a partial order and, in addition, every pair of elements in $A$ is comparable [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5]:
Formally: $\forall x, y \in A (x R y \lor y R x)$.
A total order is also sometimes called a **linear order**.

**Example:**
*   The **non-strict less-than relation ($\le$)** on $\mathbb{Q}$ is a total order, as any two rational numbers can be compared [source:cs1231s-cs1231s-extra-lecture-slides-notes9-relns-pdf#section-5].
*   The **divisibility relation ($|$)** on $\mathbb{Z}^+$ is *not* a total order because, for example, 2 and 3 are in $\mathbb{Z}^+$, but $2 \not| 3$ and $3 \not| 2$.
*   The **subset relation ($\subseteq$)** on a power set $\mathcal{P}(A)$ is generally *not* a total order (unless $|A| \le 1$). For $A=\{1,2\}$, $\{\{1\},\{2\}\}$ has two elements that are incomparable.

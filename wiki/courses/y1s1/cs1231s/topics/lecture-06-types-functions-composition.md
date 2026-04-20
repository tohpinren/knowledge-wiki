---
page_id: "y1s1-cs1231s-lecture-06-types-functions-composition"
title: "Lecture 06: Types of Functions and Composition"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Defines injective (one-to-one), surjective (onto), and bijective functions, and explores function composition and inverse functions."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-3"
  - "cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-1"
  - "cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-2"
  - "cs1231s-tutorial-tut04ans-post-pdf#section-1"
  - "cs1231s-cheatsheet-tutorials-tut06ans-post-removed-pdf#section-1"
topics:
  - "functions"
  - "function"
  - "element"
  - "domain"
  - "codomain"
  - "range"
  - "its"
  - "encrypt"
  - "inverse"
  - "composition"
source_count: 5
lecture_number: 6
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 06: Types of Functions and Composition

## Introduction to Functions

Functions are fundamental to modern mathematical discourse and serve as interesting mathematical objects. In this module, they provide a topic to practice writing and understanding proofs [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-2].

### Definition of a Function

A **function** (or **map**) from a set $A$ to a set $B$, written as $f: A \to B$, is an assignment that maps each element of $A$ to exactly one element of $B$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-1].

For an element $x \in A$, $f(x)$ denotes the element in $B$ that $f$ assigns to $x$. If $y = f(x)$, we say that $f$ maps $x$ to $y$, or $f: x \mapsto y$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-1].

The components of a function $f: A \to B$ are [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-1]:
*   $A$ is called the **domain** of $f$.
*   $B$ is called the **codomain** of $f$.
*   The **range** (or **image**) of $f$ is the set of all values $f(x)$ for $x \in A$, denoted as $\{f(x) : x \in A\}$ or $\{y \in B : y = f(x) \text{ for some } x \in A\}$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-7].

**Arrow Diagrams**
Functions can be visualized using arrow diagrams where dots on the left represent elements of the domain, dots on the right represent elements of the codomain, and arrows from left to right dots indicate the assignment. A well-defined function ensures every dot on the left (domain element) is joined to exactly one dot on the right (codomain element) [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-6].

### Defining a Function Using a General Expression

A function $f: A \to B$ can often be specified by an expression $t$ involving a special symbol $x$ (a variable). This means $f$ assigns to each $x_0 \in A$ the value of $t$ when every occurrence of $x$ in $t$ is replaced by $x_0$. In this case, we write $f: A \to B; x \mapsto t$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-2].

**Example 6.1.3:** Consider `encrypt: Z → Z; x ↦ x³ + 23x`.
For $x_0 \in \mathbb{Z}$, `encrypt` assigns $x_0³ + 23x_0$.
*   `encrypt(0) = 0³ + 23 × 0 = 0`
*   `encrypt(1) = 1³ + 23 × 1 = 24`
The range of `encrypt` is $\{x³ + 23x : x \in \mathbb{Z}\}$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-2].

### Specific Types of Functions

#### Identity Function

The **identity function** on a set $A$, denoted $id_A$, is a function $id_A: A \to A$ where $x \mapsto x$. Its domain, codomain, and range are all $A$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-3].

#### Absolute Value Function

The **absolute value function** `absval: Q → Q` for $x \in \mathbb{Q}$ is defined as [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-4]:
$$
absval(x) = \begin{cases} x, & \text{if } x \ge 0 \\ -x, & \text{otherwise} \end{cases}
$$
It has domain $\mathbb{Q}$, codomain $\mathbb{Q}$, and the range is $\mathbb{Q}_{\ge 0}$ (non-negative rational numbers) [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-4]. It is usually written as $|x|$.
*   $|1| = 1$ because $1 \ge 0$.
*   $|-23| = -(-23) = 23$ because $\sim (-23 \ge 0)$.

#### Floor and Ceiling Functions

For each $x \in \mathbb{Q}$:
*   The **floor function** `floor(x)` (or $\lfloor x \rfloor$) is the maximum integer $y$ such that $y \le x$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].
*   The **ceiling function** `ceil(x)` (or $\lceil x \rceil$) is the minimum integer $y$ such that $y \ge x$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].
Examples:
*   $\lfloor 15.11 \rfloor = 15$, $\lceil 15.11 \rceil = 16$.
*   $\lfloor -5.2 \rfloor = -6$, $\lceil -5.2 \rceil = -5$.
*   For any $x \in \mathbb{Z}$, $\lfloor x \rfloor = x = \lceil x \rceil$. The range of both functions for domain $\mathbb{Q}$ is $\mathbb{Z}$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

#### Sequences

A **sequence** is a function $a$ whose domain is $\mathbb{Z}$, $\mathbb{Z}^+$, or $\{x \in \mathbb{Z} : k \le x \le l\}$ for some integers $k, l$. If $a$ is a sequence, we may write $a_n$ for $a(n)$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-6].

**Example 6.1.13 (Harmonic sequence):** Let $a$ be the sequence $\mathbb{Z}^+ \to \mathbb{Q}$ defined by setting $a_n = 1/n$ for every $n \in \mathbb{Z}^+$. Then $a_1, a_2, a_3, \dots$ are $1, 1/2, 1/3, 1/4, \dots$ [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-6].

### Well-Defined Functions

A function is **well-defined** if its definition ensures that every element of the domain is assigned exactly one element of the codomain [source: cs1231s-cs1231s-extra-lecture-slides-6-1-fns-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].
Problems can arise if:
*   An element in the domain is not assigned any value in the codomain.
*   An element in the domain is assigned more than one value in the codomain.

**Example 6.1.17:** Define $h: \mathbb{Q} \to \mathbb{Z}$ by setting $h(m/n) = m$ for all $m, n \in \mathbb{Z}$ where $n \ne 0$ [source: cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7]. This function is not well-defined because, for instance, $1/2$ and $2/4$ are the same rational number, but $h(1/2) = 1$ and $h(2/4) = 2$, which means $1/2$ is assigned two different values.

## Equality of Functions

Two functions $f: A \to B$ and $g: C \to D$ are equal, written as $f = g$, if and only if [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7]:
1.  Their domains are equal ($A = C$).
2.  Their codomains are equal ($B = D$).
3.  They assign the same value to every element in their domain ($f(x) = g(x)$ for all $x \in A$).

**Example 6.1.20:** Let $f: \{0, 2\} \to \mathbb{Z}$ and $g: \{0, 2\} \to \mathbb{Z}$ be defined as $f(x) = 2x$ and $g(x) = x^2$ for all $x \in \{0, 2\}$.
*   For $x=0: f(0) = 0, g(0) = 0^2 = 0$.
*   For $x=2: f(2) = 4, g(2) = 2^2 = 4$.
Since their domains, codomains, and function values for each element are identical, $f = g$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

**Example 6.1.21:** Let $f: \mathbb{Z} \to \mathbb{Z}$ and $g: \mathbb{Z} \to \mathbb{Q}$ be defined as $f(x) = x^3 = g(x)$ for all $x \in \mathbb{Z}$. Here, $f \ne g$ because their codomains ($\mathbb{Z}$ vs $\mathbb{Q}$) are different [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

## Function Composition

For functions $f: A \to B$ and $g: B \to C$, their **composition** $g \circ f$ (read as "g composed with f" or "g circle f") is a function $g \circ f: A \to C$ defined such that for every $x \in A$, $(g \circ f)(x) = g(f(x))$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].
For $g \circ f$ to be well-defined, the codomain of $f$ must be equal to the domain of $g$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

### Composition with Identity Functions

For any function $f: A \to B$:
1.  Composing $f$ with the identity function on its domain: $(f \circ id_A)(x) = f(id_A(x)) = f(x)$ for all $x \in A$. Thus, $f \circ id_A = f$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].
2.  Composing $f$ with the identity function on its codomain: $(id_B \circ f)(x) = id_B(f(x)) = f(x)$ for all $x \in A$. Thus, $id_B \circ f = f$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

### Non-commutativity of Function Composition

Function composition is generally not commutative, meaning $g \circ f \ne f \circ g$.

**Example 6.1.25:** Let $f, g: \mathbb{Z} \to \mathbb{Z}$ be defined as $f(x) = 3x$ and $g(x) = x + 1$.
*   $(g \circ f)(x) = g(f(x)) = g(3x) = 3x + 1$.
*   $(f \circ g)(x) = f(g(x)) = f(x + 1) = 3(x + 1)$.
For example, $(g \circ f)(0) = 3(0) + 1 = 1$, while $(f \circ g)(0) = 3(0 + 1) = 3$. Since $1 \ne 3$, $g \circ f \ne f \circ g$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

### Associativity of Function Composition

Function composition is associative. Given $f: A \to B$, $g: B \to C$, and $h: C \to D$, then $(h \circ g) \circ f = h \circ (g \circ f)$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

**Proof of Associativity (Theorem 6.1.26):**
To prove $(h \circ g) \circ f = h \circ (g \circ f)$:
1.  **Domains:** The domain of $(h \circ g) \circ f$ is $A$, and the domain of $h \circ (g \circ f)$ is also $A$.
2.  **Codomains:** The codomain of $(h \circ g) \circ f$ is $D$, and the codomain of $h \circ (g \circ f)$ is also $D$.
3.  **Function Values:** For every $x \in A$:
    *   $((h \circ g) \circ f)(x) = (h \circ g)(f(x))$ (by definition of composition)
    *   $= h(g(f(x)))$ (by definition of composition)
    *   $= h((g \circ f)(x))$ (by definition of composition)
    *   $= (h \circ (g \circ f))(x)$ (by definition of composition)
Since the domains, codomains, and function values are equal for all elements, the functions are equal [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

## Setwise Image and Preimage

For a function $f: A \to B$:
*   If $X \subseteq A$, the **(setwise) image of $X$** under $f$ is $f(X) = \{f(x) : x \in X\}$ or $\{y \in B : y = f(x) \text{ for some } x \in X\}$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5]. Note that $f(A)$ is the range/image of $f$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].
*   If $Y \subseteq B$, the **(setwise) preimage of $Y$** under $f$ is $f^{-1}(Y) = \{x \in A : y = f(x) \text{ for some } y \in Y\}$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

It is important to note that, in general, $f^{-1}$ cannot operate on individual elements but rather on subsets (i.e., it represents the preimage, not an inverse function on elements) [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5]. The notation $f^{-1}(y)$ where $y \in B$ is only meaningful if an inverse function $f^{-1}: B \to A$ exists. If $f^{-1}$ exists, then $f^{-1}(y)$ refers to the unique element $x \in A$ such that $f(x)=y$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-7].

**Example 6.2.3:** Define $g: \mathbb{Z} \to \mathbb{Z}$ by $g(x) = x^2$.
1.  If $X = \{-1, 0, 1\}$, then $g(X) = \{g(-1), g(0), g(1)\} = \{1, 0, 1\} = \{0, 1\}$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].
2.  If $Y = \{0, 1, 2\}$, then $g^{-1}(Y) = \{x \in \mathbb{Z} : g(x) \in \{0, 1, 2\}\} = \{0, -1, 1\}$ (since $g(0)=0$, $g(1)=1$, $g(-1)=1$) [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

## Types of Functions: Injections, Surjections, and Bijections

Let $f: A \to B$ be a function.

### Surjective (Onto) Functions

A function $f$ is **surjective** (or **onto**) if every element in the codomain $B$ is the image of at least one element in the domain $A$. Symbolically: $\forall y \in B, \exists x \in A \text{ such that } y = f(x)$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5]. A surjective function is also called a **surjection**.

**Remark:** A function is surjective if and only if its codomain is equal to its range [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-9, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

**Non-surjectivity:** A function $f: A \to B$ is not surjective if and only if there exists at least one element in $B$ that is not mapped to by any element in $A$. Symbolically: $\exists y \in B, \forall x \in A \text{ such that } y \ne f(x)$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-10, cs1231s-cheatsheet-tutorials-tut06ans-post-removed-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

**Example 6.2.6 (Surjective function):** The function $f: \mathbb{Q} \to \mathbb{Q}$ defined by $f(x) = 3x + 1$ is surjective.
*   **Proof:** Take any $y \in \mathbb{Q}$. Let $x = (y - 1)/3$. Since $y \in \mathbb{Q}$, $x$ is also in $\mathbb{Q}$. Then $f(x) = 3((y - 1)/3) + 1 = (y - 1) + 1 = y$. Thus, for every $y$ in the codomain, there exists an $x$ in the domain such that $f(x)=y$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-9, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

**Example 6.2.8 (Non-surjective function):** The function $g: \mathbb{Z} \to \mathbb{Z}$ defined by $g(x) = x^2$ is not surjective.
*   **Proof:** Note that $g(x) = x^2 \ge 0$ for all $x \in \mathbb{Z}$. Therefore, no integer less than 0 (e.g., $-1$) can be an image of any $x \in \mathbb{Z}$. Since $-1 \in \mathbb{Z}$ (codomain) but $g(x) \ne -1$ for any $x \in \mathbb{Z}$, $g$ is not surjective [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-10, cs1231s-cheatsheet-tutorials-tut06ans-post-removed-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

### Injective (One-to-one) Functions

A function $f$ is **injective** (or **one-to-one**) if distinct elements in the domain always map to distinct elements in the codomain. Symbolically: $\forall x, x' \in A, (f(x) = f(x') \Rightarrow x = x')$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-8, cs1231s-cheatsheet-tutorials-tut06ans-post-removed-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5]. An injective function is also called an **injection**.

**Non-injectivity:** A function $f: A \to B$ is not injective if and only if there exist at least two distinct elements in $A$ that map to the same element in $B$. Symbolically: $\exists x, x' \in A \text{ such that } (f(x) = f(x') \land x \ne x')$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-12, cs1231s-cheatsheet-tutorials-tut06ans-post-removed-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

**Example 6.2.9 (Injective function):** The function $f: \mathbb{Q} \to \mathbb{Q}$ defined by $f(x) = 3x + 1$ is injective.
*   **Proof:** Let $x, x' \in \mathbb{Q}$ such that $f(x) = f(x')$. Then $3x + 1 = 3x' + 1$. Subtracting 1 from both sides gives $3x = 3x'$, and dividing by 3 gives $x = x'$. Thus, $f$ is injective [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-11, cs1231s-cheatsheet-tutorials-tut06ans-post-removed-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

**Example 6.2.11 (Non-injective function):** The function $g: \mathbb{Z} \to \mathbb{Z}$ defined by $g(x) = x^2$ is not injective.
*   **Proof:** Note that $g(1) = 1^2 = 1$ and $g(-1) = (-1)^2 = 1$. Here, $f(1) = f(-1)$ but $1 \ne -1$. Therefore, $g$ is not injective [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-12, cs1231s-cheatsheet-tutorials-tut06ans-post-removed-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5].

### Bijective Functions

A function $f$ is **bijective** if it is both surjective and injective. Symbolically: $\forall y \in B, \exists! x \in A \text{ such that } y = f(x)$ (meaning for every $y$ in $B$, there exists a *unique* $x$ in $A$ such that $f(x)=y$) [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-5]. A bijective function is also called a **bijection**.

## Inverse Functions

### Definition of an Inverse Function

Given a function $f: A \to B$, a function $g: B \to A$ is an **inverse** of $f$ if for all $x \in A$ and all $y \in B$, the equivalence $y = f(x) \iff x = g(y)$ holds [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-13, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-6].

**Example 6.2.14:** Define $f: \mathbb{Q} \to \mathbb{Q}$ by $f(x) = 3x + 1$. For all $x, y \in \mathbb{Q}$, $y = 3x + 1 \iff x = (y - 1)/3$.
Let $g: \mathbb{Q} \to \mathbb{Q}$ be defined by $g(y) = (y - 1)/3$. Then for all $x, y \in \mathbb{Q}$, $y = f(x) \iff x = g(y)$. Thus, $g$ is an inverse of $f$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-13, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-6].

There is no guarantee that the description of an inverse of a general function will be significantly different from its definition [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-13, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-6].

### Uniqueness of Inverses

**Proposition 6.2.16:** If a function $f: A \to B$ has inverses $g$ and $g'$, then $g = g'$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-14, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].
*   **Proof:** Let $g, g': B \to A$ be inverses of $f$. By definition of inverse, for all $x \in A$ and $y \in B$, $x = g(y) \iff y = f(x) \iff x = g'(y)$. Therefore, $g(y) = g'(y)$ for all $y \in B$. Since their domains and codomains are also the same ($B \to A$), $g = g'$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-14, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

Because inverses are unique, we can denote the inverse of a function $f$ as $f^{-1}$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-14, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

### Bijectivity and Invertibility

**Theorem 6.2.18:** A function $f: A \to B$ is bijective if and only if it has an inverse [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-15, cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-16, cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-17, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

**Proof:**
*   **("If") Suppose $f$ has an inverse $g: B \to A$. We need to show $f$ is bijective (i.e., injective and surjective).**
    1.  **Injectivity:** Let $x, x' \in A$ such that $f(x) = f(x')$. Define $y = f(x) = f(x')$. Since $g$ is an inverse of $f$, we have $x = g(y)$ and $x' = g(y)$. Therefore, $x = x'$, proving $f$ is injective [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-16, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].
    2.  **Surjectivity:** Let $y \in B$. Define $x = g(y)$. Since $g$ maps to $A$, $x \in A$. As $g$ is an inverse of $f$, $y = f(x)$. Therefore, for every $y$ in $B$, there exists an $x$ in $A$ such that $y = f(x)$, proving $f$ is surjective [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-16, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].
*   **("Only if") Suppose $f$ is bijective. We need to show $f$ has an inverse.**
    1.  Since $f$ is bijective, it is both injective and surjective. This means $\forall y \in B, \exists! x \in A$ such that $y = f(x)$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-17, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].
    2.  Define a function $g: B \to A$ by setting $g(y)$ to be the unique $x \in A$ such that $y = f(x)$ for all $y \in B$.
    3.  This function $g$ is well-defined because for each $y \in B$, there is exactly one $x \in A$ (due to bijectivity) that maps to $y$. By construction, $g$ satisfies the definition of an inverse function: $y = f(x) \iff x = g(y)$. Thus, $g$ is an inverse of $f$ [source: cs1231s-cs1231s-extra-lecture-slides-6-2-bij-1-pdf#section-17, cs1231s-cs1231s-extra-lecture-slides-notes6-fns-pdf#section-7].

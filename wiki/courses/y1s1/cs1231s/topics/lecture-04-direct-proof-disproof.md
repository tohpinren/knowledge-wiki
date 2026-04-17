---
page_id: "y1s1-cs1231s-lecture-04-direct-proof-disproof"
title: "Lecture 04: Direct Proof and Disproof"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Details methods for constructing direct proofs and disproving statements using counterexamples, along with basic definitions for integers (even, odd, prime, rational)."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1"
  - "cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2"
  - "cs1231s-cheatsheet-not-using-16pages-pdf#section-2"
topics:
  - "integer"
  - "rational"
  - "proof"
  - "integers"
  - "then"
  - "statement"
  - "true"
  - "positive"
  - "set"
  - "chapter"
source_count: 3
lecture_number: 4
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 04: Direct Proof and Disproof

This lecture introduces fundamental concepts and methods for constructing mathematical proofs, primarily focusing on direct proofs and disproofs using counterexamples. It also establishes basic definitions for different types of integers and rational numbers, which are crucial for subsequent proof-writing exercises [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1]. Proofs are written arguments that demonstrate the truth of a statement using logic and established facts [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3].

### 4.1 Direct Proof and Counterexample

In constructing proofs, it is assumed that the laws of basic algebra and the three properties of equality (reflexive, symmetric, transitive) are familiar. The set of integers is closed under addition, subtraction, and multiplication, meaning sums, differences, and products of integers are always integers. There is no integer between 0 and 1 [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4]. Quotients of integers are generally not integers, and division by zero is undefined [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

#### Basic Definitions for Integers

The following definitions are fundamental to number theory and proof construction:
*   An integer $n$ is **even** if, and only if, $n$ equals twice some integer $k$. Symbolically, $n \text{ is even} \iff \exists k \in \mathbb{Z} \text{ such that } n = 2k$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].
*   An integer $n$ is **odd** if, and only if, $n$ equals twice some integer $k$ plus 1. Symbolically, $n \text{ is odd} \iff \exists k \in \mathbb{Z} \text{ such that } n = 2k + 1$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].
*   An integer $n$ is **prime** if, and only if, $n > 1$ and for all positive integers $r$ and $s$, if $n = rs$, then either $r=1$ and $s=n$ or $r=n$ and $s=1$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].
*   An integer $n$ is **composite** if, and only if, $n > 1$ and $n=rs$ for some integers $r$ and $s$ with $1 < r < n$ and $1 < s < n$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

#### Proving Existential Statements by Constructive Proof

An existential statement, such as $\exists x \in D \text{ s.t. } Q(x)$, is true if $Q(x)$ is true for at least one element $x$ in the domain $D$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1]. To prove such a statement using a constructive proof of existence, one can either:
1.  Find a specific value of $x$ in $D$ that makes $Q(x)$ true [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].
2.  Provide a set of directions or an algorithm for finding such an $x$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

**Example 1a:** Prove that there exists an even integer $n$ that can be written in two ways as a sum of two prime numbers.
*   **Proof:** Let $n = 10$. Then $10 = 5 + 5$ and $10 = 3 + 7$. In both cases, the numbers (3, 5, 7) are prime numbers. Note that the prime numbers do not have to be distinct [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

**Example 1b:** Suppose $r$ and $s$ are integers. Prove that there is an integer $k$ such that $22r + 18s = 2k$.
*   **Proof:** Let $k = 11r + 9s$. Since integers are closed under multiplication and addition, $k$ is an integer. By the distributive law, $2k = 2(11r + 9s) = 22r + 18s$. Thus, such an integer $k$ exists [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

#### Disproving Universal Statements by Counterexample

A universal (conditional) statement is of the form $\forall x \in D, P(x) \to Q(x)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1]. Showing this statement is false is equivalent to showing its negation is true. The negation of such a statement is an existential statement: $\exists x \in D, P(x) \land \neg Q(x)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].

To disprove a universal statement, one must find a **counterexample**: a value of $x$ in $D$ for which the hypothesis $P(x)$ is true, but the conclusion $Q(x)$ is false [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

**Example 2:** Disprove the statement: $\forall a, b \in \mathbb{R}$, if $a^2 = b^2$ then $a = b$.
*   **Counterexample:** Let $a = 1$ and $b = -1$. Then $a^2 = 1^2 = 1$ and $b^2 = (-1)^2 = 1$, so $a^2 = b^2$. However, $a \neq b$ (since $1 \neq -1$). This single instance disproves the universal statement [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

#### Proving Universal Statements by Exhaustion

The method of exhaustion can be used to prove a universal conditional statement $\forall x \in D, P(x) \to Q(x)$ when the domain $D$ is finite, or when only a finite number of elements satisfy $P(x)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1]. This involves checking each case individually.

**Example 3:** Prove that for all $n \in \mathbb{Z}$, if $n$ is even and $4 \le n \le 26$, then $n$ can be written as a sum of two primes.
*   **Proof (by exhaustion):** We check all even integers $n$ from 4 to 26:
    *   $4 = 2 + 2$
    *   $6 = 3 + 3$
    *   $8 = 3 + 5$
    *   $10 = 5 + 5$ (or $3+7$)
    *   $12 = 5 + 7$
    *   $14 = 11 + 3$
    *   $16 = 5 + 11$
    *   $18 = 7 + 11$
    *   $20 = 7 + 13$
    *   $22 = 5 + 17$
    *   $24 = 5 + 19$
    *   $26 = 7 + 19$
Since the statement holds for all values in the finite domain, the proof is complete [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

#### Proving Universal Statements by Generalizing from the Generic Particular

This is a powerful technique for proving universal statements, especially when the domain is infinite. To show that every element of a set satisfies a certain property, one supposes $x$ is a particular but arbitrarily chosen element of the set, and then demonstrates that $x$ satisfies the property [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1]. The key is that the chosen element $x$ is "generic" – it has no special properties other than being part of the set.

**Example 4:** Prove that the sum of any two even integers is even.
*   **Proof:**
    1.  Let $m$ and $n$ be two particular but arbitrarily chosen even integers.
    2.  By the definition of an even number, $m = 2r$ and $n = 2s$ for some integers $r$ and $s$.
    3.  Their sum is $m + n = 2r + 2s$.
    4.  By basic algebra, $2r + 2s = 2(r + s)$.
    5.  Since integers are closed under addition, $r+s$ is an integer. Let $k = r+s$.
    6.  Therefore, $m+n = 2k$ for some integer $k$.
    7.  By the definition of an even number, $m+n$ is even.
    8.  Hence, the sum of any two even integers is even [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-1].

### 4.2 Proofs on Rational Numbers

#### Definition of Rational and Irrational Numbers

*   A real number $r$ is **rational** if, and only if, it can be expressed as a quotient of two integers with a nonzero denominator. Symbolically, $r \text{ is rational} \iff \exists a, b \in \mathbb{Z} \text{ such that } r = \frac{a}{b} \text{ and } b \neq 0$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-2, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-1].
*   A real number that is not rational is **irrational** [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-2, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-1].

#### Theorem: Every Integer is a Rational Number

*   **Proof:**
    1.  Let $a$ be a particular but arbitrarily chosen integer.
    2.  Then $a$ can be written as $\frac{a}{1}$.
    3.  This expression is in the form $\frac{x}{y}$, where $x=a$ and $y=1$ are integers, and $y \neq 0$.
    4.  By the definition of a rational number, $a$ is a rational number.
    5.  Therefore, every integer is a rational number [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-2].

#### Theorem: The Sum of Any Two Rational Numbers is Rational

*   **Proof:**
    1.  Let $r$ and $s$ be two particular but arbitrarily chosen rational numbers.
    2.  By the definition of a rational number, there exist integers $a, b, c, d$ such that $r = \frac{a}{b}$ and $s = \frac{c}{d}$, with $b \neq 0$ and $d \neq 0$.
    3.  The sum $r + s = \frac{a}{b} + \frac{c}{d}$.
    4.  Using basic algebra, $r + s = \frac{ad + bc}{bd}$.
    5.  Since integers are closed under multiplication and addition, $ad$, $bc$, and $bd$ are all integers. Also, since $b \neq 0$ and $d \neq 0$, their product $bd \neq 0$.
    6.  Therefore, $r+s$ can be expressed as a quotient of two integers with a nonzero denominator.
    7.  By the definition of a rational number, $r+s$ is rational.
    8.  Therefore, the sum of any two rational numbers is rational [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-2].

A **corollary** is a result that follows as a simple deduction from a proven theorem [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-2, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4]. For example, a corollary to the theorem above is that the double of a rational number is rational, as $2r = r+r$.

### 4.3 Proofs on Divisibility

#### Definition of Divisibility

If $n$ and $d$ are integers and $d \neq 0$, then $n$ is **divisible** by $d$ if and only if $n$ equals $d$ times some integer [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-3]. The notation $d|n$ means "$d$ divides $n$". Symbolically, for $n, d \in \mathbb{Z}$ and $d \neq 0$:
$d|n \iff \exists k \in \mathbb{Z} \text{ such that } n = dk$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-3, cs1231s-cheatsheet-not-using-16pages-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].
It is important to note that "$d|n$" is a shorthand notation for "d divides n" and is not an operation like division (e.g., $5|10=2$ is incorrect; $10/5=2$ is correct) [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].

#### Theorem: A Positive Divisor of a Positive Integer

For all positive integers $a$ and $b$, if $a|b$, then $a \le b$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-3].
*   **Proof (direct proof):**
    1.  Let $a$ and $b$ be two positive integers such that $a|b$.
    2.  By the definition of divisibility, there exists an integer $k$ such that $b = ak$.
    3.  Since both $a$ and $b$ are positive integers, $k$ must also be a positive integer, which means $k \ge 1$.
    4.  Multiplying both sides of $k \ge 1$ by $a$ (which is positive), we get $ak \ge a$.
    5.  Substituting $b=ak$, we have $b \ge a$, or $a \le b$.
    6.  Therefore, for all positive integers $a$ and $b$, if $a|b$, then $a \le b$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-3].

#### Theorem: Divisors of 1

The only divisors of 1 are 1 and -1 [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-3].
*   **Proof (by division into cases):**
    1.  Suppose $m$ is any integer that divides 1.
    2.  By the definition of divisibility, there exists an integer $k$ such that $1 = mk$.
    3.  Since $mk=1$ is positive, either both $m$ and $k$ are positive, or both $m$ and $k$ are negative.
    4.  **Case 1: Both $m$ and $k$ are positive.**
        *   Since $m|1$, by Theorem 4.3.1 (A Positive Divisor of a Positive Integer), $m \le 1$.
        *   Since $m$ is a positive integer, the only possibility is $m=1$. (If $m=1$, then $k=1$, which is a positive integer).
    5.  **Case 2: Both $m$ and $k$ are negative.**
        *   Let $m'$ = $-m$ and $k'$ = $-k$. Then $m'$ and $k'$ are positive integers.
        *   From $1=mk$, we get $1=(-m)(-k) = m'k'$.
        *   By the same reasoning as in Case 1, $m'=1$.
        *   Therefore, $-m=1$, which means $m=-1$. (If $m=-1$, then $k=-1$, which is a negative integer).
    6.  Thus, the only integers that divide 1 are 1 and -1 [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-3].

#### Theorem: Transitivity of Divisibility

For all integers $a, b,$ and $c$, if $a|b$ and $b|c$, then $a|c$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-3].
*   **Proof:**
    1.  Suppose $a, b, c$ are integers such that $a|b$ and $b|c$.
    2.  By the definition of divisibility:
        *   Since $a|b$, there exists an integer $r$ such that $b = ar$.
        *   Since $b|c$, there exists an integer $s$ such that $c = bs$.
    3.  Substitute the expression for $b$ from the first equation into the second equation: $c = (ar)s$.
    4.  By associativity of multiplication, $c = a(rs)$.
    5.  Since integers are closed under multiplication, $rs$ is an integer. Let $k = rs$.
    6.  Then $c = ak$ for some integer $k$.
    7.  By the definition of divisibility, $a|c$.
    8.  Therefore, for all integers $a, b,$ and $c$, if $a|b$ and $b|c$, then $a|c$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-3].

### 4.4 Indirect Proof

Sometimes, a direct proof can be difficult to construct. In such cases, **indirect proof methods** like proof by contradiction or proof by contraposition can be useful [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4].

#### Proof by Contradiction

To prove a statement $S$ by contradiction:
1.  Assume that the statement $S$ is false. This means its negation, $\neg S$, is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4, cs1231s-cheatsheet-not-using-16pages-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
2.  Show that this assumption leads logically to a **contradiction** (a statement that can never be true, always false) [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4, cs1231s-cheatsheet-not-using-16pages-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
3.  Conclude that the original statement $S$ must be true, because its negation leads to an impossibility [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4, cs1231s-cheatsheet-not-using-16pages-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].

**Example:** Prove that there is no greatest integer.
*   **Proof (by contradiction):**
    1.  Suppose not. That is, suppose there is a greatest integer, let's call it $g$.
    2.  By definition, this means $g > n$ for all other integers $n$.
    3.  Consider the integer $G = g + 1$.
    4.  Since integers are closed under addition, $G$ is an integer.
    5.  However, $G = g + 1 > g$. This contradicts our initial assumption that $g$ is the greatest integer.
    6.  Since our assumption leads to a contradiction, the assumption must be false.
    7.  Therefore, there is no greatest integer [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4].

A classic application of proof by contradiction is demonstrating that $\sqrt{2}$ is irrational [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4].

#### Proof by Contraposition

Proof by contraposition leverages the logical equivalence between a conditional statement $p \to q$ and its contrapositive $\neg q \to \neg p$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4, cs1231s-cheatsheet-not-using-16pages-pdf#section-1, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3]. If the contrapositive statement is proven true, then the original statement must also be true.

To prove a statement of the form $\forall x \in D, P(x) \to Q(x)$ by contraposition:
1.  Rewrite the statement into its contrapositive form: $\forall x \in D, \neg Q(x) \to \neg P(x)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4, cs1231s-cheatsheet-not-using-16pages-pdf#section-1].
2.  Prove this contrapositive statement using a direct proof:
    *   Suppose $x$ is a particular but arbitrarily chosen element of $D$ such that $Q(x)$ is false (i.e., $\neg Q(x)$ is true).
    *   Show that $P(x)$ is false (i.e., $\neg P(x)$ is true) [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4].
3.  Conclude that the original statement $\forall x \in D, P(x) \to Q(x)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4].

**Example:** Prove that for all integers $n$, if $n^2$ is even then $n$ is even.
*   **Proof (by contraposition):**
    1.  The contrapositive statement is: For all integers $n$, if $n$ is odd then $n^2$ is odd.
    2.  Let $n$ be an arbitrarily chosen odd integer.
    3.  By the definition of an odd number, $n = 2k + 1$ for some integer $k$.
    4.  Then $n^2 = (2k + 1)^2 = (2k + 1)(2k + 1)$.
    5.  Expanding, $n^2 = 4k^2 + 4k + 1$.
    6.  Rearranging, $n^2 = 2(2k^2 + 2k) + 1$.
    7.  Let $m = 2k^2 + 2k$. Since integers are closed under multiplication and addition, $m$ is an integer.
    8.  Thus, $n^2 = 2m + 1$ for some integer $m$.
    9.  By the definition of an odd number, $n^2$ is odd.
    10. Therefore, the contrapositive statement (if $n$ is odd then $n^2$ is odd) is true.
    11. By logical equivalence, the original statement (if $n^2$ is even then $n$ is even) is also true [source:cs1231s-cs1231s-extra-lecture-slides-lecture04-methods-of-proof-full-pdf#section-4].

---
page_id: "y1s1-cs1231s-lecture-08-fta"
title: "Lecture 08: Fundamental Theorem of Arithmetic"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Explores the unique prime factorization of integers and related concepts like prime numbers and composite numbers."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-1"
  - "cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-1"
  - "cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5"
  - "cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-1-pdf#section-5"
  - "cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-2"
topics:
  - "prime"
  - "integer"
  - "theorem"
  - "divisibility"
  - "has"
  - "divisor"
  - "lemma"
  - "composite"
  - "positive"
  - "numbers"
source_count: 5
lecture_number: 8
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 08: Fundamental Theorem of Arithmetic

This page explores the foundational concepts of divisibility, prime numbers, and composite numbers, culminating in the **Fundamental Theorem of Arithmetic**. This theorem asserts that every positive integer greater than or equal to 2 can be uniquely expressed as a product of prime numbers [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-1]. These concepts are fundamental in elementary number theory and have practical applications, particularly in high-speed numerical calculations [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-1].

## Divisibility

Divisibility is a core concept in number theory.

### Definition of Divisibility
For integers $n, d \in \mathbb{Z}$, $d$ is said to **divide** $n$ (written as $d | n$) if there exists an integer $k$ such that $n = dk$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1].

Other terminologies for "$d | n$" include:
*   $n$ is **divisible by** $d$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-3].
*   $n$ is a **multiple of** $d$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-3].
*   $d$ is a **factor** or **divisor** of $n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-3].

It is important to note that $d | n$ is a statement (either true or false), not a number like $d/n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1]. For $d \neq 0$, $d | n$ if and only if $n/d$ is an integer [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1].

**Example**:
*   $3 | 6$ because $6 = 3 \times 2$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-3].
*   $3 \nmid 7$ because $7 \neq 3k$ for any integer $k$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-3].

### Properties of Divisibility

1.  **Divisibility by 1 and Self-Divisibility**: For any integer $n \in \mathbb{Z}$, $1 | n$ and $n | n$ because $1 \times n = n$ and $n \times 1 = n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1].
2.  **Divisibility of Zero**: For any integer $d \in \mathbb{Z}$, $d | 0$ because $0 = d \times 0$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1].
    *   **Exercise**: Which $n \in \mathbb{Z}$ makes $0 | n$? (Only $n=0$ since $0 = 0 \times k$ for any $k$).
3.  **Negatives**: If $d | n$, then $-d | n$, $d | -n$, and $-d | -n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1].
    *   *Proof*: If $d | n$, then $n=dk$ for some integer $k$.
        *   $n = (-d)(-k)$, so $-d | n$.
        *   $-n = d(-k)$, so $d | -n$.
        *   $-n = (-d)k$, so $-d | -n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4].
4.  **Size of Divisors**: If $d | n$ and $n \neq 0$, then $|d| \leq |n|$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1].
    *   *Proof outline*: If $d | n$, then $n = dk$ for some $k \in \mathbb{Z}$. Since $n \neq 0$, $k \neq 0$. Thus $|k| \geq 1$. Taking absolute values, $|n| = |dk| = |d||k|$. Since $|k| \geq 1$, it follows that $|d||k| \geq |d| \times 1 = |d|$. Therefore, $|n| \geq |d|$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4].
    *   **Example**: The positive divisors of 6 are 1, 2, 3, 6 [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4].
5.  **Transitivity of Divisibility**: For integers $a, b, c \in \mathbb{Z}$, if $a | b$ and $b | c$, then $a | c$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1].
    *   *Proof*: If $a | b$, then $b = ak$ for some $k \in \mathbb{Z}$. If $b | c$, then $c = bl$ for some $l \in \mathbb{Z}$. Substituting $b$, we get $c = (ak)l = a(kl)$. Since $kl \in \mathbb{Z}$, it means $a | c$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4].
    *   **Example**: Since $3 | 6$ and $6 | 18$, transitivity tells us $3 | 18$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-4].
6.  **Closure Lemma (Integer Linear Combinations)**: For integers $a, b, d, m, n \in \mathbb{Z}$, if $d | m$ and $d | n$, then $d | (am + bn)$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1]. The expression $am+bn$ is called an integer linear combination of $m$ and $n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-5].
    *   *Proof*: If $d | m$, then $m = dk$ for some $k \in \mathbb{Z}$. If $d | n$, then $n = dl$ for some $l \in \mathbb{Z}$. Then $am + bn = a(dk) + b(dl) = d(ak + bl)$. Since $ak+bl \in \mathbb{Z}$, it implies $d | (am + bn)$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-5].
    *   **Example**: Since $3 | -6$ and $3 | 9$, and $-564 = 100 \times (-6) + 4 \times 9$, the Closure Lemma implies $3 | -564$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-5].

## The Division Theorem

The Division Theorem formalizes the concept of division with a remainder [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-1].

### Theorem 8.1.16 (Division Theorem)
For all $n \in \mathbb{Z}$ and $d \in \mathbb{Z}^+$, there exist **unique** integers $q, r \in \mathbb{Z}$ such that $n = dq + r$ and $0 \leq r < d$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-2].
*   $q$ is called the **quotient** ($n \text{ div } d$) and $r$ is called the **remainder** ($n \text{ mod } d$) when $n$ is divided by $d$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-6].

**Warning**: In this context, $n \text{ mod } d$ is **always non-negative**. Some programming languages may define modulo operations differently, where the result can have the same sign as $n$ or $d$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-2].

**Example**:
*   $11 \text{ div } 5 = 2$ and $11 \text{ mod } 5 = 1$ because $11 = 5 \times 2 + 1$ and $0 \leq 1 < 5$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-6].
*   $-16 \text{ div } 3 = -6$ and $-16 \text{ mod } 3 = 2$ because $-16 = 3 \times (-6) + 2$ and $0 \leq 2 < 3$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-6].

The proof of the Division Theorem involves demonstrating both the existence and uniqueness of $q$ and $r$:
*   **Existence**: Can be shown by setting $q = \lfloor n/d \rfloor$ (the floor function) and $r = n - dq$. It uses the property of floor function where $\lfloor x \rfloor$ is the unique integer $y$ such that $y \leq x < y+1$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-6].
*   **Uniqueness**: Assumes two such pairs $(q, r)$ and $(q', r')$ exist and shows that $q=q'$ and $r=r'$ by contradiction or by algebraic manipulation based on the remainder property $0 \leq r < d$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-7].

### Even and Odd Numbers
The Division Theorem is used to define and prove properties of even and odd numbers [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-7].

**Definition**:
1.  An integer is **even** if it is equal to $2k$ for some integer $k \in \mathbb{Z}$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-7].
2.  An integer is **odd** if it is equal to $2k+1$ for some integer $k \in \mathbb{Z}$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-7].

**Corollary**: Let $n \in \mathbb{Z}$. Then $n$ is either even or odd, but not both [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-7].
*   *Proof outline*: Apply the Division Theorem with $d=2$. This yields $n = 2q + r$ where $0 \leq r < 2$. Thus $r$ can only be $0$ or $1$. If $r=0$, $n=2q$ (even). If $r=1$, $n=2q+1$ (odd). The uniqueness part of the Division Theorem ensures $n$ cannot be both even and odd [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-0-pdf#section-7].

## Prime and Composite Numbers

These definitions classify positive integers based on their divisors [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-2].

### Definition 8.2.1
1.  A positive integer is **prime** if it has exactly two distinct positive divisors [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-3]. These divisors are 1 and itself [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-2].
2.  A positive integer is **composite** if it has strictly more than two positive divisors [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-3].

**Remark**:
*   The integer 1 is neither prime nor composite because it has only one positive divisor (itself) [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-3].
*   Every integer $n \geq 2$ is either prime or composite [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-3].

**Example**:
*   7 is prime because its positive divisors are 1 and 7 [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-2].
*   9 is composite because its positive divisors are 1, 3, and 9 [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-2].

### Divisors of Composite Numbers

**Lemma 8.2.4**: An integer $n$ is composite if and only if $n$ has a divisor $d$ such that $1 < d < n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-3].
*   *Proof (If)*: If such a $d$ exists, then $1, d, n$ are three distinct positive divisors of $n$, making $n$ composite.
*   *Proof (Only if)*: If $n$ is composite, it has a positive divisor $d$ such that $d \neq 1$ and $d \neq n$. By the proposition that $|d| \leq |n|$ if $d|n$ and $n \neq 0$, we have $1 < d \leq n$. Since $d \neq n$, it implies $1 < d < n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-3].

### Existence of Prime Divisors

**Lemma 8.2.5 (Prime Divisor Lemma)**: Let $n \in \mathbb{Z}_{\geq 2}$. Then $n$ has at least one prime divisor [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-3].
*   *Proof outline*:
    1.  Consider the set of all positive divisors of $n$ strictly greater than 1. This set is non-empty (since $n$ is in it) and consists of positive integers.
    2.  By the [Well-Ordering Principle](y1s1-cs1231s-lecture-07-strong-induction-recursion#well-ordering-principle) (Theorem 7.2.9), there exists a smallest divisor $d$ in this set [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-4].
    3.  Assume for contradiction that $d$ is not prime. Since $d \geq 2$, $d$ must be composite.
    4.  By Lemma 8.2.4, since $d$ is composite, it must have a divisor $c$ such that $1 < c < d$.
    5.  Since $c | d$ and $d | n$, by transitivity of divisibility, $c | n$.
    6.  This means $c$ is a divisor of $n$ strictly greater than 1, and $c < d$. This contradicts our assumption that $d$ was the *smallest* such divisor.
    7.  Therefore, $d$ must be prime [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-4].

### Sizes of Prime Divisors

**Proposition 8.2.6**: Let $n$ be a composite positive integer. Then $n$ has a prime divisor $p \leq \sqrt{n}$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-4].
*   *Proof outline*:
    1.  Since $n$ is composite, by Lemma 8.2.4, there exists a divisor $d$ such that $1 < d < n$.
    2.  By the definition of divisibility, $n = dk$ for some integer $k$.
    3.  Consider two cases:
        *   **Case 1: $d \leq \sqrt{n}$**. By the Prime Divisor Lemma (8.2.5), $d$ has a prime divisor $p$. Since $p | d$ and $d | n$, transitivity implies $p | n$. Also, by Proposition 8.1.10, $p \leq |d| = d \leq \sqrt{n}$.
        *   **Case 2: $d > \sqrt{n}$**. Since $n = dk$, we have $k = n/d$. As $d > \sqrt{n}$, then $k = n/d < n/\sqrt{n} = \sqrt{n}$. Also, $k = n/d > n/n = 1$ (since $d<n$). So $k$ is an integer such that $1 < k < \sqrt{n}$. By the Prime Divisor Lemma, $k$ has a prime divisor $p$. Since $p | k$ and $k | n$, transitivity implies $p | n$. Also, $p \leq |k| = k < \sqrt{n}$.
    4.  In both cases, $n$ has a prime divisor $p \leq \sqrt{n}$ [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-4].
*   **Example**: To check if 101 is prime, we only need to test for prime divisors up to $\sqrt{101} \approx 10.05$. The primes less than 10 are 2, 3, 5, 7. Since none of these divide 101, 101 is prime [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-4].

### The Infinitude of Primes

**Theorem 8.2.8 (Euclid)**: There are infinitely many prime numbers [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-4].
*   *Proof by contradiction*:
    1.  Assume there is a finite list of all prime numbers: $p_1, p_2, \ldots, p_k$.
    2.  Construct a new number $n = (p_1 p_2 \ldots p_k) + 1$. Note that $n \geq 2$.
    3.  By the Prime Divisor Lemma (8.2.5), $n$ must have a prime divisor, let's call it $p$.
    4.  Since $p_1, \ldots, p_k$ is a complete list of primes, $p$ must be one of them. So $p = p_i$ for some $i \in \{1, \ldots, k\}$.
    5.  This means $p_i | (p_1 p_2 \ldots p_k)$.
    6.  Since $p_i | n$ and $p_i | (p_1 p_2 \ldots p_k)$, by the Closure Lemma (8.1.14), $p_i | (n - (p_1 p_2 \ldots p_k))$.
    7.  Substituting $n$, we get $p_i | ((p_1 p_2 \ldots p_k + 1) - (p_1 p_2 \ldots p_k))$, which simplifies to $p_i | 1$.
    8.  However, the only divisors of 1 are 1 and -1. Since $p_i$ is a prime number, $p_i \geq 2$. This contradicts $p_i | 1$.
    9.  Therefore, our initial assumption must be false, and there must be infinitely many prime numbers [source: cs1231s-cs1231s-extra-lecture-slides-8-1-divprime-1-pdf#section-5].

## Greatest Common Divisors

### Definition 8.4.1
1.  A **common divisor** of integers $m$ and $n$ is an integer $d$ that divides both $m$ and $n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-4].
2.  The **greatest common divisor (GCD)** of $m$ and $n$, denoted $\text{gcd}(m, n)$, is the largest positive integer that is a common divisor of $m$ and $n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-4].

**Example**:
*   Positive divisors of 72: {1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72} [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2].
*   Positive divisors of 63: {1, 3, 7, 9, 21, 63} [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2].
*   Common positive divisors of 72 and 63: {1, 3, 9} [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2].
*   Therefore, $\text{gcd}(72, 63) = 9$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2].

**Properties of GCD**:
*   For $m \neq 0$ or $n \neq 0$, $\text{gcd}(m, n)$ exists and is positive [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-4]. This is based on Proposition 8.1.10.
*   $\text{gcd}(0, 0)$ is undefined (as every integer divides 0, there is no *greatest* common divisor) [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2].
*   $\text{gcd}(m, n) = \text{gcd}(|m|, |n|)$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2]. The common divisors of $m$ and $n$ are exactly the common divisors of $|m|$ and $|n|$.
*   If $p$ is a prime number, then for any integer $m \in \mathbb{Z}^+$, either $\text{gcd}(m, p) = 1$ or $p | m$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-5].

## The Euclidean Algorithm

The Euclidean Algorithm is an efficient method to compute the GCD of two positive integers [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-3].

### Algorithm 8.4.8 (Euclidean Algorithm)
To find $\text{gcd}(m, n)$ for $m, n \in \mathbb{Z}^+$ with $m > n > 0$: [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-3]
1.  **input** $m, n \in \mathbb{Z}^+$ with $m > n > 0$
2.  $x := m$
3.  $y := n$
4.  **while** $y \neq 0$ **do**
5.      $r := x \text{ mod } y$
6.      $x := y$
7.      $y := r$
8.  **end do**
9.  **output** $x$

**Example**: Find $\text{gcd}(1076, 414)$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-3].
*   $1076 \text{ mod } 414 = 248$
*   $414 \text{ mod } 248 = 166$
*   $248 \text{ mod } 166 = 82$
*   $166 \text{ mod } 82 = 2$
*   $82 \text{ mod } 2 = 0$
The last non-zero remainder is 2. So, $\text{gcd}(1076, 414) = 2$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-3].

### Correctness of the Euclidean Algorithm
The algorithm stops because the sequence of remainders $n > r_1 > r_2 > \ldots \geq 0$ is strictly decreasing and bounded below by 0. By the Well-Ordering Principle, this sequence must have a smallest element, which implies it eventually reaches 0 [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-4].

The correctness relies on **Lemma 8.4.11**: If $x, y, r \in \mathbb{Z}$ such that $x \text{ mod } y = r$, then $\text{gcd}(x, y) = \text{gcd}(y, r)$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-4].
*   *Proof outline*:
    1.  Let $q = x \text{ div } y$. Then $x = yq + r$ by the definition of division and remainder.
    2.  If $d$ is a common divisor of $x$ and $y$, then $d | x$ and $d | y$. By the Closure Lemma, $d | (x - yq)$, so $d | r$. Thus, $d$ is a common divisor of $y$ and $r$.
    3.  Conversely, if $d$ is a common divisor of $y$ and $r$, then $d | y$ and $d | r$. By the Closure Lemma, $d | (yq + r)$, so $d | x$. Thus, $d$ is a common divisor of $x$ and $y$.
    4.  Since the common divisors of $(x, y)$ are exactly the same as the common divisors of $(y, r)$, their greatest common divisors must be equal: $\text{gcd}(x, y) = \text{gcd}(y, r)$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-4].

Applying this lemma repeatedly to the steps of the Euclidean algorithm, we get:
$\text{gcd}(m, n) = \text{gcd}(n, r_1) = \text{gcd}(r_1, r_2) = \ldots = \text{gcd}(r_{k-1}, r_k) = r_k$, where $r_k$ is the last non-zero remainder before $r_{k+1}=0$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-4].

### The Extended Euclidean Algorithm (Bézout's Lemma)

**Theorem 8.5.2 (Bézout's Lemma)**: For all integers $m, n \in \mathbb{Z}$ with $n \neq 0$, there exist integers $s, t \in \mathbb{Z}$ such that $\text{gcd}(m, n) = ms + nt$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-5]. The expression $ms+nt$ is known as an integer linear combination of $m$ and $n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].

The values of $s$ and $t$ can be found by working backwards through the steps of the Euclidean Algorithm.

**Example**: Find $s, t$ for $\text{gcd}(1076, 414) = 2$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
From the Euclidean Algorithm:
1.  $1076 = 2 \times 414 + 248 \implies 248 = 1076 - 2 \times 414$
2.  $414 = 1 \times 248 + 166 \implies 166 = 414 - 1 \times 248$
3.  $248 = 1 \times 166 + 82 \implies 82 = 248 - 1 \times 166$
4.  $166 = 2 \times 82 + 2 \implies 2 = 166 - 2 \times 82$

Now, substitute backwards:
*   $2 = 166 - 2 \times 82$ (from (4))
*   Substitute $82$ from (3): $2 = 166 - 2 \times (248 - 1 \times 166) = 166 - 2 \times 248 + 2 \times 166 = 3 \times 166 - 2 \times 248$
*   Substitute $166$ from (2): $2 = 3 \times (414 - 1 \times 248) - 2 \times 248 = 3 \times 414 - 3 \times 248 - 2 \times 248 = 3 \times 414 - 5 \times 248$
*   Substitute $248$ from (1): $2 = 3 \times 414 - 5 \times (1076 - 2 \times 414) = 3 \times 414 - 5 \times 1076 + 10 \times 414 = (-5) \times 1076 + 13 \times 414$

So, $s = -5$ and $t = 13$, and $\text{gcd}(1076, 414) = 1076(-5) + 414(13) = 2$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].

**Remark on negative numbers**: Bézout's Lemma also applies to negative integers, as $\text{gcd}(m, n) = \text{gcd}(|m|, |n|)$. The coefficients $s, t$ might change if $m$ or $n$ are negative [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].

### Euclid's Lemma

**Theorem 8.5.5 (Euclid's Lemma)**: Let $m, n, p \in \mathbb{Z}^+$. If $p$ is prime and $p | mn$, then $p | m$ or $p | n$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-5].
*   *Proof outline*:
    1.  Assume $p$ is prime and $p | mn$.
    2.  Assume for contradiction that $p \nmid m$.
    3.  Since $p$ is prime, and $p \nmid m$, it must be that $\text{gcd}(m, p) = 1$ (from the property that if $p$ is prime, then $\text{gcd}(m, p) = 1$ or $p | m$).
    4.  By Bézout's Lemma (8.5.2), there exist integers $s, t$ such that $1 = ms + pt$.
    5.  Multiply by $n$: $n = msn + ptn = (mn)s + p(tn)$.
    6.  Since $p | mn$ (by assumption) and $p | p(tn)$, by the Closure Lemma (8.1.14), $p | ((mn)s + p(tn))$, which means $p | n$.
    7.  Therefore, if $p | mn$ and $p \nmid m$, it must be that $p | n$. This completes the proof (by showing $p|m$ or $p|n$) [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].

**Corollary 8.5.6**: Let $n, m_0, m_1, \ldots, m_n, p \in \mathbb{Z}^+$. If $p$ is prime and $p | m_0 m_1 \ldots m_n$, then $p | m_i$ for some $i \in \{0, 1, \ldots, n\}$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-5]. This is an extension of Euclid's Lemma to products of multiple integers.

## Fundamental Theorem of Arithmetic

The Fundamental Theorem of Arithmetic, also known as the Prime Factorization Theorem, states that every integer greater than or equal to 2 can be uniquely factored into primes.

### Definition 8.5.7
A **prime factorization** of an integer $n$ is a way of writing $n$ as a product of prime numbers [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-5].

**Example**:
*   A prime factorization of 100 is $2 \times 2 \times 5 \times 5 = 2^2 5^2$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
*   A prime factorization of 641 is 641 (since 641 is prime) [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].

### Theorem 8.5.9 (Fundamental Theorem of Arithmetic)
Every positive integer $n \geq 2$ has a **unique** factorization into a product of prime numbers, where the prime factors are arranged in nondecreasing order [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes8-numthy-pdf#section-5].

**Remark on Uniqueness**:
1.  The "nondecreasing order" requirement is crucial. For example, $2 \times 5$ and $5 \times 2$ are different factorizations of 10 if order matters, but are considered the same unique factorization under the nondecreasing order convention [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
2.  The theorem explicitly states that prime factors must be prime numbers. If 1 were allowed to be "prime," then $2 \times 5$ and $1 \times 2 \times 5$ would be different "prime factorizations" of 10, violating uniqueness [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5]. This reinforces why 1 is not classified as a prime number.

### Proof of Existence (by Strong Mathematical Induction)
For each $n \in \mathbb{Z}_{\geq 2}$, let $P(n)$ be the proposition "$n$ has a prime factorization" [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
1.  **Base Step**: For $n=2$, 2 is a prime number, so $2$ itself is its prime factorization. Thus, $P(2)$ is true [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
2.  **Inductive Step**: Assume $P(i)$ is true for all integers $i$ such that $2 \leq i \leq k$, for some $k \in \mathbb{Z}_{\geq 2}$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
    *   Consider $k+1$.
    *   **Case 1**: If $k+1$ is prime, then $k+1$ is its own prime factorization, so $P(k+1)$ is true [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
    *   **Case 2**: If $k+1$ is not prime, then $k+1$ is composite. By Lemma 8.2.4, $k+1$ has a divisor $d$ such that $1 < d < k+1$. Since $d$ divides $k+1$, we can write $k+1 = de$ for some integer $e$ [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
    *   From $1 < d < k+1$ and $k+1 = de$:
        *   Dividing $k+1=de$ by $d$ yields $e = (k+1)/d$. Since $d>1$, we have $e < k+1$.
        *   Since $1 < d$, multiplying by $e$ gives $e < de = k+1$. Also, $d = (k+1)/e$. Since $e<k+1$, we have $d > 1$.
        *   Thus, we have $1 < d < k+1$ and $1 < e < k+1$.
    *   Since $d$ and $e$ are both integers strictly between 1 and $k+1$, by the induction hypothesis, both $d$ and $e$ have prime factorizations.
    *   If $d = p_1 p_2 \ldots p_r$ and $e = q_1 q_2 \ldots q_s$ (where $p_i, q_j$ are primes), then $k+1 = de = (p_1 \ldots p_r)(q_1 \ldots q_s)$, which is a prime factorization of $k+1$.
    *   Therefore, $P(k+1)$ is true.
3.  By the principle of Strong Mathematical Induction, every integer $n \geq 2$ has a prime factorization [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].

### Proof of Uniqueness (by Contradiction)
1.  Assume there is an integer $n \geq 2$ that has two different prime factorizations. Let them be $p_0 p_1 \ldots p_k = n = q_0 q_1 \ldots q_l$, where $p_i$ and $q_j$ are primes arranged in nondecreasing order [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
2.  Cancel all common prime factors from both sides. If the factorizations were identical, nothing would be left. Since we assumed they are different, some primes must remain on both sides. Let the result of cancellation be $p'_0 p'_1 \ldots p'_{k'} = q'_0 q'_1 \ldots q'_{l'}$, where no prime appears on both sides [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].
3.  From $p'_0 p'_1 \ldots p'_{k'} = q'_0 q'_1 \ldots q'_{l'}$, we know that $p'_0$ divides the left side, so $p'_0$ divides the right side, $q'_0 q'_1 \ldots q'_{l'}$.
4.  By Corollary 8.5.6 (Euclid's Lemma for multiple factors), since $p'_0$ is a prime and divides the product $q'_0 q'_1 \ldots q'_{l'}$, $p'_0$ must divide at least one of the $q'_j$ factors. Let's say $p'_0 | q'_i$ for some $i \in \{0, 1, \ldots, l'\}$.
5.  Since $q'_i$ is a prime number, its only positive divisors are 1 and $q'_i$. As $p'_0$ is a prime, $p'_0 \neq 1$. Therefore, $p'_0$ must be equal to $q'_i$.
6.  This contradicts our step 2, which stated that after cancellation, no prime appears on both sides of the equation. Since $p'_0 = q'_i$, this means they should have been cancelled.
7.  This contradiction proves that our initial assumption of two different prime factorizations must be false. Therefore, the prime factorization of any integer $n \geq 2$ is unique [source: cs1231s-cs1231s-extra-lecture-slides-8-3-gcdfta-0-pdf#section-5].

---
page_id: "y1s1-ma2001-orthogonal-sets-projections"
title: "Orthogonal Sets and Projections"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Concepts of orthogonal vectors and sets, orthonormal bases, and computing orthogonal projections onto subspaces."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-tutorial-tutorial8-pdf#section-1"
  - "ma2001-cheatsheet-cheatsheet-pdf#section-4"
topics:
  - "question"
  - "let"
  - "show"
  - "basis"
  - "orthonormal"
  - "find"
  - "prove"
  - "vectors"
  - "det"
  - "rank"
source_count: 2
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Orthogonal Sets and Projections

Orthogonal Sets and Projections
This page covers concepts related to orthogonal vectors and sets, orthonormal bases, and computing orthogonal projections onto subspaces.

### Orthogonal Vectors and Sets

A set of vectors $\{u_1, u_2, \ldots, u_n\}$ in a vector space is called an **orthogonal set** if any two distinct vectors in the set are orthogonal. This means their inner product is zero: $u_i \cdot u_j = 0$ for all $i \neq j$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

The inner product of two vectors $u = (u_1, \ldots, u_n)$ and $v = (v_1, \ldots, v_n)$ in $\mathbb{R}^n$ is defined as $u \cdot v = u^T v = u_1 v_1 + \ldots + u_n v_n$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

The **norm** (or length) of a vector $u$ is given by $||u|| = \sqrt{u \cdot u}$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

A fundamental property for orthogonal vectors is the **Pythagorean theorem**:
If $\{u_1, u_2, \ldots, u_n\}$ is an orthogonal set of vectors, then the squared norm of their sum is equal to the sum of their squared norms:
$||u_1 + u_2 + \cdots + u_n||^2 = ||u_1||^2 + ||u_2||^2 + \cdots + ||u_n||^2$ [source: ma2001-tutorial-tutorial8-pdf#section-1].

For $n=2$, this can be interpreted geometrically in $\mathbb{R}^2$. If two vectors $u_1$ and $u_2$ are orthogonal, they form the sides of a right-angled triangle, and their sum $u_1 + u_2$ forms the hypotenuse. The Pythagorean theorem then states that the square of the hypotenuse's length is the sum of the squares of the other two sides' lengths [source: ma2001-tutorial-tutorial8-pdf#section-1].

### Orthonormal Sets and Bases

An **orthonormal set** is an orthogonal set where every vector has a norm of 1. That is, $||u_i|| = 1$ for all $i$, in addition to $u_i \cdot u_j = 0$ for $i \neq j$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

An **orthonormal basis** for a vector space $V$ is a basis that is also an orthonormal set [source: ma2001-tutorial-tutorial8-pdf#section-3].

To check if a set $S = \{u_1, \ldots, u_k\}$ is an orthogonal basis for a vector space $V$:
1.  Verify that $S$ is an orthogonal set.
2.  Verify that $|S| = \text{dim}(V)$ or that $S$ spans $V$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

If $S = \{u_1, \ldots, u_k\}$ is an orthonormal basis for a subspace $V$ of $\mathbb{R}^n$:
*   For any vector $v \in V$, its coordinate vector with respect to $S$, denoted $(v)_S$, has the same norm as $v$: $||(v)_S|| = ||v||$ [source: ma2001-tutorial-tutorial8-pdf#section-3].
*   For any vectors $v, w \in V$, the distance between their coordinate vectors $d((v)_S, (w)_S)$ is equal to the distance between the vectors themselves $d(v, w)$ [source: ma2001-tutorial-tutorial8-pdf#section-3].
*   For any nonzero vectors $v, w \in V$, the angle between $(v)_S$ and $(w)_S$ (in $\mathbb{R}^k$) is equal to the angle between $v$ and $w$ (in $\mathbb{R}^n$) [source: ma2001-tutorial-tutorial8-pdf#section-3]. The angle between two vectors $u,v$ is given by $\cos \angle(u,v) = \frac{u \cdot v}{||u|| ||v||}$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

### Orthogonal Matrices

An **orthogonal matrix** $A$ is a square matrix such that its transpose is equal to its inverse: $A^T = A^{-1}$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].
This implies $A^T A = I$. The rows and columns of an orthogonal matrix form an orthonormal basis for $\mathbb{R}^n$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

### Orthogonal Projections

Given a vector $w \in \mathbb{R}^n$ and a subspace $V$ with an orthogonal basis $S = \{s_1, s_2, \ldots, s_k\}$, the **orthogonal projection** of $w$ onto $V$ (denoted as $p$) can be computed as:
$p = \frac{w \cdot s_1}{s_1 \cdot s_1} s_1 + \frac{w \cdot s_2}{s_2 \cdot s_2} s_2 + \cdots + \frac{w \cdot s_k}{s_k \cdot s_k} s_k$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

If $S$ is an *orthonormal* basis, the formula simplifies because $s_i \cdot s_i = ||s_i||^2 = 1$:
$p = (w \cdot s_1) s_1 + (w \cdot s_2) s_2 + \cdots + (w \cdot s_k) s_k$.

### Orthogonal Complements

For a subspace $W$ of $\mathbb{R}^n$, its **orthogonal complement**, denoted $W^\perp$, is the set of all vectors $u \in \mathbb{R}^n$ that are orthogonal to every vector in $W$ [source: ma2001-tutorial-tutorial8-pdf#section-6]:
$W^\perp = \{u \in \mathbb{R}^n \mid u \text{ is orthogonal to } W\}$.

Properties of orthogonal complements:
*   $W^\perp$ is itself a subspace of $\mathbb{R}^n$ [source: ma2001-tutorial-tutorial8-pdf#section-6].
*   The sum of the dimension of a subspace and its orthogonal complement equals the dimension of the ambient space: $\text{dim}(W) + \text{dim}(W^\perp) = n$ [source: ma2001-tutorial-tutorial8-pdf#section-6].
*   The only vector common to a subspace and its orthogonal complement is the zero vector: $U \cap U^\perp = \{0\}$ for any subspace $U$ [source: ma2001-tutorial-tutorial8-pdf#section-7].
*   The orthogonal complement of the orthogonal complement of a subspace is the subspace itself: $(U^\perp)^\perp = U$ [source: ma2001-tutorial-tutorial8-pdf#section-7].
*   If $U$ is a subspace of $V$, then $V^\perp$ is a subspace of $U^\perp$ [source: ma2001-tutorial-tutorial8-pdf#section-7].
*   The orthogonal complement of the sum of two subspaces is the intersection of their orthogonal complements: $(U + V)^\perp = U^\perp \cap V^\perp$ [source: ma2001-tutorial-tutorial8-pdf#section-7].
    *   Note: It is not generally true that $(U \cap V)^\perp = U^\perp + V^\perp$ [source: ma2001-tutorial-tutorial8-pdf#section-7].

These concepts are crucial for understanding various advanced topics in linear algebra, including the [gram-schmidt-process:Gram-Schmidt Process] and [least-squares-solutions:Least Squares Solutions].

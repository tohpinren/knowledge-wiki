---
page_id: "y1s1-ma2001-gram-schmidt-process"
title: "Gram-Schmidt Process"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Algorithm for converting a linearly independent set of vectors into an orthonormal set, forming an orthonormal basis."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1"
  - "ma2001-hw4-hw4-q-pdf#section-1"
  - "ma2001-tutorial-tutorial8sol-pdf#section-2"
topics:
  - "least"
  - "squares"
  - "fit"
  - "eigenspace"
  - "transformation"
  - "orthogonal"
  - "given"
  - "eigenvalues"
  - "matrix"
  - "find"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Gram-Schmidt Process

The Gram-Schmidt Process is an algorithm used in linear algebra to transform a set of linearly independent vectors into an orthonormal set, which forms an orthonormal basis for the subspace spanned by the original vectors. An orthonormal basis simplifies many calculations, especially those involving projections and coordinate representations.

### What is an Orthonormal Basis?

Before diving into the Gram-Schmidt process, it's essential to understand what an orthonormal basis entails:
*   **Orthogonal Set**: A set of vectors $\{u_1, u_2, \ldots, u_k\}$ is orthogonal if every pair of distinct vectors in the set is orthogonal, meaning their dot product is zero ($u_i \cdot u_j = 0$ for $i \neq j$).
*   **Normalized Vectors**: A vector $u$ is normalized if its length (or norm) is 1 (i.e., $||u|| = 1$). To normalize a non-zero vector $u$, divide it by its norm: $\frac{u}{||u||}$.
*   **Orthonormal Set**: A set of vectors is orthonormal if it is an orthogonal set, and all vectors in the set are normalized.
*   **Orthonormal Basis**: An orthonormal set that also forms a basis for a vector space $V$.

For orthogonal vectors $u_i$, Pythagoras' Theorem states that the square of the norm of their sum is the sum of the squares of their individual norms: $||u_1 + \ldots + u_n||^2 = ||u_1||^2 + \ldots + ||u_n||^2$ [source:ma2001-tutorial-tutorial8sol-pdf#section-1].

### The Gram-Schmidt Algorithm

Given a linearly independent set of vectors $\{v_1, v_2, \ldots, v_k\}$ that forms a basis for a subspace $V$, the Gram-Schmidt process constructs an orthonormal basis $\{q_1, q_2, \ldots, q_k\}$ for $V$ as follows:

1.  **Initialize $q_1$**: Take the first vector $v_1$. The first orthogonal vector $u_1$ is simply $v_1$. Normalize it to get $q_1$:
    $u_1 = v_1$
    $q_1 = \frac{u_1}{||u_1||}$

2.  **Construct $q_2$**: Take the second vector $v_2$. To make it orthogonal to $u_1$ (or $q_1$), subtract its projection onto $q_1$. The resulting vector $u_2$ will be orthogonal to $u_1$. Then normalize $u_2$.
    $u_2 = v_2 - \text{proj}_{q_1} v_2 = v_2 - (v_2 \cdot q_1)q_1$
    $q_2 = \frac{u_2}{||u_2||}$

3.  **Construct $q_3$**: Take the third vector $v_3$. To make it orthogonal to both $q_1$ and $q_2$, subtract its projection onto $q_1$ and its projection onto $q_2$. The resulting vector $u_3$ will be orthogonal to $u_1$ and $u_2$. Then normalize $u_3$.
    $u_3 = v_3 - \text{proj}_{q_1} v_3 - \text{proj}_{q_2} v_3 = v_3 - (v_3 \cdot q_1)q_1 - (v_3 \cdot q_2)q_2$
    $q_3 = \frac{u_3}{||u_3||}$

4.  **General Step for $q_j$**: For any subsequent vector $v_j$ (where $j > 1$), subtract its projections onto all previously constructed orthonormal vectors $q_1, \ldots, q_{j-1}$. The resulting vector $u_j$ will be orthogonal to all previous $u_i$'s. Then normalize $u_j$.
    $u_j = v_j - \sum_{i=1}^{j-1} (v_j \cdot q_i)q_i$
    $q_j = \frac{u_j}{||u_j||}$

This process generates an orthogonal set $\{u_1, u_2, \ldots, u_k\}$, which is then normalized to form the orthonormal set $\{q_1, q_2, \ldots, q_k\}$. This set forms an orthonormal basis for $V$.

### Example: Applying Gram-Schmidt

Let's apply the Gram-Schmidt process to a specific set of vectors to find an orthonormal basis.
Given the vectors $v_1 = (4, 0, 2, 4)$, $v_2 = (3, 0, 3, 0)$, and $v_3 = (1, 4, 3, 5)$. These vectors are linearly independent and form a basis for a subspace $V$ [source:ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1]. We aim to transform this set into an orthonormal basis for $V$ [source:ma2001-hw4-hw4-q-pdf#section-1].

**Step 1: Find $q_1$**
Let $u_1 = v_1 = (4, 0, 2, 4)$.
Calculate its norm: $||u_1|| = \sqrt{4^2 + 0^2 + 2^2 + 4^2} = \sqrt{16 + 0 + 4 + 16} = \sqrt{36} = 6$.
Normalize $u_1$ to get $q_1$:
$q_1 = \frac{u_1}{||u_1||} = \frac{1}{6}(4, 0, 2, 4) = (\frac{4}{6}, 0, \frac{2}{6}, \frac{4}{6}) = (\frac{2}{3}, 0, \frac{1}{3}, \frac{2}{3})$ [source:ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1]

**Step 2: Find $q_2$**
Let $u_2 = v_2 - (v_2 \cdot q_1)q_1$.
First, calculate the dot product $v_2 \cdot q_1$:
$v_2 \cdot q_1 = (3, 0, 3, 0) \cdot (\frac{2}{3}, 0, \frac{1}{3}, \frac{2}{3}) = (3 \cdot \frac{2}{3}) + (0 \cdot 0) + (3 \cdot \frac{1}{3}) + (0 \cdot \frac{2}{3}) = 2 + 0 + 1 + 0 = 3$.
Now, calculate $u_2$:
$u_2 = (3, 0, 3, 0) - 3 \cdot (\frac{2}{3}, 0, \frac{1}{3}, \frac{2}{3}) = (3, 0, 3, 0) - (2, 0, 1, 2) = (1, 0, 2, -2)$ [source:ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1]
Calculate its norm: $||u_2|| = \sqrt{1^2 + 0^2 + 2^2 + (-2)^2} = \sqrt{1 + 0 + 4 + 4} = \sqrt{9} = 3$.
Normalize $u_2$ to get $q_2$:
$q_2 = \frac{u_2}{||u_2||} = \frac{1}{3}(1, 0, 2, -2) = (\frac{1}{3}, 0, \frac{2}{3}, -\frac{2}{3})$ [source:ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1]

**Step 3: Find $q_3$**
Let $u_3 = v_3 - (v_3 \cdot q_1)q_1 - (v_3 \cdot q_2)q_2$.
First, calculate the dot product $v_3 \cdot q_1$:
$v_3 \cdot q_1 = (1, 4, 3, 5) \cdot (\frac{2}{3}, 0, \frac{1}{3}, \frac{2}{3}) = (1 \cdot \frac{2}{3}) + (4 \cdot 0) + (3 \cdot \frac{1}{3}) + (5 \cdot \frac{2}{3}) = \frac{2}{3} + 0 + 1 + \frac{10}{3} = \frac{2}{3} + \frac{3}{3} + \frac{10}{3} = \frac{15}{3} = 5$.
Next, calculate the dot product $v_3 \cdot q_2$:
$v_3 \cdot q_2 = (1, 4, 3, 5) \cdot (\frac{1}{3}, 0, \frac{2}{3}, -\frac{2}{3}) = (1 \cdot \frac{1}{3}) + (4 \cdot 0) + (3 \cdot \frac{2}{3}) + (5 \cdot (-\frac{2}{3})) = \frac{1}{3} + 0 + 2 - \frac{10}{3} = \frac{1}{3} + \frac{6}{3} - \frac{10}{3} = -\frac{3}{3} = -1$.
Now, calculate $u_3$:
$u_3 = (1, 4, 3, 5) - 5 \cdot (\frac{2}{3}, 0, \frac{1}{3}, \frac{2}{3}) - (-1) \cdot (\frac{1}{3}, 0, \frac{2}{3}, -\frac{2}{3})$
$u_3 = (1, 4, 3, 5) - (\frac{10}{3}, 0, \frac{5}{3}, \frac{10}{3}) + (\frac{1}{3}, 0, \frac{2}{3}, -\frac{2}{3})$
$u_3 = (1 - \frac{10}{3} + \frac{1}{3}, 4 - 0 + 0, 3 - \frac{5}{3} + \frac{2}{3}, 5 - \frac{10}{3} - \frac{2}{3})$
$u_3 = (\frac{3 - 10 + 1}{3}, 4, \frac{9 - 5 + 2}{3}, \frac{15 - 10 - 2}{3})$
$u_3 = (-\frac{6}{3}, 4, \frac{6}{3}, \frac{3}{3}) = (-2, 4, 2, 1)$ [source:ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1]
Calculate its norm: $||u_3|| = \sqrt{(-2)^2 + 4^2 + 2^2 + 1^2} = \sqrt{4 + 16 + 4 + 1} = \sqrt{25} = 5$.
Normalize $u_3$ to get $q_3$:
$q_3 = \frac{u_3}{||u_3||} = \frac{1}{5}(-2, 4, 2, 1) = (-\frac{2}{5}, \frac{4}{5}, \frac{2}{5}, \frac{1}{5})$ [source:ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1]

Thus, the orthonormal basis for $V$ is $\{(\frac{2}{3}, 0, \frac{1}{3}, \frac{2}{3}), (\frac{1}{3}, 0, \frac{2}{3}, -\frac{2}{3}), (-\frac{2}{5}, \frac{4}{5}, \frac{2}{5}, \frac{1}{5})\}$ [source:ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1].

### Application: Orthogonal Projection onto a Subspace

Once an orthonormal basis $\{q_1, \ldots, q_k\}$ for a subspace $V$ is found, calculating the [orthogonal projection](ma2001-orthogonal-sets-projections.md) of any vector $u$ onto $V$ becomes straightforward. The projection $p$ is given by:
$p = (u \cdot q_1)q_1 + (u \cdot q_2)q_2 + \ldots + (u \cdot q_k)q_k$

Using the orthonormal basis derived above for subspace $V$, we can find the orthogonal projection of vector $u = (0, -5, 16, 13)$ onto $V$ [source:ma2001-hw4-hw4-q-pdf#section-1].

1.  **Calculate $(u \cdot q_1)q_1$**:
    $u \cdot q_1 = (0, -5, 16, 13) \cdot (\frac{2}{3}, 0, \frac{1}{3}, \frac{2}{3}) = 0 + 0 + \frac{16}{3} + \frac{26}{3} = \frac{42}{3} = 14$.
    $(u \cdot q_1)q_1 = 14 \cdot (\frac{2}{3}, 0, \frac{1}{3}, \frac{2}{3}) = (\frac{28}{3}, 0, \frac{14}{3}, \frac{28}{3})$.

2.  **Calculate $(u \cdot q_2)q_2$**:
    $u \cdot q_2 = (0, -5, 16, 13) \cdot (\frac{1}{3}, 0, \frac{2}{3}, -\frac{2}{3}) = 0 + 0 + \frac{32}{3} - \frac{26}{3} = \frac{6}{3} = 2$.
    $(u \cdot q_2)q_2 = 2 \cdot (\frac{1}{3}, 0, \frac{2}{3}, -\frac{2}{3}) = (\frac{2}{3}, 0, \frac{4}{3}, -\frac{4}{3})$.

3.  **Calculate $(u \cdot q_3)q_3$**:
    $u \cdot q_3 = (0, -5, 16, 13) \cdot (-\frac{2}{5}, \frac{4}{5}, \frac{2}{5}, \frac{1}{5}) = 0 - \frac{20}{5} + \frac{32}{5} + \frac{13}{5} = \frac{-20+32+13}{5} = \frac{25}{5} = 5$.
    $(u \cdot q_3)q_3 = 5 \cdot (-\frac{2}{5}, \frac{4}{5}, \frac{2}{5}, \frac{1}{5}) = (-2, 4, 2, 1)$.

4.  **Sum the projections to find $p$**:
    $p = (\frac{28}{3}, 0, \frac{14}{3}, \frac{28}{3}) + (\frac{2}{3}, 0, \frac{4}{3}, -\frac{4}{3}) + (-2, 4, 2, 1)$
    $p = (\frac{30}{3} - 2, 0 + 4, \frac{18}{3} + 2, \frac{24}{3} + 1)$
    $p = (10 - 2, 4, 6 + 2, 8 + 1) = (8, 4, 8, 9)$ [source:ma2001-hw4-a0251957u-ma2001-hw4-pdf#section-1].
This is the orthogonal projection of $u$ onto $V$.

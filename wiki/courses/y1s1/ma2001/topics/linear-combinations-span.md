---
page_id: "y1s1-ma2001-linear-combinations-span"
title: "Linear Combinations and Span"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Understanding how vectors combine to form new vectors, and defining the span of a set of vectors as a subspace."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter3-pdf#section-2"
  - "ma2001-tutorial-tutorial5-pdf#section-1"
  - "ma2001-lab-lab3-pdf#section-1"
  - "ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-1"
topics:
  - "vector"
  - "vectors"
  - "linear"
  - "span"
  - "set"
  - "linearly"
  - "basis"
  - "space"
  - "let"
  - "determine"
source_count: 4
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Linear Combinations and Span

In linear algebra, understanding how vectors interact and combine is fundamental. This page introduces the concepts of linear combinations, which describe how vectors can be scaled and added to form new vectors, and linear span, which defines the set of all possible vectors that can be created through these combinations from a given set. We will also introduce the idea of a subspace, which is a vector space contained within a larger one, often defined by a linear span.

---

## Introduction to Vectors and Euclidean _n_-Space

Before delving into linear combinations and span, we first establish the foundational concepts of vectors and Euclidean $n$-space ($R^n$).

### Geometric Vectors
A **nonzero vector** can be represented geometrically as a directed line segment, or an arrow, characterized by its direction and magnitude (length). The **zero vector**, denoted by $0$, is a point with zero length and no specific direction. Two vectors are considered **equal** if they possess the same length and direction [source: ma2001-lecture-chapter3-pdf#section-1].

Fundamental operations for geometric vectors include:
*   **Addition ($u + v$)**: This operation is commutative ($u + v = v + u$) [source: ma2001-lecture-chapter3-pdf#section-1].
*   **Negative ($-u$)**: The negative of a vector $u$ has the same length as $u$ but points in the reverse direction [source: ma2001-lecture-chapter3-pdf#section-1].
*   **Difference ($u - v$)**: Defined as $u + (-v)$ [source: ma2001-lecture-chapter3-pdf#section-1].
*   **Scalar Multiple ($cu$)**: For a real number $c$ and vector $u$:
    *   If $c > 0$, $cu$ has the same direction as $u$ and its length is $c$ times the length of $u$.
    *   If $c < 0$, $cu$ has the reverse direction of $u$ and its length is $|c|$ times the length of $u$.
    *   $0u = 0$ (the zero vector).
    *   $(-1)u = -u$ [source: ma2001-lecture-chapter3-pdf#section-1].

### Coordinate Systems and _n_-Vectors
In coordinate systems like the $xy$-plane or $xyz$-space, a vector $u$ can be positioned with its initial point at the origin $(0, 0)$ or $(0, 0, 0)$. The coordinates of its end point are called the **components** of $u$. For example, in the $xy$-plane, $u = (u_1, u_2)$, and in $xyz$-space, $u = (u_1, u_2, u_3)$ [source: ma2001-lecture-chapter3-pdf#section-1]. Algebraically, vectors can be identified with points in these spaces.

This concept extends to **$n$-vectors** or **ordered $n$-tuples**, which are sequences of $n$ real numbers $(u_1, u_2, \dots, u_n)$. Each number $u_i$ is the $i$-th component or coordinate of the $n$-vector [source: ma2001-lecture-chapter3-pdf#section-1].

For two $n$-vectors $u = (u_1, \dots, u_n)$ and $v = (v_1, \dots, v_n)$:
*   **Equality**: $u = v$ if and only if $u_i = v_i$ for all $i = 1, \dots, n$ [source: ma2001-lecture-chapter3-pdf#section-1].
*   **Addition**: $u + v = (u_1 + v_1, u_2 + v_2, \dots, u_n + v_n)$ [source: ma2001-lecture-chapter3-pdf#section-1].
*   **Scalar Multiple**: For a real number $c$, $cu = (cu_1, cu_2, \dots, cu_n)$ [source: ma2001-lecture-chapter3-pdf#section-1].
*   **Zero Vector**: The $n$-vector $(0, 0, \dots, 0)$ is denoted by $0$ [source: ma2001-lecture-chapter3-pdf#section-1].
*   **Negative**: The negative of $u$ is $(-1)u = (-u_1, -u_2, \dots, -u_n)$, denoted by $-u$ [source: ma2001-lecture-chapter3-pdf#section-1].
*   **Subtraction**: $u - v = u + (-v) = (u_1 - v_1, u_2 - v_2, \dots, u_n - v_n)$ [source: ma2001-lecture-chapter3-pdf#section-1].

**Example 3.1.4:**
Let $u = (1, 2, 3, 4)$ and $v = (-1, -2, -3, 0)$. Then:
*   $u + v = (1 + (-1), 2 + (-2), 3 + (-3), 4 + 0) = (0, 0, 0, 4)$
*   $u - v = (1 - (-1), 2 - (-2), 3 - (-3), 4 - 0) = (2, 4, 6, 4)$
*   $3u = (3 \cdot 1, 3 \cdot 2, 3 \cdot 3, 3 \cdot 4) = (3, 6, 9, 12)$
*   $3u + 4v = (3 \cdot 1 + 4 \cdot (-1), 3 \cdot 2 + 3 \cdot (-2), 3 \cdot 3 + 3 \cdot (-3), 3 \cdot 4 + 3 \cdot 0) = (-1, -2, -3, 12)$ [source: ma2001-lecture-chapter3-pdf#section-1]

**Notation**: $n$-vectors can be identified with $1 \times n$ row matrices (row vectors) or $n \times 1$ column matrices (column vectors). It is important not to mix notation within the same context [source: ma2001-lecture-chapter3-pdf#section-1].

These operations satisfy several basic properties, such as commutativity of addition ($u + v = v + u$), associativity of addition and scalar multiplication ($u + (v + w) = (u + v) + w$, $c(du) = (cd)u$), distributive properties ($c(u + v) = cu + cv$, $(c + d)u = cu + du$), existence of additive identity ($u + 0 = u$), additive inverse ($u + (-u) = 0$), and scalar identity ($1u = u$) [source: ma2001-lecture-chapter3-pdf#section-1].

The set of all $n$-vectors of real numbers is called **Euclidean $n$-space** or simply **$n$-space**, denoted by $R^n$ [source: ma2001-lecture-chapter3-pdf#section-1].
In set notation, $R^n = \{ (u_1, u_2, \dots, u_n) \mid u_1, u_2, \dots, u_n \in R \}$ [source: ma2001-lecture-chapter3-pdf#section-1].

Subsets of $R^n$ can represent solution sets of linear equations, lines, or planes. For example, a line in $R^2$ can be expressed as $\{ (x, y) \mid ax + by = c \}$, and a plane in $R^3$ as $\{ (x, y, z) \mid ax + by + cz = d \}$ [source: ma2001-lecture-chapter3-pdf#section-1].

## Linear Combinations

A vector $v$ is a **linear combination** of vectors $u_1, u_2, \dots, u_k$ in $R^n$ if it can be expressed in the form $v = c_1u_1 + c_2u_2 + \dots + c_ku_k$, where $c_1, c_2, \dots, c_k$ are real numbers (scalars) [source: ma2001-lecture-chapter3-pdf#section-2, ma2001-lab-lab3-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].

To determine if a vector $v$ is a linear combination of a set of vectors $u_1, \dots, u_k$, we set up the vector equation $v = c_1u_1 + c_2u_2 + \dots + c_ku_k$. This translates into a system of linear equations. If this system is consistent (has at least one solution for $c_1, \dots, c_k$), then $v$ is a linear combination of $u_1, \dots, u_k$ [source: ma2001-lab-lab3-pdf#section-1].

### Examples of Linear Combinations
**Example 3.2.2.1(a):**
Let $u_1 = (2, 1, 3)$, $u_2 = (1, -1, 2)$, $u_3 = (3, 0, 5)$. Is $v = (3, 3, 4)$ a linear combination of $u_1, u_2, u_3$?
We write $v = au_1 + bu_2 + cu_3$:
$(3, 3, 4) = a(2, 1, 3) + b(1, -1, 2) + c(3, 0, 5)$
$(3, 3, 4) = (2a + b + 3c, a - b, 3a + 2b + 5c)$
This forms the linear system:
$2a + b + 3c = 3$
$a - b = 3$
$3a + 2b + 5c = 4$

Using Gaussian Elimination on the augmented matrix:
$\begin{pmatrix} 2 & 1 & 3 & 3 \\ 1 & -1 & 0 & 3 \\ 3 & 2 & 5 & 4 \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} \begin{pmatrix} 2 & 1 & 3 & 3 \\ 0 & -3/2 & -3/2 & 3/2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$

The system is consistent, having infinitely many solutions (e.g., $(a, b, c) = (2 - t, -1 - t, t)$ for any real $t$). Thus, $v$ is a linear combination of $u_1, u_2, u_3$. For instance, with $t=0$, we get $a=2, b=-1, c=0$, so $v = 2u_1 - u_2 + 0u_3$ [source: ma2001-lecture-chapter3-pdf#section-2].

**Example 3.2.2.1(b):**
Using the same vectors $u_1, u_2, u_3$, is $w = (1, 2, 4)$ a linear combination?
The system becomes:
$2a + b + 3c = 1$
$a - b = 2$
$3a + 2b + 5c = 4$

Using Gaussian Elimination:
$\begin{pmatrix} 2 & 1 & 3 & 1 \\ 1 & -1 & 0 & 2 \\ 3 & 2 & 5 & 4 \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} \begin{pmatrix} 2 & 1 & 3 & 1 \\ 0 & -3/2 & -3/2 & 3/2 \\ 0 & 0 & 0 & 3 \end{pmatrix}$

The last row implies $0 = 3$, which is inconsistent. Therefore, $w$ is not a linear combination of $u_1, u_2, u_3$ [source: ma2001-lecture-chapter3-pdf#section-2].

### Standard Basis Vectors
For $R^3$, the vectors $e_1 = (1, 0, 0)$, $e_2 = (0, 1, 0)$, and $e_3 = (0, 0, 1)$ are called the directional vectors of the $x$-, $y$-, and $z$-axes, respectively. Any vector $(x, y, z) \in R^3$ can be written as a linear combination of these: $(x, y, z) = xe_1 + ye_2 + ze_3$ [source: ma2001-lecture-chapter3-pdf#section-2].

## Linear Spans

The **linear span** of a set of vectors $S = \{u_1, u_2, \dots, u_k\}$ in $R^n$ is the set of all possible linear combinations of these vectors. It is denoted by $\text{span}(S)$ or $\text{span}\{u_1, u_2, \dots, u_k\}$ [source: ma2001-lecture-chapter3-pdf#section-2, ma2001-lab-lab3-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
$\text{span}(S) = \{ c_1u_1 + c_2u_2 + \dots + c_ku_k \mid c_1, c_2, \dots, c_k \in R \}$ [source: ma2001-lecture-chapter3-pdf#section-2].

### Determining if a Set of Vectors Spans $R^n$
A set of vectors $S = \{u_1, u_2, \dots, u_k\} \subseteq R^n$ spans $R^n$ if and only if every vector $v \in R^n$ can be expressed as a linear combination of the vectors in $S$. This means the vector equation $c_1u_1 + c_2u_2 + \dots + c_ku_k = v$ must have a solution for $c_1, \dots, c_k$ for any $v = (v_1, \dots, v_n) \in R^n$ [source: ma2001-lecture-chapter3-pdf#section-2].

This is equivalent to checking the consistency of a linear system where the vectors $u_i$ form the columns of a matrix $A$, and the vector $v$ is the right-hand side. The system $Ac = v$ must be consistent for all $v \in R^n$.
A key criterion is to examine the row-echelon form of the matrix $A$ formed by the vectors $u_i$ as columns. If a row-echelon form of $A$ has **no zero rows**, then the linear system is always consistent, meaning $\text{span}(S) = R^n$. Conversely, if it has at least one zero row, the system is not always consistent, and thus $\text{span}(S) \neq R^n$ [source: ma2001-lecture-chapter3-pdf#section-2, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
The `rref` (reduced row-echelon form) command in MATLAB can be used to perform this check [source: ma2001-lab-lab3-pdf#section-1].

**Theorem 3.2.7:** If $S = \{u_1, u_2, \dots, u_k\} \subseteq R^n$ and $k < n$, then $\text{span}(S) \neq R^n$. In other words, you need at least $n$ vectors to span $R^n$ [source: ma2001-lecture-chapter3-pdf#section-2].
*   One vector cannot span $R^2$.
*   One or two vectors cannot span $R^3$.

**Example 3.2.4.4:**
Show that $\text{span}\{ (1, 0, 1), (1, 1, 0), (0, 1, 1) \} = R^3$.
We need to show that for any $(x, y, z) \in R^3$, there exist scalars $a, b, c$ such that:
$a(1, 0, 1) + b(1, 1, 0) + c(0, 1, 1) = (x, y, z)$
This leads to the system:
$a + b = x$
$b + c = y$
$a + c = z$
The augmented matrix is:
$\begin{pmatrix} 1 & 1 & 0 & x \\ 0 & 1 & 1 & y \\ 1 & 0 & 1 & z \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} \begin{pmatrix} 1 & 1 & 0 & x \\ 0 & 1 & 1 & y \\ 0 & 0 & 2 & z - x + y \end{pmatrix}$
Since there are no zero rows in the coefficient matrix, the system is consistent for all $x, y, z \in R$. Thus, the vectors span $R^3$ [source: ma2001-lecture-chapter3-pdf#section-2].

**Example 3.2.4.5:**
Show that $\text{span}\{ (1, 1, 1), (1, 2, 0), (2, 1, 3), (2, 3, 1) \} \neq R^3$.
We set up the equation $a(1, 1, 1) + b(1, 2, 0) + c(2, 1, 3) + d(2, 3, 1) = (x, y, z)$.
The augmented matrix:
$\begin{pmatrix} 1 & 1 & 2 & 2 & x \\ 1 & 2 & 1 & 3 & y \\ 1 & 0 & 3 & 1 & z \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} \begin{pmatrix} 1 & 1 & 2 & 2 & x \\ 0 & 1 & -1 & 1 & y-x \\ 0 & 0 & 0 & 0 & z+x-2y \end{pmatrix}$
The system is inconsistent if $z + x - 2y \neq 0$. For example, for $(x, y, z) = (1, 0, 0)$, $z + x - 2y = 1 + 0 - 0 = 1 \neq 0$. Thus, $(1, 0, 0)$ is not in the span, and the set of vectors does not span $R^3$ [source: ma2001-lecture-chapter3-pdf#section-2].

### Basic Properties of Spans
1.  The zero vector $0$ is always an element of $\text{span}(S)$ [source: ma2001-lecture-chapter3-pdf#section-2].
2.  If $v_1, \dots, v_r$ are vectors in $\text{span}(S)$, and $c_1, \dots, c_r$ are real numbers, then $c_1v_1 + \dots + c_rv_r$ is also in $\text{span}(S)$ [source: ma2001-lecture-chapter3-pdf#section-2]. This property highlights that a span forms a [[vector-spaces-subspaces-intro#Subspaces|subspace]].

### Relationship Between Spans
Let $S_1 = \{u_1, \dots, u_k\}$ and $S_2 = \{v_1, \dots, v_m\}$ be subsets of $R^n$.
Then $\text{span}(S_1) \subseteq \text{span}(S_2)$ if and only if each $u_i$ is a linear combination of $v_1, \dots, v_m$ [source: ma2001-lecture-chapter3-pdf#section-2].
To show $\text{span}(S_1) = \text{span}(S_2)$, you must demonstrate that $\text{span}(S_1) \subseteq \text{span}(S_2)$ AND $\text{span}(S_2) \subseteq \text{span}(S_1)$ [source: ma2001-lecture-chapter3-pdf#section-2].

This involves checking the consistency of multiple linear systems. For instance, to show that a set of vectors $U = \{u_1, u_2, u_3\}$ is a subset of the span of $V = \{v_1, v_2\}$, one would set up and solve for consistency the linear systems for $u_1, u_2, u_3$ as linear combinations of $v_1, v_2$. If all are consistent, then $\text{span}(U) \subseteq \text{span}(V)$ [source: ma2001-lecture-chapter3-pdf#section-2]. The process can be streamlined by setting up a combined augmented matrix where $V$ forms the coefficient matrix and $U$ forms the augmented part, then reducing it to check consistency for all $u_i$ simultaneously [source: ma2001-tutorial-tutorial5-pdf#section-2].

## Redundant Vectors

A vector $u_k$ in a set $S = \{u_1, u_2, \dots, u_k\}$ is considered a **redundant vector** if it can be expressed as a linear combination of the other vectors in the set $S$. If $u_k$ is redundant, then removing it from the set does not change the span: $\text{span}\{u_1, u_2, \dots, u_{k-1}\} = \text{span}\{u_1, u_2, \dots, u_k\}$ [source: ma2001-lecture-chapter3-pdf#section-2].

**Example 3.2.13:**
Let $u_1 = (1, 1, 0, 2)$, $u_2 = (1, 0, 0, 1)$, $u_3 = (0, 1, 0, 1)$.
It can be checked that $u_3 = u_1 - u_2$.
Thus, $u_3$ is a redundant vector, and $\text{span}\{u_1, u_2, u_3\} = \text{span}\{u_1, u_2\}$ [source: ma2001-lecture-chapter3-pdf#section-2].

## Geometric Interpretation of Linear Spans

The linear span of a set of vectors has clear geometric interpretations in $R^2$ and $R^3$.

*   **Span of one nonzero vector in $R^2$ or $R^3$**: If $u$ is a nonzero vector, $\text{span}\{u\} = \{cu \mid c \in R\}$ represents a **line passing through the origin** in $R^2$ or $R^3$ [source: ma2001-lecture-chapter3-pdf#section-2].
    *   In $R^2$, for $u=(u_1, u_2)$, $\text{span}\{u\} = \{ (x, y) \mid u_2x - u_1y = 0 \}$.
    *   In $R^3$, for $u=(u_1, u_2, u_3)$, $\text{span}\{u\} = \{ (cu_1, cu_2, cu_3) \mid c \in R \}$.

*   **Span of two non-parallel nonzero vectors in $R^2$ or $R^3$**: If $u$ and $v$ are nonzero and not parallel, $\text{span}\{u, v\} = \{su + tv \mid s, t \in R\}$ represents a **plane containing the origin**.
    *   In $R^2$, if $u$ and $v$ are non-parallel, $\text{span}\{u, v\} = R^2$ [source: ma2001-lecture-chapter3-pdf#section-2].
    *   In $R^3$, if $u=(u_1, u_2, u_3)$ and $v=(v_1, v_2, v_3)$, $\text{span}\{u, v\}$ is a plane defined by an equation $ax + by + cz = 0$, where $(a, b, c)$ is a non-trivial solution to the system $u_1a + u_2b + u_3c = 0$ and $v_1a + v_2b + v_3c = 0$ [source: ma2001-lecture-chapter3-pdf#section-2].

### Generalization to Lines and Planes Not Through the Origin
The concept of span can be generalized to describe lines and planes that do not necessarily pass through the origin. These are defined by translating a span (which always passes through the origin) by a fixed vector $x$.
*   A **line** in $R^n$ is defined as $L = \{x + w \mid w \in \text{span}\{u\}\}$, where $x, u \in R^n$ and $u$ is a nonzero vector. This means the line $L$ is parallel to $\text{span}\{u\}$ and passes through the point $x$ [source: ma2001-lecture-chapter3-pdf#section-2].
*   A **plane** in $R^n$ is defined as $P = \{x + w \mid w \in \text{span}\{u, v\}\}$, where $x, u, v \in R^n$, $u, v$ are nonzero, and $u$ is not a multiple of $v$. This means the plane $P$ is parallel to $\text{span}\{u, v\}$ and contains the point $x$ [source: ma2001-lecture-chapter3-pdf#section-2].
*   More generally, a **$k$-plane** in $R^n$ is $Q = \{x + w \mid w \in \text{span}\{u_1, \dots, u_r\}\}$, where $k$ is the [[dimension-rank-nullity#Dimension of a Vector Space|dimension]] of $\text{span}\{u_1, \dots, u_r\}$ [source: ma2001-lecture-chapter3-pdf#section-2].

## Introduction to Subspaces

A subset $V$ of $R^n$ is called a **subspace** of $R^n$ if $V$ is the linear span of some set of vectors $S = \{u_1, u_2, \dots, u_k\}$ from $R^n$. In this case, we say that $V$ is spanned by $S$, or $S$ spans $V$ [source: ma2001-lecture-chapter3-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].

### Trivial Subspaces
There are two fundamental or "trivial" subspaces of $R^n$:
1.  The **zero space**: The set containing only the zero vector, $\{0\} = \text{span}\{0\}$. This is a subspace of $R^n$ [source: ma2001-lecture-chapter3-pdf#section-3].
2.  **$R^n$ itself**: The entire Euclidean $n$-space is a subspace of itself. For instance, $R^n = \text{span}\{e_1, e_2, \dots, e_n\}$, where $e_i$ are the standard basis vectors [source: ma2001-lecture-chapter3-pdf#section-3].

### Examples of Subspaces
**Example 3.3.4.1:**
Let $V_1 = \{ (a + 4b, a) \mid a, b \in R \} \subseteq R^2$.
For any $a, b \in R$, $(a + 4b, a) = a(1, 1) + b(4, 0)$.
So, $V_1 = \text{span}\{(1, 1), (4, 0)\}$, which means $V_1$ is a subspace of $R^2$ [source: ma2001-lecture-chapter3-pdf#section-3].

**Example 3.3.4.2:**
Let $V_2 = \{ (x, y, z) \mid x + y - z = 0 \} \subseteq R^3$.
The equation $x + y - z = 0$ is a homogeneous linear equation. Its general solution can be found by setting free variables. Let $y=s$ and $z=t$. Then $x = z - y = t - s$.
So, $(x, y, z) = (-s + t, s, t) = s(-1, 1, 0) + t(1, 0, 1)$.
Thus, $V_2 = \text{span}\{(-1, 1, 0), (1, 0, 1)\}$, making $V_2$ a subspace of $R^3$ [source: ma2001-lecture-chapter3-pdf#section-3]. This span is a plane in $R^3$ containing the origin [source: ma2001-lecture-chapter3-pdf#section-3].

**Solution sets of homogeneous linear systems (HLS)** are always subspaces. This is because the general solution to a homogeneous system $Ax = 0$ can always be written as a linear combination of a set of fixed vectors (the basis vectors for the solution space), which means the solution set is a span [source: ma2001-lecture-chapter3-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].

### How to Determine if a Subset is a Subspace
If a subset $V$ of $R^n$ can be expressed as $\text{span}\{u_1, u_2, \dots, u_k\}$, where $u_1, \dots, u_k$ are constant vectors, then $V$ is a subspace of $R^n$ [source: ma2001-lecture-chapter3-pdf#section-3].

An alternative, equivalent definition of a subspace is:
A non-empty subset $V$ of $R^n$ is a subspace if and only if for all $u, v \in V$ and scalars $c, d \in R$, $cu + dv \in V$ (i.e., it is closed under vector addition and scalar multiplication) [source: ma2001-lecture-chapter3-pdf#section-3].

To show a subset $W$ is **not** a subspace, it is easier to show that it fails one of the subspace properties:
*   $0 \notin W$ (the zero vector is not in $W$) [source: ma2001-lecture-chapter3-pdf#section-3].
*   There exists a vector $v \in W$ and a scalar $c \in R$ such that $cv \notin W$ (not closed under scalar multiplication) [source: ma2001-lecture-chapter3-pdf#section-3].
*   There exist vectors $u, v \in W$ such that $u + v \notin W$ (not closed under vector addition) [source: ma2001-lecture-chapter3-pdf#section-3].

**Example 3.3.4.3:**
Let $V_3 = \{ (1, a) \mid a \in R \} \subseteq R^2$.
The zero vector $(0, 0)$ is not of the form $(1, a)$ for any $a \in R$. Therefore, $V_3$ is not a subspace of $R^2$ [source: ma2001-lecture-chapter3-pdf#section-3].

**Example 3.3.4.4:**
Let $V_4 = \{ (x, y, z) \mid x^2 \le y^2 \le z^2 \} \subseteq R^3$.
Observe that $(1, 1, 2) \in V_4$ since $1^2 \le 1^2 \le 2^2$ (i.e., $1 \le 1 \le 4$).
Also, $(1, 1, -2) \in V_4$ since $1^2 \le 1^2 \le (-2)^2$ (i.e., $1 \le 1 \le 4$).
However, their sum is $(1, 1, 2) + (1, 1, -2) = (2, 2, 0)$.
For $(2, 2, 0)$, we check $x^2 \le y^2 \le z^2$: $2^2 \le 2^2 \le 0^2$ (i.e., $4 \le 4 \le 0$), which is false.
Thus, $(2, 2, 0) \notin V_4$, so $V_4$ is not closed under vector addition and therefore not a subspace of $R^3$ [source: ma2001-lecture-chapter3-pdf#section-3].

### Geometrical Interpretation of Subspaces
In $R^2$, all subspaces are:
*   The zero space $\{ (0, 0) \}$.
*   Lines passing through the origin.
*   $R^2$ itself [source: ma2001-lecture-chapter3-pdf#section-3].

In $R^3$, all subspaces are:
*   The zero space $\{ (0, 0, 0) \}$.
*   Lines passing through the origin.
*   Planes containing the origin.
*   $R^3$ itself [source: ma2001-lecture-chapter3-pdf#section-3].

---
This page establishes the foundational understanding of linear combinations, span, and subspaces, which are critical for further topics in linear algebra, such as linear independence and bases.

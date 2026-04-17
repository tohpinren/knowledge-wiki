---
page_id: "y1s1-ma2001-vector-spaces-subspaces-intro"
title: "Introduction to Vector Spaces and Subspaces"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Defining vector spaces and their axioms, with a focus on Euclidean n-space (R\u207f) and conditions for a subset to be a subspace."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter3-pdf#section-1"
  - "ma2001-linear-algebra-pdf-pdf#section-2"
  - "ma2001-ma2001-trial-run-2022-pdf#section-1"
topics:
  - "vector"
  - "vectors"
  - "linear"
  - "span"
  - "set"
  - "linearly"
  - "basis"
  - "space"
  - "matrix"
  - "row"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Introduction to Vector Spaces and Subspaces

## Introduction to Vector Spaces and Subspaces

Linear algebra is a fundamental course that introduces concepts and techniques primarily within the context of Euclidean spaces, denoted as $\mathbb{R}^n$ [source:ma2001-ma2001-trial-run-2022-pdf#section-1]. The module emphasizes developing computational skills, geometric intuition, and understanding formal proofs related to vectors and matrices [source:ma2001-ma2001-trial-run-2022-pdf#section-1]. This page begins by defining vectors and their operations in Euclidean space, leading to the formal definition of vector spaces and, more specifically, subspaces.

---

### Euclidean $n$-Space ($\mathbb{R}^n$)

The study of vector spaces often begins by understanding vectors in a geometric context. Euclid of Alexandria, a pivotal ancient mathematician, laid the groundwork for plane geometry with "The Elements" [source:ma2001-lecture-chapter3-pdf#section-3].

#### Geometric Vectors

A nonzero vector is geometrically represented as a directed line segment or an arrow, possessing both direction and magnitude (length) [source:ma2001-lecture-chapter3-pdf#section-4]. The zero vector, denoted by $\mathbf{0}$, is a point with zero length and no specific direction [source:ma2001-lecture-chapter3-pdf#section-4]. Two vectors are considered equal if they share the same length and direction [source:ma2001-lecture-chapter3-pdf#section-4].

Fundamental operations for geometric vectors include:
*   **Addition ($\mathbf{u} + \mathbf{v}$)**: Performed using the parallelogram rule. Vector addition is commutative, meaning $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ [source:ma2001-lecture-chapter3-pdf#section-5].
*   **Negative of a Vector ($-\mathbf{u}$)**: A vector with the same length as $\mathbf{u}$ but in the reverse direction [source:ma2001-lecture-chapter3-pdf#section-6].
*   **Difference ($\mathbf{u} - \mathbf{v}$)**: Defined as $\mathbf{u} + (-\mathbf{v})$ [source:ma2001-lecture-chapter3-pdf#section-7].
*   **Scalar Multiple ($c\mathbf{u}$)**: For a real number $c$:
    *   If $c > 0$, $c\mathbf{u}$ has the same direction as $\mathbf{u}$ and its length is $c$ times the length of $\mathbf{u}$ [source:ma2001-lecture-chapter3-pdf#section-8].
    *   If $c < 0$, $c\mathbf{u}$ has the reverse direction of $\mathbf{u}$ and its length is $|c|$ times the length of $\mathbf{u}$ [source:ma2001-lecture-chapter3-pdf#section-8].
    *   If $c = 0$, $0\mathbf{u} = \mathbf{0}$ (the zero vector) [source:ma2001-lecture-chapter3-pdf#section-8].
    *   $(-1)\mathbf{u} = -\mathbf{u}$ [source:ma2001-lecture-chapter3-pdf#section-8].

#### Coordinate Systems

Vectors can be described algebraically using coordinate systems.
*   **$xy$-plane (2D)**: A vector $\mathbf{u}$ starting at the origin $(0, 0)$ is identified by its endpoint coordinates $(u_1, u_2)$, which are called the **components** of $\mathbf{u}$. Thus, $\mathbf{u} = (u_1, u_2)$ [source:ma2001-lecture-chapter3-pdf#section-9].
    *   Addition: If $\mathbf{u} = (u_1, u_2)$ and $\mathbf{v} = (v_1, v_2)$, then $\mathbf{u} + \mathbf{v} = (u_1 + v_1, u_2 + v_2)$ [source:ma2001-lecture-chapter3-pdf#section-10].
    *   Scalar Multiplication: If $\mathbf{u} = (u_1, u_2)$ and $c$ is a real constant, then $c\mathbf{u} = (cu_1, cu_2)$ [source:ma2001-lecture-chapter3-pdf#section-11].
*   **$xyz$-space (3D)**: Similarly, a vector $\mathbf{u}$ starting at the origin $(0, 0, 0)$ is identified by its endpoint coordinates $(u_1, u_2, u_3)$, so $\mathbf{u} = (u_1, u_2, u_3)$ [source:ma2001-lecture-chapter3-pdf#section-12].
    *   Addition: $\mathbf{u} + \mathbf{v} = (u_1 + v_1, u_2 + v_2, u_3 + v_3)$ [source:ma2001-lecture-chapter3-pdf#section-13].
    *   Scalar Multiplication: $c\mathbf{u} = (cu_1, cu_2, cu_3)$ [source:ma2001-lecture-chapter3-pdf#section-13].

#### $n$-Vectors (Ordered $n$-Tuples)

The concept generalizes to $n$-dimensions. An **$n$-vector** or **ordered $n$-tuple** of real numbers has the form $(\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_i, \dots, \mathbf{u}_n)$, where $u_1, u_2, \dots, u_n$ are real numbers [source:ma2001-lecture-chapter3-pdf#section-14]. The number $u_i$ is called the $i$-th **component** or **coordinate** [source:ma2001-lecture-chapter3-pdf#section-14].

For two $n$-vectors $\mathbf{u} = (u_1, \dots, u_n)$ and $\mathbf{v} = (v_1, \dots, v_n)$:
1.  **Equality**: $\mathbf{u} = \mathbf{v}$ if and only if $u_i = v_i$ for all $i = 1, \dots, n$ [source:ma2001-lecture-chapter3-pdf#section-14].
2.  **Addition**: $\mathbf{u} + \mathbf{v} = (u_1 + v_1, u_2 + v_2, \dots, u_n + v_n)$ [source:ma2001-lecture-chapter3-pdf#section-14].
3.  **Scalar Multiple**: For a real number $c$, $c\mathbf{u} = (cu_1, cu_2, \dots, cu_n)$ [source:ma2001-lecture-chapter3-pdf#section-15].
4.  **Zero Vector**: The $n$-vector $(0, 0, \dots, 0)$ is the **zero vector**, denoted by $\mathbf{0}$ [source:ma2001-lecture-chapter3-pdf#section-15].
5.  **Negative**: The negative of $\mathbf{u}$ is $-\mathbf{u} = (-u_1, -u_2, \dots, -u_n)$ [source:ma2001-lecture-chapter3-pdf#section-15].
6.  **Subtraction**: $\mathbf{u} - \mathbf{v} = \mathbf{u} + (-\mathbf{v}) = (u_1 - v_1, u_2 - v_2, \dots, u_n - v_n)$ [source:ma2001-lecture-chapter3-pdf#section-15].

**Example**:
Let $\mathbf{u} = (1, 2, 3, 4)$ and $\mathbf{v} = (-1, -2, -3, 0)$.
*   $\mathbf{u} + \mathbf{v} = (1+(-1), 2+(-2), 3+(-3), 4+0) = (0, 0, 0, 4)$ [source:ma2001-lecture-chapter3-pdf#section-16].
*   $\mathbf{u} - \mathbf{v} = (1-(-1), 2-(-2), 3-(-3), 4-0) = (2, 4, 6, 4)$ [source:ma2001-lecture-chapter3-pdf#section-16].
*   $3\mathbf{u} = (3 \cdot 1, 3 \cdot 2, 3 \cdot 3, 3 \cdot 4) = (3, 6, 9, 12)$ [source:ma2001-lecture-chapter3-pdf#section-16].

$n$-vectors can be identified with $1 \times n$ row matrices or $n \times 1$ column matrices [source:ma2001-lecture-chapter3-pdf#section-17]. It is crucial not to mix these notations within the same context to avoid confusion [source:ma2001-lecture-chapter3-pdf#section-17].

#### Basic Properties of $n$-Vectors

For $n$-vectors $\mathbf{u}, \mathbf{v}, \mathbf{w}$ and real numbers $c, d$:
1.  $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ (Commutativity of addition) [source:ma2001-lecture-chapter3-pdf#section-18].
2.  $\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w}$ (Associativity of addition) [source:ma2001-lecture-chapter3-pdf#section-18].
3.  $\mathbf{u} + \mathbf{0} = \mathbf{u} = \mathbf{0} + \mathbf{u}$ (Additive identity) [source:ma2001-lecture-chapter3-pdf#section-18].
4.  $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$ (Additive inverse) [source:ma2001-lecture-chapter3-pdf#section-18].
5.  $c(d\mathbf{u}) = (cd)\mathbf{u}$ (Associativity of scalar multiplication) [source:ma2001-lecture-chapter3-pdf#section-18].
6.  $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ (Distributivity of scalar multiplication over vector addition) [source:ma2001-lecture-chapter3-pdf#section-18].
7.  $(c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}$ (Distributivity of scalar addition over scalar multiplication) [source:ma2001-lecture-chapter3-pdf#section-18].
8.  $1\mathbf{u} = \mathbf{u}$ (Multiplicative identity for scalars) [source:ma2001-lecture-chapter3-pdf#section-18].

These properties are easily verifiable by expressing the $n$-vectors in their component forms [source:ma2001-linear-algebra-pdf-pdf#section-5].

#### Definition of Euclidean $n$-Space

The set of all $n$-vectors of real numbers is called the **Euclidean $n$-space** or simply **$n$-space**, denoted by $\mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-19]. The set of all real numbers is denoted by $\mathbb{R}$ [source:ma2001-lecture-chapter3-pdf#section-19].
So, $\mathbf{u} \in \mathbb{R}^n$ if and only if $\mathbf{u} = (u_1, u_2, \dots, u_n)$ for some $u_1, u_2, \dots, u_n \in \mathbb{R}$ [source:ma2001-lecture-chapter3-pdf#section-19].
In set notation, $\mathbb{R}^n = \{ (u_1, u_2, \dots, u_n) \mid u_1, u_2, \dots, u_n \in \mathbb{R} \}$ [source:ma2001-lecture-chapter3-pdf#section-19].

#### Subsets of $\mathbb{R}^n$

Subsets of $\mathbb{R}^n$ can represent various geometric objects or solution spaces:

*   **Explicitly defined sets**: A set $B = \{ (u_1, u_2, u_3, u_4) \in \mathbb{R}^4 \mid u_1 = 0 \text{ and } u_2 = u_4 \}$ can be explicitly written as $B = \{ (0, a, b, a) \mid a, b \in \mathbb{R} \}$ [source:ma2001-lecture-chapter3-pdf#section-20].
*   **Solution sets of linear systems**: If a system of linear equations has $n$ variables, its solution set forms a subset of $\mathbb{R}^n$. For example, the general solution to a system like:
    $x+y+z=0$
    $x-y+2z=1$
    can be expressed in vector form as $(x, y, z) = (\frac{1}{2} - \frac{3}{2}t, -\frac{1}{2} + \frac{1}{2}t, t)$ for any $t \in \mathbb{R}$ [source:ma2001-lecture-chapter3-pdf#section-21].
*   **Lines and Planes**:
    *   A line in $\mathbb{R}^2$ can be expressed implicitly as $\{ (x, y) \mid ax + by = c \}$ or explicitly as $\{ (\frac{c-bt}{a}, t) \mid t \in \mathbb{R} \}$ if $a \neq 0$, or $\{ (t, \frac{c-at}{b}) \mid t \in \mathbb{R} \}$ if $b \neq 0$ [source:ma2001-lecture-chapter3-pdf#section-22].
    *   A plane in $\mathbb{R}^3$ can be expressed implicitly as $\{ (x, y, z) \mid ax + by + cz = d \}$ [source:ma2001-lecture-chapter3-pdf#section-23]. Explicit forms exist depending on which coefficients are non-zero.
    *   Lines in $\mathbb{R}^3$ are usually represented explicitly by a point on the line $(a_0, b_0, c_0)$ and a direction vector $(a, b, c)$, forming the set $\{ (a_0, b_0, c_0) + t(a, b, c) \mid t \in \mathbb{R} \}$ [source:ma2001-lecture-chapter3-pdf#section-24]. A line in $\mathbb{R}^3$ cannot be represented by a single implicit equation but rather as the intersection of two non-parallel planes [source:ma2001-lecture-chapter3-pdf#section-25].

#### Finite Sets
For a finite set $S$, $|S|$ denotes the number of elements contained in $S$ [source:ma2001-lecture-chapter3-pdf#section-26].
For example, if $S_1 = \{1, 2, 3, 4\}$, then $|S_1| = 4$. If $S_2 = \{ (1, 2, 3, 4) \}$, then $|S_2| = 1$ (as it contains one element, an $n$-vector) [source:ma2001-lecture-chapter3-pdf#section-26].

---

### Linear Combinations and Linear Spans

#### Linear Combinations

Given vectors $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k \in \mathbb{R}^n$, for any real numbers $c_1, c_2, \dots, c_k$, the vector $c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k$ is called a **linear combination** of $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k$ [source:ma2001-lecture-chapter3-pdf#section-28].

**Example**: Determining if $\mathbf{v}$ is a linear combination of $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$.
Let $\mathbf{u}_1 = (2, 1, 3)$, $\mathbf{u}_2 = (1, -1, 2)$, $\mathbf{u}_3 = (3, 0, 5)$, and $\mathbf{v} = (3, 3, 4)$. To check if $\mathbf{v}$ is a linear combination, we try to find scalars $a, b, c$ such that $\mathbf{v} = a\mathbf{u}_1 + b\mathbf{u}_2 + c\mathbf{u}_3$:
$(3, 3, 4) = a(2, 1, 3) + b(1, -1, 2) + c(3, 0, 5)$
This leads to the system of linear equations:
$2a + b + 3c = 3$
$a - b = 3$
$3a + 2b + 5c = 4$
Solving this system (e.g., using [[gaussian-elimination-rref#Gaussian Elimination|Gaussian Elimination]]), we obtain a general solution $(a, b, c) = (2-t, -1-t, t)$, where $t$ is an arbitrary parameter [source:ma2001-lecture-chapter3-pdf#section-30]. Since a solution exists, $\mathbf{v}$ is a linear combination of $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$. For example, setting $t=0$ gives $(2, -1, 0)$, so $\mathbf{v} = 2\mathbf{u}_1 - \mathbf{u}_2 + 0\mathbf{u}_3$ [source:ma2001-lecture-chapter3-pdf#section-30].
If the system of equations were inconsistent (no solution), then $\mathbf{v}$ would not be a linear combination [source:ma2001-lecture-chapter3-pdf#section-32].

**Directional Vectors**:
The standard unit vectors $\mathbf{e}_1 = (1, 0, 0)$, $\mathbf{e}_2 = (0, 1, 0)$, and $\mathbf{e}_3 = (0, 0, 1)$ in $\mathbb{R}^3$ are called the directional vectors of the $x$-axis, $y$-axis, and $z$-axis, respectively [source:ma2001-lecture-chapter3-pdf#section-33]. Any vector $(x, y, z) \in \mathbb{R}^3$ can be written as a linear combination of these: $(x, y, z) = x\mathbf{e}_1 + y\mathbf{e}_2 + z\mathbf{e}_3$ [source:ma2001-lecture-chapter3-pdf#section-33].

#### Linear Span

The **linear span** of a set of vectors $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ in $\mathbb{R}^n$, denoted by $\text{span}(S)$ or $\text{span}\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$, is the set of *all possible linear combinations* of these vectors:
$\text{span}(S) = \{ c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k \mid c_1, c_2, \dots, c_k \in \mathbb{R} \}$ [source:ma2001-lecture-chapter3-pdf#section-34].

**Examples of Spans**:
*   The set $V = \{ (2a+b, a, 3b-a) \mid a, b \in \mathbb{R} \}$ can be written as $V = \text{span}\{ (2, 1, -1), (1, 0, 3) \}$ because $(2a+b, a, 3b-a) = a(2, 1, -1) + b(1, 0, 3)$ [source:ma2001-lecture-chapter3-pdf#section-35].
*   To show that $\text{span}\{ (1, 0, 1), (1, 1, 0), (0, 1, 1) \} = \mathbb{R}^3$, we must demonstrate that any vector $(x, y, z) \in \mathbb{R}^3$ can be expressed as a linear combination of the given vectors. This means the corresponding linear system $a(1,0,1) + b(1,1,0) + c(0,1,1) = (x,y,z)$ must be consistent for all $x, y, z$. The augmented matrix of this system can be reduced to a row-echelon form with no zero rows, indicating consistency for all $x,y,z$ [source:ma2001-lecture-chapter3-pdf#section-37].
*   If a set of vectors cannot span $\mathbb{R}^n$, it means there exist vectors in $\mathbb{R}^n$ that cannot be formed by their linear combinations. This often occurs when the matrix formed by the vectors (as columns) has a row-echelon form with at least one zero row, leading to inconsistent systems for certain right-hand sides [source:ma2001-lecture-chapter3-pdf#section-39].

#### When $\text{span}(S) = \mathbb{R}^n$

Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\} \subseteq \mathbb{R}^n$, where $\mathbf{u}_i = (a_{i1}, a_{i2}, \dots, a_{in})$. For any $\mathbf{v} = (v_1, v_2, \dots, v_n) \in \mathbb{R}^n$, $\mathbf{v} \in \text{span}(S)$ if and only if the vector equation $c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k = \mathbf{v}$ has a solution for $c_1, \dots, c_k$ [source:ma2001-lecture-chapter3-pdf#section-40]. This is equivalent to the linear system formed by the components being consistent:
$a_{11}c_1 + a_{21}c_2 + \dots + a_{k1}c_k = v_1$
$a_{12}c_1 + a_{22}c_2 + \dots + a_{k2}c_k = v_2$
$\vdots$
$a_{1n}c_1 + a_{2n}c_2 + \dots + a_{kn}c_k = v_n$ [source:ma2001-lecture-chapter3-pdf#section-40].

If the row-echelon form of matrix $A$ (whose columns are the vectors $\mathbf{u}_i$) has no zero rows, the system is always consistent, and thus $\text{span}(S) = \mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-41]. Conversely, if there is at least one zero row, $\text{span}(S) \neq \mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-41].

A key theorem states that if $k < n$ (number of vectors is less than the dimension of the space), then $S$ cannot span $\mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-43]. For instance, one vector cannot span $\mathbb{R}^2$, and one or two vectors cannot span $\mathbb{R}^3$ [source:ma2001-lecture-chapter3-pdf#section-43].

#### Basic Properties of Linear Spans
Let $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\} \subseteq \mathbb{R}^n$.
1.  The zero vector $\mathbf{0} \in \text{span}(S)$ (because $\mathbf{0} = 0\mathbf{u}_1 + 0\mathbf{u}_2 + \dots + 0\mathbf{u}_k$) [source:ma2001-lecture-chapter3-pdf#section-44].
2.  If $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_r \in \text{span}(S)$ and $c_1, \dots, c_r \in \mathbb{R}$, then any linear combination $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_r\mathbf{v}_r \in \text{span}(S)$ [source:ma2001-lecture-chapter3-pdf#section-44]. This means that a linear span is closed under vector addition and scalar multiplication.

#### When $\text{span}(S_1) \subseteq \text{span}(S_2)$
Let $S_1 = \{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ and $S_2 = \{\mathbf{v}_1, \dots, \mathbf{v}_m\}$ be subsets of $\mathbb{R}^n$. Then $\text{span}(S_1) \subseteq \text{span}(S_2)$ if and only if each vector $\mathbf{u}_i \in S_1$ is a linear combination of the vectors in $S_2$ [source:ma2001-lecture-chapter3-pdf#section-46]. This property is essential for proving the equality of spans, by showing mutual inclusion (i.e., $\text{span}(S_1) = \text{span}(S_2)$ if $\text{span}(S_1) \subseteq \text{span}(S_2)$ and $\text{span}(S_2) \subseteq \text{span}(S_1)$) [source:ma2001-lecture-chapter3-pdf#section-47].

#### Redundant Vectors
A vector $\mathbf{u}_k$ in a set $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ is considered a **redundant vector** if it can be expressed as a linear combination of the other vectors in the set ($\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_{k-1}$) [source:ma2001-lecture-chapter3-pdf#section-55]. In this case, removing the redundant vector does not change the span: $\text{span}\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_{k-1}\} = \text{span}\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ [source:ma2001-lecture-chapter3-pdf#section-55].

**Example**: If $\mathbf{u}_1 = (1, 1, 0, 2)$, $\mathbf{u}_2 = (1, 0, 0, 1)$, and $\mathbf{u}_3 = (0, 1, 0, 1)$, it's easy to check that $\mathbf{u}_3 = \mathbf{u}_1 - \mathbf{u}_2$. Thus, $\mathbf{u}_3$ is redundant, and $\text{span}\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\} = \text{span}\{\mathbf{u}_1, \mathbf{u}_2\}$ [source:ma2001-lecture-chapter3-pdf#section-55].

#### Geometrical Interpretation of Span
*   **$\text{span}\{\mathbf{u}\}$ (single nonzero vector)**: This is a line passing through the origin [source:ma2001-lecture-chapter3-pdf#section-56]. In $\mathbb{R}^2$ with $\mathbf{u} = (u_1, u_2)$, it is the line $\{(x, y) \mid u_2x - u_1y = 0 \}$. In $\mathbb{R}^3$ with $\mathbf{u} = (u_1, u_2, u_3)$, it is the line $\{ (cu_1, cu_2, cu_3) \mid c \in \mathbb{R} \}$ [source:ma2001-lecture-chapter3-pdf#section-56].
*   **$\text{span}\{\mathbf{u}, \mathbf{v}\}$ (two nonzero, non-parallel vectors)**: This forms a plane containing the origin [source:ma2001-lecture-chapter3-pdf#section-57]. In $\mathbb{R}^2$, if $\mathbf{u}$ and $\mathbf{v}$ are non-parallel, $\text{span}\{\mathbf{u}, \mathbf{v}\} = \mathbb{R}^2$ [source:ma2001-lecture-chapter3-pdf#section-57]. In $\mathbb{R}^3$, $\text{span}\{\mathbf{u}, \mathbf{v}\}$ defines a plane containing the origin, given by $\{ (x, y, z) \mid ax + by + cz = 0 \}$, where $(a, b, c)$ is a non-trivial solution to the system $u_1a + u_2b + u_3c = 0$ and $v_1a + v_2b + v_3c = 0$ [source:ma2001-lecture-chapter3-pdf#section-58].

This idea can be generalized:
*   A **line in $\mathbb{R}^n$** is a set $L = \{ \mathbf{x} + \mathbf{w} \mid \mathbf{w} \in \text{span}\{\mathbf{u}\} \}$, where $\mathbf{u}$ is a nonzero vector and $\mathbf{x} \in \mathbb{R}^n$ is a point on the line [source:ma2001-lecture-chapter3-pdf#section-61].
*   A **plane in $\mathbb{R}^n$** is a set $P = \{ \mathbf{x} + \mathbf{w} \mid \mathbf{w} \in \text{span}\{\mathbf{u}, \mathbf{v}\} \}$, where $\mathbf{u}, \mathbf{v}$ are nonzero non-multiples of each other, and $\mathbf{x} \in \mathbb{R}^n$ is a point on the plane [source:ma2001-lecture-chapter3-pdf#section-61].
*   More generally, a **$k$-plane in $\mathbb{R}^n$** is a set $Q = \{ \mathbf{x} + \mathbf{w} \mid \mathbf{w} \in \text{span}\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_r\} \}$, where $k$ is the "dimension" of the span [source:ma2001-lecture-chapter3-pdf#section-62].

---

### Subspaces

The concept of a linear span demonstrates that a set of vectors can form a "smaller space" within $\mathbb{R}^n$ that behaves similarly to $\mathbb{R}^n$ itself (e.g., lines or planes through the origin) [source:ma2001-lecture-chapter3-pdf#section-64]. This leads to the formal definition of a subspace.

#### Definition of a Subspace
Let $V$ be a subset of $\mathbb{R}^n$. $V$ is called a **subspace** of $\mathbb{R}^n$ if $V = \text{span}(S)$ for some set of vectors $S = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k\}$ in $\mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-65].
We say that $V$ is a subspace spanned by $S$ (or by $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k$), and conversely, $S$ spans $V$ [source:ma2001-lecture-chapter3-pdf#section-65].

#### Trivial Subspaces
There are two immediate examples of subspaces:
1.  **Zero Space**: The set $\{\mathbf{0}\} = \text{span}\{\mathbf{0}\}$ (containing only the zero vector) is a subspace of $\mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-66].
2.  **$\mathbb{R}^n$ itself**: The entire Euclidean $n$-space $\mathbb{R}^n$ is a subspace of $\mathbb{R}^n$. This is because $\mathbb{R}^n = \text{span}\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\}$, where $\mathbf{e}_i$ are the standard unit vectors (e.g., $(1,0,\dots,0)$) [source:ma2001-lecture-chapter3-pdf#section-66]. Any vector $\mathbf{u} = (u_1, \dots, u_n) \in \mathbb{R}^n$ can be written as $u_1\mathbf{e}_1 + \dots + u_n\mathbf{e}_n$ [source:ma2001-lecture-chapter3-pdf#section-66].

**Examples of Subspaces**:
*   $V_1 = \{ (a + 4b, a) \mid a, b \in \mathbb{R} \} \subseteq \mathbb{R}^2$. This can be written as $V_1 = \text{span}\{ (1, 1), (4, 0) \}$, so $V_1$ is a subspace of $\mathbb{R}^2$ [source:ma2001-lecture-chapter3-pdf#section-67]. In fact, $V_1 = \mathbb{R}^2$.
*   $V_2 = \{ (x, y, z) \mid x + y - z = 0 \} \subseteq \mathbb{R}^3$. The general solution to $x + y - z = 0$ is $(x, y, z) = (-s + t, s, t) = s(-1, 1, 0) + t(1, 0, 1)$ for arbitrary parameters $s, t$ [source:ma2001-lecture-chapter3-pdf#section-67]. Thus, $V_2 = \text{span}\{ (-1, 1, 0), (1, 0, 1) \}$, meaning $V_2$ is a subspace of $\mathbb{R}^3$ (geometrically, a plane containing the origin) [source:ma2001-lecture-chapter3-pdf#section-67].

#### How to Determine if a Subset is a Subspace
A subset $V$ of $\mathbb{R}^n$ is a subspace if all vectors in $V$ can be written as a linear combination $c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k$, where $c_i$ are arbitrary parameters and $\mathbf{u}_i$ are constant vectors [source:ma2001-lecture-chapter3-pdf#section-68].

To show a set $W$ is *not* a subspace, it's often easier to show it fails to satisfy certain properties, rather than showing it *cannot* be written as a span [source:ma2001-lecture-chapter3-pdf#section-69]. From the basic properties of linear spans, a subspace $V$ must satisfy:
1.  $\mathbf{0} \in V$ (it must contain the zero vector) [source:ma2001-lecture-chapter3-pdf#section-70].
2.  For any $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_r \in V$ and $c_1, \dots, c_r \in \mathbb{R}$, their linear combination $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_r\mathbf{v}_r \in V$. This implies that $V$ is closed under vector addition (take $c_1=c_2=1, r=2$) and scalar multiplication (take $r=1$) [source:ma2001-lecture-chapter3-pdf#section-70].

Therefore, a subset $W$ is *not* a subspace if:
*   $W$ does not contain the zero vector [source:ma2001-lecture-chapter3-pdf#section-70].
*   There exists $\mathbf{v} \in W$ and $c \in \mathbb{R}$ such that $c\mathbf{v} \notin W$ (not closed under scalar multiplication) [source:ma2001-lecture-chapter3-pdf#section-70].
*   There exist $\mathbf{u}, \mathbf{v} \in W$ such that $\mathbf{u} + \mathbf{v} \notin W$ (not closed under vector addition) [source:ma2001-lecture-chapter3-pdf#section-70].

**Examples of Subsets that are NOT Subspaces**:
*   $V_3 = \{ (1, a) \mid a \in \mathbb{R} \} \subseteq \mathbb{R}^2$. This set does not contain the zero vector $(0,0)$, as $(0,0) \neq (1,a)$ for any $a \in \mathbb{R}$ [source:ma2001-lecture-chapter3-pdf#section-71]. Hence, $V_3$ is not a subspace of $\mathbb{R}^2$.
*   $V_4 = \{ (x, y, z) \mid x^2 \le y^2 \le z^2 \} \subseteq \mathbb{R}^3$. While $(1,1,2) \in V_4$ and $(1,1,-2) \in V_4$, their sum $(1,1,2) + (1,1,-2) = (2,2,0)$. For $(2,2,0)$, $x^2 = 4, y^2 = 4, z^2 = 0$. Since $4 \not\le 0$, $(2,2,0) \notin V_4$. Thus, $V_4$ is not closed under addition, and therefore not a subspace [source:ma2001-lecture-chapter3-pdf#section-71].

#### Geometrical Interpretation of Subspaces
*   **In $\mathbb{R}^2$**: All subspaces are:
    1.  The zero space $\{ (0, 0) \}$
    2.  Lines through the origin
    3.  $\mathbb{R}^2$ itself
    These correspond to dimensions 0, 1, and 2 respectively. [source:ma2001-lecture-chapter3-pdf#section-72]
*   **In $\mathbb{R}^3$**: All subspaces are:
    1.  The zero space $\{ (0, 0, 0) \}$
    2.  Lines through the origin
    3.  Planes containing the origin
    4.  $\mathbb{R}^3$ itself
    These correspond to dimensions 0, 1, 2, and 3 respectively. [source:ma2001-lecture-chapter3-pdf#section-72]

#### Solution Spaces of Homogeneous Linear Systems
The solution set of a homogeneous system of linear equations in $n$ variables is always a subspace of $\mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-73].
**Proof Idea**:
If a homogeneous system $A\mathbf{x}=\mathbf{0}$ has only the trivial solution, its solution set is $\{\mathbf{0}\}$, which is the zero space (a subspace).
If it has infinitely many solutions, the general solution can be written as $\mathbf{x} = t_1\mathbf{u}_1 + t_2\mathbf{u}_2 + \dots + t_k\mathbf{u}_k$, where $t_i$ are arbitrary parameters and $\mathbf{u}_i$ are fixed vectors [source:ma2001-lecture-chapter3-pdf#section-75]. This form is precisely the definition of a linear span: $\text{span}\{\mathbf{u}_1, \dots, \mathbf{u}_k\}$, which is a subspace of $\mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-75].

**Example**:
The linear system:
$x - 2y + 3z = 0$
$2x - 4y + 6z = 0$
$3x - 6y + 9z = 0$
has a general solution $(x, y, z) = (2s - 3t, s, t) = s(2, 1, 0) + t(-3, 0, 1)$, where $s, t$ are arbitrary parameters [source:ma2001-lecture-chapter3-pdf#section-76]. The solution set is $\text{span}\{ (2, 1, 0), (-3, 0, 1) \}$, which is a plane in $\mathbb{R}^3$ containing the origin [source:ma2001-lecture-chapter3-pdf#section-76].

#### Alternative Definition of a Subspace
An equivalent definition of a subspace, often used in abstract linear algebra, is:
A non-empty subset $V$ of $\mathbb{R}^n$ is called a **subspace** of $\mathbb{R}^n$ if and only if for all $\mathbf{u}, \mathbf{v} \in V$ and $c, d \in \mathbb{R}$, the linear combination $c\mathbf{u} + d\mathbf{v} \in V$ [source:ma2001-lecture-chapter3-pdf#section-79]. This means the set is closed under vector addition and scalar multiplication.

This alternative definition provides a neater way to prove certain properties. For instance, to prove that the solution set of a homogeneous system $A\mathbf{x}=\mathbf{0}$ is a subspace:
1.  **Non-empty**: $\mathbf{x}=\mathbf{0}$ is always a solution to $A\mathbf{x}=\mathbf{0}$, so $\mathbf{0} \in V$, making $V$ non-empty [source:ma2001-lecture-chapter3-pdf#section-80].
2.  **Closure under linear combinations**: Let $\mathbf{u}, \mathbf{v} \in V$. This means $A\mathbf{u}=\mathbf{0}$ and $A\mathbf{v}=\mathbf{0}$. For any $c, d \in \mathbb{R}$, consider the linear combination $c\mathbf{u} + d\mathbf{v}$.
    $A(c\mathbf{u} + d\mathbf{v}) = A(c\mathbf{u}) + A(d\mathbf{v}) = c(A\mathbf{u}) + d(A\mathbf{v}) = c\mathbf{0} + d\mathbf{0} = \mathbf{0}$ [source:ma2001-lecture-chapter3-pdf#section-80].
    Since $A(c\mathbf{u} + d\mathbf{v}) = \mathbf{0}$, $c\mathbf{u} + d\mathbf{v}$ is also a solution, meaning $c\mathbf{u} + d\mathbf{v} \in V$.
Thus, $V$ is a subspace of $\mathbb{R}^n$ [source:ma2001-lecture-chapter3-pdf#section-80].

---
page_id: "y1s1-ma2001-linear-independence-bases"
title: "Linear Independence and Bases"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Criteria for linear independence of vectors, definition of a basis for a vector space, and methods for finding a basis."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
  - "y1s1-cs1231s-lecture-03-predicates-quantifiers"
source_refs:
  - "ma2001-lecture-chapter3-pdf#section-3"
  - "ma2001-tutorial-tutorial6-pdf#section-1"
  - "ma2001-lab-lab3-pdf#section-2"
  - "ma2001-cheatsheet-cheatsheet-pdf#section-2"
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
  - "independent"
source_count: 4
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Linear Independence and Bases

This page discusses the concepts of linear independence and dependence, defines a basis for a vector space, and explores the dimension of vector spaces and subspaces, including methods to find a basis and determine dimension. It also introduces coordinate systems relative to a basis and transition matrices.

### 1. Linear Independence

The concept of linear independence is crucial for identifying "redundant vectors" within a set, which are vectors that can be expressed as linear combinations of others in the set [source: ma2001-lecture-chapter3-pdf#section-3].

#### 1.1. Definition of Linear Independence and Dependence

Let $S = \{u_1, u_2, \dots, u_k\}$ be a set of vectors in $\mathbb{R}^n$. Consider the vector equation:
$c_1u_1 + c_2u_2 + \dots + c_ku_k = \mathbf{0}$ (\*) [source: ma2001-lecture-chapter3-pdf#section-3]

This equation always has the **trivial solution** where $c_1 = 0, c_2 = 0, \dots, c_k = 0$ [source: ma2001-lecture-chapter3-pdf#section-3].

*   **Linearly Independent Set:** The set $S$ is called **linearly independent**, and the vectors $u_1, u_2, \dots, u_k$ are said to be **linearly independent**, if the vector equation (\*) has *only* the trivial solution [source: ma2001-lecture-chapter3-pdf#section-3].
*   **Linearly Dependent Set:** The set $S$ is called **linearly dependent**, and the vectors $u_1, u_2, \dots, u_k$ are said to be **linearly dependent**, if the vector equation (\*) has *non-trivial solutions*. This means there exist real numbers $a_1, a_2, \dots, a_k$, not all of them zero, such that $a_1u_1 + a_2u_2 + \dots + a_ku_k = \mathbf{0}$ [source: ma2001-lecture-chapter3-pdf#section-3].

To check for linear independence, you can form a homogeneous linear system by setting the linear combination equal to the zero vector. If the system has only the trivial solution, the vectors are linearly independent. If there are infinitely many solutions, they are linearly dependent [source: ma2001-lecture-chapter3-pdf#section-3]. MATLAB's `rref` command can be used to solve such systems by checking for non-pivot columns (which indicate arbitrary parameters and thus non-trivial solutions) [source: ma2001-lab-lab3-pdf#section-3].

**Example 1: Determining Linear Dependence**
Determine if $S_1 = \{(2,2,2), (0,0,3), (0,1,1)\}$ is linearly independent in $\mathbb{R}^3$.
To check, we set up the equation $c_1(2,2,2) + c_2(0,0,3) + c_3(0,1,1) = (0,0,0)$.
This leads to the system:
$2c_1 = 0$
$2c_1 + c_3 = 0$
$2c_1 + 3c_2 + c_3 = 0$
Solving this system yields $c_1=0$, $c_3=0$, and $3c_2=0 \implies c_2=0$. Since only the trivial solution exists, $S_1$ is linearly independent [source: ma2001-tutorial-tutorial6-pdf#section-1].

**Example 2: Determining Linear Dependence using Gaussian Elimination**
Determine whether the vectors $u_1=(1, -2, 3)$, $u_2=(5, 6, -1)$, $u_3=(3, 2, 1)$ are linearly independent.
Solution: Set up the vector equation $c_1u_1 + c_2u_2 + c_3u_3 = \mathbf{0}$:
$c_1(1, -2, 3) + c_2(5, 6, -1) + c_3(3, 2, 1) = (0, 0, 0)$
This leads to the system:
$c_1 + 5c_2 + 3c_3 = 0$
$-2c_1 + 6c_2 + 2c_3 = 0$
$3c_1 - c_2 + c_3 = 0$
By Gaussian elimination, it is found that there are infinitely many solutions (i.e., non-trivial solutions). Therefore, the vectors are linearly dependent [source: ma2001-lecture-chapter3-pdf#section-3].

#### 1.2. Special Cases of Linear Dependence

*   **Single Vector:** A set $S = \{u\}$ is linearly dependent if and only if $u = \mathbf{0}$ [source: ma2001-lecture-chapter3-pdf#section-3]. If $u \ne \mathbf{0}$, then $a u = \mathbf{0}$ implies $a=0$, so it's linearly independent.
*   **Two Vectors:** A set $S = \{u, v\}$ is linearly dependent if and only if one vector is a scalar multiple of the other (i.e., they are parallel) [source: ma2001-lecture-chapter3-pdf#section-3].
*   **Set Containing the Zero Vector:** If a set $S = \{u_1, u_2, \dots, u_k\}$ contains the zero vector, then $S$ is linearly dependent. For example, if $u_i = \mathbf{0}$, we can choose $c_i=1$ and all other $c_j=0$ to form a non-trivial solution to $c_1u_1 + \dots + c_ku_k = \mathbf{0}$ [source: ma2001-lecture-chapter3-pdf#section-3].

#### 1.3. Relationship Between Linear Dependence and Linear Combinations

For a set $S = \{u_1, u_2, \dots, u_k\} \subseteq \mathbb{R}^n$ where $k \ge 2$:
*   $S$ is linearly dependent if and only if at least one vector $u_i \in S$ can be written as a linear combination of the other vectors in $S$ [source: ma2001-lecture-chapter3-pdf#section-3]. This $u_i$ is considered a "redundant vector" [source: ma2001-lecture-chapter3-pdf#section-3].
*   $S$ is linearly independent if and only if no vector in $S$ can be written as a linear combination of the other vectors in $S$ [source: ma2001-lecture-chapter3-pdf#section-3]. In this case, there are no redundant vectors [source: ma2001-lecture-chapter3-pdf#section-3].

#### 1.4. Linear Dependence in Higher Dimensions

If a set $S = \{u_1, u_2, \dots, u_k\} \subseteq \mathbb{R}^n$ has more vectors than the dimension of the space (i.e., $k > n$), then $S$ is linearly dependent [source: ma2001-lecture-chapter3-pdf#section-3]. This is because the linear system $c_1u_1 + \dots + c_ku_k = \mathbf{0}$ will have $n$ equations and $k$ unknowns. If $k > n$, there must be non-trivial solutions, implying linear dependence [source: ma2001-lecture-chapter3-pdf#section-3].
*   In $\mathbb{R}^2$, any set of three or more vectors must be linearly dependent [source: ma2001-lecture-chapter3-pdf#section-3].
*   In $\mathbb{R}^3$, any set of four or more vectors must be linearly dependent [source: ma2001-lecture-chapter3-pdf#section-3].

#### 1.5. Geometrical Interpretation of Linear Dependence

*   **Two Vectors:** In $\mathbb{R}^2$ or $\mathbb{R}^3$, two vectors $u, v$ are linearly dependent if and only if they lie on the same line (when placed with their initial points at the origin) [source: ma2001-lecture-chapter3-pdf#section-3]. If they are not on the same line, they are linearly independent.
*   **Three Vectors:** In $\mathbb{R}^3$, three vectors $u, v, w$ are linearly dependent if and only if they lie on the same line or the same plane (when placed with their initial points at the origin) [source: ma2001-lecture-chapter3-pdf#section-3]. If they do not lie on the same plane, they are linearly independent.

#### 1.6. Adding an Independent Vector

Let $u_1, u_2, \dots, u_k$ be linearly independent vectors in $\mathbb{R}^n$. If $u_{k+1}$ is not a linear combination of $u_1, u_2, \dots, u_k$, then the set $\{u_1, u_2, \dots, u_k, u_{k+1}\}$ is linearly independent [source: ma2001-lecture-chapter3-pdf#section-4].

### 2. Bases for Vector Spaces

A **basis** for a vector space is a fundamental concept that provides a minimal set of vectors capable of describing all other vectors in that space uniquely.

#### 2.1. Conventions for Vector Spaces and Subspaces

*   A set $V$ is called a **vector space** if either $V = \mathbb{R}^n$ or $V$ is a [ma2001-vector-spaces-subspaces-intro#subspace|subspace of $\mathbb{R}^n$] [source: ma2001-lecture-chapter3-pdf#section-5].
*   Given a vector space $W$ (which can be $\mathbb{R}^n$ or a subspace of $\mathbb{R}^n$), a set $V$ is called a **subspace of $W$** if $V$ is itself a vector space and $V \subseteq W$ [source: ma2001-lecture-chapter3-pdf#section-5].

#### 2.2. Definition of a Basis

Let $V$ be a vector space and $S = \{u_1, u_2, \dots, u_k\}$ be a subset of $V$. The set $S$ is called a **basis** for $V$ if the following two conditions are met:
1.  $S$ is **linearly independent** [source: ma2001-lecture-chapter3-pdf#section-5, ma2001-cheatsheet-cheatsheet-pdf#section-2].
2.  $S$ **spans $V$** (i.e., $V = \text{span}(S)$) [source: ma2001-lecture-chapter3-pdf#section-5, ma2001-cheatsheet-cheatsheet-pdf#section-2].

**Example:**
Show that $S = \{(1, 2, 1), (2, 9, 0), (3, 3, 4)\}$ is a basis for $\mathbb{R}^3$.
To prove $S$ is a basis, we need to show it is linearly independent and spans $\mathbb{R}^3$.
(a) **Linear Independence:** Set $c_1(1, 2, 1) + c_2(2, 9, 0) + c_3(3, 3, 4) = (0, 0, 0)$. This gives the system:
$c_1 + 2c_2 + 3c_3 = 0$
$2c_1 + 9c_2 + 3c_3 = 0$
$c_1 + 4c_3 = 0$
Solving this system (e.g., using Gaussian elimination), we find that it has only the trivial solution ($c_1=c_2=c_3=0$). Thus, $S$ is linearly independent [source: ma2001-lecture-chapter3-pdf#section-5].
(b) **Spans $\mathbb{R}^3$:** To check if $S$ spans $\mathbb{R}^3$, we can form a matrix with the vectors in $S$ as columns and find its row-echelon form. If the row-echelon form has no zero rows, then the vectors span $\mathbb{R}^3$.
The matrix $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 9 & 3 \\ 1 & 0 & 4 \end{pmatrix}$ can be transformed to a row-echelon form like $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 5 & -3 \\ 0 & 0 & -1/5 \end{pmatrix}$ using Gaussian elimination. Since there are no zero rows, $\text{span}(S) = \mathbb{R}^3$ [source: ma2001-lecture-chapter3-pdf#section-5].
Since $S$ is both linearly independent and spans $\mathbb{R}^3$, $S$ is a basis for $\mathbb{R}^3$ [source: ma2001-lecture-chapter3-pdf#section-5].

#### 2.3. Remarks on Bases

*   A basis for $V$ is a set of the **smallest size** that can span $V$ [source: ma2001-lecture-chapter3-pdf#section-5].
*   For convenience, the **empty set ($\emptyset$)** is defined to be the basis for the **zero space** $\{\mathbf{0}\}$ [source: ma2001-lecture-chapter3-pdf#section-5].
*   Except for the zero space, any vector space has **infinitely many different bases** [source: ma2001-lecture-chapter3-pdf#section-5].

#### 2.4. Coordinate Systems Relative to a Basis

If $S = \{u_1, u_2, \dots, u_k\}$ is a basis for a vector space $V$, then every vector $v \in V$ can be expressed as a linear combination of the basis vectors in **exactly one way**:
$v = c_1u_1 + c_2u_2 + \dots + c_ku_k$ [source: ma2001-lecture-chapter3-pdf#section-5].

The real numbers $c_1, c_2, \dots, c_k$ are called the **coordinates of $v$ relative to the basis $S$**. The vector $(c_1, c_2, \dots, c_k) \in \mathbb{R}^k$ is called the **coordinate vector of $v$ relative to $S$**, denoted as $(v)_S$ [source: ma2001-lecture-chapter3-pdf#section-5]. It's assumed the basis vectors are in a fixed order.

**Example: Finding a Coordinate Vector**
Let $S = \{(1, 2, 1), (2, 9, 0), (3, 3, 4)\}$ be a basis for $\mathbb{R}^3$. Find the coordinate vector of $v = (5, -1, 9)$ relative to $S$.
Solution: We need to find $a, b, c$ such that $a(1, 2, 1) + b(2, 9, 0) + c(3, 3, 4) = (5, -1, 9)$.
Solving this system yields $a = 1, b = -1, c = 2$.
So, $v = 1(1, 2, 1) - 1(2, 9, 0) + 2(3, 3, 4)$.
The coordinate vector of $v$ relative to $S$ is $(v)_S = (1, -1, 2)$ [source: ma2001-lecture-chapter3-pdf#section-5].

#### 2.5. Standard Basis for $\mathbb{R}^n$

The **standard basis** for $\mathbb{R}^n$ is the set $E = \{e_1, e_2, \dots, e_n\}$, where:
$e_1 = (1, 0, \dots, 0)$
$e_2 = (0, 1, 0, \dots, 0)$
$\vdots$
$e_n = (0, \dots, 0, 1)$ [source: ma2001-lecture-chapter3-pdf#section-5].

Any vector $u = (u_1, u_2, \dots, u_n) \in \mathbb{R}^n$ can be written as $u = u_1e_1 + u_2e_2 + \dots + u_ne_n$. This shows that $E$ spans $\mathbb{R}^n$. Furthermore, setting $c_1e_1 + \dots + c_ne_n = \mathbf{0}$ directly implies $c_1=0, \dots, c_n=0$, so $E$ is linearly independent. Thus, $E$ is a basis for $\mathbb{R}^n$ [source: ma2001-lecture-chapter3-pdf#section-5].
For any vector $u \in \mathbb{R}^n$, its coordinate vector relative to the standard basis $E$ is simply itself: $(u)_E = u$ [source: ma2001-lecture-chapter3-pdf#section-5].

#### 2.6. Properties of Coordinate Systems

Let $S$ be a basis for a vector space $V$ with $|S| = k$. Let $v_1, v_2, \dots, v_r \in V$.
1.  The vectors $v_1, v_2, \dots, v_r$ are linearly dependent in $V$ if and only if their coordinate vectors $(v_1)_S, (v_2)_S, \dots, (v_r)_S$ are linearly dependent in $\mathbb{R}^k$. Similarly, they are linearly independent in $V$ if and only if their coordinate vectors are linearly independent in $\mathbb{R}^k$ [source: ma2001-lecture-chapter3-pdf#section-5, ma2001-cheatsheet-cheatsheet-pdf#section-2].
2.  The set $\{v_1, v_2, \dots, v_r\}$ spans $V$ if and only if the set of coordinate vectors $\{(v_1)_S, (v_2)_S, \dots, (v_r)_S\}$ spans $\mathbb{R}^k$ [source: ma2001-lecture-chapter3-pdf#section-5, ma2001-cheatsheet-cheatsheet-pdf#section-2].

### 3. Dimensions of Vector Spaces

The **dimension** of a vector space is a fundamental property that quantifies its "size."

#### 3.1. Definition of Dimension

The **dimension of a vector space $V$**, denoted by $\dim(V)$, is defined as the number of vectors in any basis for $V$ [source: ma2001-lecture-chapter3-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-2].

A key theorem states that every basis for a given vector space $V$ has the same number of vectors [source: ma2001-lecture-chapter3-pdf#section-6].
*   Any subset of $V$ with *more than* $\dim(V)$ vectors is always linearly dependent [source: ma2001-lecture-chapter3-pdf#section-6].
*   Any subset of $V$ with *less than* $\dim(V)$ vectors cannot span $V$ [source: ma2001-lecture-chapter3-pdf#section-6].

The dimension of the **zero space** $\{\mathbf{0}\}$ is defined to be $0$ [source: ma2001-lecture-chapter3-pdf#section-6].
The dimension of $\mathbb{R}^n$ is $n$, i.e., $\dim(\mathbb{R}^n) = n$ [source: ma2001-lecture-chapter3-pdf#section-6].

#### 3.2. Dimensions of Subspaces

*   In $\mathbb{R}^2$, non-zero subspaces are lines through the origin (dimension 1) or $\mathbb{R}^2$ itself (dimension 2) [source: ma2001-lecture-chapter3-pdf#section-6].
*   In $\mathbb{R}^3$, non-zero subspaces are lines through the origin (dimension 1), planes containing the origin (dimension 2), or $\mathbb{R}^3$ itself (dimension 3) [source: ma2001-lecture-chapter3-pdf#section-6].

**Example: Finding a Basis and Dimension for a Subspace**
Find a basis for and determine the dimension of the subspace $W = \{(x, y, z) \mid y = z\}$ of $\mathbb{R}^3$.
Solution: Every vector in $W$ is of the form $(x, y, y) = x(1, 0, 0) + y(0, 1, 1)$.
So, $W = \text{span}\{(1, 0, 0), (0, 1, 1)\}$ [source: ma2001-lecture-chapter3-pdf#section-6].
To check for linear independence of $\{(1, 0, 0), (0, 1, 1)\}$, set $c_1(1, 0, 0) + c_2(0, 1, 1) = (0, 0, 0)$. This implies $c_1 = 0$ and $c_2 = 0$.
Thus, $\{(1, 0, 0), (0, 1, 1)\}$ is linearly independent.
Since the set is linearly independent and spans $W$, it is a basis for $W$.
The dimension of $W$ is 2, because there are two vectors in its basis [source: ma2001-lecture-chapter3-pdf#section-6].

#### 3.3. Basis and Dimension for Solution Spaces of Homogeneous Systems

The solution set of a homogeneous system of linear equations $A\mathbf{x} = \mathbf{0}$ in $n$ variables is a subspace of $\mathbb{R}^n$ [source: ma2001-lecture-chapter3-pdf#section-3]. This is often called the [ma2001-row-column-nullspace#nullspace|nullspace] of $A$.

To find a basis and dimension for the solution space:
1.  Perform Gaussian elimination (or Gauss-Jordan elimination) on the augmented matrix $(A|\mathbf{0})$ to obtain the reduced row-echelon form (RREF) $(R|\mathbf{0})$ [source: ma2001-lecture-chapter3-pdf#section-6, ma2001-lab-lab3-pdf#section-1].
2.  Identify the pivot columns and non-pivot columns in $R$. The variables corresponding to non-pivot columns are **arbitrary parameters** [source: ma2001-lecture-chapter3-pdf#section-6].
3.  Express the general solution in vector form $\mathbf{x} = t_1u_1 + t_2u_2 + \dots + t_ku_k$, where $t_1, \dots, t_k$ are the arbitrary parameters and $u_1, \dots, u_k$ are fixed vectors [source: ma2001-lecture-chapter3-pdf#section-6].
4.  The set $\{u_1, u_2, \dots, u_k\}$ forms a basis for the solution space. These vectors are always linearly independent [source: ma2001-lecture-chapter3-pdf#section-6].
5.  The dimension of the solution space is $k$, which is equal to the number of arbitrary parameters, or equivalently, the number of non-pivot columns in $R$ [source: ma2001-lecture-chapter3-pdf#section-6].

**Example:** Consider the homogeneous linear system:
$2v + 2w - x + z = 0$
$-v - w + 2x - 3y + z = 0$
$x + y + z = 0$
$v + w - 2x - z = 0$
The augmented matrix can be reduced to RREF:
$\begin{pmatrix} 2 & 2 & -1 & 0 & 1 & 0 \\ -1 & -1 & 2 & -3 & 1 & 0 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 1 & 1 & -2 & 0 & -1 & 0 \end{pmatrix} \xrightarrow{\text{Gauss-Jordan Elimination}} \begin{pmatrix} 1 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix}$ [source: ma2001-lecture-chapter3-pdf#section-6]
The variables are $v, w, x, y, z$. The pivot columns correspond to $v, x, y$. The non-pivot columns correspond to $w, z$. Let $w = s$ and $z = t$ (arbitrary parameters).
From RREF:
$v + w + z = 0 \implies v = -s - t$
$x + z = 0 \implies x = -t$
$y = 0$
The general solution in vector form is:
$\begin{pmatrix} v \\ w \\ x \\ y \\ z \end{pmatrix} = \begin{pmatrix} -s-t \\ s \\ -t \\ 0 \\ t \end{pmatrix} = s\begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + t\begin{pmatrix} -1 \\ 0 \\ -1 \\ 0 \\ 1 \end{pmatrix}$ [source: ma2001-lecture-chapter3-pdf#section-6]
Thus, the basis for the solution space is $\{(-1, 1, 0, 0, 0), (-1, 0, -1, 0, 1)\}$, and the dimension of the solution space is 2 [source: ma2001-lecture-chapter3-pdf#section-6].

#### 3.4. Equivalent Conditions for a Basis

Let $V$ be a vector space of dimension $k$, and let $S$ be a subset of $V$. The following statements are equivalent:
1.  $S$ is a basis for $V$ (i.e., $S$ is linearly independent and $S$ spans $V$).
2.  $S$ is linearly independent and $|S| = k$.
3.  $S$ spans $V$ and $|S| = k$. [source: ma2001-lecture-chapter3-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-2]

This theorem is very useful because it means if you know the dimension $k$ of a vector space $V$, you only need to check two out of the three properties (linear independence, spanning $V$, or having $k$ elements) to determine if a set $S$ is a basis for $V$ [source: ma2001-lecture-chapter3-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-2].

**Example:**
Show that $S = \{u_1=(2, 0, -1), u_2=(4, 0, 7), u_3=(-1, 1, 4)\}$ is a basis for $\mathbb{R}^3$.
Solution: We know that $\dim(\mathbb{R}^3) = 3$. The set $S$ has 3 vectors, so $|S|=3=k$.
By Theorem 3.6.7, we only need to show that $S$ is linearly independent (or spans $\mathbb{R}^3$).
Set $c_1u_1 + c_2u_2 + c_3u_3 = \mathbf{0}$:
$c_1(2, 0, -1) + c_2(4, 0, 7) + c_3(-1, 1, 4) = (0, 0, 0)$
This implies $c_1 = 0, c_2 = 0, c_3 = 0$ (the trivial solution).
Therefore, $S$ is linearly independent. Since $S$ is linearly independent and $|S| = \dim(\mathbb{R}^3)$, $S$ is a basis for $\mathbb{R}^3$ [source: ma2001-lecture-chapter3-pdf#section-6].

#### 3.5. Dimension of Subspaces (Theorem 3.6.9)

Let $U$ be a subspace of a vector space $V$. Then $\dim(U) \le \dim(V)$.
Furthermore, if $U \neq V$, then $\dim(U) < \dim(V)$ [source: ma2001-lecture-chapter3-pdf#section-6].

**Example:** Let $V$ be a plane in $\mathbb{R}^3$ containing the origin. $V$ is a vector space of dimension 2. If $U$ is a subspace of $V$ such that $U \neq V$, then $\dim(U) < 2$. This means $U$ is either the zero space (dimension 0) or a line through the origin (dimension 1) [source: ma2001-lecture-chapter3-pdf#section-6].

#### 3.6. Invertible Matrices and Bases (Theorem 3.6.11)

For an $n \times n$ matrix $A$, the following statements are equivalent [source: ma2001-lecture-chapter3-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-3]:
1.  $A$ is invertible.
2.  The linear system $A\mathbf{x} = \mathbf{0}$ has only the trivial solution.
3.  The reduced row-echelon form of $A$ is an identity matrix.
4.  $A$ can be expressed as a product of elementary matrices.
5.  $\det(A) \neq 0$.
6.  The rows of $A$ form a basis for $\mathbb{R}^n$.
7.  The columns of $A$ form a basis for $\mathbb{R}^n$.

This theorem connects many key concepts in linear algebra, showing how invertibility, solution types, RREF, determinants, and properties of rows/columns as bases are all interrelated. The equivalence of 7 and 1 is particularly relevant to bases: the columns of $A$ form a basis for $\mathbb{R}^n$ if and only if $A$ is invertible [source: ma2001-lecture-chapter3-pdf#section-6]. This means the columns are linearly independent and span $\mathbb{R}^n$.

### 4. Transition Matrices

Transition matrices allow us to convert coordinate vectors from one basis to another within the same vector space.

#### 4.1. Column Coordinate Vectors

If $S = \{u_1, u_2, \dots, u_k\}$ is a basis for a vector space $V$ and $v = c_1u_1 + c_2u_2 + \dots + c_ku_k$, the **column vector**
$\begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_k \end{pmatrix}$
is also called the **coordinate vector of $v$ relative to $S$**, and is denoted as $[v]_S$ [source: ma2001-lecture-chapter3-pdf#section-7]. This is distinct from the row vector notation $(v)_S$ previously introduced.

#### 4.2. Definition of Transition Matrix

Let $S = \{u_1, u_2, \dots, u_k\}$ and $T = \{v_1, v_2, \dots, v_k\}$ be two bases for a vector space $V$ [source: ma2001-lecture-chapter3-pdf#section-7].
Any vector $w \in V$ can be expressed as $w = c_1u_1 + c_2u_2 + \dots + c_ku_k$. The coordinate vector of $w$ relative to $S$ is $[w]_S = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_k \end{pmatrix}$ [source: ma2001-lecture-chapter3-pdf#section-7].

Since $T$ is also a basis for $V$, each vector $u_i$ from basis $S$ can be written as a linear combination of the vectors in $T$:
$u_j = a_{1j}v_1 + a_{2j}v_2 + \dots + a_{kj}v_k$
The coordinate vector of $u_j$ relative to $T$ is $[u_j]_T = \begin{pmatrix} a_{1j} \\ a_{2j} \\ \vdots \\ a_{kj} \end{pmatrix}$ [source: ma2001-lecture-chapter3-pdf#section-7].

The **transition matrix from $S$ to $T$**, denoted $P$, is formed by using the coordinate vectors of the $S$-basis vectors relative to $T$ as its columns:
$P = \begin{pmatrix} [u_1]_T & [u_2]_T & \dots & [u_k]_T \end{pmatrix}$ [source: ma2001-lecture-chapter3-pdf#section-7, ma2001-cheatsheet-cheatsheet-pdf#section-2].

This matrix $P$ allows us to convert coordinates from basis $S$ to basis $T$:
$[w]_T = P[w]_S$ [source: ma2001-lecture-chapter3-pdf#section-7, ma2001-cheatsheet-cheatsheet-pdf#section-2].

**Example: Finding a Transition Matrix**
Let $S = \{u_1=(1, 0, -1), u_2=(0, -1, 0), u_3=(1, 0, 2)\}$ and $T = \{v_1=(1, 1, 1), v_2=(1, 1, 0), v_3=(-1, 0, 0)\}$. Both $S$ and $T$ are bases for $\mathbb{R}^3$. Find the transition matrix from $S$ to $T$.
Solution: We need to express each vector in $S$ as a linear combination of vectors in $T$. This means solving $u_j = a_{1j}v_1 + a_{2j}v_2 + a_{3j}v_3$ for $j=1,2,3$.
This is equivalent to solving the augmented matrix $[T|S]$:
$\begin{pmatrix} 1 & 1 & -1 & \mid & 1 & 0 & 1 \\ 1 & 1 & 0 & \mid & 0 & -1 & 0 \\ 1 & 0 & 0 & \mid & -1 & 0 & 2 \end{pmatrix} \xrightarrow{\text{Gauss-Jordan Elimination}} \begin{pmatrix} 1 & 0 & 0 & \mid & -1 & 0 & 2 \\ 0 & 1 & 0 & \mid & 1 & -1 & -2 \\ 0 & 0 & 1 & \mid & -1 & -1 & -1 \end{pmatrix}$ [source: ma2001-lecture-chapter3-pdf#section-7]
The columns on the right side of the reduced matrix are $[u_1]_T, [u_2]_T, [u_3]_T$.
So, $u_1 = -v_1 + v_2 - v_3$, $u_2 = -v_2 - v_3$, $u_3 = 2v_1 - 2v_2 - v_3$.
The transition matrix from $S$ to $T$ is $P = \begin{pmatrix} -1 & 0 & 2 \\ 1 & -1 & -2 \\ -1 & -1 & -1 \end{pmatrix}$ [source: ma2001-lecture-chapter3-pdf#section-7].

#### 4.3. Invertibility of Transition Matrices

Let $S$ and $T$ be two bases for a vector space $V$, and let $P$ be the transition matrix from $S$ to $T$.
1.  $P$ is invertible [source: ma2001-lecture-chapter3-pdf#section-7].
2.  $P^{-1}$ is the transition matrix from $T$ to $S$ [source: ma2001-lecture-chapter3-pdf#section-7, ma2001-cheatsheet-cheatsheet-pdf#section-2].

This means we have the relationship $[w]_S = P^{-1}[w]_T$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-2].

**Example:** Continuing from the previous example, if we have $[w]_S = (2, -1, 2)$, we can find $[w]_T$ using $P$:
$[w]_T = P[w]_S = \begin{pmatrix} -1 & 0 & 2 \\ 1 & -1 & -2 \\ -1 & -1 & -1 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} -2+0+4 \\ 2+1-4 \\ -2+1-2 \end{pmatrix} = \begin{pmatrix} 2 \\ -1 \\ -3 \end{pmatrix}$
So, $[w]_T = (2, -1, -3)$ [source: ma2001-lecture-chapter3-pdf#section-7].

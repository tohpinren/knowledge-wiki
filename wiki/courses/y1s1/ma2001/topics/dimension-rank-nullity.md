---
page_id: "y1s1-ma2001-dimension-rank-nullity"
title: "Dimension, Rank, and Nullity"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Defining the dimension of a vector space, and the concepts of rank and nullity of a matrix with the Rank-Nullity Theorem."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter4-pdf#section-1"
  - "ma2001-tutorial-tutorial7-pdf#section-1"
  - "ma2001-cheatsheet-cheatsheet-pdf#section-3"
topics:
  - "row"
  - "space"
  - "matrix"
  - "column"
  - "rank"
  - "columns"
  - "form"
  - "vectors"
  - "tutorial"
  - "questions"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Dimension, Rank, and Nullity

The dimension of a vector space is a fundamental property that quantifies the number of vectors in any basis for that space. For matrices, specific dimensions are associated with their row space, column space, and nullspace, leading to the concepts of rank and nullity, which are intrinsically linked by the Rank-Nullity Theorem.

---

### Row Spaces and Column Spaces

For an $m \times n$ matrix $A = (a_{ij})$, its rows $r_1, \dots, r_m$ are vectors in $\mathbb{R}^n$, and its columns $c_1, \dots, c_n$ are vectors in $\mathbb{R}^m$ [source:ma2001-lecture-chapter4-pdf#section-1]. Vectors in $\mathbb{R}^n$ can be identified as $1 \times n$ row vector matrices or $n \times 1$ column vector matrices (i.e., $(u_1, u_2, \dots, u_n)$ as `[u1 u2 ... un]` and $(u_1, u_2, \dots, u_n)^T$ as a column matrix) [source:ma2001-lecture-chapter4-pdf#section-1].

The **row space** of $A$ is the subspace of $\mathbb{R}^n$ spanned by its rows, denoted as $\text{span}\{r_1, r_2, \dots, r_m\}$ [source:ma2001-lecture-chapter4-pdf#section-1].
The **column space** of $A$ is the subspace of $\mathbb{R}^m$ spanned by its columns, denoted as $\text{span}\{c_1, c_2, \dots, c_n\}$ [source:ma2001-lecture-chapter4-pdf#section-1].

Notably, the column space of $A$ is equivalent to the row space of $A^T$, and the row space of $A$ is equivalent to the column space of $A^T$ [source:ma2001-lecture-chapter4-pdf#section-1].

#### Row Equivalent Matrices and Row Space

Two matrices, $A$ and $B$, are **row equivalent** if $B$ can be obtained from $A$ through a sequence of [[invertible-elementary-matrices#Elementary Row Operations|elementary row operations]] [source:ma2001-lecture-chapter4-pdf#section-1]. Row equivalence is an equivalence relation, meaning it is reflexive, symmetric, and transitive [source:ma2001-lecture-chapter4-pdf#section-1]. A matrix is row equivalent to its [[gaussian-elimination-rref#Row Echelon Form and Reduced Row Echelon Form|row-echelon form]] [source:ma2001-lecture-chapter4-pdf#section-1].

A key property is that if two matrices $A$ and $B$ are row equivalent, then their row spaces are identical [source:ma2001-lecture-chapter4-pdf#section-1]. This is because elementary row operations preserve the span of the rows [source:ma2001-lecture-chapter4-pdf#section-1].

**Finding a Basis for the Row Space:**
If $R$ is a row-echelon form of matrix $A$, then the nonzero rows of $R$ form a basis for the row space of $R$, and consequently, also for the row space of $A$ [source:ma2001-lecture-chapter4-pdf#section-2]. This is because the nonzero rows of a row-echelon form are linearly independent.

**Example:**
To find a basis for the row space of a matrix $A$, reduce it to its row-echelon form $R$. The nonzero rows of $R$ will constitute the basis.
For example, if a matrix $A$ reduces to $R = \begin{pmatrix} 2 & 2 & -1 & 0 & 1 \\ 0 & 0 & 3/2 & -3 & 3/2 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$, then a basis for the row space of $A$ is $\{(2, 2, -1, 0, 1), (0, 0, 3/2, -3, 3/2), (0, 0, 0, 3, 0)\}$ [source:ma2001-lecture-chapter4-pdf#section-2].

#### Column Spaces and Pivot Columns

Unlike row space, row operations generally *do not* preserve the column space of a matrix [source:ma2001-lecture-chapter4-pdf#section-2]. However, elementary row operations preserve the linear (in)dependence relations among the columns [source:ma2001-lecture-chapter4-pdf#section-2].

**Finding a Basis for the Column Space:**
If $R$ is a row-echelon form of matrix $A$, a basis for the column space of $A$ can be obtained by taking the columns of the *original matrix* $A$ that correspond to the [[gaussian-elimination-rref#Row Echelon Form and Reduced Row Echelon Form|pivot columns]] in $R$ [source:ma2001-lecture-chapter4-pdf#section-2]. The pivot columns in $R$ themselves form a basis for the column space of $R$.

**Example:**
If matrix $A$ reduces to row-echelon form $R$, identify the columns of $R$ that contain leading entries (pivots). Then, select the corresponding columns from the *original matrix A*. These selected columns form a basis for the column space of $A$ [source:ma2001-lecture-chapter4-pdf#section-2].

#### Relationship to Linear Systems

The column space of an $m \times n$ matrix $A$ can be defined as the set of all possible vectors $Au$ where $u \in \mathbb{R}^n$, i.e., $\{Au \mid u \in \mathbb{R}^n\}$ [source:ma2001-lecture-chapter4-pdf#section-2].
A linear system $Ax = b$ is [[linear-systems-solution-types#Consistent and Inconsistent Systems|consistent]] if and only if the vector $b$ lies in the column space of $A$ [source:ma2001-lecture-chapter4-pdf#section-2]. This means $b$ can be expressed as a linear combination of the columns of $A$.

### Ranks

The **rank** of a matrix $A$, denoted $\text{rank}(A)$, is defined as the dimension of its row space (which is equal to the dimension of its column space) [source:ma2001-lecture-chapter4-pdf#section-3, ma2001-cheatsheet-cheatsheet-pdf#section-3].

**Theorem (Dimension of Row and Column Spaces):**
For any matrix $A$, the row space of $A$ and the column space of $A$ have the same dimension [source:ma2001-lecture-chapter4-pdf#section-3]. This dimension is equal to:
*   The number of nonzero rows in any row-echelon form of $A$.
*   The number of leading entries (pivots) in any row-echelon form of $A$.
*   The number of pivot columns in any row-echelon form of $A$.

**Properties of Rank:**
*   $\text{rank}(0) = 0$ [source:ma2001-lecture-chapter4-pdf#section-3, ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   $\text{rank}(I_n) = n$ for an identity matrix $I_n$ [source:ma2001-lecture-chapter4-pdf#section-3, ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   For an $m \times n$ matrix $A$, $\text{rank}(A) \le \min\{m, n\}$ [source:ma2001-lecture-chapter4-pdf#section-3, ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   A matrix $A$ has **full rank** if $\text{rank}(A) = \min\{m, n\}$ [source:ma2001-lecture-chapter4-pdf#section-3].
*   For a square matrix $A$, $A$ is of full rank if and only if $\det(A) \ne 0$ [source:ma2001-lecture-chapter4-pdf#section-3].
*   $\text{rank}(A) = \text{rank}(A^T)$ [source:ma2001-lecture-chapter4-pdf#section-3, ma2001-cheatsheet-cheatsheet-pdf#section-3].

**Rank and Consistency of Linear Systems:**
A linear system $Ax=b$ is consistent if and only if $\text{rank}(A) = \text{rank}([A|b])$, where $[A|b]$ is the augmented matrix [source:ma2001-lecture-chapter4-pdf#section-3]. If $\text{rank}(A) \ne \text{rank}([A|b])$, the system is inconsistent.

**Rank of Product of Matrices:**
For matrices $A$ ($m \times n$) and $B$ ($n \times p$), $\text{rank}(AB) \le \min\{\text{rank}(A), \text{rank}(B)\}$ [source:ma2001-lecture-chapter4-pdf#section-3, ma2001-cheatsheet-cheatsheet-pdf#section-3].

### Nullspaces and Nullities

The **nullspace** of an $m \times n$ matrix $A$, denoted $\text{null}(A)$ or $N(A)$, is the solution space of the homogeneous linear system $Ax = 0$ [source:ma2001-lecture-chapter4-pdf#section-4, ma2001-cheatsheet-cheatsheet-pdf#section-3]. It is a subspace of $\mathbb{R}^n$ [source:ma2001-lecture-chapter4-pdf#section-4]. Vectors in the nullspace are typically written as column vectors [source:ma2001-lecture-chapter4-pdf#section-4].

The **nullity** of $A$, denoted $\text{nullity}(A)$, is the dimension of the nullspace of $A$ [source:ma2001-lecture-chapter4-pdf#section-4, ma2001-cheatsheet-cheatsheet-pdf#section-3]. Since $N(A)$ is a subspace of $\mathbb{R}^n$, $\text{nullity}(A) \le \text{dim}(\mathbb{R}^n) = n$ [source:ma2001-lecture-chapter4-pdf#section-4].

**Finding a Basis for the Nullspace and Nullity:**
To find a basis for the nullspace of $A$, solve the homogeneous system $Ax=0$ by reducing $A$ to its reduced row-echelon form. Express the solution in terms of free variables (parameters). The vectors corresponding to these parameters form a basis for the nullspace, and the number of these vectors is the nullity.

**Example:**
If the general solution to $Ax=0$ is given by $x = s\begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + t\begin{pmatrix} -1 \\ 0 \\ -1 \\ 0 \\ 1 \end{pmatrix}$, where $s, t$ are arbitrary parameters, then a basis for the nullspace is $\{(-1, 1, 0, 0, 0)^T, (-1, 0, -1, 0, 1)^T\}$, and the nullity of $A$ is 2 [source:ma2001-lecture-chapter4-pdf#section-4].

### Dimension Theorem for Matrices (Rank-Nullity Theorem)

The **Dimension Theorem for matrices**, also known as the **Rank-Nullity Theorem**, states that for any $m \times n$ matrix $A$:
$\text{rank}(A) + \text{nullity}(A) = \text{the number of columns of } A$ [source:ma2001-lecture-chapter4-pdf#section-5, ma2001-cheatsheet-cheatsheet-pdf#section-3].

**Proof Outline:**
Let $R$ be a row-echelon form of $A$.
*   $\text{rank}(A) = \text{dim}(\text{column space of } A) = \text{the number of pivot columns in } R$ [source:ma2001-lecture-chapter4-pdf#section-5].
*   $\text{nullity}(A) = \text{dim}(\text{solution space of } Ax=0) = \text{the number of non-pivot columns in } R$ [source:ma2001-lecture-chapter4-pdf#section-5].
Summing these gives:
$\text{rank}(A) + \text{nullity}(A) = (\text{number of pivot columns}) + (\text{number of non-pivot columns}) = \text{total number of columns of } R = \text{total number of columns of } A$ [source:ma2001-lecture-chapter4-pdf#section-5].

This theorem provides a powerful relationship between the column space (which relates to solvability and range) and the nullspace (which relates to uniqueness of solutions) of a matrix.

**Examples using Rank-Nullity Theorem:**
Given an $m \times n$ matrix $A$:
*   If $A$ is a $3 \times 4$ matrix and $\text{rank}(A) = 3$:
    *   $\text{nullity}(A) = 4 - \text{rank}(A) = 4 - 3 = 1$ [source:ma2001-lecture-chapter4-pdf#section-5].
    *   Since $\text{rank}(A) = \text{rank}(A^T)$, $\text{nullity}(A^T) = 3 - \text{rank}(A^T) = 3 - 3 = 0$ [source:ma2001-lecture-chapter4-pdf#section-5].
*   If $A$ is a $7 \times 5$ matrix and $\text{nullity}(A) = 3$:
    *   $\text{rank}(A) = 5 - \text{nullity}(A) = 5 - 3 = 2$ [source:ma2001-lecture-chapter4-pdf#section-5].
    *   $\text{nullity}(A^T) = 7 - \text{rank}(A^T) = 7 - \text{rank}(A) = 7 - 2 = 5$ [source:ma2001-lecture-chapter4-pdf#section-5].

### General Solution of Linear Systems

The structure of the solution set for a consistent linear system $Ax=b$ is closely related to the nullspace of $A$. If $x=v$ is any particular solution to $Ax=b$, then the **general solution set** for $Ax=b$ is given by $\{u+v \mid u \in \text{nullspace of } A\}$ [source:ma2001-lecture-chapter4-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-3].
This means the general solution can be expressed as:
$x = (\text{a general solution for } Ax=0) + (\text{one particular solution to } Ax=b)$ [source:ma2001-lecture-chapter4-pdf#section-6].

A consistent linear system $Ax=b$ has only one unique solution if and only if the nullspace of $A$ is $\{0\}$ (i.e., $\text{nullity}(A) = 0$) [source:ma2001-lecture-chapter4-pdf#section-6]. This implies that if the nullity is greater than zero, there are infinitely many solutions. This concept has parallels in the general solution of ordinary differential equations [source:ma2001-lecture-chapter4-pdf#section-6].

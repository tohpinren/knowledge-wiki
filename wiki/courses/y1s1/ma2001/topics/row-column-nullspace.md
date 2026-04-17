---
page_id: "y1s1-ma2001-row-column-nullspace"
title: "Row Space, Column Space, and Nullspace"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Understanding the row space, column space, and nullspace (kernel) of a matrix, and how to find their bases."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter4-pdf#section-2"
  - "ma2001-lab-lab4-pdf#section-1"
  - "ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2"
topics:
  - "row"
  - "space"
  - "matrix"
  - "column"
  - "rank"
  - "columns"
  - "form"
  - "vectors"
  - "activity"
  - "basis"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Row Space, Column Space, and Nullspace

This page introduces the fundamental vector spaces associated with matrices: the row space, column space, and nullspace (also known as the kernel). Understanding these spaces is crucial for analyzing the properties of matrices, solving linear systems, and comprehending linear transformations.

---

## Row Spaces and Column Spaces

For an $m \times n$ matrix $A$, its rows are vectors in $\mathbb{R}^n$ and its columns are vectors in $\mathbb{R}^m$ [source: ma2001-lecture-chapter4-pdf#section-1].

### Definitions

*   **Row Space:** The row space of an $m \times n$ matrix $A$ is the subspace of $\mathbb{R}^n$ spanned by its rows. If $r_1, \dots, r_m$ are the row vectors of $A$, then the row space of $A$ is $span\{r_1, r_2, \dots, r_m\} \subseteq \mathbb{R}^n$ [source: ma2001-lecture-chapter4-pdf#section-1, ma2001-lecture-chapter4-pdf#section-2].
*   **Column Space:** The column space of an $m \times n$ matrix $A$ is the subspace of $\mathbb{R}^m$ spanned by its columns. If $c_1, \dots, c_n$ are the column vectors of $A$, then the column space of $A$ is $span\{c_1, c_2, \dots, c_n\} \subseteq \mathbb{R}^m$ [source: ma2001-lecture-chapter4-pdf#section-2].

**Relationship with Transpose:** The column space of $A$ is equal to the row space of $A^T$, and the row space of $A$ is equal to the column space of $A^T$ [source: ma2001-lecture-chapter4-pdf#section-1, ma2001-lecture-chapter4-pdf#section-2]. This is due to the identification of row vectors with column vectors and vice versa [source: ma2001-lecture-chapter4-pdf#section-1, ma2001-lecture-chapter4-pdf#section-3].

**Example:**
Let $A = \begin{pmatrix} 2 & -1 & 0 \\ 1 & -1 & 3 \\ -5 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$.
*   The row vectors are $r_1 = [2, -1, 0]$, $r_2 = [1, -1, 3]$, $r_3 = [-5, 1, 0]$, $r_4 = [1, 0, 1]$.
    The row space of $A$ is $span\{r_1, r_2, r_3, r_4\} = \{a(2, -1, 0) + b(1, -1, 3) + c(-5, 1, 0) + d(1, 0, 1) \mid a,b,c,d \in \mathbb{R}\} = \{(2a+b-5c+d, -a-b+c, 3b+d) \mid a,b,c,d \in \mathbb{R}\}$ [source: ma2001-lecture-chapter4-pdf#section-4].
*   The column vectors are $c_1 = \begin{pmatrix} 2 \\ 1 \\ -5 \\ 1 \end{pmatrix}$, $c_2 = \begin{pmatrix} -1 \\ -1 \\ 1 \\ 0 \end{pmatrix}$, $c_3 = \begin{pmatrix} 0 \\ 3 \\ 0 \\ 1 \end{pmatrix}$.
    The column space of $A$ is $span\{c_1, c_2, c_3\} = \{a\begin{pmatrix} 2 \\ 1 \\ -5 \\ 1 \end{pmatrix} + b\begin{pmatrix} -1 \\ -1 \\ 1 \\ 0 \end{pmatrix} + c\begin{pmatrix} 0 \\ 3 \\ 0 \\ 1 \end{pmatrix} \mid a,b,c \in \mathbb{R}\} = \{\begin{pmatrix} 2a-b \\ a-b+3c \\ -5a+b \\ a+c \end{pmatrix} \mid a,b,c \in \mathbb{R}\}$ [source: ma2001-lecture-chapter4-pdf#section-5].

### Row Equivalent Matrices

Two matrices $A$ and $B$ are **row equivalent** if $B$ can be obtained from $A$ through a series of [elementary row operations](ma2001-matrix-operations#elementary-row-operations) [source: ma2001-lecture-chapter4-pdf#section-6]. Row equivalence is an equivalence relation on matrices, meaning it is reflexive, symmetric, and transitive [source: ma2001-lecture-chapter4-pdf#section-6].

A matrix is row equivalent to its [row-echelon form](ma2001-gaussian-elimination-rref#row-echelon-form). Specifically, two matrices are row equivalent if and only if they have the same reduced row-echelon form (RREF) [source: ma2001-lecture-chapter4-pdf#section-7].

**Theorem:** If two matrices $A$ and $B$ are row equivalent, then their row spaces are identical: $Row(A) = Row(B)$ [source: ma2001-lecture-chapter4-pdf#section-8]. Elementary row operations preserve the row space of a matrix [source: ma2001-lecture-chapter4-pdf#section-8, ma2001-lecture-chapter4-pdf#section-9].

**Example:**
$A = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 2 & 4 \\ 1/2 & 1 & 2 \end{pmatrix} \xrightarrow{R_1 \leftrightarrow R_3} \xrightarrow{2R_1} \xrightarrow{R_1 - R_2} D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 4 \\ 0 & 0 & 1 \end{pmatrix}$.
Since $A$ and $D$ are row equivalent, $Row(A) = Row(D)$.
Thus, $span\{(0,0,1), (0,2,4), (1/2,1,2)\} = span\{(1,0,0), (0,2,4), (0,0,1)\}$ [source: ma2001-lecture-chapter4-pdf#section-10].

### Finding a Basis for the Row Space

Let $A$ be a matrix and $R$ be a row-echelon form of $A$. The nonzero rows of $R$ form a basis for the row space of $R$, and thus for the row space of $A$ [source: ma2001-lecture-chapter4-pdf#section-11]. This is because the nonzero rows of a matrix in row-echelon form are linearly independent.

**Steps using MATLAB:**
1.  Input matrix $A$.
2.  Apply the command `rref(A)` to get its reduced row-echelon form.
3.  The nonzero rows of the RREF form a basis for the row space of $A$ [source: ma2001-lab-lab4-pdf#section-2].

**Example:**
$A = \begin{pmatrix} 2 & 2 & -1 & 0 & 1 \\ -1 & -1 & 2 & -3 & 1 \\ 0 & 0 & 1 & 1 & 1 \\ 1 & 1 & -2 & 0 & -1 \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} R = \begin{pmatrix} 2 & 2 & -1 & 0 & 1 \\ 0 & 0 & 3/2 & -3 & 3/2 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$.
The nonzero rows of $R$ are linearly independent and form a basis for $Row(A)$:
$\{(2, 2, -1, 0, 1), (0, 0, 3/2, -3, 3/2), (0, 0, 0, 3, 0)\}$ [source: ma2001-lecture-chapter4-pdf#section-11].

### Finding a Basis for the Column Space

**Warning:** In general, the column space of $A$ is **not** equal to the column space of a row-equivalent matrix $B$ [source: ma2001-lecture-chapter4-pdf#section-12].

**Example:**
$A = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \xrightarrow{R_1 \leftrightarrow R_2} B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
$Col(A) = \{ (0, y)^T \mid y \in \mathbb{R} \}$
$Col(B) = \{ (x, 0)^T \mid x \in \mathbb{R} \}$
Here, $Col(A) \neq Col(B)$ [source: ma2001-lecture-chapter4-pdf#section-12].

Let $A$ be a matrix and $R$ be a row-echelon form of $A$. A basis for the column space of $A$ can be obtained by taking the columns of $A$ that correspond to the pivot columns in $R$ [source: ma2001-lecture-chapter4-pdf#section-13, ma2001-lecture-chapter4-pdf#section-15]. The columns of $A$ corresponding to the pivot columns of $R$ are linearly independent and form a basis for $Col(A)$ [source: ma2001-lecture-chapter4-pdf#section-14, ma2001-lecture-chapter4-pdf#section-15].

**Steps using MATLAB:**
1.  Input matrix $A$.
2.  Apply the command `rref(A)` to get its reduced row-echelon form.
3.  Identify the pivot columns in the RREF.
4.  The columns from the original matrix $A$ that correspond to these pivot columns form a basis for the column space of $A$ [source: ma2001-lab-lab4-pdf#section-2].

**Example:**
Using the same matrix $A$ as before:
$A = \begin{pmatrix} 2 & 2 & -1 & 0 & 1 \\ -1 & -1 & 2 & -3 & 1 \\ 0 & 0 & 1 & 1 & 1 \\ 1 & 1 & -2 & 0 & -1 \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} R = \begin{pmatrix} \mathbf{2} & 2 & -1 & 0 & 1 \\ 0 & 0 & \mathbf{3/2} & -3 & 3/2 \\ 0 & 0 & 0 & \mathbf{3} & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$.
The pivot columns in $R$ are the 1st, 3rd, and 4th columns.
Therefore, the corresponding columns from $A$ form a basis for $Col(A)$:
$\left\{\begin{pmatrix} 2 \\ -1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ 2 \\ 1 \\ -2 \end{pmatrix}, \begin{pmatrix} 0 \\ -3 \\ 1 \\ 0 \end{pmatrix}\right\}$ [source: ma2001-lecture-chapter4-pdf#section-15].

### Finding a Basis for a Linear Span (General Method)

Given a set of vectors $W = \{u_1, u_2, \dots, u_k\}$, to find a basis for $span(W)$:

**Method 1: Using Row Vectors (Row Space Method)** [source: ma2001-lecture-chapter4-pdf#section-16]
1.  Form a matrix $A$ where the given vectors are its **row vectors**.
2.  Reduce $A$ to its row-echelon form $R$.
3.  The nonzero rows of $R$ form a basis for $span(W)$.

**Example:** Find a basis for $W = span\{u_1, \dots, u_6\}$ where $u_1=(1,2,2,1)$, $u_2=(3,6,6,3)$, $u_3=(4,9,9,5)$, $u_4=(-2,-1,-1,1)$, $u_5=(5,8,9,4)$, $u_6=(4,2,7,3)$.
Place them as rows of a matrix and perform Gaussian elimination:
$\begin{pmatrix} 1 & 2 & 2 & 1 \\ 3 & 6 & 6 & 3 \\ 4 & 9 & 9 & 5 \\ -2 & -1 & -1 & 1 \\ 5 & 8 & 9 & 4 \\ 4 & 2 & 7 & 3 \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} \begin{pmatrix} 1 & 2 & 2 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$.
A basis for $W$ is $\{(1, 2, 2, 1), (0, 1, 1, 1), (0, 0, 1, 1)\}$ [source: ma2001-lecture-chapter4-pdf#section-16].

**Method 2: Using Column Vectors (Column Space Method)** [source: ma2001-lecture-chapter4-pdf#section-17]
1.  Form a matrix $A$ where the given vectors are its **column vectors**.
2.  Reduce $A$ to its row-echelon form $R$.
3.  Identify the pivot columns in $R$.
4.  The columns from the original matrix $A$ corresponding to these pivot columns form a basis for $span(W)$.

**Example:** Using the same vectors as above, form a matrix with them as columns:
$\begin{pmatrix} 1 & 3 & 4 & -2 & 5 & 4 \\ 2 & 6 & 9 & -1 & 8 & 2 \\ 2 & 6 & 9 & -1 & 9 & 7 \\ 1 & 3 & 5 & 1 & 4 & 3 \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} \begin{pmatrix} \mathbf{1} & 3 & 4 & -2 & 5 & 4 \\ 0 & 0 & \mathbf{1} & 3 & -2 & -6 \\ 0 & 0 & 0 & 0 & \mathbf{1} & 5 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix}$.
The pivot columns are the 1st, 3rd, and 5th columns.
A basis for $W$ is $\{(1, 2, 2, 1)^T, (4, 9, 9, 5)^T, (5, 8, 9, 4)^T\}$ [source: ma2001-lecture-chapter4-pdf#section-17]. Note that the vectors are written as column vectors here.

### Extending a Linearly Independent Set to a Basis

To extend a linearly independent set $S$ to a basis for $\mathbb{R}^n$:
1.  Form a matrix $A$ using the vectors in $S$ as rows.
2.  Reduce $A$ to its row-echelon form $R$.
3.  Identify the non-pivot columns in $R$.
4.  For each non-pivot column, create a vector with a '1' at the position corresponding to that column and '0's elsewhere. These new vectors, when added to the original set $S$, form a basis for $\mathbb{R}^n$.

**Example:** Extend $S = \{(1, 4, -2, 5, 1), (2, 9, -1, 8, 2), (2, 9, -1, 9, 3)\}$ to a basis for $\mathbb{R}^5$.
1.  Form matrix $A$ with $S$ vectors as rows: $A = \begin{pmatrix} 1 & 4 & -2 & 5 & 1 \\ 2 & 9 & -1 & 8 & 2 \\ 2 & 9 & -1 & 9 & 3 \end{pmatrix}$ [source: ma2001-lecture-chapter4-pdf#section-19].
2.  Reduce $A$ to $R$: $A \xrightarrow{\text{Gaussian Elimination}} R = \begin{pmatrix} \mathbf{1} & 4 & -2 & 5 & 1 \\ 0 & \mathbf{1} & 3 & -2 & 0 \\ 0 & 0 & 0 & \mathbf{1} & 1 \end{pmatrix}$ [source: ma2001-lecture-chapter4-pdf#section-20, ma2001-lecture-chapter4-pdf#section-21].
3.  The non-pivot columns are the 3rd and 5th columns [source: ma2001-lecture-chapter4-pdf#section-21].
4.  Create vectors $(0, 0, 1, 0, 0)$ and $(0, 0, 0, 0, 1)$ [source: ma2001-lecture-chapter4-pdf#section-22, ma2001-lecture-chapter4-pdf#section-23].
5.  The extended basis for $\mathbb{R}^5$ is:
    $\{(1, 4, -2, 5, 1), (2, 9, -1, 8, 2), (2, 9, -1, 9, 3), (0, 0, 1, 0, 0), (0, 0, 0, 0, 1)\}$ [source: ma2001-lecture-chapter4-pdf#section-23].

### Column Space and Linear Systems

A linear system $Ax=b$ is **consistent** if and only if the vector $b$ lies in the column space of $A$ [source: ma2001-lecture-chapter4-pdf#section-26, ma2001-lecture-chapter4-pdf#section-27, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-1]. This is because a solution to $Ax=b$ means that $b$ can be written as a linear combination of the column vectors of $A$ [source: ma2001-lecture-chapter4-pdf#section-25, ma2001-lecture-chapter4-pdf#section-26, ma2001-lecture-chapter4-pdf#section-27, ma2001-lecture-chapter4-pdf#section-28, ma2001-lecture-chapter4-pdf#section-29, ma2001-lecture-chapter4-pdf#section-30].
The column space of $A$ can also be defined as the set of all possible vectors $Au$ for $u \in \mathbb{R}^n$, i.e., $Col(A) = \{Au \mid u \in \mathbb{R}^n\}$ [source: ma2001-lecture-chapter4-pdf#section-26, ma2001-lecture-chapter4-pdf#section-28, ma2001-lecture-chapter4-pdf#section-29].

---

## Ranks

The **rank of a matrix** $A$, denoted $rank(A)$, is the dimension of its row space (which is equal to the dimension of its column space) [source: ma2001-lecture-chapter4-pdf#section-32, ma2001-lecture-chapter4-pdf#section-33, ma2001-lecture-chapter4-pdf#section-34].

### Properties of Rank

*   The dimension of the row space of $A$ is equal to the number of nonzero rows in any row-echelon form $R$ of $A$ [source: ma2001-lecture-chapter4-pdf#section-32, ma2001-lecture-chapter4-pdf#section-33].
*   The dimension of the column space of $A$ is equal to the number of pivot columns in any row-echelon form $R$ of $A$ [source: ma2001-lecture-chapter4-pdf#section-32, ma2001-lecture-chapter4-pdf#section-33].
*   Since the number of nonzero rows in a row-echelon form is equal to the number of leading entries, which is also equal to the number of pivot columns, the row space and column space of a matrix always have the same dimension [source: ma2001-lecture-chapter4-pdf#section-32, ma2001-lecture-chapter4-pdf#section-33].

**Further properties:**
*   $rank(0) = 0$ [source: ma2001-lecture-chapter4-pdf#section-34].
*   $rank(I_n) = n$ (for an $n \times n$ identity matrix) [source: ma2001-lecture-chapter4-pdf#section-34].
*   For an $m \times n$ matrix $A$, $rank(A) \leq \min\{m, n\}$ [source: ma2001-lecture-chapter4-pdf#section-34].
*   If $rank(A) = \min\{m, n\}$, then $A$ is said to have **full rank** [source: ma2001-lecture-chapter4-pdf#section-34].
*   A square matrix $A$ is of full rank if and only if $det(A) \neq 0$ [source: ma2001-lecture-chapter4-pdf#section-34].
*   $rank(A) = rank(A^T)$ [source: ma2001-lecture-chapter4-pdf#section-34].

**Example:**
$C = \begin{pmatrix} 2 & 0 & 3 & -1 & 8 \\ 2 & 1 & 1 & -2 & 5 \\ -4 & -3 & 0 & 5 & -7 \end{pmatrix} \xrightarrow{\text{Gaussian Elimination}} \begin{pmatrix} 2 & 0 & 3 & -1 & 8 \\ 0 & 1 & -2 & -1 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$.
*   A basis for the row space of $C$ is $\{(2, 0, 3, -1, 8), (0, 1, -2, -1, -3)\}$ [source: ma2001-lecture-chapter4-pdf#section-33].
*   A basis for the column space of $C$ is $\{(2, 2, -4)^T, (0, 1, -3)^T\}$ (from the original matrix, corresponding to pivot columns 1 and 2) [source: ma2001-lecture-chapter4-pdf#section-33].
*   The dimension of both the row space and column space is 2. Therefore, $rank(C) = 2$ [source: ma2001-lecture-chapter4-pdf#section-33].

**Using MATLAB `rank` command:**
The rank of a matrix $A$ can be directly obtained using the command `rank(A)` [source: ma2001-lab-lab4-pdf#section-2].

### Rank and Linear Systems

A linear system $Ax=b$ is consistent if and only if $rank(A) = rank([A|b])$ (where $[A|b]$ is the augmented matrix) [source: ma2001-lecture-chapter4-pdf#section-35, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-1].

**Example:**
Consider the system $\begin{cases} 2x-y = 1 \\ x-y+3z = 0 \\ -5x+y = 0 \\ x+z = 0 \end{cases}$, which can be written as $A x = b$, where $A = \begin{pmatrix} 2 & -1 & 0 \\ 1 & -1 & 3 \\ -5 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$ and $b = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}$.
The augmented matrix $[A|b]$ is $\begin{pmatrix} 2 & -1 & 0 & 1 \\ 1 & -1 & 3 & 0 \\ -5 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \end{pmatrix}$.
Performing Gaussian elimination on $[A|b]$ yields $\begin{pmatrix} 2 & -1 & 0 & 1 \\ 0 & -1/2 & 3 & -1/2 \\ 0 & 0 & -9 & 4 \\ 0 & 0 & 0 & 7/9 \end{pmatrix}$.
From this, $rank(A) = 3$ (number of pivot columns in $A$'s part of the RREF).
However, $rank([A|b]) = 4$ (as the last row implies $0 = 7/9$, which is inconsistent).
Since $rank(A) \neq rank([A|b])$, the system is inconsistent [source: ma2001-lecture-chapter4-pdf#section-35].

### Ranks of Product of Matrices

For matrices $A$ ($m \times n$) and $B$ ($n \times p$), $rank(AB) \leq \min\{rank(A), rank(B)\}$ [source: ma2001-lecture-chapter4-pdf#section-36].

---

## Nullspaces and Nullities

### Definitions

Let $A$ be an $m \times n$ matrix. The solution space of the homogeneous linear system $Ax=0$ is known as the **nullspace (or kernel) of A**, denoted $Null(A)$ or $Ker(A)$ [source: ma2001-lecture-chapter4-pdf#section-38]. The nullspace is a subspace of $\mathbb{R}^n$ [source: ma2001-lecture-chapter4-pdf#section-38].

The dimension of the nullspace of $A$ is called the **nullity of A**, denoted $nullity(A)$ [source: ma2001-lecture-chapter4-pdf#section-38].
$nullity(A) = dim(Null(A)) \leq dim(\mathbb{R}^n) = n$ [source: ma2001-lecture-chapter4-pdf#section-38].
Vectors in nullspaces, as well as solution sets of linear systems, are typically written as column vectors [source: ma2001-lecture-chapter4-pdf#section-38].

### Finding a Basis for the Nullspace

To find a basis for the nullspace of $A$, solve the homogeneous system $Ax=0$ using Gaussian-Jordan elimination to find the general solution [source: ma2001-lab-lab4-pdf#section-5]. The vectors that span this general solution form a basis for $Null(A)$.

**Steps using MATLAB:**
1.  Input matrix $A$.
2.  Use the command `null(A, 'r')` to obtain a basis for the nullspace of $A$. The columns of the resulting matrix $N$ give a basis for $Null(A)$ [source: ma2001-lab-lab4-pdf#section-5].

**Example:** Find a basis for the nullspace of $A = \begin{pmatrix} 2 & 2 & -1 & 0 & 1 \\ -1 & -1 & 2 & -3 & 1 \\ 0 & 0 & 1 & 1 & 1 \\ 1 & 1 & -2 & 0 & -1 \end{pmatrix}$.
First, augment $A$ with a column of zeros and reduce to RREF:
$\begin{pmatrix} 2 & 2 & -1 & 0 & 1 & 0 \\ -1 & -1 & 2 & -3 & 1 & 0 \\ 0 & 0 & 1 & 1 & 1 & 0 \\ 1 & 1 & -2 & 0 & -1 & 0 \end{pmatrix} \xrightarrow{\text{Gauss-Jordan Elimination}} \begin{pmatrix} 1 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix}$.
From the RREF, the system $Ax=0$ is equivalent to:
$x_1 + x_2 + x_5 = 0 \implies x_1 = -x_2 - x_5$
$x_3 + x_5 = 0 \implies x_3 = -x_5$
$x_4 = 0$
Let $x_2 = s$ and $x_5 = t$ (free variables).
The general solution $x = \begin{pmatrix} -s-t \\ s \\ -t \\ 0 \\ t \end{pmatrix} = s\begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + t\begin{pmatrix} -1 \\ 0 \\ -1 \\ 0 \\ 1 \end{pmatrix}$.
A basis for $Null(A)$ is $\left\{\begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ -1 \\ 0 \\ 1 \end{pmatrix}\right\}$.
Thus, $nullity(A) = 2$ [source: ma2001-lecture-chapter4-pdf#section-39, ma2001-lecture-chapter4-pdf#section-40].

### Dimension Theorem for Matrices

Let $A$ be an $m \times n$ matrix. Then:
$rank(A) + nullity(A) = \text{number of columns of } A$ [source: ma2001-lecture-chapter4-pdf#section-43].

**Proof Sketch:**
*   $rank(A)$ is the dimension of the column space, which equals the number of pivot columns in the RREF of $A$ [source: ma2001-lecture-chapter4-pdf#section-44].
*   $nullity(A)$ is the dimension of the solution space of $Ax=0$, which equals the number of non-pivot columns (free variables) in the RREF of $A$ [source: ma2001-lecture-chapter4-pdf#section-44].
*   The total number of columns in $A$ (or its RREF) is the sum of pivot columns and non-pivot columns.
*   Therefore, $rank(A) + nullity(A) = (\text{number of pivot columns}) + (\text{number of non-pivot columns}) = \text{number of columns of } A$ [source: ma2001-lecture-chapter4-pdf#section-44].

**Examples:**
*   If $A$ is a $3 \times 4$ matrix and $rank(A) = 3$:
    *   $nullity(A) = 4 - rank(A) = 4 - 3 = 1$.
    *   $nullity(A^T) = 3 - rank(A^T) = 3 - rank(A) = 3 - 3 = 0$ (since $rank(A) = rank(A^T)$) [source: ma2001-lecture-chapter4-pdf#section-45].
*   If $A$ is a $7 \times 5$ matrix and $nullity(A) = 3$:
    *   $rank(A) = 5 - nullity(A) = 5 - 3 = 2$.
    *   $nullity(A^T) = 7 - rank(A^T) = 7 - rank(A) = 7 - 2 = 5$ [source: ma2001-lecture-chapter4-pdf#section-45].

### Nullspace and General Solutions of Linear Systems

Suppose $x=v$ is a particular solution to a linear system $Ax=b$. Then the general solution set for $Ax=b$ is given by $\{u+v \mid u \in Null(A)\}$, where $Null(A)$ is the nullspace of $A$ (i.e., the solution space for $Ax=0$) [source: ma2001-lecture-chapter4-pdf#section-46, ma2001-lecture-chapter4-pdf#section-47, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-1].
This means the general solution $x$ for $Ax=b$ can be expressed as:
$x = (\text{a general solution for } Ax=0) + (\text{one particular solution to } Ax=b)$ [source: ma2001-lecture-chapter4-pdf#section-46].

A consistent linear system $Ax=b$ has only one solution if and only if the nullspace of $A$ is $\{0\}$ (i.e., $nullity(A)=0$) [source: ma2001-lecture-chapter4-pdf#section-46].

This concept is analogous to solving ordinary differential equations, where the general solution is also given by the sum of the complementary solution (solving the homogeneous equation) and a particular solution [source: ma2001-lecture-chapter4-pdf#section-51, ma2001-lecture-chapter4-pdf#section-52].

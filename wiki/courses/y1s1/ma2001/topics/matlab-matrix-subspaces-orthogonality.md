---
page_id: "y1s1-ma2001-matlab-matrix-subspaces-orthogonality"
title: "MATLAB for Matrix Subspaces and Orthogonality"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Utilizing MATLAB commands to explore row space, column space, nullspace, dot products, and orthogonal sets."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lab-lab4-pdf#section-1"
  - "ma2001-lab-lab4sol-pdf#section-1"
topics:
  - "activity"
  - "basis"
  - "using"
  - "vectors"
  - "space"
  - "matrix"
  - "finding"
  - "command"
  - "columns"
  - "form"
source_count: 2
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# MATLAB for Matrix Subspaces and Orthogonality

This page introduces how to use MATLAB commands to solve problems related to matrix subspaces (row space, column space, nullspace) and orthogonal sets (dot product, norm, orthonormal bases) [source:ma2001-lab-lab4-pdf#section-1]. New MATLAB commands covered include `rank`, `null`, `norm`, and `orth` [source:ma2001-lab-lab4-pdf#section-1].

---

## Row Space and Column Space

### Finding a Basis for the Row Space

To find a basis for the row space of a matrix (e.g., matrix A or B), you can use the `rref()` command in MATLAB [source:ma2001-lab-lab4-pdf#section-1]. The non-zero rows of the resulting reduced row-echelon form constitute the basis for the row space [source:ma2001-lab-lab4sol-pdf#section-1].

**Example: Matrix A** [source:ma2001-lab-lab4-pdf#section-1]
Given matrix A:
$$
A = \begin{pmatrix}
1 & 4 & 1 & 2 & 8 \\
2 & 8 & 2 & 3 & 12 \\
3 & 12 & 3 & -1 & -4 \\
4 & 16 & -1 & -4 & -16
\end{pmatrix}
$$
1.  Input matrix A into MATLAB.
    ```matlab
    A = [1 4 1 2 8; 2 8 2 3 12; 3 12 3 -1 -4; 4 16 -1 -4 -16];
    ```
2.  Apply the `rref(A)` command.
    ```matlab
    rref(A)
    ```
    The reduced row-echelon form will show non-zero rows that form the basis.
    A basis for the row space of A is:
    $\{(1, 4, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 4)\}$ [source:ma2001-lab-lab4sol-pdf#section-1].

**Example: Matrix B** [source:ma2001-lab-lab4-pdf#section-1]
Given matrix B:
$$
B = \begin{pmatrix}
1 & 1 & 1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 & 1 & -1 \\
1 & 3 & 4 & 8 & 16 & 32 \\
4 & 1 & 7 & 7 & 19 & 31
\end{pmatrix}
$$
1.  Input matrix B into MATLAB.
    ```matlab
    B = [1 1 1 1 1 1; 1 -1 1 -1 1 -1; 1 3 4 8 16 32; 4 1 7 7 19 31];
    ```
2.  Apply the `rref(B)` command.
    ```matlab
    rref(B)
    ```
    A basis for the row space of B is:
    $\{(1,0,0,0,-4,-8), (0,1,0,0,0,0), (0,0,1,0,5,8), (0,0,0,1,0,1)\}$ [source:ma2001-lab-lab4sol-pdf#section-1].

### Finding a Basis for the Column Space

To find a basis for the column space of a matrix:
1.  Obtain the reduced row-echelon form of the matrix using `rref()` [source:ma2001-lab-lab4-pdf#section-2].
2.  Identify the pivot columns in the reduced row-echelon form [source:ma2001-lab-lab4-pdf#section-2].
3.  The basis for the column space consists of the *corresponding columns from the original matrix* [source:ma2001-lab-lab4-pdf#section-2].

**Example: Matrix A** [source:ma2001-lab-lab4-pdf#section-2]
From `rref(A)`, the pivot columns are 1, 3, and 4 [source:ma2001-lab-lab4sol-pdf#section-1].
A basis for the column space of A is given by columns 1, 3, and 4 of the original matrix A:
$$
\left\{ \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \\ 3 \\ -1 \end{pmatrix}, \begin{pmatrix} 2 \\ 3 \\ -1 \\ -4 \end{pmatrix} \right\}
$$ [source:ma2001-lab-lab4sol-pdf#section-1]

**Example: Matrix B** [source:ma2001-lab-lab4-pdf#section-2]
From `rref(B)`, the pivot columns are 1, 2, 3, and 4 [source:ma2001-lab-lab4sol-pdf#section-2].
A basis for the column space of B is given by columns 1, 2, 3, and 4 of the original matrix B:
$$
\left\{ \begin{pmatrix} 1 \\ 1 \\ 1 \\ 4 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ 4 \\ 7 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 8 \\ 7 \end{pmatrix} \right\}
$$ [source:ma2001-lab-lab4sol-pdf#section-2]

### Finding the Rank of a Matrix

The rank of a matrix is the dimension of its row space (which is equal to the dimension of its column space) [source:ma2001-lab-lab4-pdf#section-2].
In MATLAB, the rank can be determined in two ways:
1.  **From RREF**: Count the number of non-zero rows (or pivot columns) in the reduced row-echelon form [source:ma2001-lab-lab4-pdf#section-2].
    *   For matrix A, rank(A) = 3 [source:ma2001-lab-lab4sol-pdf#section-2].
    *   For matrix B, rank(B) = 4 [source:ma2001-lab-lab4sol-pdf#section-2].
2.  **Using `rank()` command**: MATLAB provides a direct command `rank(A)` [source:ma2001-lab-lab4-pdf#section-2].
    ```matlab
    rank(A) % Returns 3
    rank(B) % Returns 4
    ```

**Invertible Matrices and Rank** [source:ma2001-lab-lab4-pdf#section-2]
An $n \times n$ matrix is invertible if and only if its rank is equal to $n$ [source:ma2001-lab-lab4-pdf#section-2, ma2001-lab-lab4sol-pdf#section-2].

**Example: Identity Matrix** [source:ma2001-lab-lab4-pdf#section-2]
The $n \times n$ identity matrix can be generated using `eye(n)`. For a $4 \times 4$ identity matrix:
```matlab
I = eye(4);
rank(I) % Returns 4
```
Thus, a $4 \times 4$ identity matrix has a rank of 4 [source:ma2001-lab-lab4sol-pdf#section-2].

**Example: Matrix C** [source:ma2001-lab-lab4-pdf#section-2]
Given matrix C:
$$
C = \begin{pmatrix}
1 & 0 & 2 & 0 & 3 \\
1 & 1 & 0 & 2 & 2 \\
1 & 2 & 3 & 4 & 1 \\
1 & 1 & 1 & 1 & 1 \\
0 & 1 & 2 & 1 & 0
\end{pmatrix}
$$
1.  Input matrix C into MATLAB.
    ```matlab
    C = [1 0 2 0 3; 1 1 0 2 2; 1 2 3 4 1; 1 1 1 1 1; 0 1 2 1 0];
    ```
2.  Find its rank using `rank(C)`.
    ```matlab
    rank(C) % Returns 5
    ```
Since C is a $5 \times 5$ matrix and its rank is 5, C is an invertible matrix [source:ma2001-lab-lab4sol-pdf#section-2]. This can also be verified by checking if `rref(C)` is the identity matrix or if `det(C)` is non-zero.

---

## Bases for Vector Spaces (Revision)

### Finding a Basis for a Linear Span

To find a basis for a vector space $V = \text{span}(S)$ where $S = \{u_1, u_2, \dots, u_k\}$ is a set of vectors:
1.  Form a matrix D using the vectors $u_1, \dots, u_k$ as its *columns* [source:ma2001-lab-lab4-pdf#section-3]. This means $V$ is the column space of D [source:ma2001-lab-lab4-pdf#section-3].
2.  Apply `rref()` to D. Identify the pivot columns in the reduced row-echelon form.
3.  The corresponding columns from the *original matrix D* form a basis for $V$ [source:ma2001-lab-lab4-pdf#section-4].

**Example:** [source:ma2001-lab-lab4-pdf#section-3]
Let $S = \{u_1, u_2, u_3, u_4, u_5\}$ where:
$u_1 = (1, 1, 1, 1, 1)$
$u_2 = (1, -1, 1, -1, 1)$
$u_3 = (2, 0, 2, 0, 2)$
$u_4 = (1, -2, 4, -8, 16)$
$u_5 = (0, 4, -6, 16, -30)$

1.  Form matrix D with these vectors as columns:
    ```matlab
    D = [1 1 2 1 0; 1 -1 0 -2 4; 1 1 2 4 -6; 1 -1 0 -8 16; 1 1 2 16 -30];
    ```
2.  Apply `rref(D)`:
    ```matlab
    rref(D)
    ```
    The reduced row-echelon form is:
    $$
    \begin{pmatrix}
    1 & 0 & 1 & 0 & 1 \\
    0 & 1 & 1 & 0 & 1 \\
    0 & 0 & 0 & 1 & -2 \\
    0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0
    \end{pmatrix}
    $$ [source:ma2001-lab-lab4sol-pdf#section-3]
3.  The pivot columns are 1, 2, and 4. The basis $S'$ for $V$ consists of the first, second, and fourth original vectors in $S$:
    $S' = \{(1,1,1,1,1), (1,-1,1,-1,1), (1,-2,4,-8,16)\}$ [source:ma2001-lab-lab4sol-pdf#section-3].

### Extending a Linearly Independent Set to a Basis for $\text{R}^n$

Given a basis $S'$ for a subspace $V$ of $\text{R}^n$, you can extend it to a basis for $\text{R}^n$.
**Example:** Extend the basis $S'$ obtained above (which is a basis for a subspace of $\text{R}^5$) to a basis for $\text{R}^5$ [source:ma2001-lab-lab4-pdf#section-4].
$S' = \{(1,1,1,1,1), (1,-1,1,-1,1), (1,-2,4,-8,16)\}$

1.  Form a matrix E using the vectors in $S'$ as *rows* (using the "row space" method) [source:ma2001-lab-lab4-pdf#section-4].
    ```matlab
    E = [1 1 1 1 1; 1 -1 1 -1 1; 1 -2 4 -8 16];
    ```
2.  Apply `rref(E)`:
    ```matlab
    rref(E)
    ```
    The reduced row-echelon form is:
    $$
    \begin{pmatrix}
    1 & 0 & 0 & 2 & -4 \\
    0 & 1 & 0 & 1 & 0 \\
    0 & 0 & 1 & -2 & 5
    \end{pmatrix}
    $$ [source:ma2001-lab-lab4sol-pdf#section-4]
3.  Observe which columns do not have leading entries (non-pivot columns). In this case, columns 4 and 5 are non-pivot columns [source:ma2001-lab-lab4sol-pdf#section-4].
4.  To complete `rref(E)` to a $5 \times 5$ identity matrix (so every column has a leading entry), you need to add two rows: $(0,0,0,1,0)$ and $(0,0,0,0,1)$ [source:ma2001-lab-lab4sol-pdf#section-4]. These two vectors extend the set $S'$ to a basis for $\text{R}^5$ [source:ma2001-lab-lab4-pdf#section-4].

---

## Nullspaces

### Finding a Basis for the Nullspace

The nullspace of a matrix A consists of all vectors $x$ such that $Ax = 0$.
1.  **Manual Method (using RREF)**:
    *   Find the reduced row-echelon form of A using `rref(A)`.
    *   Solve the system $Ax = 0$ by hand to find the general solution, expressing the basic variables in terms of the free variables.
    *   From the general solution, derive a basis for the solution space (which is the nullspace of A) [source:ma2001-lab-lab4-pdf#section-5].

**Example: Matrix A** [source:ma2001-lab-lab4-pdf#section-5]
Using `rref(A)` from the previous section, the general solution for $Ax=0$ is:
$$
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix} = s \begin{pmatrix} -4 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + t \begin{pmatrix} 0 \\ 0 \\ 0 \\ -4 \\ 1 \end{pmatrix}
$$ [source:ma2001-lab-lab4sol-pdf#section-4]
A basis for the nullspace of A is therefore:
$$
\left\{ \begin{pmatrix} -4 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 0 \\ -4 \\ 1 \end{pmatrix} \right\}
$$ [source:ma2001-lab-lab4sol-pdf#section-4]

2.  **Using `null()` command**: MATLAB provides a direct command `null(A, 'r')` to obtain a basis for the nullspace [source:ma2001-lab-lab4-pdf#section-5]. The `'r'` argument ensures the basis vectors are rational, which often aligns with manual calculations.
    ```matlab
    A = [1 4 1 2 8; 2 8 2 3 12; 3 12 3 -1 -4; 4 16 -1 -4 -16];
    N = null(A, 'r')
    ```
    The columns of `N` give a basis for the nullspace of A [source:ma2001-lab-lab4-pdf#section-5].
    $$
    N = \begin{pmatrix}
    -4 & 0 \\
    1 & 0 \\
    0 & 0 \\
    0 & -4 \\
    0 & 1
    \end{pmatrix}
    $$ [source:ma2001-lab-lab4sol-pdf#section-5]
    This result matches the basis derived manually.

**Verification of Nullspace Basis** [source:ma2001-lab-lab4-pdf#section-5]
If $n_1$ and $n_2$ are the column vectors of $N$, they are vectors in the nullspace. This means $An_1 = 0$ and $An_2 = 0$. Therefore, the matrix multiplication $AN$ should result in a zero matrix [source:ma2001-lab-lab4sol-pdf#section-5].
```matlab
A * N % Returns a matrix of zeros
```

**Example: Matrix B** [source:ma2001-lab-lab4-pdf#section-5]
Repeat for matrix B using `null(B, 'r')`:
```matlab
B = [1 1 1 1 1 1; 1 -1 1 -1 1 -1; 1 3 4 8 16 32; 4 1 7 7 19 31];
N_B = null(B, 'r')
```
A basis for the nullspace of B is given by:
$$
N_B = \begin{pmatrix}
4 & 8 \\
0 & 0 \\
-5 & -8 \\
0 & -1 \\
1 & 0 \\
0 & 1
\end{pmatrix}
$$ [source:ma2001-lab-lab4sol-pdf#section-5]

---

## Dot Product and Norm

### Performing Dot Products on Vectors

The dot product of two vectors $u$ and $v$ can be computed in MATLAB.
**Example:** [source:ma2001-lab-lab4-pdf#section-6]
Let $u = (1, 2, 3, 4, 5)$ and $v = (1, 0, 1, -1, 2)$.

1.  Input $u$ and $v$ as row matrices:
    ```matlab
    u = [1 2 3 4 5];
    v = [1 0 1 -1 2];
    ```
2.  The dot product $u \cdot v$ is computed by typing `u*v'` (where `v'` is the transpose of `v`):
    ```matlab
    u * v' % Returns 10
    ```
    Note that `u*v` or `u'*v` will not yield the dot product [source:ma2001-lab-lab4-pdf#section-6].
3.  Compute $u \cdot u$ and $v \cdot v$:
    ```matlab
    u * u' % Returns 55
    v * v' % Returns 7
    ``` [source:ma2001-lab-lab4sol-pdf#section-5]

### Finding the Norm of a Vector

The norm (or length) of a vector $u$ is the square root of $u \cdot u$.
1.  **Manual Calculation**:
    For vector $u$: `sqrt(u*u')`
    ```matlab
    sqrt(u*u') % Returns sqrt(55) approx 7.4162
    ```
    For vector $v$: `sqrt(v*v')`
    ```matlab
    sqrt(v*v') % Returns sqrt(7) approx 2.6458
    ``` [source:ma2001-lab-lab4sol-pdf#section-6]
2.  **Using `norm()` command**: MATLAB provides a direct command `norm(u)` [source:ma2001-lab-lab4-pdf#section-6].
    ```matlab
    norm(u) % Returns 7.4162
    norm(v) % Returns 2.6458
    ```

---

## Orthonormal Basis

### Checking if a Set of Vectors is Orthogonal

A set of vectors is orthogonal if the dot product of any two distinct vectors in the set is zero.
**Example:** [source:ma2001-lab-lab4-pdf#section-6]
Let $a = (1, 1, 1, 1)$, $b = (1, 0, -1, 0)$, and $c = (1, -1, 1, -1)$.

1.  Form a matrix F using vectors $a, b, c$ as rows:
    ```matlab
    F = [1 1 1 1; 1 0 -1 0; 1 -1 1 -1];
    ```
2.  Pre-multiply F by its transpose, $F^T$ (type `F*F'`).
    ```matlab
    F * F'
    ```
    The product is:
    $$
    FF^T = \begin{pmatrix}
    4 & 0 & 0 \\
    0 & 2 & 0 \\
    0 & 0 & 4
    \end{pmatrix}
    $$ [source:ma2001-lab-lab4sol-pdf#section-6]
    If the product $FF^T$ is a diagonal matrix, the set is orthogonal [source:ma2001-lab-lab4-pdf#section-6]. This is because the non-diagonal entries of $FF^T$ are given by the dot product between two different vectors (rows of F and columns of $F^T$) [source:ma2001-lab-lab4sol-pdf#section-6]. Since these entries are 0, it implies $a \cdot b = 0$, $a \cdot c = 0$, and $b \cdot c = 0$, meaning the set is orthogonal [source:ma2001-lab-lab4sol-pdf#section-6].

### Checking if a Set of Vectors is Orthonormal

A set of vectors is orthonormal if it is orthogonal and each vector has a norm of 1 (i.e., they are unit vectors).
If the product $FF^T$ (where F has the vectors as rows) is an *identity matrix*, then the set is orthonormal [source:ma2001-lab-lab4-pdf#section-7]. This implies that not only are the vectors orthogonal, but their dot product with themselves (the diagonal entries) is 1, meaning their norms are 1 [source:ma2001-lab-lab4sol-pdf#section-7].

**Example:** [source:ma2001-lab-lab4-pdf#section-7]
Let $d = (\cos(\pi/3), 0, \sin(\pi/3))$, $e = (0, 1, 0)$, $f = (\sin(\pi/3), 0, -\cos(\pi/3))$.
```matlab
pi_over_3 = pi/3;
d = [cos(pi_over_3) 0 sin(pi_over_3)];
e = [0 1 0];
f = [sin(pi_over_3) 0 -cos(pi_over_3)];
F_orthonormal = [d; e; f];
F_orthonormal * F_orthonormal'
```
The product $F F^T$ is:
$$
FF^T = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$ [source:ma2001-lab-lab4sol-pdf#section-7]
Since $FF^T$ is the identity matrix, the set $\{d, e, f\}$ is orthonormal [source:ma2001-lab-lab4sol-pdf#section-7].

### Finding an Orthonormal Basis for a Subspace

To find an orthonormal basis for a subspace $V = \text{span}(S)$:
1.  Form a matrix G using the vectors in $S$ as *columns* [source:ma2001-lab-lab4-pdf#section-7].
2.  Use the MATLAB command `orth(G)` [source:ma2001-lab-lab4-pdf#section-8]. The columns of the resulting matrix $Q$ give an orthonormal basis for $V$ [source:ma2001-lab-lab4-pdf#section-8].

**Example:** [source:ma2001-lab-lab4-pdf#section-7]
Let $V = \text{span}(S)$ where $S = \{w_1, w_2, w_3\}$ and:
$w_1 = (1, 1, 1, 1)$
$w_2 = (1, 1, 0, 0)$
$w_3 = (0, 1, 1, 0)$

1.  Form a $4 \times 3$ matrix G using $w_1, w_2, w_3$ as columns:
    ```matlab
    G = [1 1 0; 1 1 1; 1 0 1; 1 0 0];
    ```
2.  Apply `rref(G)` to check that $S$ is a basis for $V$:
    ```matlab
    rref(G)
    ```
    The reduced row-echelon form shows three pivot columns, confirming $S$ is a basis [source:ma2001-lab-lab4sol-pdf#section-7].
3.  Check if $S$ is orthogonal by multiplying $G^T G$ (since vectors are columns in G):
    ```matlab
    G' * G
    ```
    The result is:
    $$
    G^T G = \begin{pmatrix}
    4 & 2 & 2 \\
    2 & 2 & 1 \\
    2 & 1 & 2
    \end{pmatrix}
    $$ [source:ma2001-lab-lab4sol-pdf#section-7]
    Since this is not a diagonal matrix, $S$ is not orthogonal [source:ma2001-lab-lab4sol-pdf#section-7].
4.  Use `orth()` to obtain an orthonormal basis:
    ```matlab
    Q = orth(G)
    ```
    The columns of $Q$ form an orthonormal basis for $V$:
    $$
    Q = \begin{pmatrix}
    -0.4835 & 0.7071 & -0.1273 \\
    -0.6635 & 0 & 0.5565 \\
    -0.4835 & -0.7071 & -0.1273 \\
    -0.3035 & 0 & -0.8111
    \end{pmatrix}
    $$ [source:ma2001-lab-lab4sol-pdf#section-7]
    An orthonormal basis for $V$ is given by:
    $\{(-0.4835, -0.6635, -0.4835, -0.3035)$, $(0.7071, 0, -0.7071, 0)$, $(-0.1273, 0.5565, -0.1273, -0.8111)\}$ [source:ma2001-lab-lab4sol-pdf#section-8].

5.  **Verify Orthonormality**: Multiply $Q^T Q$.
    ```matlab
    Q' * Q
    ```
    The result is an identity matrix (allowing for minor floating-point errors):
    $$
    Q^T Q = \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{pmatrix}
    $$ [source:ma2001-lab-lab4sol-pdf#section-8]
    This confirms that the columns of $Q$ form an orthonormal set.

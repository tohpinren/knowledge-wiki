---
page_id: "y1s1-ma2001-matrix-operations"
title: "Matrix Operations and Types"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Definitions of matrices, basic operations (addition, scalar multiplication, matrix multiplication, transpose), and special matrix types (square, diagonal, identity)."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
  - "y1s1-acc1701x-lecture-01"
source_refs:
  - "ma2001-lecture-chapter2-pdf#section-2"
  - "ma2001-cheatsheet-cheatsheet-pdf#section-1"
  - "ma2001-tutorial-tutorial2-pdf#section-1"
topics:
  - "matrix"
  - "example"
  - "matrices"
  - "det"
  - "invertible"
  - "square"
  - "row"
  - "examples"
  - "basis"
  - "rank"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Matrix Operations and Types

Matrices are fundamental to linear algebra, providing a concise way to represent and manipulate data in various mathematical and scientific contexts. This page introduces the basic definitions of matrices, explores common matrix operations, and categorizes different types of matrices.

---

## 1. Introduction to Matrices

A **matrix** is defined as a rectangular array of numbers, which are referred to as **entries** [source: ma2001-lecture-chapter2-pdf#section-2]. The size of a matrix is specified by its dimensions, $m \times n$, where $m$ represents the number of rows and $n$ represents the number of columns. An entry located in the $i$-th row and $j$-th column is called the **($i, j$)-entry**, denoted as $a_{ij}$ for a matrix $A$ [source: ma2001-lecture-chapter2-pdf#section-3].

In general, an $m \times n$ matrix $A$ can be written as:
$$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
$$
Alternatively, if the size is known, a matrix $A$ can be simply written as $A = (a_{ij})$ [source: ma2001-lecture-chapter2-pdf#section-6].

### 1.1 Examples of Matrices
*   A $3 \times 2$ matrix:
    $$
    \begin{pmatrix}
    1 & 2 \\
    3 & 4 \\
    0 & -1
    \end{pmatrix}
    $$
    Here, the $(1, 2)$-entry is $2$, and the $(3, 1)$-entry is $0$ [source: ma2001-lecture-chapter2-pdf#section-4].
*   A $1 \times 1$ matrix, such as $(4)$, is often treated as a single number in computation [source: ma2001-lecture-chapter2-pdf#section-4].

### 1.2 Column and Row Matrices
*   A **column matrix** (or **column vector**) is a matrix that has only one column [source: ma2001-lecture-chapter2-pdf#section-5]. For example, a $3 \times 1$ matrix:
    $$
    \begin{pmatrix}
    1 \\
    1 \\
    2
    \end{pmatrix}
    $$
*   A **row matrix** (or **row vector**) is a matrix that has only one row [source: ma2001-lecture-chapter2-pdf#section-5]. For example, a $1 \times 3$ matrix:
    $$
    \begin{pmatrix}
    2 & 1 & 0
    \end{pmatrix}
    $$
*   A $1 \times 1$ matrix like $(4)$ is considered both a column and a row matrix [source: ma2001-lecture-chapter2-pdf#section-5].

---

## 2. Special Matrix Types

Certain matrices possess unique structures or properties, leading to special classifications:

### 2.1 Square Matrices
A matrix is a **square matrix** if it has an equal number of rows and columns ($m = n$). An $n \times n$ matrix is referred to as a square matrix of **order $n$** [source: ma2001-lecture-chapter2-pdf#section-7].
Examples include $1 \times 1$, $2 \times 2$, $3 \times 3$, and $4 \times 4$ matrices [source: ma2001-lecture-chapter2-pdf#section-8].

### 2.2 Diagonal Entries
For a square matrix $A = (a_{ij})$ of order $n$, the **diagonal** of $A$ refers to the sequence of entries $a_{11}, a_{22}, \ldots, a_{nn}$. Each $a_{ii}$ is a **diagonal entry**, while $a_{ij}$ with $i \neq j$ are **non-diagonal entries** [source: ma2001-lecture-chapter2-pdf#section-7].

### 2.3 Diagonal Matrices
A square matrix is a **diagonal matrix** if all its non-diagonal entries are zero [source: ma2001-lecture-chapter2-pdf#section-7]. That is, $a_{ij} = 0$ whenever $i \neq j$.
Examples:
$$
\begin{pmatrix}
4
\end{pmatrix}, \quad
\begin{pmatrix}
0 & 0 \\
0 & 2
\end{pmatrix}, \quad
\begin{pmatrix}
1 & 0 & 0 \\
0 & 3 & 0 \\
0 & 0 & 2
\end{pmatrix}
$$
For a diagonal matrix $D$, $D^k$ is also a diagonal matrix where its diagonal elements are raised to the power $k$ [source: ma2001-tutorial-tutorial2-pdf#section-2].

### 2.4 Scalar Matrices
A diagonal matrix is a **scalar matrix** if all its diagonal entries are the same constant, $c$ [source: ma2001-lecture-chapter2-pdf#section-7]. That is, $a_{ij} = 0$ if $i \neq j$, and $a_{ij} = c$ if $i = j$.
Examples:
$$
\begin{pmatrix}
4
\end{pmatrix}, \quad
\begin{pmatrix}
2 & 0 \\
0 & 2
\end{pmatrix}, \quad
\begin{pmatrix}
3 & 0 & 0 & 0 \\
0 & 3 & 0 & 0 \\
0 & 0 & 3 & 0 \\
0 & 0 & 0 & 3
\end{pmatrix}
$$

### 2.5 Identity Matrices
A diagonal matrix is an **identity matrix** if all its diagonal entries are $1$ [source: ma2001-lecture-chapter2-pdf#section-7]. The identity matrix of order $n$ is denoted by $I_n$, or simply $I$ when the order is clear.
Examples:
$$
I_1 = \begin{pmatrix} 1 \end{pmatrix}, \quad
I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

### 2.6 Zero Matrices
A matrix in which all entries are equal to zero is called a **zero matrix** [source: ma2001-lecture-chapter2-pdf#section-7]. A zero matrix of size $m \times n$ is denoted by $0_{m \times n}$, or simply $0$ when the size is evident.
Examples:
$$
0_{1 \times 1} = \begin{pmatrix} 0 \end{pmatrix}, \quad
0_{2 \times 4} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad
0_{4 \times 3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
$$

### 2.7 Symmetric Matrices
A square matrix $A = (a_{ij})$ is **symmetric** if $a_{ij} = a_{ji}$ for all $i, j$ [source: ma2001-lecture-chapter2-pdf#section-7].
Examples:
$$
\begin{pmatrix}
4
\end{pmatrix}, \quad
\begin{pmatrix}
0 & 4 \\
4 & 2
\end{pmatrix}, \quad
\begin{pmatrix}
1 & -1 & 0 \\
-1 & 3 & 2 \\
0 & 2 & 2
\end{pmatrix}
$$

### 2.8 Triangular Matrices
A square matrix $A = (a_{ij})$ is:
*   **Upper triangular** if $a_{ij} = 0$ whenever $i > j$ [source: ma2001-lecture-chapter2-pdf#section-7].
*   **Lower triangular** if $a_{ij} = 0$ whenever $i < j$ [source: ma2001-lecture-chapter2-pdf#section-7].
Both upper and lower triangular matrices are generally referred to as **triangular matrices** [source: ma2001-lecture-chapter2-pdf#section-7].
Examples of upper triangular matrices:
$$
\begin{pmatrix}
4
\end{pmatrix}, \quad
\begin{pmatrix}
0 & 4 \\
0 & 2
\end{pmatrix}, \quad
\begin{pmatrix}
1 & -1 & 0 \\
0 & 3 & 2 \\
0 & 0 & 2
\end{pmatrix}
$$
Examples of lower triangular matrices:
$$
\begin{pmatrix}
4
\end{pmatrix}, \quad
\begin{pmatrix}
2 & 0 & 0 & 0 \\
1 & 3 & 0 & 0 \\
6 & 0 & 0 & 0 \\
-2 & -1 & 0 & 1
\end{pmatrix}
$$

---

## 3. Matrix Operations

### 3.1 Matrix Equality
Two matrices $A = (a_{ij})_{m \times n}$ and $B = (b_{ij})_{p \times q}$ are considered **equal** if they have the same size (i.e., $m=p$ and $n=q$) and their corresponding entries are equal ($a_{ij} = b_{ij}$ for all $i, j$) [source: ma2001-lecture-chapter2-pdf#section-17].

For example, given:
$$
A = \begin{pmatrix} 1 & x \\ 2 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & -1 \\ 2 & 4 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & -1 & 0 \\ 2 & 4 & 0 \end{pmatrix}
$$
Then $A = B$ if and only if $x = -1$. However, $B \neq C$ and $A \neq C$ for any value of $x$, because $B$ and $C$ have different sizes [source: ma2001-lecture-chapter2-pdf#section-17].

### 3.2 Matrix Addition and Subtraction
Given two matrices $A = (a_{ij})_{m \times n}$ and $B = (b_{ij})_{m \times n}$ of the same size:
*   Their **sum** $A+B$ is an $m \times n$ matrix where each entry is the sum of the corresponding entries of $A$ and $B$: $A+B = (a_{ij} + b_{ij})_{m \times n}$ [source: ma2001-lecture-chapter2-pdf#section-18].
*   Their **difference** $A-B$ is an $m \times n$ matrix where each entry is the difference of the corresponding entries of $A$ and $B$: $A-B = (a_{ij} - b_{ij})_{m \times n}$ [source: ma2001-lecture-chapter2-pdf#section-20].

**Example:**
Let $A = \begin{pmatrix} 2 & 3 & 4 \\ 4 & 5 & 6 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 2 & 3 \\ -1 & -1 & -1 \end{pmatrix}$ [source: ma2001-lecture-chapter2-pdf#section-19, ma2001-lecture-chapter2-pdf#section-21].
Then:
$$
A+B = \begin{pmatrix} 2+1 & 3+2 & 4+3 \\ 4+(-1) & 5+(-1) & 6+(-1) \end{pmatrix} = \begin{pmatrix} 3 & 5 & 7 \\ 3 & 4 & 5 \end{pmatrix}
$$
$$
A-B = \begin{pmatrix} 2-1 & 3-2 & 4-3 \\ 4-(-1) & 5-(-1) & 6-(-1) \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 5 & 6 & 7 \end{pmatrix}
$$
Matrix subtraction can also be defined using matrix addition: $A - B = A + (-B)$, where $-B$ is the matrix $(-1)B$ [source: ma2001-lecture-chapter2-pdf#section-24].

### 3.3 Scalar Multiplication
Given a matrix $A = (a_{ij})_{m \times n}$ and a real constant $c$ (called a **scalar**), their product $cA$ is an $m \times n$ matrix where each entry of $A$ is multiplied by $c$: $cA = (ca_{ij})_{m \times n}$ [source: ma2001-lecture-chapter2-pdf#section-22].

**Example:**
Let $A = \begin{pmatrix} 2 & 3 & 4 \\ 4 & 5 & 6 \end{pmatrix}$ [source: ma2001-lecture-chapter2-pdf#section-23].
Then:
$$
4A = \begin{pmatrix} 4 \cdot 2 & 4 \cdot 3 & 4 \cdot 4 \\ 4 \cdot 4 & 4 \cdot 5 & 4 \cdot 6 \end{pmatrix} = \begin{pmatrix} 8 & 12 & 16 \\ 16 & 20 & 24 \end{pmatrix}
$$

### 3.4 Properties of Matrix Addition and Scalar Multiplication
Let $A, B, C$ be matrices of the same size, and $c, d$ be scalars.
1.  **Commutative law for matrix addition:** $A + B = B + A$ [source: ma2001-lecture-chapter2-pdf#section-25].
2.  **Associative law for matrix addition:** $A + (B + C) = (A + B) + C$ [source: ma2001-lecture-chapter2-pdf#section-25]. Due to this property, we can write $A_1 + A_2 + \dots + A_k$ without parentheses to indicate the order of addition [source: ma2001-lecture-chapter2-pdf#section-28].
3.  $c(A + B) = cA + cB$ [source: ma2001-lecture-chapter2-pdf#section-25].
4.  $(c + d)A = cA + dA$ [source: ma2001-lecture-chapter2-pdf#section-25].
5.  $(cd)A = c(dA) = d(cA)$ [source: ma2001-lecture-chapter2-pdf#section-25].
6.  $A + 0 = 0 + A = A$, where $0$ is the zero matrix of the same size as $A$ [source: ma2001-lecture-chapter2-pdf#section-25].
7.  $A - A = 0$, where $0$ is the zero matrix [source: ma2001-lecture-chapter2-pdf#section-25].
8.  $0A = 0$, where the left $0$ is the number zero and the right $0$ is the zero matrix [source: ma2001-lecture-chapter2-pdf#section-25].

### 3.5 Matrix Multiplication
Given an $m \times p$ matrix $A = (a_{ij})$ and a $p \times n$ matrix $B = (b_{ij})$, their product $AB$ is an $m \times n$ matrix whose $(i, j)$-entry is given by:
$$
(AB)_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{ip}b_{pj} = \sum_{k=1}^{p} a_{ik}b_{kj}
$$
This operation is defined for $i=1, \ldots, m$ and $j=1, \ldots, n$ [source: ma2001-lecture-chapter2-pdf#section-29].
A crucial condition for matrix multiplication $AB$ to be computable is that the **number of columns of $A$ must be equal to the number of rows of $B$** [source: ma2001-lecture-chapter2-pdf#section-29].

**Example:**
Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 \\ 2 & 3 \\ -1 & -2 \end{pmatrix}$ [source: ma2001-lecture-chapter2-pdf#section-33].
Then $AB$ is a $2 \times 2$ matrix:
$$
AB = \begin{pmatrix}
1 \cdot 1 + 2 \cdot 2 + 3 \cdot (-1) & 1 \cdot 1 + 2 \cdot 3 + 3 \cdot (-2) \\
4 \cdot 1 + 5 \cdot 2 + 6 \cdot (-1) & 4 \cdot 1 + 5 \cdot 3 + 6 \cdot (-2)
\end{pmatrix} = \begin{pmatrix}
1+4-3 & 1+6-6 \\
4+10-6 & 4+15-12
\end{pmatrix} = \begin{pmatrix}
2 & 1 \\
8 & 7
\end{pmatrix}
$$

#### 3.5.1 Matrix Multiplication is Not Commutative
In general, matrix multiplication is **not commutative**, meaning $AB \neq BA$, even if both products are defined [source: ma2001-lecture-chapter2-pdf#section-35, ma2001-cheatsheet-cheatsheet-pdf#section-1].
To distinguish between $AB$ and $BA$:
*   $AB$ is the **pre-multiplication** of $A$ to $B$.
*   $BA$ is the **post-multiplication** of $A$ to $B$ [source: ma2001-lecture-chapter2-pdf#section-36].

**Example:**
Let $A = \begin{pmatrix} -1 & 0 \\ 2 & 3 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$ [source: ma2001-lecture-chapter2-pdf#section-35].
Then $AB = \begin{pmatrix} -1 & -2 \\ 11 & 4 \end{pmatrix}$ and $BA = \begin{pmatrix} 3 & 6 \\ -3 & 0 \end{pmatrix}$. Clearly, $AB \neq BA$ [source: ma2001-lecture-chapter2-pdf#section-35].

#### 3.5.2 Zero Product Property
If $AB=0$, it is **not necessary** that $A=0$ or $B=0$ [source: ma2001-lecture-chapter2-pdf#section-37].
**Example:**
Let $A = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$. Neither $A$ nor $B$ is a zero matrix, but $AB = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0$ [source: ma2001-lecture-chapter2-pdf#section-37].

### 3.6 Properties of Matrix Multiplication
1.  **Associative law for matrix multiplication:** If $A$ is $m \times p$, $B$ is $p \times q$, and $C$ is $q \times n$ matrices, then $A(BC) = (AB)C$ [source: ma2001-lecture-chapter2-pdf#section-38, ma2001-cheatsheet-cheatsheet-pdf#section-1]. We can write the product as $ABC$ without parentheses [source: ma2001-lecture-chapter2-pdf#section-38].
2.  **Distributive laws:**
    *   $A(B_1 + B_2) = AB_1 + AB_2$ (if $A$ is $m \times p$, $B_1, B_2$ are $p \times n$) [source: ma2001-lecture-chapter2-pdf#section-38, ma2001-cheatsheet-cheatsheet-pdf#section-1].
    *   $(C_1 + C_2)A = C_1A + C_2A$ (if $C_1, C_2$ are $p \times n$, $A$ is $m \times p$) [source: ma2001-lecture-chapter2-pdf#section-38, ma2001-cheatsheet-cheatsheet-pdf#section-1].
3.  **Scalar multiplication association:** If $A$ is $m \times p$, $B$ is $p \times n$, and $c$ is a scalar, then $c(AB) = (cA)B = A(cB)$ [source: ma2001-lecture-chapter2-pdf#section-39].
4.  **Multiplication by zero and identity matrices:** If $A$ is an $m \times n$ matrix:
    *   $A0_{n \times q} = 0_{m \times q}$
    *   $0_{p \times m}A = 0_{p \times n}$
    *   $AI_n = I_mA = A$ [source: ma2001-lecture-chapter2-pdf#section-39].

### 3.7 Powers of Square Matrices
For a square matrix $A$ and a non-negative integer $n$:
$$
A^n = \begin{cases} I & \text{if } n=0 \\ AA \cdots A \text{ ($n$ times)} & \text{if } n \ge 1 \end{cases}
$$
where $I$ is the identity matrix [source: ma2001-lecture-chapter2-pdf#section-43].

**Property:** For a square matrix $A$ and non-negative integers $n, m$, $A^m A^n = A^{m+n}$ [source: ma2001-lecture-chapter2-pdf#section-44, ma2001-cheatsheet-cheatsheet-pdf#section-1].

**Example:**
Let $A = \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}$ [source: ma2001-lecture-chapter2-pdf#section-43].
Then $A^3 = A \cdot A \cdot A$:
$$
A^3 = \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 3 & 8 \\ 4 & 11 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 11 & 30 \\ 15 & 41 \end{pmatrix}
$$

### 3.8 Transpose of a Matrix
The **transpose** of an $m \times n$ matrix $A$, denoted by $A^T$ (or $A^t$), is an $n \times m$ matrix whose $(i, j)$-entry is the $(j, i)$-entry of $A$ [source: ma2001-lecture-chapter2-pdf#section-55, ma2001-cheatsheet-cheatsheet-pdf#section-1]. Essentially, the rows of $A$ become the columns of $A^T$ and vice versa.

**Example:**
Let $A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \end{pmatrix}$ [source: ma2001-lecture-chapter2-pdf#section-55].
Then $A^T = \begin{pmatrix} 1 & 5 \\ 2 & 6 \\ 3 & 7 \\ 4 & 8 \end{pmatrix}$

#### 3.8.1 Properties of Transposes
Let $A$ and $B$ be matrices of appropriate sizes, and $c$ be a scalar:
1.  $(A^T)^T = A$ [source: ma2001-lecture-chapter2-pdf#section-57, ma2001-cheatsheet-cheatsheet-pdf#section-1].
2.  $(A + B)^T = A^T + B^T$ (if $A, B$ are $m \times n$) [source: ma2001-lecture-chapter2-pdf#section-57, ma2001-cheatsheet-cheatsheet-pdf#section-1].
3.  $(cA)^T = cA^T$ [source: ma2001-lecture-chapter2-pdf#section-57, ma2001-cheatsheet-cheatsheet-pdf#section-1].
4.  $(AB)^T = B^T A^T$ (if $A$ is $m \times n$ and $B$ is $n \times p$) [source: ma2001-lecture-chapter2-pdf#section-57, ma2001-cheatsheet-cheatsheet-pdf#section-1].

#### 3.8.2 Symmetric Matrices Revisited
A square matrix $A$ is symmetric if and only if $A = A^T$ [source: ma2001-lecture-chapter2-pdf#section-56].

### 3.9 Representing Linear Systems as Matrix Equations
A system of linear equations can be elegantly represented using matrix multiplication. For the system:
$$
\begin{align*}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\
&\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m
\end{align*}
$$
This system can be rewritten as the matrix equation $Ax = b$, where:
*   $A = (a_{ij})_{m \times n}$ is the **coefficient matrix**.
*   $x = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$ is the **variable matrix** (or vector).
*   $b = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{pmatrix}$ is the **constant matrix** (or vector) [source: ma2001-lecture-chapter2-pdf#section-51].

Alternatively, the linear system can be expressed as a linear combination of the column vectors of $A$: $x_1 \mathbf{c}_1 + x_2 \mathbf{c}_2 + \cdots + x_n \mathbf{c}_n = \mathbf{b}$, or $\sum_{j=1}^{n} x_j \mathbf{c}_j = \mathbf{b}$ [source: ma2001-lecture-chapter2-pdf#section-52].

A matrix $\mathbf{u}$ is a **solution** to the linear system $Ax = b$ if the equation is satisfied when $\mathbf{x} = \mathbf{u}$, i.e., $A\mathbf{u} = \mathbf{b}$ [source: ma2001-lecture-chapter2-pdf#section-54].

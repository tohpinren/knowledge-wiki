---
page_id: "y1s1-ma2001-invertible-elementary-matrices"
title: "Invertible Matrices and Elementary Matrices"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Conditions for matrix invertibility, methods for finding inverses (Gauss-Jordan elimination), and the role of elementary matrices."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter2-pdf#section-3"
  - "ma2001-tutorial-tutorial3-pdf#section-1"
  - "ma2001-cheatsheet-cheatsheet-pdf#section-2"
topics:
  - "matrix"
  - "example"
  - "matrices"
  - "det"
  - "invertible"
  - "square"
  - "row"
  - "examples"
  - "elementary"
  - "write"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Invertible Matrices and Elementary Matrices

This page delves into the concept of invertible matrices, exploring the conditions under which a matrix can have an inverse, the properties of these inverses, and the crucial role of elementary matrices in determining invertibility and computing inverses.

## Inverses of Square Matrices

In the realm of real numbers, solving an equation like $ax = b$ (where $a \ne 0$) is straightforward: $x = \frac{1}{a}b = a^{-1}b$. However, this concept of "division" does not directly exist for matrices [source: ma2001-lecture-chapter2-pdf#section-6]. Instead, we introduce the idea of an **inverse matrix**, which serves a similar purpose for certain square matrices.

### Definition of an Invertible Matrix

A square matrix $A$ of order $n$ is said to be **invertible** (or **non-singular**) if there exists another square matrix $B$ of the same order $n$ such that:
$AB = I$ and $BA = I$
where $I$ is the [[matrix-operations#Identity Matrix|identity matrix]] of order $n$. The matrix $B$ is then called an **inverse** of $A$ [source: ma2001-lecture-chapter2-pdf#section-6].

If a square matrix does not have an inverse, it is called a **singular matrix** [source: ma2001-lecture-chapter2-pdf#section-6].

**Example 1: Identifying an Invertible Matrix**
Consider the matrices:
$A = \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix}$ and $B = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$
To check if $A$ is invertible and $B$ is its inverse, we compute $AB$ and $BA$:
$AB = \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix} \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 2(3)+(-5)(1) & 2(5)+(-5)(2) \\ (-1)(3)+3(1) & (-1)(5)+3(2) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$ [source: ma2001-lecture-chapter2-pdf#section-6]
$BA = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 3(2)+5(-1) & 3(-5)+5(3) \\ 1(2)+2(-1) & 1(-5)+2(3) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$ [source: ma2001-lecture-chapter2-pdf#section-6]
Since $AB = I$ and $BA = I$, $A$ is invertible and $B$ is its inverse.

**Example 2: Identifying a Singular Matrix (Proof by Contradiction)**
Let $A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$. To show $A$ is singular, assume for contradiction that $A$ has an inverse $B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
Then, $BA = I$:
$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} a(1)+b(1) & a(0)+b(0) \\ c(1)+d(1) & c(0)+d(0) \end{pmatrix} = \begin{pmatrix} a+b & 0 \\ c+d & 0 \end{pmatrix}$
For this to be equal to $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, we would need $0 = 1$ in the (2,2) entry, which is impossible. Hence, our assumption is wrong, and $A$ is singular [source: ma2001-lecture-chapter2-pdf#section-6].

### Cancellation Laws for Matrix Multiplication

If $A$ is an invertible $m \times m$ matrix:
1.  If $B_1$ and $B_2$ are $m \times n$ matrices such that $AB_1 = AB_2$, then $B_1 = B_2$. (Pre-multiplication by $A^{-1}$ on both sides yields $A^{-1}AB_1 = A^{-1}AB_2 \implies IB_1 = IB_2 \implies B_1 = B_2$).
2.  If $C_1$ and $C_2$ are $n \times m$ matrices such that $C_1A = C_2A$, then $C_1 = C_2$. (Post-multiplication by $A^{-1}$ on both sides yields $C_1AA^{-1} = C_2AA^{-1} \implies C_1I = C_2I \implies C_1 = C_2$) [source: ma2001-lecture-chapter2-pdf#section-6].

**Important Note:** If $A$ is not invertible, the cancellation laws may not hold. For example, let $A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, $B_1 = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$, and $B_2 = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$.
Then $AB_1 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 2 & 0 \end{pmatrix}$.
And $AB_2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 2 & 0 \end{pmatrix}$.
So $AB_1 = AB_2$, but $B_1 \ne B_2$ [source: ma2001-lecture-chapter2-pdf#section-6].

### Uniqueness of Inverses

If a square matrix $A$ has an inverse, that inverse is unique.
**Proof:** Assume $B$ and $C$ are both inverses of $A$. By definition, $AB = I$, $BA = I$, $AC = I$, and $CA = I$ [source: ma2001-lecture-chapter2-pdf#section-6].
Starting with $AB = I$:
$CAB = CI$ (Pre-multiply by $C$)
$(CA)B = C$ (By [[matrix-operations#Matrix Multiplication Properties|associativity of matrix multiplication]] and identity property)
$IB = C$ (Since $CA = I$)
$B = C$ (By identity property)
Therefore, the inverse of a matrix is unique. This allows us to denote the unique inverse of an invertible matrix $A$ by $A^{-1}$ [source: ma2001-lecture-chapter2-pdf#section-6].

### Inverse of a $2 \times 2$ Matrix

For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
$A$ is invertible if and only if $ad - bc \ne 0$.
If $A$ is invertible, its inverse is given by the formula:
$A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ [source: ma2001-lecture-chapter2-pdf#section-6].
The quantity $ad - bc$ is known as the [[determinants-properties#Determinant of a 2x2 Matrix|determinant of a $2 \times 2$ matrix]].

### Properties of Inverses

Let $A$ and $B$ be invertible matrices of the same size, and let $c$ be a non-zero scalar.
1.  $(A^{-1})^{-1} = A$ [source: ma2001-lecture-chapter2-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-1].
2.  $(cA)^{-1} = \frac{1}{c}A^{-1}$ [source: ma2001-lecture-chapter2-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-1].
3.  $(A^T)^{-1} = (A^{-1})^T$ [source: ma2001-lecture-chapter2-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-1].
4.  $(AB)^{-1} = B^{-1}A^{-1}$ [source: ma2001-lecture-chapter2-pdf#section-6, ma2001-cheatsheet-cheatsheet-pdf#section-1].
    *   This property extends to products of multiple invertible matrices: $(A_1A_2 \cdots A_k)^{-1} = A_k^{-1} \cdots A_2^{-1}A_1^{-1}$ [source: ma2001-lecture-chapter2-pdf#section-6].

### Powers of Square Matrices

For an invertible matrix $A$ and a positive integer $n$, we define:
$A^{-n} = (A^{-1})^n = A^{-1}A^{-1} \cdots A^{-1}$ ($n$ times) [source: ma2001-lecture-chapter2-pdf#section-6].

**Properties:**
1.  $A^r A^s = A^{r+s}$ for any integers $r$ and $s$ (including negative values if $A$ is invertible) [source: ma2001-lecture-chapter2-pdf#section-6].
2.  $(A^n)^{-1} = (A^{-1})^n$ [source: ma2001-lecture-chapter2-pdf#section-6].

## Elementary Matrices

Elementary matrices are fundamental in understanding matrix invertibility and provide a systematic way to compute inverses.

### Elementary Row Operations (EROs)

Recall that [[gaussian-elimination-rref#Elementary Row Operations|Elementary Row Operations]] (EROs) are used to transform matrices. These operations can be represented by multiplying the matrix by an **elementary matrix** [source: ma2001-lecture-chapter2-pdf#section-7].

An **elementary matrix** is a square matrix obtained by performing a *single* elementary row operation on an [[matrix-operations#Identity Matrix|identity matrix]] [source: ma2001-lecture-chapter2-pdf#section-7].

There are three types of elementary matrices, corresponding to the three types of EROs:

1.  **Multiplying a row by a non-zero constant ($kR_i$):**
    *   An elementary matrix $E$ for this operation is formed by multiplying the $i$-th row of the identity matrix $I$ by $k$.
    *   If $E$ is an elementary matrix for $kR_i$, then $E$ is invertible if $k \ne 0$, and $E^{-1}$ is the elementary matrix for $\frac{1}{k}R_i$ [source: ma2001-lecture-chapter2-pdf#section-7].
    *   Example: $E_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & k & 0 \\ 0 & 0 & 1 \end{pmatrix}$ corresponds to multiplying row 2 by $k$.
    *   $E_1^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1/k & 0 \\ 0 & 0 & 1 \end{pmatrix}$.

2.  **Interchanging two rows ($R_i \leftrightarrow R_j$):**
    *   An elementary matrix $E$ for this operation is formed by interchanging the $i$-th and $j$-th rows of the identity matrix $I$.
    *   This type of elementary matrix $E$ is invertible, and its inverse is itself: $E^{-1} = E$ [source: ma2001-lecture-chapter2-pdf#section-7].
    *   Example: $E_2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$ corresponds to interchanging row 2 and row 3.
    *   $E_2^{-1} = E_2$.

3.  **Adding a multiple of one row to another ($R_j + kR_i$):**
    *   An elementary matrix $E$ for this operation is formed by adding $k$ times row $i$ to row $j$ of the identity matrix $I$.
    *   This type of elementary matrix $E$ is invertible, and its inverse is the elementary matrix for $R_j - kR_i$ [source: ma2001-lecture-chapter2-pdf#section-7].
    *   Example: $E_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ k & 0 & 1 \end{pmatrix}$ corresponds to adding $k$ times row 1 to row 3.
    *   $E_3^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -k & 0 & 1 \end{pmatrix}$.

**Key Property:** All elementary matrices are invertible, and their inverses are also elementary matrices [source: ma2001-lecture-chapter2-pdf#section-7].

### Equivalence of Statements for Invertible Matrices

For a square matrix $A$ of order $n$, the following statements are equivalent [source: ma2001-lecture-chapter2-pdf#section-7]:

1.  $A$ is invertible.
2.  The linear system $Ax = 0$ has only the trivial solution ($x=0$).
    *   **Proof (1 $\implies$ 2):** If $A$ is invertible, then $Ax = 0 \implies A^{-1}(Ax) = A^{-1}0 \implies (A^{-1}A)x = 0 \implies Ix = 0 \implies x = 0$. Thus, only the trivial solution exists [source: ma2001-lecture-chapter2-pdf#section-7].
3.  The [[gaussian-elimination-rref#Reduced Row-Echelon Form (RREF)|reduced row-echelon form]] (RREF) of $A$ is the identity matrix $I$.
    *   **Proof (2 $\implies$ 3):** If $Ax=0$ has only the trivial solution, then in its augmented matrix representation $(A | 0)$, every column must be a [[gaussian-elimination-rref#Pivot Positions and Pivot Columns|pivot column]]. For an $n \times n$ matrix, this means there are $n$ pivot columns. When transformed to RREF using [[gaussian-elimination-rref#Gauss-Jordan Elimination|Gauss-Jordan Elimination]], the resulting matrix will have $n$ leading entries (pivots), all equal to 1, and zeros everywhere else, making it the identity matrix $I$. So, the RREF of $A$ is $I$ [source: ma2001-lecture-chapter2-pdf#section-7].
4.  $A$ can be expressed as a product of elementary matrices ($A = E_k E_{k-1} \cdots E_1$).
    *   **Proof (3 $\implies$ 4):** If the RREF of $A$ is $I$, it means that $A$ can be transformed into $I$ by a sequence of elementary row operations. Each ERO corresponds to multiplication by an elementary matrix. So, $E_k \cdots E_2 E_1 A = I$. Since each elementary matrix is invertible, we can multiply by their inverses to isolate $A$: $A = (E_k \cdots E_2 E_1)^{-1}I = E_1^{-1}E_2^{-1} \cdots E_k^{-1}$. Since the inverse of an elementary matrix is also an elementary matrix, $A$ is a product of elementary matrices [source: ma2001-lecture-chapter2-pdf#section-7].
    *   **Proof (4 $\implies$ 1):** If $A$ is a product of elementary matrices, $A = E_k \cdots E_1$. Since each $E_i$ is an invertible matrix, their product $A$ is also invertible (recall the property $(A_1 \cdots A_k)^{-1} = A_k^{-1} \cdots A_1^{-1}$) [source: ma2001-lecture-chapter2-pdf#section-6, ma2001-lecture-chapter2-pdf#section-7].

### Finding Inverses using Gauss-Jordan Elimination

The equivalence above (specifically, RREF of $A$ is $I$ if $A$ is invertible) provides a practical method for finding the inverse of a matrix.
To find $A^{-1}$ for an $n \times n$ matrix $A$:
1.  Form the $n \times 2n$ augmented matrix $[A | I]$, where $I$ is the identity matrix of the same order as $A$.
2.  Apply [[gaussian-elimination-rref#Gauss-Jordan Elimination|Gauss-Jordan Elimination]] to transform the left side of the augmented matrix into the identity matrix.
3.  If $A$ is invertible, the process will yield $[I | A^{-1}]$. If $A$ is singular, you will not be able to transform the left side into $I$ (it will result in a row of zeros) [source: ma2001-lecture-chapter2-pdf#section-7, ma2001-cheatsheet-cheatsheet-pdf#section-1].

**Example: Finding an Inverse**
Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 3 \\ 1 & 0 & 8 \end{pmatrix}$.
Form the augmented matrix $[A | I]$:
$\left[ \begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 2 & 5 & 3 & 0 & 1 & 0 \\ 1 & 0 & 8 & 0 & 0 & 1 \end{array} \right]$
Perform Gauss-Jordan Elimination:
*   $R_2 \to R_2 - 2R_1$, $R_3 \to R_3 - R_1$:
    $\left[ \begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & -3 & -2 & 1 & 0 \\ 0 & -2 & 5 & -1 & 0 & 1 \end{array} \right]$
*   $R_3 \to R_3 + 2R_2$:
    $\left[ \begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & -3 & -2 & 1 & 0 \\ 0 & 0 & -1 & -5 & 2 & 1 \end{array} \right]$
*   $R_3 \to -R_3$:
    $\left[ \begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & -3 & -2 & 1 & 0 \\ 0 & 0 & 1 & 5 & -2 & -1 \end{array} \right]$
*   $R_2 \to R_2 + 3R_3$, $R_1 \to R_1 - 3R_3$:
    $\left[ \begin{array}{ccc|ccc} 1 & 2 & 0 & -14 & 6 & 3 \\ 0 & 1 & 0 & 13 & -5 & -3 \\ 0 & 0 & 1 & 5 & -2 & -1 \end{array} \right]$
*   $R_1 \to R_1 - 2R_2$:
    $\left[ \begin{array}{ccc|ccc} 1 & 0 & 0 & -40 & 16 & 9 \\ 0 & 1 & 0 & 13 & -5 & -3 \\ 0 & 0 & 1 & 5 & -2 & -1 \end{array} \right]$
Thus, $A^{-1} = \begin{pmatrix} -40 & 16 & 9 \\ 13 & -5 & -3 \\ 5 & -2 & -1 \end{pmatrix}$ [source: ma2001-lecture-chapter2-pdf#section-7, ma2001-tutorial-tutorial3-pdf#section-2].

### Checking for Invertibility (without finding the full inverse)

A square matrix $A$ is invertible if and only if its row-echelon form (or reduced row-echelon form) has *no zero rows*. If a row-echelon form of $A$ has at least one zero row, then $A$ is singular [source: ma2001-lecture-chapter2-pdf#section-7].
For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $A$ is invertible if and only if $ad - bc \ne 0$. This condition implies that the RREF of $A$ will be $I$. If $ad - bc = 0$, the RREF will have a row of zeros, making $A$ singular [source: ma2001-lecture-chapter2-pdf#section-7].

### Theorem: Unilateral Condition for Inverse

Let $A$ and $B$ be square matrices of the same size. If $AB = I$, then the following are true:
1.  $A$ is invertible.
2.  $B$ is invertible.
3.  $A^{-1} = B$.
4.  $B^{-1} = A$.
5.  $BA = I$.

This theorem is powerful because it states that for square matrices, if one multiplication ($AB$ or $BA$) yields the identity matrix, the other multiplication *must also* yield the identity, and the matrices are inverses of each other [source: ma2001-lecture-chapter2-pdf#section-7].

**Proof:**
Consider the linear system $Bx = 0$.
If $Bx = 0$, then $A(Bx) = A(0) \implies (AB)x = 0 \implies Ix = 0 \implies x = 0$.
Since the linear system $Bx = 0$ has only the trivial solution, by the equivalence theorem (statement 2 above), $B$ is invertible [source: ma2001-lecture-chapter2-pdf#section-7].
Since $B$ is invertible, $B^{-1}$ exists.
Given $AB = I$, post-multiply by $B^{-1}$: $ABB^{-1} = IB^{-1} \implies AI = B^{-1} \implies A = B^{-1}$.
Since $A = B^{-1}$, it follows that $A$ is invertible and $A^{-1} = (B^{-1})^{-1} = B$ (using inverse property 1).
Finally, substituting $A^{-1} = B$ into $BA = I$ (from definition), we get $BA = I$ [source: ma2001-lecture-chapter2-pdf#section-7].

### Working with Invertible Matrices in Equations

Sometimes, the inverse of a matrix can be found or properties deduced from a matrix equation.
**Example:** Suppose $A$ is a square matrix such that $A^2 - 3A - 6I = 0$.
We can rearrange this equation to find $A^{-1}$:
$A^2 - 3A = 6I$
Factor out $A$ on the left side:
$A(A - 3I) = 6I$
To obtain the identity matrix on the right, divide by $6$:
$A \left( \frac{1}{6}(A - 3I) \right) = I$
By the unilateral condition theorem, since $A \left( \frac{1}{6}(A - 3I) \right) = I$, $A$ is invertible and its inverse is $A^{-1} = \frac{1}{6}(A - 3I)$ [source: ma2001-lecture-chapter2-pdf#section-7].

### Singular Matrices and Products

Let $A$ and $B$ be square matrices of the same size. If $A$ is singular, then both $AB$ and $BA$ are also singular [source: ma2001-lecture-chapter2-pdf#section-7].
**Proof (for AB being singular):** Assume for contradiction that $AB$ is invertible. Then $(AB)^{-1}$ exists.
We know that $(AB)^{-1}(AB) = I$.
This implies that $B(AB)^{-1}A = I$
But then $A$ would be invertible with inverse $B(AB)^{-1}$. This contradicts our initial assumption that $A$ is singular. Therefore, $AB$ must be singular. A similar proof applies to $BA$.

### Elementary Column Operations

Just as elementary row operations can be represented by pre-multiplication with elementary matrices, **elementary column operations** can be represented by **post-multiplication** with elementary matrices. If $A$ is an $m \times n$ matrix and $E$ is an $n \times n$ elementary matrix, then $AE$ is the matrix obtained from $A$ by performing an elementary column operation [source: ma2001-lecture-chapter2-pdf#section-7].

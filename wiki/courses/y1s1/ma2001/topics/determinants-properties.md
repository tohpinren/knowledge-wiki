---
page_id: "y1s1-ma2001-determinants-properties"
title: "Determinants and their Properties"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Calculation methods for determinants (cofactor expansion, row reduction) and their properties, including relation to invertibility."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter2-pdf#section-4"
  - "ma2001-hw2-hw2-q-pdf#section-1"
  - "ma2001-tutorial-tutorial4-pdf#section-1"
  - "ma2001-cheatsheet-cheatsheet-pdf#section-3"
topics:
  - "matrix"
  - "example"
  - "matrices"
  - "det"
  - "invertible"
  - "square"
  - "row"
  - "examples"
  - "points"
  - "question"
source_count: 4
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Determinants and their Properties

This page details the definition, calculation methods, and fundamental properties of determinants, emphasizing their crucial role in determining matrix invertibility and solving linear systems. This content corresponds to Section 2.5 of the MA2001 module [source:ma2001-lecture-chapter2-pdf#section-2].

## Introduction to Determinants

For a square matrix, a special scalar value called its **determinant** can be computed. This value is instrumental in determining whether the matrix is [[invertible-elementary-matrices#Invertible Matrices|invertible]] [source:ma2001-lecture-chapter2-pdf#section-2].

Given an $n \times n$ matrix $A = (a_{ij})$ [source:ma2001-lecture-chapter2-pdf#section-2]:

1.  If $n=1$, i.e., $A = [a_{11}]$, then $\det(A) = a_{11}$ [source:ma2001-lecture-chapter2-pdf#section-2].
2.  If $n > 1$, the determinant is defined recursively using **minors** and **cofactors** [source:ma2001-lecture-chapter2-pdf#section-2].

The determinant of a matrix $A$ can be denoted as $\det(A)$ or by writing the matrix entries between vertical bars (e.g., $|A|$) [source:ma2001-lecture-chapter2-pdf#section-2].

### Minors and Cofactors

For an $n \times n$ matrix $A$:

*   The **minor** $M_{ij}$ is the $(n-1) \times (n-1)$ matrix obtained by deleting the $i$-th row and $j$-th column of $A$ [source:ma2001-lecture-chapter2-pdf#section-2].
*   The **$(i, j)$-cofactor** $A_{ij}$ is defined as $A_{ij} = (-1)^{i+j} \det(M_{ij})$ [source:ma2001-lecture-chapter2-pdf#section-2].

### Determinant of a $2 \times 2$ Matrix

For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the determinant is given by the formula:
$\det(A) = ad - bc$ [source:ma2001-lecture-chapter2-pdf#section-2].

This formula is derived from cofactor expansion along the first row:
$\det(A) = a_{11}A_{11} + a_{12}A_{12}$
$A_{11} = (-1)^{1+1} \det(M_{11}) = (1) \det([d]) = d$ [source:ma2001-lecture-chapter2-pdf#section-2].
$A_{12} = (-1)^{1+2} \det(M_{12}) = (-1) \det([c]) = -c$ [source:ma2001-lecture-chapter2-pdf#section-2].
So, $\det(A) = a_{11}d + a_{12}(-c) = ad - bc$ [source:ma2001-lecture-chapter2-pdf#section-2].

## Cofactor Expansion

The determinant of an $n \times n$ matrix $A$ can be calculated by **cofactor expansion** along any row or any column [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].

For any row $i \in \{1, 2, \dots, n\}$:
$\det(A) = a_{i1}A_{i1} + a_{i2}A_{i2} + \dots + a_{in}A_{in}$ (Cofactor expansion along the $i$-th row) [source:ma2001-lecture-chapter2-pdf#section-2].

For any column $j \in \{1, 2, \dots, n\}$:
$\det(A) = a_{1j}A_{1j} + a_{2j}A_{2j} + \dots + a_{nj}A_{nj}$ (Cofactor expansion along the $j$-th column) [source:ma2001-lecture-chapter2-pdf#section-2].

**Example:**
For a $3 \times 3$ matrix $B = \begin{pmatrix} -3 & -2 & 4 \\ 4 & 3 & 1 \\ 0 & 2 & 4 \end{pmatrix}$, expanding along the first row [source:ma2001-lecture-chapter2-pdf#section-2]:
$\det(B) = (-3) \det \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} - (-2) \det \begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix} + (4) \det \begin{pmatrix} 4 & 3 \\ 0 & 2 \end{pmatrix}$
$= (-3)(3 \cdot 4 - 1 \cdot 2) + 2(4 \cdot 4 - 1 \cdot 0) + 4(4 \cdot 2 - 3 \cdot 0)$
$= (-3)(10) + 2(16) + 4(8)$
$= -30 + 32 + 32 = 34$ [source:ma2001-lecture-chapter2-pdf#section-2].

Alternatively, expanding along the second column [source:ma2001-lecture-chapter2-pdf#section-2]:
$\det(B) = (-2) A_{12} + (3) A_{22} + (2) A_{32}$
$A_{12} = (-1)^{1+2} \det \begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix} = -1(16) = -16$
$A_{22} = (-1)^{2+2} \det \begin{pmatrix} -3 & 4 \\ 0 & 4 \end{pmatrix} = 1(-12) = -12$
$A_{32} = (-1)^{3+2} \det \begin{pmatrix} -3 & 4 \\ 4 & 1 \end{pmatrix} = -1(-3 - 16) = 19$
$\det(B) = (-2)(-16) + (3)(-12) + (2)(19) = 32 - 36 + 38 = 34$ [source:ma2001-lecture-chapter2-pdf#section-2].

For $3 \times 3$ matrices, Sarrus' rule provides a diagrammatic method for calculation, but this method **cannot be generalized to higher-order matrices** [source:ma2001-lecture-chapter2-pdf#section-2].

## Geometric Interpretation of Determinants

*   For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the absolute value of its determinant, $|\det(A)| = |ad - bc|$, represents the **area of the parallelogram** formed by the vectors $(a, c)$ and $(b, d)$ (or $(a, b)$ and $(c, d)$) starting from the origin [source:ma2001-lecture-chapter2-pdf#section-2].
*   For a $3 \times 3$ matrix, the absolute value of its determinant represents the **volume of the parallelepiped** formed by its column (or row) vectors [source:ma2001-lecture-chapter2-pdf#section-2].

## Properties of Determinants

Determinants have several important properties that simplify their calculation and highlight their relationship with matrix operations [source:ma2001-cheatsheet-cheatsheet-pdf#section-3].

### Determinant of Triangular Matrices

If $A$ is a square [[matrix-operations#Triangular Matrices|triangular matrix]] (upper, lower, or diagonal), then its determinant is the product of its diagonal entries ($a_{11}a_{22}\dots a_{nn}$) [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].

**Examples:**
*   $\det(I) = 1 \cdot 1 \cdot \dots \cdot 1 = 1$ for an identity matrix $I$ [source:ma2001-lecture-chapter2-pdf#section-2].
*   $\det \begin{pmatrix} -2 & 3.5 & 2 \\ 0 & 5 & -26 \\ 0 & 0 & 2 \end{pmatrix} = (-2) \cdot 5 \cdot 2 = -20$ [source:ma2001-lecture-chapter2-pdf#section-2].

### Determinant of Transpose

For any square matrix $A$, the determinant of its transpose is equal to the determinant of the original matrix:
$\det(A^T) = \det(A)$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].

### Determinants with Identical Rows or Columns

If a square matrix $A$ has two identical rows or two identical columns, its determinant is zero [source:ma2001-lecture-chapter2-pdf#section-2].

**Examples:**
*   $\det \begin{pmatrix} 4 & -2 \\ 4 & -2 \end{pmatrix} = 0$
*   $\det \begin{pmatrix} 1 & 2 & 4 \\ -1 & 10 & 4 \\ 1 & 2 & 4 \end{pmatrix} = 0$ (Row 1 and Row 3 are identical) [source:ma2001-lecture-chapter2-pdf#section-2].

### Effect of Elementary Row Operations on Determinants

Elementary row operations change the determinant in predictable ways [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3]:

1.  **Multiplying a row by a constant $k$**: If $B$ is obtained from $A$ by multiplying a row by a constant $k$, then $\det(B) = k \det(A)$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   Equivalently, $\det(E) = k$ for the elementary matrix $E$ representing this operation [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].
2.  **Interchanging two rows**: If $B$ is obtained from $A$ by interchanging two rows, then $\det(B) = -\det(A)$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   Equivalently, $\det(E) = -1$ for the elementary matrix $E$ representing this operation [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].
3.  **Adding a multiple of one row to another row**: If $B$ is obtained from $A$ by adding $k$ times one row to another row, then $\det(B) = \det(A)$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   Equivalently, $\det(E) = 1$ for the elementary matrix $E$ representing this operation [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].

These properties can be summarized by the relationship $\det(EA) = \det(E)\det(A)$ for an elementary matrix $E$ [source:ma2001-lecture-chapter2-pdf#section-2]. Similar rules apply to [[matrix-operations#Elementary Column Operations|elementary column operations]] [source:ma2001-lecture-chapter2-pdf#section-2].

### Determinant of Scalar Multiplication

If $A$ is an $n \times n$ matrix and $c$ is a scalar, then:
$\det(cA) = c^n \det(A)$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].
It is generally **false** that $\det(cA) = c \det(A)$ unless $n=1$.

### Determinant of Matrix Multiplication

For two square matrices $A$ and $B$ of the same size, the determinant of their product is the product of their determinants:
$\det(AB) = \det(A)\det(B)$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].
A related property often tested is $\det(AB) = \det(BA)$, which is true if both products are defined, because $\det(A)\det(B) = \det(B)\det(A)$. However, $AB$ is not necessarily equal to $BA$ (matrix multiplication is not commutative).

### Determinant of an Inverse

If $A$ is an [[invertible-elementary-matrices#Invertible Matrices|invertible matrix]], then:
$\det(A^{-1}) = \frac{1}{\det(A)}$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].

This property follows directly from $\det(AA^{-1}) = \det(I) = 1$. Since $\det(AA^{-1}) = \det(A)\det(A^{-1})$, we get $\det(A)\det(A^{-1}) = 1$, implying $\det(A^{-1}) = 1/\det(A)$ [source:ma2001-lecture-chapter2-pdf#section-2].

## Determinants and Matrix Invertibility

A square matrix $A$ is **invertible** if and only if its determinant is non-zero ($\det(A) \neq 0$) [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3]. If $\det(A) = 0$, the matrix $A$ is called **singular** (non-invertible) [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].

This relationship is part of a fundamental theorem regarding invertible square matrices [source:ma2001-cheatsheet-cheatsheet-pdf#section-3]:
For a square matrix $A$, the following statements are equivalent [source:ma2001-lecture-chapter2-pdf#section-2]:
1.  $A$ is invertible.
2.  The [[linear-systems-solution-types#Homogeneous Systems|homogeneous linear system]] $A\mathbf{x} = \mathbf{0}$ has only the trivial solution ($\mathbf{x} = \mathbf{0}$).
3.  The [[gaussian-elimination-rref#Reduced Row Echelon Form (RREF)|reduced row-echelon form]] of $A$ is the identity matrix $I$.
4.  $A$ can be expressed as a product of [[invertible-elementary-matrices#Elementary Matrices|elementary matrices]].
5.  $\det(A) \neq 0$.
6.  The rows/columns of $A$ form a [[linear-independence-bases#Basis|basis]] for $\mathbb{R}^n$.
7.  $A$ has [[dimension-rank-nullity#Rank|full rank]].
8.  $0$ is not an [[eigenvalues-eigenvectors#Eigenvalues|eigenvalue]] of $A$.

If $A$ is singular, then both $AB$ and $BA$ are also singular for any square matrix $B$ of the same size [source:ma2001-lecture-chapter2-pdf#section-2].

## Calculating Determinants via Row Reduction

The properties of elementary row operations on determinants allow for an efficient method to compute determinants by transforming the matrix into a triangular form using [[gaussian-elimination-rref#Gaussian Elimination|Gaussian elimination]] [source:ma2001-lecture-chapter2-pdf#section-2].

1.  Apply elementary row operations to transform $A$ into a triangular matrix $U$ (or $L$).
2.  Keep track of how each operation changes the determinant:
    *   Swapping rows: Multiply current determinant by $-1$.
    *   Multiplying a row by $k$: Divide current determinant by $k$.
    *   Adding a multiple of one row to another: Does not change the determinant.
3.  The determinant of the triangular matrix is the product of its diagonal entries.
4.  Adjust this product by the factors recorded in step 2 to find $\det(A)$.

**Example:**
To find $\det(A)$ for $A = \begin{pmatrix} 3 & -1 & 1 & 1 \\ 3 & -1 & 2 & 1 \\ 0 & 2 & 4 & 0 \\ 0 & 0 & 2 & -1 \end{pmatrix}$ [source:ma2001-lecture-chapter2-pdf#section-2]:
$\det(A) = \det \begin{pmatrix} 3 & -1 & 1 & 1 \\ 3 & -1 & 2 & 1 \\ 0 & 2 & 4 & 0 \\ 0 & 0 & 2 & -1 \end{pmatrix}$
$R_2 - R_1 \rightarrow R_2$ (no change to det)
$= \det \begin{pmatrix} 3 & -1 & 1 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 2 & 4 & 0 \\ 0 & 0 & 2 & -1 \end{pmatrix}$
$R_2 \leftrightarrow R_3$ (multiply by $-1$)
$= - \det \begin{pmatrix} 3 & -1 & 1 & 1 \\ 0 & 2 & 4 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 2 & -1 \end{pmatrix}$
$R_4 - 2R_3 \rightarrow R_4$ (no change to det)
$= - \det \begin{pmatrix} 3 & -1 & 1 & 1 \\ 0 & 2 & 4 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$
This is a triangular matrix. Its determinant is the product of diagonal entries $(3)(2)(1)(-1) = -6$.
So, $\det(A) = -(-6) = 6$ [source:ma2001-lecture-chapter2-pdf#section-2].

## Adjoint Matrix and Inverse Formula

The **(classical) adjoint** of an $n \times n$ matrix $A$, denoted $\text{adj}(A)$, is the transpose of the matrix of its cofactors [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].
$\text{adj}(A) = \begin{pmatrix} A_{11} & A_{12} & \dots & A_{1n} \\ A_{21} & A_{22} & \dots & A_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{n1} & A_{n2} & \dots & A_{nn} \end{pmatrix}^T = \begin{pmatrix} A_{11} & A_{21} & \dots & A_{n1} \\ A_{12} & A_{22} & \dots & A_{n2} \\ \vdots & \vdots & \ddots & \vdots \\ A_{1n} & A_{2n} & \dots & A_{nn} \end{pmatrix}$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].

If $A$ is an invertible matrix, its inverse can be found using the adjoint matrix:
$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$ [source:ma2001-lecture-chapter2-pdf#section-2, ma2001-cheatsheet-cheatsheet-pdf#section-3].

**Example for $2 \times 2$ matrix:**
For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the cofactors are:
$A_{11} = d$, $A_{12} = -c$
$A_{21} = -b$, $A_{22} = a$ [source:ma2001-lecture-chapter2-pdf#section-2].
So, the cofactor matrix is $\begin{pmatrix} d & -c \\ -b & a \end{pmatrix}$.
The adjoint is $\text{adj}(A) = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix}^T = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ [source:ma2001-lecture-chapter2-pdf#section-2].
Thus, $A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, assuming $ad - bc \neq 0$ [source:ma2001-lecture-chapter2-pdf#section-2].

**Properties of the Adjoint Matrix** (from [[ma2001-tutorial-tutorial4-pdf#section-4|Tutorial 4, Question 5]]):
Let $A$ be an invertible matrix of order $n \geq 2$.
1.  $\text{adj}(A)$ is invertible.
2.  $\det(\text{adj}(A)) = (\det(A))^{n-1}$.
3.  $\text{adj}(A^{-1}) = (\text{adj}(A))^{-1} = \frac{1}{\det(A)} A$.
4.  If $\det(A)=1$, then $\text{adj}(\text{adj}(A)) = A$.

## Cramer's Rule

**Cramer's Rule** provides a method to find the unique solution of a [[linear-systems-intro#System of Linear Equations|system of linear equations]] $A\mathbf{x} = \mathbf{b}$ if $A$ is an invertible matrix [source:ma2001-lecture-chapter2-pdf#section-2].

Given a linear system $A\mathbf{x} = \mathbf{b}$, where $A = (a_{ij})$ is an $n \times n$ invertible matrix, $\mathbf{x} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$, and $\mathbf{b} = \begin{pmatrix} b_1 \\ \vdots \\ b_n \end{pmatrix}$ [source:ma2001-lecture-chapter2-pdf#section-2].

Let $A_i$ be the $n \times n$ matrix obtained by replacing the $i$-th column of $A$ with the vector $\mathbf{b}$ [source:ma2001-lecture-chapter2-pdf#section-2].
Then the unique solution $\mathbf{x}$ is given by:
$x_i = \frac{\det(A_i)}{\det(A)}$ for $i = 1, 2, \dots, n$ [source:ma2001-lecture-chapter2-pdf#section-2].

**Example:**
Consider the linear system [source:ma2001-lecture-chapter2-pdf#section-2]:
$x + y + 3z = 0$
$2x - 2y + 2z = 4$
$3x + 9y = 3$

In matrix form, $A\mathbf{x} = \mathbf{b}$:
$\begin{pmatrix} 1 & 1 & 3 \\ 2 & -2 & 2 \\ 3 & 9 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 4 \\ 3 \end{pmatrix}$ [source:ma2001-lecture-chapter2-pdf#section-2].

First, calculate $\det(A)$:
$\det(A) = 1(0 - 18) - 1(0 - 6) + 3(18 - (-6)) = -18 + 6 + 3(24) = -12 + 72 = 60$.

Now, form $A_x, A_y, A_z$:
$A_x = \begin{pmatrix} 0 & 1 & 3 \\ 4 & -2 & 2 \\ 3 & 9 & 0 \end{pmatrix}$, $A_y = \begin{pmatrix} 1 & 0 & 3 \\ 2 & 4 & 2 \\ 3 & 3 & 0 \end{pmatrix}$, $A_z = \begin{pmatrix} 1 & 1 & 0 \\ 2 & -2 & 4 \\ 3 & 9 & 3 \end{pmatrix}$ [source:ma2001-lecture-chapter2-pdf#section-2].

Calculate their determinants:
$\det(A_x) = 0 - 1(0 - 6) + 3(36 - (-6)) = 6 + 3(42) = 6 + 126 = 132$ [source:ma2001-lecture-chapter2-pdf#section-2].
$\det(A_y) = 1(0 - 6) - 0 + 3(6 - 12) = -6 + 3(-6) = -6 - 18 = -24$ [source:ma2001-lecture-chapter2-pdf#section-2].
$\det(A_z) = 1(-6 - 36) - 1(6 - 12) + 0 = -42 - 1(-6) = -42 + 6 = -36$ [source:ma2001-lecture-chapter2-pdf#section-2].

Finally, apply Cramer's Rule:
$x = \frac{\det(A_x)}{\det(A)} = \frac{132}{60} = 2.2$ [source:ma2001-lecture-chapter2-pdf#section-2].
$y = \frac{\det(A_y)}{\det(A)} = \frac{-24}{60} = -0.4$ [source:ma2001-lecture-chapter2-pdf#section-2].
$z = \frac{\det(A_z)}{\det(A)} = \frac{-36}{60} = -0.6$ [source:ma2001-lecture-chapter2-pdf#section-2].

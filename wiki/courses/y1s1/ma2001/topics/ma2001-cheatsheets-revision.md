---
page_id: "y1s1-ma2001-ma2001-cheatsheets-revision"
title: "MA2001 Cheatsheets & Revision Guides"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Curated cheatsheets and revision materials summarizing key linear algebra concepts for MA2001."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-cheatsheet-cheatsheet-pdf#section-1"
  - "ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-1"
  - "ma2001-ma2001-pdf#section-1"
  - "ma2001-revision-pdf#section-1"
topics:
  - "det"
  - "basis"
  - "rank"
  - "span"
  - "orthogonal"
  - "matrix"
  - "matrices"
  - "properties"
  - "space"
  - "vector"
source_count: 4
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# MA2001 Cheatsheets & Revision Guides

This page provides a curated collection of cheatsheets and revision materials summarizing key linear algebra concepts for MA2001.

***

### 1. Systems of Linear Equations

A **system of linear equations** (or a **linear system**) is a finite set of linear equations involving variables $x_1, x_2, \ldots, x_n$ [source: ma2001-revision-pdf#section-1]. Such systems can have:
*   **No solution** (inconsistent system)
*   **Exactly one solution** (consistent system, unique solution)
*   **Infinitely many solutions** (consistent system) [source: ma2001-revision-pdf#section-2, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-1].

**Representation of Linear Systems**:
A general form of a linear system is:
$a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n = b_1$
$a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n = b_2$
$\vdots$
$a_{m1}x_1 + a_{m2}x_2 + \ldots + a_{mn}x_n = b_m$
where $a_{ij}$ and $b_i$ are real constants [source: ma2001-revision-pdf#section-2].

*   **Augmented Matrix**: A system of linear equations can be represented by a rectangular array of numbers called an **augmented matrix** [source: ma2001-revision-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-1].
    $ \begin{pmatrix} a_{11} & a_{12} & \ldots & a_{1n} & | & b_1 \\ a_{21} & a_{22} & \ldots & a_{2n} & | & b_2 \\ \vdots & \vdots & \ddots & \vdots & | & \vdots \\ a_{m1} & a_{m2} & \ldots & a_{mn} & | & b_m \end{pmatrix} $
*   **Matrix Formulation (Ax = b)**: The linear system can be written in the form $Ax = b$, where $A$ is the coefficient matrix, $x$ is the column vector of variables, and $b$ is the column vector of constants. The augmented matrix is then denoted as $(A | b)$ [source: ma2001-revision-pdf#section-4].

**Elementary Row Operations (EROs)**
Elementary row operations transform a matrix $A$ into a row-equivalent matrix $B$. These operations are used to simplify systems of linear equations without changing their solution set [source: ma2001-revision-pdf#section-5, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-1].
The three types of EROs are:
1.  **Multiplying a row by a non-zero constant $k$**: $kR_i \to R_i$ [source: ma2001-revision-pdf#section-5].
2.  **Interchanging two rows $i$ and $j$**: $R_i \leftrightarrow R_j$ [source: ma2001-revision-pdf#section-6].
3.  **Adding $k$ times row $i$ to row $j$**: $R_j + kR_i \to R_j$ [source: ma2001-revision-pdf#section-7].
These operations can be represented by elementary matrices $E_k, \ldots, E_1$ such that $E_k \ldots E_1 A = B$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].

**Gaussian Elimination and Gauss-Jordan Elimination**
*   **Gaussian Elimination** is an algorithm that reduces a matrix to its **row-echelon form (REF)** using EROs. In REF, leading entries (pivot points) move rightwards in successive rows, rows with all zeros are at the bottom, and columns containing leading entries have zeros below them [source: ma2001-revision-pdf#section-8].
*   **Gauss-Jordan Elimination** further reduces a matrix to its **reduced row-echelon form (RREF)**. In RREF, all leading entries are 1, and each leading 1 is the only non-zero entry in its column [source: ma2001-revision-pdf#section-9].

**Types of Solutions from RREF**
To determine the solution type of $Ax=b$, apply Gaussian Elimination to the augmented matrix $(A|b)$ to obtain $(R|b')$ in row-echelon form [source: ma2001-revision-pdf#section-10].
*   **No solution (Inconsistent System)**: The system has no solution if the last column of $(R|b')$ is a pivot column. This means there is a row of the form $[0 \ 0 \ \ldots \ 0 \ | \ \gamma]$ where $\gamma \neq 0$ [source: ma2001-revision-pdf#section-11, ma2001-ma2001-pdf#section-1].
*   **Unique Solution (Consistent System)**: The system has only one solution if the last column of $(R|b')$ is not a pivot column, and every column of $R$ is a pivot column (i.e., the number of non-zero rows equals the number of variables) [source: ma2001-revision-pdf#section-12, ma2001-ma2001-pdf#section-1].
*   **Infinitely Many Solutions (Consistent System)**: The system has infinitely many solutions if the last column of $(R|b')$ is not a pivot column, and $R$ has at least one non-pivot column (i.e., the number of non-zero rows is less than the number of variables). The number of free parameters equals the number of variables minus the number of non-zero rows [source: ma2001-revision-pdf#section-13, ma2001-ma2001-pdf#section-1].

**Homogeneous Linear Systems**
A linear system $Ax=0$ is called a **homogeneous linear system** [source: ma2001-revision-pdf#section-14].
*   The vector $x=0$ is always a solution, called the **trivial solution**.
*   A homogeneous system either has only the trivial solution or infinitely many solutions (non-trivial solutions) [source: ma2001-revision-pdf#section-14, ma2001-ma2001-pdf#section-1].

The system $Ax=b$ is **consistent** if and only if $b$ lies in the [[row-column-nullspace#Column Space|column space]] of $A$ [source: ma2001-revision-pdf#section-47]. If $x=v$ is a particular solution to $Ax=b$, then the general solution is $x = u+v$, where $u$ is the general solution to the homogeneous system $Ax=0$ (i.e., $u$ is in the [[row-column-nullspace#Nullspace|nullspace]] of $A$) [source: ma2001-revision-pdf#section-47, ma2001-cheatsheet-cheatsheet-pdf#section-3].

### 2. Matrix Operations and Types

A matrix $A$ is denoted as $(a_{ij})_{m \times n}$, where $m$ is the number of rows and $n$ is the number of columns.

**Matrix Addition and Scalar Multiplication**
*   **Addition**: For $A=(a_{ij})_{m \times n}$ and $B=(b_{ij})_{m \times n}$, $A+B = (a_{ij}+b_{ij})_{m \times n}$ [source: ma2001-revision-pdf#section-15].
*   **Scalar Multiplication**: For a constant $c$, $cA = (ca_{ij})_{m \times n}$ [source: ma2001-revision-pdf#section-15].

**Matrix Multiplication**
For $A=(a_{ij})_{m \times p}$ and $B=(b_{ij})_{p \times n}$, the product $AB = (ab_{ij})_{m \times n}$ where $ab_{ij} = \sum_{k=1}^{p} a_{ik}b_{kj}$ [source: ma2001-revision-pdf#section-16, ma2001-cheatsheet-cheatsheet-pdf#section-1].
Properties:
*   Matrix multiplication is **associative** ($A(BC) = (AB)C$) and **distributive** ($A(B+C) = AB+AC$, $(A+B)C = AC+BC$) [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].
*   For square matrix $A$, $A^m A^n = A^{m+n}$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].
*   Matrix multiplication is generally **not commutative** ($AB \neq BA$) [source: ma2001-revision-pdf#section-16].
*   $AB=0$ does not necessarily imply $A=0$ or $B=0$ [source: ma2001-revision-pdf#section-16].

**Transposes and Powers of Matrices**
*   **Transpose**: The transpose of $A=(a_{ij})$, denoted $A^T$ (or $A^t$), is the matrix whose $(i,j)$-entry is $a_{ji}$. The rows of $A$ become the columns of $A^T$ and vice versa [source: ma2001-revision-pdf#section-18].
    *   Properties: $(A^T)^T = A$, $(A+B)^T = A^T+B^T$, $(AB)^T = B^T A^T$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].
*   **Powers**: For a square matrix $A$ and non-negative integer $k$:
    *   $A^k = I$ if $k=0$
    *   $A^k = A \cdot A \ldots A$ ($k$ times) if $k \geq 1$ [source: ma2001-revision-pdf#section-18].
    *   If $A$ is invertible and $k>0$, then $A^{-k} = (A^{-1})^k$ [source: ma2001-revision-pdf#section-18].

**Invertible Matrices**
A square matrix $A$ of order $n$ is **invertible** if there exists a square matrix $B$ of order $n$ such that $AB=I$ and $BA=I$. Matrix $B$ is called the **inverse** of $A$, denoted $A^{-1}$ [source: ma2001-revision-pdf#section-19].
*   A square matrix is **singular** if it has no inverse [source: ma2001-revision-pdf#section-19].
*   **Properties for invertible $A, B$ and non-zero scalar $c$**:
    1.  $(cA)^{-1} = (1/c)A^{-1}$ [source: ma2001-revision-pdf#section-19].
    2.  $(A^T)^{-1} = (A^{-1})^T$ [source: ma2001-revision-pdf#section-19].
    3.  $(A^{-1})^{-1} = A$ [source: ma2001-revision-pdf#section-19].
    4.  $(AB)^{-1} = B^{-1}A^{-1}$ [source: ma2001-revision-pdf#section-19, ma2001-cheatsheet-cheatsheet-pdf#section-1].

**Equivalency Statements for Invertible Square Matrices**:
For an $n \times n$ matrix $A$, the following statements are equivalent [source: ma2001-revision-pdf#section-20, ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-ma2001-pdf#section-8]:
1.  $A$ is invertible.
2.  The linear system $Ax=0$ has only the trivial solution.
3.  The [[gaussian-elimination-rref#Reduced Row-Echelon Form|reduced row-echelon form]] of $A$ is the identity matrix $I$.
4.  $A$ can be expressed as a product of elementary matrices.
5.  $\det(A) \neq 0$.
6.  The rows of $A$ form a [[linear-independence-bases#Bases|basis]] for $R^n$.
7.  The columns of $A$ form a basis for $R^n$.
8.  $\text{rank}(A) = n$ (i.e., $A$ has full rank).
9.  $0$ is not an [[eigenvalues-eigenvectors#Eigenvalues|eigenvalue]] of $A$.

If $AB=I$ for square matrices $A, B$ of the same size, then $A$ and $B$ are both invertible, $A^{-1}=B$, $B^{-1}=A$, and $BA=I$ [source: ma2001-revision-pdf#section-21].

**Finding Inverses**:
To find the inverse of an invertible matrix $A$, use Gauss-Jordan Elimination on the augmented matrix $(A|I)$ to obtain $(I|A^{-1})$ [source: ma2001-revision-pdf#section-22, ma2001-cheatsheet-cheatsheet-pdf#section-1].
To check if a square matrix $A$ is invertible, reduce $A$ to its row-echelon form $R$. If $R$ has no zero row, then $A$ is invertible; otherwise, $A$ is singular [source: ma2001-revision-pdf#section-22].

### 3. Determinants

The **determinant** of a square matrix is a scalar value that can be computed from its entries.

*   **2x2 Matrix**: For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $\det(A) = ad - bc$ [source: ma2001-revision-pdf#section-23].
*   **3x3 Matrix (Sarrus' Rule)**: For $A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}$, $\det(A) = aei + bfg + cdh - ceg - afh - bdi$. This method cannot be generalized to higher orders [source: ma2001-revision-pdf#section-23].
*   **Cofactor Expansion**: For an $n \times n$ matrix $A=(a_{ij})$, let $M_{ij}$ be the $(n-1) \times (n-1)$ matrix obtained by deleting row $i$ and column $j$. The $(i,j)$-cofactor is $A_{ij} = (-1)^{i+j} \det(M_{ij})$.
    The determinant of $A$ can be found by expanding along any row $i$ or column $j$:
    $\det(A) = a_{i1}A_{i1} + a_{i2}A_{i2} + \ldots + a_{in}A_{in}$ (row expansion)
    $\det(A) = a_{1j}A_{1j} + a_{2j}A_{2j} + \ldots + a_{nj}A_{nj}$ (column expansion) [source: ma2001-revision-pdf#section-24, ma2001-cheatsheet-cheatsheet-pdf#section-1].

**Properties of Determinants**:
*   **Elementary Row Operations**:
    1.  Multiplying a row by $k$: $\det(B_1) = k \det(A)$ [source: ma2001-revision-pdf#section-25].
    2.  Interchanging two rows: $\det(B_2) = - \det(A)$ [source: ma2001-revision-pdf#section-25].
    3.  Adding a multiple of one row to another: $\det(B_3) = \det(A)$ [source: ma2001-revision-pdf#section-25].
*   For a **triangular matrix** (upper or lower), $\det(A)$ is the product of its diagonal entries [source: ma2001-revision-pdf#section-25, ma2001-ma2001-pdf#section-3].
*   **General Properties for invertible matrices $A, B$ and non-zero scalar $c$**:
    1.  $\det(A) = \det(A^T)$ [source: ma2001-revision-pdf#section-26].
    2.  $\det(cA) = c^n \det(A)$ for an $n \times n$ matrix $A$ [source: ma2001-revision-pdf#section-26].
    3.  $\det(AB) = \det(A)\det(B)$ [source: ma2001-revision-pdf#section-26, ma2001-cheatsheet-cheatsheet-pdf#section-1].
    4.  If $A$ is invertible, $\det(A^{-1}) = 1/\det(A)$ [source: ma2001-revision-pdf#section-26, ma2001-cheatsheet-cheatsheet-pdf#section-1].

**Adjoint Matrix**:
The adjoint of $A$, denoted $\text{adj}(A)$, is the transpose of the cofactor matrix. $\text{adj}(A)_{ij} = A_{ji}$.
$A \text{adj}(A) = \det(A)I$. If $\det(A) \neq 0$, then $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].
**Cramer's Rule**: For $Ax=b$, $x_n = \frac{\det(A \text{ with n-th col replaced by } b)}{\det(A)}$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].

### 4. Vector Spaces and Subspaces

**Euclidean n-space ($\mathbb{R}^n$)**
The Euclidean $n$-space, or simply $n$-space, is the set $\mathbb{R}^n = \{(u_1, u_2, \ldots, u_n) | u_1, u_2, \ldots, u_n \in \mathbb{R}\}$. A vector in $\mathbb{R}^n$ can be identified as a matrix [source: ma2001-revision-pdf#section-27].
*   **Row vector**: $(u_1, u_2, \ldots, u_n)$ (a $1 \times n$ matrix).
*   **Column vector**: $(u_1, u_2, \ldots, u_n)^T$ (an $n \times 1$ matrix) [source: ma2001-revision-pdf#section-27].

**Linear Combinations and Span**
*   **Linear Combination**: For a set of vectors $S = \{u_1, u_2, \ldots, u_k\}$ in $\mathbb{R}^n$ and real numbers $a_1, a_2, \ldots, a_k$, the vector $a_1u_1 + a_2u_2 + \ldots + a_ku_k$ is called a **linear combination** of $u_1, u_2, \ldots, u_k$ [source: ma2001-revision-pdf#section-28].
*   **Linear Span (span(S))**: The set of all linear combinations of $u_1, u_2, \ldots, u_k$ is called the **linear span** of $S$, denoted $\text{span}(S)$ or $\text{span}\{u_1, u_2, \ldots, u_k\}$ [source: ma2001-revision-pdf#section-28, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
    *   **Geometrical Interpretation**:
        *   The span of a single non-zero vector $u$ in $\mathbb{R}^2$ or $\mathbb{R}^3$ is a line through the origin [source: ma2001-revision-pdf#section-29].
        *   The span of two non-parallel, non-zero vectors $u, v$ in $\mathbb{R}^2$ or $\mathbb{R}^3$ is a plane containing the origin [source: ma2001-revision-pdf#section-29].
    *   To check if a vector $v$ is in $\text{span}(U) = \{u_1, \ldots, u_k\}$, verify if $[u_1 \ u_2 \ \ldots \ u_k \ | \ v]$ is consistent [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].

**Subspaces**
*   **Definition**: A subset $V$ of $\mathbb{R}^n$ is called a **subspace** of $\mathbb{R}^n$ if $V = \text{span}(S)$ for some set of vectors $S = \{u_1, \ldots, u_k\}$ in $\mathbb{R}^n$ [source: ma2001-revision-pdf#section-30].
*   **Alternative Definition**: A non-empty subset $V$ of $\mathbb{R}^n$ is a subspace if and only if it satisfies closure under addition and scalar multiplication:
    1.  The zero vector $0 \in V$.
    2.  For any $u, v \in V$, $u+v \in V$.
    3.  For any $u \in V$ and scalar $c \in \mathbb{R}$, $cu \in V$.
    This can be combined: for any $u, v \in V$ and $c, d \in \mathbb{R}$, $cu+dv \in V$ [source: ma2001-revision-pdf#section-30, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
    *   The solution set of a homogeneous linear system $Ax=0$ is always a subspace of $\mathbb{R}^n$ [source: ma2001-ma2001-pdf#section-2].
*   **Checking Subspaces**: To show $V$ is a subspace, demonstrate that every vector in $V$ can be written as a linear combination of constant vectors with arbitrary parameters, and verify the conditions. To show $V$ is *not* a subspace, find a violation of one of the properties (e.g., $0 \notin V$) [source: ma2001-revision-pdf#section-31, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
*   **Geometrical Interpretation of Subspaces**:
    *   In $\mathbb{R}^2$: the zero space $\{(0,0)\}$, lines through the origin, and $\mathbb{R}^2$ itself [source: ma2001-revision-pdf#section-32].
    *   In $\mathbb{R}^3$: the zero space $\{(0,0,0)\}$, lines through the origin, planes containing the origin, and $\mathbb{R}^3$ itself [source: ma2001-revision-pdf#section-32].

### 5. Linear Independence, Bases, and Dimension

**Linear Independence**
A set of vectors $S = \{u_1, u_2, \ldots, u_k\}$ in $\mathbb{R}^n$ is **linearly independent (LI)** if the vector equation $c_1u_1 + c_2u_2 + \ldots + c_ku_k = 0$ has only the trivial solution ($c_1=c_2=\ldots=c_k=0$) [source: ma2001-revision-pdf#section-33, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-3].
*   If there are non-trivial solutions, $S$ is **linearly dependent (LD)** [source: ma2001-revision-pdf#section-33].
*   $S$ is LD if and only if at least one vector in $S$ can be written as a linear combination of the others [source: ma2001-revision-pdf#section-34, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-3].
*   $S$ is LI if and only if no vector in $S$ can be written as a linear combination of the others [source: ma2001-revision-pdf#section-34].
*   If $k > n$, a set of $k$ vectors in $\mathbb{R}^n$ is always linearly dependent [source: ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-3].
*   **Geometrical Interpretation**: Two vectors $u, v$ are LD if and only if they lie on the same line through the origin. Three vectors $u, v, w$ are LD if and only if they lie on the same line or the same plane through the origin [source: ma2001-revision-pdf#section-35, ma2001-revision-pdf#section-36].

**Bases**
A set of vectors $S = \{u_1, u_2, \ldots, u_k\}$ is a **basis** for a vector space $V$ if:
1.  $S$ is linearly independent.
2.  $S$ spans $V$ [source: ma2001-revision-pdf#section-37, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-4].
*   The empty set $\emptyset$ is the basis for the zero space $\{0\}$ [source: ma2001-revision-pdf#section-37].
*   The **standard basis** for $\mathbb{R}^n$ is $E = \{e_1, e_2, \ldots, e_n\}$, where $e_i$ are the standard unit vectors [source: ma2001-revision-pdf#section-59, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-4].

**Dimension**
The **dimension** of a vector space $V$, denoted $\dim(V)$, is the number of vectors in any basis for $V$. This number is unique [source: ma2001-revision-pdf#section-37, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
*   $\dim(\mathbb{R}^n) = n$ [source: ma2001-revision-pdf#section-39].
*   For a vector space $V$ with $\dim(V)=k$:
    *   Any subset of $V$ with more than $k$ vectors is linearly dependent.
    *   Any subset of $V$ with less than $k$ vectors cannot span $V$.
    *   If any two of "S is LI", "S spans V", "$|S|=\dim(V)$" are true, then all three are true [source: ma2001-revision-pdf#section-38, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-4].

**Finding Bases**:
Two common methods to find a basis for a span of vectors $W = \text{span}\{u_1, \ldots, u_k\}$:
1.  **Row Vectors Method**: Place the vectors as rows of a matrix and perform Gaussian Elimination to obtain the row-echelon form. The non-zero rows of the REF form a basis for $W$ (which is the row space of the original matrix) [source: ma2001-revision-pdf#section-40].
2.  **Column Vectors Method**: Place the vectors as columns of a matrix $A$. Perform Gaussian Elimination to find the pivot columns in the REF ($R$). The corresponding columns from the *original* matrix $A$ form a basis for $W$ (which is the column space of $A$) [source: ma2001-revision-pdf#section-41].

### 6. Fundamental Matrix Subspaces

For an $m \times n$ matrix $A$:
*   **Row Space (row(A))**: The span of the row vectors of $A$ [source: ma2001-revision-pdf#section-42].
    *   The non-zero rows of the row-echelon form $R$ of $A$ form a basis for $\text{row}(A)$ [source: ma2001-revision-pdf#section-43, ma2001-cheatsheet-cheatsheet-pdf#section-1].
    *   Row operations preserve the row space [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].
*   **Column Space (col(A))**: The span of the column vectors of $A$ [source: ma2001-revision-pdf#section-42].
    *   Row operations preserve linear (in)dependence of columns but can destroy other information like column space [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].
    *   The pivot columns of the row-echelon form $R$ correspond to linearly independent columns in $A$. These corresponding columns from the *original* matrix $A$ form a basis for $\text{col}(A)$ [source: ma2001-revision-pdf#section-44, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-3].
    *   $Ax=b$ is consistent if and only if $b \in \text{col}(A)$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-1].
*   **Nullspace (null(A))**: The solution set of the homogeneous linear system $Ax=0$. It is a subspace of $\mathbb{R}^n$ [source: ma2001-revision-pdf#section-45, ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   To find a basis for $\text{null}(A)$, solve $Ax=0$ using Gaussian (or Gauss-Jordan) Elimination. Express the general solution in terms of arbitrary parameters (free variables). The fixed vectors corresponding to these parameters form a basis for $\text{null}(A)$ [source: ma2001-revision-pdf#section-45].

**Rank and Nullity**
*   **Rank (rank(A))**: The dimension of the row space of $A$, which is equal to the dimension of the column space of $A$. It is also equal to the number of non-zero rows in $R$ (REF) and the number of pivot columns in $R$ [source: ma2001-revision-pdf#section-46, ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
    *   $\text{rank}(A) \leq \min\{m, n\}$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
    *   $A$ has full rank if $\text{rank}(A) = \min\{m, n\}$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].
    *   $\text{rank}(A) = \text{rank}(A^T)$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   $\text{rank}(AB) \leq \min\{\text{rank}(A), \text{rank}(B)\}$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   **Nullity (nullity(A))**: The dimension of the nullspace of $A$. It is equal to the number of non-pivot columns in $R$ (i.e., the number of free variables) [source: ma2001-revision-pdf#section-46].
*   **Rank-Nullity Theorem (Dimension Theorem for Matrices)**: For an $m \times n$ matrix $A$, $\text{rank}(A) + \text{nullity}(A) = n$ (the number of columns in $A$) [source: ma2001-revision-pdf#section-46, ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-2].

### 7. Orthogonality

Let $u=(u_1, \ldots, u_n)$ and $v=(v_1, \ldots, v_n)$ be two vectors in $\mathbb{R}^n$.
*   **Dot Product (Inner Product)**: $u \cdot v = u^T v = u_1v_1 + u_2v_2 + \ldots + u_nv_n$ [source: ma2001-revision-pdf#section-48, ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   Properties: $u \cdot v = v \cdot u$, $(u+v) \cdot w = u \cdot w + v \cdot w$, $(cu) \cdot v = c(u \cdot v)$ [source: ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].
*   **Norm (Length)**: $||u|| = \sqrt{u \cdot u} = \sqrt{u_1^2 + u_2^2 + \ldots + u_n^2}$ [source: ma2001-revision-pdf#section-48, ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   $||u||^2 = u \cdot u \ge 0$. $u \cdot u = 0$ if and only if $u=0$ [source: ma2001-revision-pdf#section-48].
    *   A vector $u$ is a **unit vector** if $||u||=1$ [source: ma2001-revision-pdf#section-48].
    *   $||cu|| = |c| ||u||$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   **Distance**: $d(u,v) = ||u-v|| = \sqrt{(u_1-v_1)^2 + \ldots + (u_n-v_n)^2}$ [source: ma2001-revision-pdf#section-49, ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   **Angle**: The angle $\theta$ between $u$ and $v$ is given by $\cos \theta = \frac{u \cdot v}{||u|| ||v||}$ [source: ma2001-revision-pdf#section-49, ma2001-cheatsheet-cheatsheet-pdf#section-3]. This value is well-defined as $-1 \le \frac{u \cdot v}{||u|| ||v||} \le 1$.
    *   Triangle Inequality: $||u+v|| \le ||u|| + ||v||$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

**Orthogonal Sets and Bases**
*   **Orthogonal Vectors**: Two vectors $u, v$ in $\mathbb{R}^n$ are **orthogonal** if $u \cdot v = 0$ [source: ma2001-revision-pdf#section-50]. (This is equivalent to perpendicularity in $\mathbb{R}^2$ and $\mathbb{R}^3$) [source: ma2001-revision-pdf#section-50].
*   **Orthogonal Set**: A set of vectors $S$ is an **orthogonal set** if every pair of distinct vectors in $S$ are orthogonal [source: ma2001-revision-pdf#section-50].
*   **Orthonormal Set**: An **orthonormal set** is an orthogonal set where every vector in $S$ is a unit vector [source: ma2001-revision-pdf#section-50].
*   **Orthogonal Basis**: A basis $S$ for a vector space $V$ is an **orthogonal basis** if $S$ is an orthogonal set [source: ma2001-revision-pdf#section-51].
*   **Orthonormal Basis**: A basis $S$ for a vector space $V$ is an **orthonormal basis** if $S$ is an orthonormal set [source: ma2001-revision-pdf#section-51].
*   **Checking for Orthogonal/Orthonormal Basis**: To show $S$ is an orthogonal (or orthonormal) basis for $V$, check:
    1.  $S$ is orthogonal (or orthonormal).
    2.  $|S| = \dim(V)$ (if $\dim(V)$ is known), OR $S$ spans $V$ (if $\dim(V)$ is unknown) [source: ma2001-revision-pdf#section-51, ma2001-cheatsheet-cheatsheet-pdf#section-3].

**Gram-Schmidt Process**
Given a basis $U = \{u_1, u_2, \ldots, u_k\}$ for a vector space $V$, the Gram-Schmidt Process transforms it into an **orthogonal basis** $V = \{v_1, v_2, \ldots, v_k\}$:
$v_1 = u_1$
$v_2 = u_2 - \frac{u_2 \cdot v_1}{v_1 \cdot v_1} v_1$
$v_3 = u_3 - \frac{u_3 \cdot v_1}{v_1 \cdot v_1} v_1 - \frac{u_3 \cdot v_2}{v_2 \cdot v_2} v_2$
$\vdots$
$v_k = u_k - \sum_{j=1}^{k-1} \frac{u_k \cdot v_j}{v_j \cdot v_j} v_j$
To obtain an **orthonormal basis**, normalize each vector $v_j$ by dividing by its length: $w_j = \frac{v_j}{||v_j||}$ [source: ma2001-revision-pdf#section-52, ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].

**Orthogonal Complement ($V^\perp$)**
For a subspace $V$ of $\mathbb{R}^n$, the set of all vectors $u \in \mathbb{R}^n$ that are orthogonal to every vector in $V$ is called the **orthogonal complement** of $V$, denoted $V^\perp$.
If $V = \text{span}\{v_1, \ldots, v_k\}$, then $u \in V^\perp$ if and only if $u \cdot v_i = 0$ for all $i=1, \ldots, k$. $V^\perp$ is also a subspace of $\mathbb{R}^n$ [source: ma2001-revision-pdf#section-53].

**Projections**
Every vector $u \in \mathbb{R}^n$ can be uniquely written as $u = n + p$, where $p$ is a vector in a subspace $V$, and $n$ is a vector orthogonal to $V$ (i.e., $n \in V^\perp$). The vector $p$ is called the **projection of $u$ onto $V$** [source: ma2001-revision-pdf#section-54].
*   If $S = \{u_1, \ldots, u_k\}$ is an orthogonal basis for $V$, the projection of $w$ onto $V$ is:
    $p = \frac{w \cdot u_1}{u_1 \cdot u_1} u_1 + \frac{w \cdot u_2}{u_2 \cdot u_2} u_2 + \ldots + \frac{w \cdot u_k}{u_k \cdot u_k} u_k$ [source: ma2001-revision-pdf#section-55, ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   If $T = \{v_1, \ldots, v_k\}$ is an orthonormal basis for $V$, the projection of $w$ onto $V$ is:
    $p = (w \cdot v_1)v_1 + (w \cdot v_2)v_2 + \ldots + (w \cdot v_k)v_k$ [source: ma2001-revision-pdf#section-55, ma2001-cheatsheet-cheatsheet-pdf#section-3].

**Least Squares Solutions (Best Approximations)**
For a subspace $V$, the projection $p$ of $u$ onto $V$ is the **best approximation** of $u$ in $V$, meaning $d(u,p) \le d(u,v)$ for all $v \in V$ [source: ma2001-revision-pdf#section-56].
For a linear system $Ax=b$, a vector $u \in \mathbb{R}^n$ is a **least squares solution** if $||b-Au|| \le ||b-Av||$ for all $v \in \mathbb{R}^n$ [source: ma2001-revision-pdf#section-57, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].
*   The vector $p=Au$ is the projection of $b$ onto the [[row-column-nullspace#Column Space|column space]] of $A$.
*   A least squares solution $u$ is found by solving the **Normal Equations**: $A^T A u = A^T b$ [source: ma2001-revision-pdf#section-57, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].

### 8. Coordinate Systems and Transition Matrices

**Coordinate Systems**
Given a basis $S = \{u_1, u_2, \ldots, u_k\}$ for a vector space $V$, any vector $v \in V$ can be expressed uniquely as $v = c_1u_1 + c_2u_2 + \ldots + c_ku_k$.
The vector $(c_1, c_2, \ldots, c_k)$ (as a row vector) or
$ \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_k \end{pmatrix} $ (as a column vector)
is called the **coordinate vector of $v$ relative to $S$**, denoted $(v)_S$ or $[v]_S$ [source: ma2001-revision-pdf#section-58, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-4].
*   Properties of Coordinate Vectors:
    *   $u=v \iff [u]_S = [v]_S$.
    *   $[c_1v_1 + \ldots + c_rv_r]_S = c_1[v_1]_S + \ldots + c_r[v_r]_S$.
    *   Vectors $v_1, \ldots, v_r$ are LI iff $[v_1]_S, \ldots, [v_r]_S$ are LI in $\mathbb{R}^k$.
    *   $\text{span}\{v_1, \ldots, v_r\} = V$ iff $\text{span}\{[v_1]_S, \ldots, [v_r]_S\} = \mathbb{R}^k$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-4].
*   For an orthogonal basis $S = \{u_1, \ldots, u_k\}$, $(w)_S = \left(\frac{w \cdot u_1}{u_1 \cdot u_1}, \ldots, \frac{w \cdot u_k}{u_k \cdot u_k}\right)$ [source: ma2001-revision-pdf#section-60].
*   For an orthonormal basis $T = \{v_1, \ldots, v_k\}$, $(w)_S = (w \cdot v_1, \ldots, w \cdot v_k)$ [source: ma2001-revision-pdf#section-60].

**Transition Matrices**
Let $S = \{u_1, \ldots, u_k\}$ and $T = \{v_1, \ldots, v_k\}$ be two bases for a vector space $V$. The **transition matrix from $S$ to $T$**, denoted $P_{S,T}$ or simply $P$, transforms coordinates from basis $S$ to basis $T$.
*   It is defined as $P = [[u_1]_T \ [u_2]_T \ \ldots \ [u_k]_T]$, where $[u_i]_T$ is the coordinate vector of $u_i$ relative to basis $T$ [source: ma2001-revision-pdf#section-61, ma2001-cheatsheet-cheatsheet-pdf#section-1, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-4].
*   For any vector $w \in V$, $[w]_T = P[w]_S$ [source: ma2001-revision-pdf#section-62].
*   $P$ is invertible, and $P^{-1}$ is the transition matrix from $T$ to $S$ (i.e., $P_{T,S} = P_{S,T}^{-1}$) [source: ma2001-revision-pdf#section-62, ma2001-cheatsheet-cheatsheet-pdf#section-1].
*   If both $S$ and $T$ are orthonormal bases, then $P$ is an [[#Orthogonal Matrices|orthogonal matrix]] [source: ma2001-revision-pdf#section-62, ma2001-cheatsheet-cheatsheet-pdf#section-1].

**Orthogonal Matrices**
An invertible matrix $A$ is called **orthogonal** if $A^{-1} = A^T$ [source: ma2001-revision-pdf#section-62, ma2001-cheatsheet-cheatsheet-pdf#section-3].
The following statements are equivalent for an $n \times n$ matrix $A$:
1.  $A$ is an orthogonal matrix.
2.  The rows of $A$ form an orthonormal basis for $\mathbb{R}^n$.
3.  The columns of $A$ form an orthonormal basis for $\mathbb{R}^n$ [source: ma2001-revision-pdf#section-62, ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   Note: Transition matrices between two orthonormal bases are orthogonal [source: ma2001-cheatsheet-cheatsheet-pdf#section-3].

### 9. Eigenvalues and Eigenvectors

Let $A$ be a square matrix of order $n$.
*   **Eigenvector**: A non-zero column vector $u \in \mathbb{R}^n$ is an **eigenvector** of $A$ if $Au = \lambda u$ for some scalar $\lambda$ [source: ma2001-revision-pdf#section-63, ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   **Eigenvalue**: The scalar $\lambda$ is called an **eigenvalue** of $A$, and $u$ is the eigenvector associated with $\lambda$ [source: ma2001-revision-pdf#section-63, ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   **Characteristic Equation**: $\lambda$ is an eigenvalue of $A$ if and only if $\det(\lambda I - A) = 0$ [source: ma2001-revision-pdf#section-63, ma2001-cheatsheet-cheatsheet-pdf#section-3].
    *   The polynomial $\det(\lambda I - A)$ is the **characteristic polynomial** of $A$ [source: ma2001-revision-pdf#section-64].
*   **Eigenvalues of Triangular Matrices**: If $A$ is a triangular matrix, its eigenvalues are its diagonal entries [source: ma2001-revision-pdf#section-64, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].
    *   *Warning*: You cannot find eigenvalues by reducing $A$ to a triangular matrix using row operations [source: ma2001-revision-pdf#section-64]. You must reduce $(\lambda I - A)$ to a triangular matrix.

**Eigenspaces**
For an eigenvalue $\lambda$ of $A$, the solution space of the linear system $(\lambda I - A)x = 0$ is called the **eigenspace** of $A$ associated with $\lambda$, denoted $E_\lambda$ or $E_\lambda(A)$ [source: ma2001-revision-pdf#section-65, ma2001-cheatsheet-cheatsheet-pdf#section-3].
*   A non-zero vector $u \in E_\lambda$ is an eigenvector of $A$ associated with $\lambda$ [source: ma2001-revision-pdf#section-65].
*   The dimension of $E_\lambda$ is the number of linearly independent eigenvectors associated with $\lambda$.

### 10. Diagonalization

A square matrix $A$ is **diagonalizable** if there exists an invertible matrix $P$ such that $P^{-1}AP = D$, where $D$ is a diagonal matrix [source: ma2001-revision-pdf#section-66, ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].
*   $A$ is diagonalizable if and only if $A$ has $n$ linearly independent eigenvectors [source: ma2001-revision-pdf#section-66, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].

**Steps to Diagonalize a Matrix A**:
1.  **Find eigenvalues**: Solve the characteristic equation $\det(\lambda I - A) = 0$ to find distinct eigenvalues $\lambda_1, \ldots, \lambda_k$ [source: ma2001-revision-pdf#section-67, ma2001-cheatsheet-cheatsheet-pdf#section-3].
2.  **Find bases for eigenspaces**: For each eigenvalue $\lambda_i$, find a basis $S_{\lambda_i}$ for its eigenspace $E_{\lambda_i}$ by solving $(\lambda_i I - A)x = 0$ [source: ma2001-revision-pdf#section-67, ma2001-cheatsheet-cheatsheet-pdf#section-3].
3.  **Check diagonalizability**:
    *   Let $S = S_{\lambda_1} \cup S_{\lambda_2} \cup \ldots \cup S_{\lambda_k}$ be the union of the eigenbases. If $|S| < n$, $A$ is not diagonalizable.
    *   If $|S| = n$, then $A$ is diagonalizable. Form the matrix $P = [u_1 \ u_2 \ \ldots \ u_n]$ where the columns are the vectors from $S$. Then $P$ is an invertible matrix that diagonalizes $A$. The diagonal matrix $D$ will have the eigenvalues on its diagonal in the same order as their corresponding eigenvectors in $P$ [source: ma2001-revision-pdf#section-67, ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].

**Orthogonally Diagonalizable Matrices**
A square matrix $A$ is **orthogonally diagonalizable** if there exists an orthogonal matrix $P$ such that $P^T A P = D$, where $D$ is a diagonal matrix [source: ma2001-revision-pdf#section-66, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].
*   $A$ is orthogonally diagonalizable if and only if $A$ is **symmetric** ($A = A^T$) [source: ma2001-revision-pdf#section-66, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].
    *   The eigenvectors of a symmetric matrix corresponding to distinct eigenvalues are orthogonal [source: ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5].

**Steps to Orthogonally Diagonalize a Matrix A (for symmetric A)**:
1.  Find distinct eigenvalues $\lambda_1, \ldots, \lambda_k$ [source: ma2001-revision-pdf#section-68].
2.  For each $\lambda_i$, find a basis $S_{\lambda_i}$ for $E_{\lambda_i}$. Then use the [[#Gram-Schmidt Process|Gram-Schmidt Process]] to transform $S_{\lambda_i}$ into an orthonormal basis $T_{\lambda_i}$ for $E_{\lambda_i}$ [source: ma2001-revision-pdf#section-68, ma2001-cheatsheet-cheatsheet-pdf#section-3].
3.  Let $T = T_{\lambda_1} \cup T_{\lambda_2} \cup \ldots \cup T_{\lambda_k}$. Form $P = [v_1 \ v_2 \ \ldots \ v_n]$ where the columns are the vectors from $T$. $P$ will be an orthogonal matrix that orthogonally diagonalizes $A$ [source: ma2001-revision-pdf#section-68].

**Powers of Matrices using Diagonalization**
If $A$ is diagonalizable, $A = P D P^{-1}$. Then $A^m = P D^m P^{-1}$, where $D^m$ is obtained by raising each diagonal entry of $D$ to the power $m$ [source: ma2001-revision-pdf#section-69, ma2001-cheatsheet-cheatsheet-pdf#section-3, ma2001-cheatsheet-ma1101r-cheatsheet-finals-1-copy-pdf#section-5]. This also works for negative integers $m$ if $A$ is invertible.

### 11. Linear Transformations

A **linear transformation** $T$ is a mapping $T: \mathbb{R}^n \to \mathbb{R}^m$ such that for all vectors $u, v$ in $\mathbb{R}^n$ and scalar $c$:
1.  $T(u+v) = T(u) + T(v)$
2.  $T(cu) = cT(u)$ [source: ma2001-cheatsheet-cheatsheet-pdf#section-4].
*   If $n=m$, $T$ is called a **linear operator** on $\mathbb{R}^n$ [source: ma2001-revision-pdf#section-70].

**Standard Matrix of a Linear Transformation**
For any linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, there exists a unique $m \times n$ matrix $A$, called the **standard matrix for $T$**, such that $T(u) = Au$ for all $u \in \mathbb{R}^n$ [source: ma2001-revision-pdf#section-70].
*   If $E = \{e_1, e_2, \ldots, e_n\}$ is the standard basis for $\mathbb{R}^n$, then $A = [T(e_1) \ T(e_2) \ \ldots \ T(e_n)]$ [source: ma2001-revision-pdf#section-70, ma2001-cheatsheet-cheatsheet-pdf#section-4].

**Compositions of Mappings**
If $S: \mathbb{R}^n \to \mathbb{R}^m$ and $T: \mathbb{R}^m \to \mathbb{R}^k$ are linear transformations, their **composition** $T \circ S$ is a mapping $T \circ S: \mathbb{R}^n \to \mathbb{R}^k$ defined by $(T \circ S)(u) = T(S(u))$. $T \circ S$ is also a linear transformation [source: ma2001-revision-pdf#section-71].
*   If $A$ is the standard matrix for $S$ and $B$ is the standard matrix for $T$, then the standard matrix for $T \circ S$ is $BA$ [source: ma2001-revision-pdf#section-71, ma2001-cheatsheet-cheatsheet-pdf#section-4].

**Ranges and Kernels (Nullspace)**
Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation with standard matrix $A$.
*   **Range (R(T))**: The set of all images of $T$, $R(T) = \{T(u) | u \in \mathbb{R}^n\} \subseteq \mathbb{R}^m$. The range of $T$ is equal to the [[row-column-nullspace#Column Space|column space]] of $A$, $R(T) = \text{col}(A)$ [source: ma2001-revision-pdf#section-72].
*   **Kernel (Ker(T))**: The set of vectors in $\mathbb{R}^n$ whose image under $T$ is the zero vector in $\mathbb{R}^m$, $Ker(T) = \{u \in \mathbb{R}^n | T(u) = 0\} \subseteq \mathbb{R}^n$. The kernel of $T$ is equal to the [[row-column-nullspace#Nullspace|nullspace]] of $A$, $Ker(T) = \text{null}(A)$ [source: ma2001-revision-pdf#section-72].

**Rank and Nullity of Linear Transformations**
*   **Rank (rank(T))**: The dimension of the range of $T$, $\text{rank}(T) = \dim(R(T))$. This is equal to $\text{rank}(A)$ [source: ma2001-revision-pdf#section-73].
*   **Nullity (nullity(T))**: The dimension of the kernel of $T$, $\text{nullity}(T) = \dim(Ker(T))$. This is equal to $\text{nullity}(A)$ [source: ma2001-revision-pdf#section-73].
*   **Dimension Theorem for Linear Transformations**: $\text{rank}(T) + \text{nullity}(T) = n$ (the dimension of the domain $\mathbb{R}^n$) [source: ma2001-revision-pdf#section-73, ma2001-cheatsheet-cheatsheet-pdf#section-4]. This is consistent with the Rank-Nullity Theorem for matrices.

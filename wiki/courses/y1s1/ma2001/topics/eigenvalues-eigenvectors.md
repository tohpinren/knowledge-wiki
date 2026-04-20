---
page_id: "y1s1-ma2001-eigenvalues-eigenvectors"
title: "Eigenvalues and Eigenvectors"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Introduction to eigenvalues and eigenvectors, their computation, and properties, including eigenspaces."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter6-pdf#section-1"
  - "ma2001-tutorial-tutorial10-pdf#section-1"
  - "ma2001-finals-exam1516sem2-pdf#section-1"
topics:
  - "matrix"
  - "eigenvalues"
  - "diagonalizable"
  - "orthogonal"
  - "can"
  - "diagonal"
  - "its"
  - "basis"
  - "similar"
  - "question"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Eigenvalues and Eigenvectors

In linear algebra, eigenvalues and eigenvectors are fundamental concepts that reveal intrinsic properties of linear transformations and matrices. They are particularly useful for understanding the long-term behavior of dynamic systems, efficiently computing powers of matrices, and simplifying complex systems through diagonalization [source:ma2001-lecture-chapter6-pdf#section-1]. All vectors discussed in this context are considered column vectors [source:ma2001-lecture-chapter6-pdf#section-1].

### Motivation: Population Dynamics Example

Consider a system modeling population dynamics, such as rural and urban population movement. Suppose each year, 4% of the rural population moves to urban areas, and 1% of the urban population moves to rural areas [source:ma2001-lecture-chapter6-pdf#section-3].

Let $a_n$ be the rural population and $b_n$ be the urban population after $n$ years. The system can be represented by a matrix equation:
$$
\begin{pmatrix} a_n \\ b_n \end{pmatrix} = \begin{pmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{pmatrix} \begin{pmatrix} a_{n-1} \\ b_{n-1} \end{pmatrix}
$$
If we let $\mathbf{x}_n = \begin{pmatrix} a_n \\ b_n \end{pmatrix}$ and $A = \begin{pmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{pmatrix}$, then $\mathbf{x}_n = A\mathbf{x}_{n-1}$. To study the long-term effect (i.e., for large $n$), we need to compute $A^n\mathbf{x}_0$ [source:ma2001-lecture-chapter6-pdf#section-4].

This computation becomes significantly simpler if matrix $A$ can be expressed in the form $PDP^{-1}$, where $D$ is a [[diagonalization#Diagonal Matrix|diagonal matrix]] and $P$ is an invertible matrix. In this case, $A^n = PD^nP^{-1}$. Computing $D^n$ is trivial since for a diagonal matrix $D = \begin{pmatrix} d_1 & 0 \\ 0 & d_2 \end{pmatrix}$, $D^n = \begin{pmatrix} d_1^n & 0 \\ 0 & d_2^n \end{pmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-5, ma2001-lecture-chapter6-pdf#section-6].

For the given matrix $A$, it can be shown that $A = P D P^{-1}$ where $P = \begin{pmatrix} 1 & 1 \\ 4 & -1 \end{pmatrix}$ and $D = \begin{pmatrix} 1 & 0 \\ 0 & 0.95 \end{pmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-5]. As $n \to \infty$, $D^n \to \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, which leads to the long-term population distribution where 20% of the total population stays rural and 80% stays urban [source:ma2001-lecture-chapter6-pdf#section-7, ma2001-lecture-chapter6-pdf#section-8]. The crucial step here is expressing $A$ in the $PDP^{-1}$ form, which relies on the concepts of eigenvalues and eigenvectors [source:ma2001-lecture-chapter6-pdf#section-8].

### Definition of Eigenvalues and Eigenvectors

Let $A$ be a square matrix of order $n$.
*   A **nonzero column vector** $\mathbf{u} \in \mathbb{R}^n$ is called an **eigenvector** of $A$ if $A\mathbf{u} = \lambda\mathbf{u}$ for some scalar $\lambda$ [source:ma2001-lecture-chapter6-pdf#section-1].
*   The scalar $\lambda$ is called an **eigenvalue** of $A$, and $\mathbf{u}$ is said to be an eigenvector of $A$ associated with the eigenvalue $\lambda$ [source:ma2001-lecture-chapter6-pdf#section-1].

Essentially, when a matrix $A$ acts on an eigenvector $\mathbf{u}$, the resulting vector $A\mathbf{u}$ is simply a scaled version of $\mathbf{u}$, where $\lambda$ is the scaling factor.

#### Examples of Eigenvectors and Eigenvalues

1.  **For the Population Dynamics Matrix** [source:ma2001-lecture-chapter6-pdf#section-1]:
    Let $A = \begin{pmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{pmatrix}$, $\mathbf{u} = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$, and $\mathbf{v} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
    *   $A\mathbf{u} = \begin{pmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{pmatrix} \begin{pmatrix} 1 \\ 4 \end{pmatrix} = \begin{pmatrix} 0.96 + 0.04 \\ 0.04 + 3.96 \end{pmatrix} = \begin{pmatrix} 1 \\ 4 \end{pmatrix} = 1 \cdot \mathbf{u}$.
        So, $\lambda = 1$ is an eigenvalue, and $\mathbf{u}$ is an eigenvector associated with $\lambda = 1$.
    *   $A\mathbf{v} = \begin{pmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 0.96 - 0.01 \\ 0.04 - 0.99 \end{pmatrix} = \begin{pmatrix} 0.95 \\ -0.95 \end{pmatrix} = 0.95 \cdot \mathbf{v}$.
        So, $\lambda = 0.95$ is an eigenvalue, and $\mathbf{v}$ is an eigenvector associated with $\lambda = 0.95$.

2.  **For a 3x3 Matrix** [source:ma2001-lecture-chapter6-pdf#section-1]:
    Let $B = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{pmatrix}$, $\mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$, $\mathbf{v} = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$, and $\mathbf{w} = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}$.
    *   $B\mathbf{u} = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 1+4+1 \\ 2+8+2 \\ 1+4+1 \end{pmatrix} = \begin{pmatrix} 6 \\ 12 \\ 6 \end{pmatrix} = 6 \cdot \mathbf{u}$.
        So, $\lambda = 6$ is an eigenvalue, and $\mathbf{u}$ is an eigenvector associated with $\lambda = 6$.
    *   $B\mathbf{v} = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = \begin{pmatrix} 1+0-1 \\ 2+0-2 \\ 1+0-1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = 0 \cdot \mathbf{v}$.
        So, $\lambda = 0$ is an eigenvalue, and $\mathbf{v}$ is an eigenvector associated with $\lambda = 0$.
    *   $B\mathbf{w} = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1-2+1 \\ 2-4+2 \\ 1-2+1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = 0 \cdot \mathbf{w}$.
        So, $\lambda = 0$ is an eigenvalue, and $\mathbf{w}$ is an eigenvector associated with $\lambda = 0$.

### How to Find Eigenvalues

To find the eigenvalues of a square matrix $A$ of order $n$, we start with the definition $A\mathbf{u} = \lambda\mathbf{u}$ for a nonzero vector $\mathbf{u}$ [source:ma2001-lecture-chapter6-pdf#section-1].
This equation can be rewritten as:
1.  $A\mathbf{u} - \lambda\mathbf{u} = \mathbf{0}$
2.  To combine the terms, we introduce the identity matrix $I$: $A\mathbf{u} - \lambda I\mathbf{u} = \mathbf{0}$
3.  Factoring out $\mathbf{u}$: $(\lambda I - A)\mathbf{u} = \mathbf{0}$

For this linear system $(\lambda I - A)\mathbf{u} = \mathbf{0}$ to have non-trivial solutions (i.e., nonzero eigenvectors $\mathbf{u}$), the matrix $(\lambda I - A)$ must be singular (not invertible). This occurs when its determinant is zero [source:ma2001-lecture-chapter6-pdf#section-1].
Thus, eigenvalues $\lambda$ are found by solving the equation:
$$
\det(\lambda I - A) = 0
$$
This equation, when expanded, results in a polynomial in $\lambda$ of degree $n$ [source:ma2001-lecture-chapter6-pdf#section-1].

### Characteristic Polynomials and Equations

*   The equation $\det(\lambda I - A) = 0$ is called the **characteristic equation** of $A$ [source:ma2001-lecture-chapter6-pdf#section-1].
*   The polynomial $\det(\lambda I - A)$ is called the **characteristic polynomial** of $A$ [source:ma2001-lecture-chapter6-pdf#section-1].

The eigenvalues of $A$ are simply the roots of its characteristic polynomial.

#### Examples of Finding Characteristic Polynomials and Eigenvalues

1.  **For the Population Dynamics Matrix** [source:ma2001-lecture-chapter6-pdf#section-1]:
    Let $A = \begin{pmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{pmatrix}$.
    The characteristic polynomial is:
    $\det(\lambda I - A) = \det \begin{pmatrix} \lambda - 0.96 & -0.01 \\ -0.04 & \lambda - 0.99 \end{pmatrix}$
    $= (\lambda - 0.96)(\lambda - 0.99) - (-0.01)(-0.04)$
    $= \lambda^2 - 1.95\lambda + 0.9504 - 0.0004$
    $= \lambda^2 - 1.95\lambda + 0.95$
    $= (\lambda - 1)(\lambda - 0.95)$
    Setting this to zero, the eigenvalues are $\lambda = 1$ and $\lambda = 0.95$.

2.  **For a 3x3 Matrix B** [source:ma2001-lecture-chapter6-pdf#section-1]:
    Let $B = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{pmatrix}$.
    The characteristic polynomial is:
    $\det(\lambda I - B) = \det \begin{pmatrix} \lambda - 1 & -2 & -1 \\ -2 & \lambda - 4 & -2 \\ -1 & -2 & \lambda - 1 \end{pmatrix}$
    Expanding this determinant (using cofactor expansion or row/column operations):
    $= (\lambda - 1)[(\lambda - 4)(\lambda - 1) - (-2)(-2)] - (-2)[(-2)(\lambda - 1) - (-2)(-1)] + (-1)[(-2)(-2) - (\lambda - 4)(-1)]$
    $= (\lambda - 1)(\lambda^2 - 5\lambda + 4 - 4) + 2(-2\lambda + 2 - 2) - 1(4 + \lambda - 4)$
    $= (\lambda - 1)(\lambda^2 - 5\lambda) + 2(-2\lambda) - \lambda$
    $= \lambda^3 - 5\lambda^2 - \lambda^2 + 5\lambda - 4\lambda - \lambda$
    $= \lambda^3 - 6\lambda^2$
    $= \lambda^2(\lambda - 6)$
    Setting this to zero, the eigenvalues are $\lambda = 6$ and $\lambda = 0$ (with algebraic multiplicity 2).

3.  **For a 3x3 Matrix C with irrational eigenvalues** [source:ma2001-lecture-chapter6-pdf#section-1]:
    Let $C = \begin{pmatrix} 0 & -1 & 0 \\ 0 & 0 & 2 \\ 1 & 1 & 1 \end{pmatrix}$.
    The characteristic polynomial is:
    $\det(\lambda I - C) = \det \begin{pmatrix} \lambda & 1 & 0 \\ 0 & \lambda & -2 \\ -1 & -1 & \lambda - 1 \end{pmatrix}$
    $= \lambda[\lambda(\lambda - 1) - (-2)(-1)] - 1[0(\lambda - 1) - (-2)(-1)] + 0[\dots]$
    $= \lambda(\lambda^2 - \lambda - 2) - 1(0 - 2)$
    $= \lambda^3 - \lambda^2 - 2\lambda + 2$
    $= \lambda^2(\lambda - 1) - 2(\lambda - 1)$
    $= (\lambda - 1)(\lambda^2 - 2)$
    $= (\lambda - 1)(\lambda - \sqrt{2})(\lambda + \sqrt{2})$
    Setting this to zero, the eigenvalues are $\lambda = 1, \lambda = \sqrt{2}$, and $\lambda = -\sqrt{2}$.

### Invertible Matrices and Eigenvalues

For an $n \times n$ matrix $A$, the following statements are equivalent [source:ma2001-lecture-chapter6-pdf#section-1]:
1.  $A$ is invertible.
2.  The linear system $A\mathbf{x} = \mathbf{0}$ has only the trivial solution ($\mathbf{x} = \mathbf{0}$).
3.  The reduced row-echelon form of $A$ is an identity matrix.
4.  $A$ can be expressed as a product of elementary matrices.
5.  $\det(A) \neq 0$.
6.  The rows of $A$ form a basis for $\mathbb{R}^n$.
7.  The columns of $A$ form a basis for $\mathbb{R}^n$.
8.  $\text{rank}(A) = n$.
9.  $0$ is not an eigenvalue of $A$.

The equivalence between statements 1-8 is established in [[invertible-elementary-matrices#Invertible Matrix Theorem|Theorem 3.6.11]] and [[matrix-operations#Determinant of Elementary Matrices|Remark 4.2.5.2]].
To prove the equivalence $9 \iff 5$:
*   $0$ is not an eigenvalue of $A$
*   $\iff \det(0I - A) \neq 0$ (by Remark 6.1.5, which is the definition of characteristic equation) [source:ma2001-lecture-chapter6-pdf#section-1]
*   $\iff \det(-A) \neq 0$
*   $\iff (-1)^n \det(A) \neq 0$ (by [[determinants-properties#Determinant Properties|Theorem 2.5.22.1]])
*   $\iff \det(A) \neq 0$ [source:ma2001-lecture-chapter6-pdf#section-1]

### Eigenvalues of Triangular Matrices

If $A$ is an $n \times n$ [[matrix-operations#Types of Matrices|triangular matrix]] (either upper or lower), its eigenvalues are its diagonal entries [source:ma2001-lecture-chapter6-pdf#section-1].

**Proof Sketch:**
Let $A$ be an upper triangular matrix:
$$
A = \begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
0 & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & a_{nn}
\end{pmatrix}
$$
Then, $\lambda I - A$ is also an upper triangular matrix:
$$
\lambda I - A = \begin{pmatrix}
\lambda - a_{11} & -a_{12} & \dots & -a_{1n} \\
0 & \lambda - a_{22} & \dots & -a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & \lambda - a_{nn}
\end{pmatrix}
$$
The determinant of a triangular matrix is the product of its diagonal entries (by [[determinants-properties#Determinant of Triangular Matrices|Theorem 3.2.14]]).
So, $\det(\lambda I - A) = (\lambda - a_{11})(\lambda - a_{22})\dots(\lambda - a_{nn})$ [source:ma2001-lecture-chapter6-pdf#section-1].
Setting $\det(\lambda I - A) = 0$ implies $\lambda = a_{11}, \lambda = a_{22}, \dots, \lambda = a_{nn}$. The same argument applies to lower triangular matrices.

#### Examples for Triangular Matrices

1.  The eigenvalues of $\begin{pmatrix} -1 & 3.5 & 14 \\ 0 & 5 & -26 \\ 0 & 0 & 2 \end{pmatrix}$ are $-1, 5,$ and $2$ [source:ma2001-lecture-chapter6-pdf#section-1].
2.  The eigenvalues of $\begin{pmatrix} -2 & 0 & 0 \\ 99 & 0 & 0 \\ 10 & -4.5 & 10 \end{pmatrix}$ are $-2, 0,$ and $10$ [source:ma2001-lecture-chapter6-pdf#section-1].

**Important Warning**: In general, you **cannot** find eigenvalues by reducing a matrix $A$ to a triangular matrix using row operations, because row operations change the eigenvalues. However, you *can* use row operations to reduce $\lambda I - A$ to a triangular matrix to find $\det(\lambda I - A)$ [source:ma2001-lecture-chapter6-pdf#section-1].

A common exam question for this theorem is given as:
**Question 2 (i):** Find the eigenvalues for $A = \begin{pmatrix} 2 & 0 & 0 & 0 \\ 1 & 3 & 0 & 0 \\ 1 & 0 & 3 & 0 \\ 1 & 1 & 1 & 1 \end{pmatrix}$. Justify your answer. [source:ma2001-finals-exam1516sem2-pdf#section-4]
**Solution:** Since $A$ is a lower triangular matrix, its eigenvalues are its diagonal entries. Therefore, the eigenvalues of $A$ are $2, 3, 3, 1$.

### Eigenspaces

Let $A$ be a square matrix of order $n$, and $\lambda$ be an eigenvalue of $A$.
The **solution space** of the linear system $(\lambda I - A)\mathbf{x} = \mathbf{0}$ is called the **eigenspace** of $A$ associated with the eigenvalue $\lambda$ [source:ma2001-lecture-chapter6-pdf#section-1]. It is denoted by $E_\lambda$ or $E_\lambda(A)$.
If $\mathbf{u}$ is a nonzero vector in $E_\lambda$, then $\mathbf{u}$ is an eigenvector of $A$ associated with $\lambda$ [source:ma2001-lecture-chapter6-pdf#section-1].

The eigenspace $E_\lambda$ is essentially the null space of the matrix $(\lambda I - A)$, i.e., $E_\lambda = \text{null}(\lambda I - A)$.

#### Examples of Finding Eigenspaces

To find a basis for an eigenspace $E_\lambda$, we solve the homogeneous system $(\lambda I - A)\mathbf{x} = \mathbf{0}$ for each eigenvalue $\lambda$.

1.  **For Population Dynamics Matrix** [source:ma2001-lecture-chapter6-pdf#section-1]:
    Let $A = \begin{pmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{pmatrix}$. Eigenvalues are $\lambda_1 = 1$ and $\lambda_2 = 0.95$.
    *   **For $\lambda_1 = 1$**: We solve $(1I - A)\mathbf{x} = \mathbf{0}$.
        $\begin{pmatrix} 1 - 0.96 & -0.01 \\ -0.04 & 1 - 0.99 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$
        $\begin{pmatrix} 0.04 & -0.01 \\ -0.04 & 0.01 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$
        Row reducing the augmented matrix:
        $\begin{pmatrix} 0.04 & -0.01 & | & 0 \\ -0.04 & 0.01 & | & 0 \end{pmatrix} \xrightarrow{R_2 \to R_2 + R_1} \begin{pmatrix} 0.04 & -0.01 & | & 0 \\ 0 & 0 & | & 0 \end{pmatrix}$
        $0.04x - 0.01y = 0 \implies 4x = y$.
        Let $x = t$ for some $t \in \mathbb{R}$. Then $y = 4t$.
        The eigenvectors are of the form $\begin{pmatrix} t \\ 4t \end{pmatrix} = t \begin{pmatrix} 1 \\ 4 \end{pmatrix}$.
        So, $E_1 = \text{span}\left\{ \begin{pmatrix} 1 \\ 4 \end{pmatrix} \right\}$ (or $\text{span}\left\{ \begin{pmatrix} 0.25 \\ 1 \end{pmatrix} \right\}$).

    *   **For $\lambda_2 = 0.95$**: We solve $(0.95I - A)\mathbf{x} = \mathbf{0}$.
        $\begin{pmatrix} 0.95 - 0.96 & -0.01 \\ -0.04 & 0.95 - 0.99 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$
        $\begin{pmatrix} -0.01 & -0.01 \\ -0.04 & -0.04 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$
        Row reducing:
        $\begin{pmatrix} -0.01 & -0.01 & | & 0 \\ -0.04 & -0.04 & | & 0 \end{pmatrix} \xrightarrow{R_2 \to R_2 - 4R_1} \begin{pmatrix} -0.01 & -0.01 & | & 0 \\ 0 & 0 & | & 0 \end{pmatrix}$
        $-0.01x - 0.01y = 0 \implies x = -y$.
        Let $y = t$. Then $x = -t$.
        The eigenvectors are of the form $\begin{pmatrix} -t \\ t \end{pmatrix} = t \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.
        So, $E_{0.95} = \text{span}\left\{ \begin{pmatrix} -1 \\ 1 \end{pmatrix} \right\}$.

2.  **For a 3x3 Matrix B with repeated eigenvalue** [source:ma2001-lecture-chapter6-pdf#section-1]:
    Let $B = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{pmatrix}$. Eigenvalues are $\lambda_1 = 6$ and $\lambda_2 = 0$ (multiplicity 2).
    *   **For $\lambda_1 = 6$**: We solve $(6I - B)\mathbf{x} = \mathbf{0}$.
        $\begin{pmatrix} 6 - 1 & -2 & -1 \\ -2 & 6 - 4 & -2 \\ -1 & -2 & 6 - 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$
        $\begin{pmatrix} 5 & -2 & -1 \\ -2 & 2 & -2 \\ -1 & -2 & 5 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$
        Row reducing:
        $\begin{pmatrix} 5 & -2 & -1 & | & 0 \\ -2 & 2 & -2 & | & 0 \\ -1 & -2 & 5 & | & 0 \end{pmatrix} \xrightarrow{R_1 \leftrightarrow R_3} \begin{pmatrix} -1 & -2 & 5 & | & 0 \\ -2 & 2 & -2 & | & 0 \\ 5 & -2 & -1 & | & 0 \end{pmatrix}$
        $\xrightarrow{R_1 \to -R_1} \begin{pmatrix} 1 & 2 & -5 & | & 0 \\ -2 & 2 & -2 & | & 0 \\ 5 & -2 & -1 & | & 0 \end{pmatrix}$
        $\xrightarrow{R_2 \to R_2 + 2R_1, R_3 \to R_3 - 5R_1} \begin{pmatrix} 1 & 2 & -5 & | & 0 \\ 0 & 6 & -12 & | & 0 \\ 0 & -12 & 24 & | & 0 \end{pmatrix}$
        $\xrightarrow{R_2 \to (1/6)R_2, R_3 \to R_3 + 2R_2} \begin{pmatrix} 1 & 2 & -5 & | & 0 \\ 0 & 1 & -2 & | & 0 \\ 0 & 0 & 0 & | & 0 \end{pmatrix}$
        From $R_2: y - 2z = 0 \implies y = 2z$.
        From $R_1: x + 2y - 5z = 0 \implies x + 2(2z) - 5z = 0 \implies x + 4z - 5z = 0 \implies x = z$.
        Let $z = t$. Then $x = t$ and $y = 2t$.
        The eigenvectors are of the form $\begin{pmatrix} t \\ 2t \\ t \end{pmatrix} = t \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$.
        So, $E_6 = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \right\}$.

    *   **For $\lambda_2 = 0$**: We solve $(0I - B)\mathbf{x} = \mathbf{0}$.
        $\begin{pmatrix} -1 & -2 & -1 \\ -2 & -4 & -2 \\ -1 & -2 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$
        Row reducing:
        $\begin{pmatrix} -1 & -2 & -1 & | & 0 \\ -2 & -4 & -2 & | & 0 \\ -1 & -2 & -1 & | & 0 \end{pmatrix} \xrightarrow{R_2 \to R_2 - 2R_1, R_3 \to R_3 - R_1} \begin{pmatrix} -1 & -2 & -1 & | & 0 \\ 0 & 0 & 0 & | & 0 \\ 0 & 0 & 0 & | & 0 \end{pmatrix}$
        $-x - 2y - z = 0 \implies x = -2y - z$.
        Let $y = s$ and $z = t$. Then $x = -2s - t$.
        The eigenvectors are of the form $\begin{pmatrix} -2s - t \\ s \\ t \end{pmatrix} = s \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}$.
        So, $E_0 = \text{span}\left\{ \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} \right\}$.

3.  **From Tutorial 10, Question 1**:
    Given $A = \begin{pmatrix} -2 & 0 & -2 & 1 \\ -1 & -1 & -2 & 1 \\ 1 & 0 & 1 & -1 \\ 0 & 0 & 0 & -1 \end{pmatrix}$.
    *The characteristic polynomial and eigenvalues would be computed first (as per Q1a in Tutorial 10), then the basis for each eigenspace.* [source:ma2001-tutorial-tutorial10-pdf#section-1, ma2001-tutorial-tutorial10-pdf#section-2]
    The general procedure involves:
    1.  Compute $\det(\lambda I - A) = 0$ to find eigenvalues $\lambda$.
    2.  For each $\lambda$, solve $(\lambda I - A)\mathbf{x} = \mathbf{0}$ using Gaussian elimination to find the basis vectors for $E_\lambda$.

### Introduction to Diagonalization

The concepts of eigenvalues and eigenvectors are crucial for [[diagonalization|diagonalizing a matrix]]. A square matrix $A$ is called **diagonalizable** if there exists an invertible matrix $P$ such that $P^{-1}AP$ is a [[diagonalization#Diagonal Matrix|diagonal matrix]] $D$ [source:ma2001-lecture-chapter6-pdf#section-3]. The matrix $P$ is said to diagonalize $A$ [source:ma2001-lecture-chapter6-pdf#section-3]. This process leverages the eigenvectors of $A$ to form the columns of $P$ and the corresponding eigenvalues to form the diagonal entries of $D$. This is essential for applications like computing high powers of matrices, as seen in the population dynamics example.

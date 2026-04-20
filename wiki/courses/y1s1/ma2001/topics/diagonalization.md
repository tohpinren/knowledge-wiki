---
page_id: "y1s1-ma2001-diagonalization"
title: "Diagonalization of Matrices"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Process of diagonalizing a square matrix using eigenvalues and eigenvectors to simplify computations involving matrix powers."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter6-pdf#section-3"
  - "ma2001-tutorial-tutorial10sol-pdf#section-1"
  - "ma2001-finals-exam1516sem2soln-pdf#section-1"
topics:
  - "matrix"
  - "eigenvalues"
  - "diagonalizable"
  - "orthogonal"
  - "can"
  - "diagonal"
  - "its"
  - "basis"
  - "symmetric"
  - "eigenspace"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Diagonalization of Matrices

Diagonalization is a powerful technique in linear algebra used to simplify computations involving powers of square matrices. This process decomposes a square matrix $A$ into the form $PDP^{-1}$, where $D$ is a diagonal matrix, significantly streamlining the calculation of high powers of $A$ and enabling the study of long-term effects in various systems, such as population dynamics [source:ma2001-lecture-chapter6-pdf#section-1]. Throughout this chapter, all vectors are treated as column vectors [source:ma2001-lecture-chapter6-pdf#section-1].

## Introduction to Diagonalization
Consider a system where the state at time $n$ depends on the state at time $n-1$, represented by a matrix equation $x_n = A x_{n-1}$. For example, in population dynamics, if $a_n$ is the rural population and $b_n$ is the urban population after $n$ years, and there are annual movements (e.g., 4% rural to urban, 1% urban to rural), the system can be modeled as:
$a_n = 0.96a_{n-1} + 0.01b_{n-1}$
$b_n = 0.04a_{n-1} + 0.99b_{n-1}$ [source:ma2001-lecture-chapter6-pdf#section-1]

This can be written in matrix form as $x_n = A x_{n-1}$, where $x_n = \begin{bmatrix} a_n \\ b_n \end{bmatrix}$ and $A = \begin{bmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{bmatrix}$. To study the long-term effect (i.e., as $n \to \infty$), we need to compute $A^n x_0$ [source:ma2001-lecture-chapter6-pdf#section-1].

Directly computing $A^n$ for large $n$ can be cumbersome. However, if matrix $A$ can be expressed in the form $A = PDP^{-1}$ where $D$ is a diagonal matrix, then computing powers of $A$ becomes much simpler:
$A^n = (PDP^{-1})^n = (PDP^{-1})(PDP^{-1})\cdots(PDP^{-1})$ ($n$ times)
Since $P^{-1}P = I$ (the identity matrix), this simplifies to:
$A^n = PD(P^{-1}P)D(P^{-1}P)\cdots(P^{-1}P)DP^{-1}$
$A^n = PDID\cdots IDP^{-1} = PD^n P^{-1}$ [source:ma2001-lecture-chapter6-pdf#section-1]

The advantage of this form is that computing $D^n$ for a diagonal matrix $D = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix}$ is straightforward: $D^n = \begin{bmatrix} \lambda_1^n & 0 \\ 0 & \lambda_2^n \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-1]. For the population dynamics example, $A$ can be written as $A = P D P^{-1}$ with $P = \begin{bmatrix} 1 & 1 \\ 4 & -1 \end{bmatrix}$ and $D = \begin{bmatrix} 1 & 0 \\ 0 & 0.95 \end{bmatrix}$. Then $A^n = P \begin{bmatrix} 1^n & 0 \\ 0 & 0.95^n \end{bmatrix} P^{-1}$ [source:ma2001-lecture-chapter6-pdf#section-1].

As $n \to \infty$, $D^n = \begin{bmatrix} 1^n & 0 \\ 0 & 0.95^n \end{bmatrix} \to \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$.
Therefore, $\lim_{n \to \infty} A^n = P \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} P^{-1} = \begin{bmatrix} 1 & 1 \\ 4 & -1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 4 & -1 \end{bmatrix}^{-1} = \begin{bmatrix} 0.2 & 0.2 \\ 0.8 & 0.8 \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-1].
This implies that in the long run, the rural population stabilizes at 20% of the total population, and the urban population stabilizes at 80% [source:ma2001-lecture-chapter6-pdf#section-1]. The crucial step here is to express $A$ in the form $PDP^{-1}$ where $D$ is a diagonal matrix [source:ma2001-lecture-chapter6-pdf#section-1].

## Eigenvalues and Eigenvectors

**Definition:**
Let $A$ be a square matrix of order $n$. A nonzero column vector $u \in \mathbb{R}^n$ is called an **eigenvector** of $A$ if $Au = \lambda u$ for some scalar $\lambda$. The scalar $\lambda$ is called an **eigenvalue** of $A$, and $u$ is said to be an eigenvector of $A$ associated with the eigenvalue $\lambda$ [source:ma2001-lecture-chapter6-pdf#section-3].

**Examples:**
For the matrix $A = \begin{bmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{bmatrix}$, we can verify:
*   $A \begin{bmatrix} 1 \\ 4 \end{bmatrix} = \begin{bmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{bmatrix} \begin{bmatrix} 1 \\ 4 \end{bmatrix} = \begin{bmatrix} 0.96 + 0.04 \\ 0.04 + 3.96 \end{bmatrix} = \begin{bmatrix} 1 \\ 4 \end{bmatrix} = 1 \cdot \begin{bmatrix} 1 \\ 4 \end{bmatrix}$. So, $1$ is an eigenvalue, and $\begin{bmatrix} 1 \\ 4 \end{bmatrix}$ is an eigenvector associated with $1$ [source:ma2001-lecture-chapter6-pdf#section-3].
*   $A \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 0.96 - 0.01 \\ 0.04 - 0.99 \end{bmatrix} = \begin{bmatrix} 0.95 \\ -0.95 \end{bmatrix} = 0.95 \cdot \begin{bmatrix} 1 \\ -1 \end{bmatrix}$. So, $0.95$ is an eigenvalue, and $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$ is an eigenvector associated with $0.95$ [source:ma2001-lecture-chapter6-pdf#section-3].

### Finding Eigenvalues
To find eigenvalues $\lambda$ for a square matrix $A$ of order $n$:
1.  Start with the definition: $Au = \lambda u$ for a nonzero vector $u$.
2.  Rewrite as: $\lambda u - Au = 0$.
3.  Factor out $u$: $(\lambda I - A)u = 0$, where $I$ is the identity matrix of order $n$.
4.  For this homogeneous linear system to have non-trivial solutions (i.e., $u \neq 0$), the matrix $(\lambda I - A)$ must be singular. This means its determinant must be zero: $\det(\lambda I - A) = 0$ [source:ma2001-lecture-chapter6-pdf#section-3].

**Characteristic Polynomial and Equation:**
The equation $\det(\lambda I - A) = 0$ is called the **characteristic equation** of $A$. The polynomial $\det(\lambda I - A)$ (which is a polynomial in $\lambda$ of degree $n$) is called the **characteristic polynomial** of $A$ [source:ma2001-lecture-chapter6-pdf#section-3]. The roots of the characteristic polynomial are the eigenvalues.

**Examples:**
*   For $A = \begin{bmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{bmatrix}$:
    $\det(\lambda I - A) = \det \left( \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \begin{bmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{bmatrix} \right) = \det \begin{bmatrix} \lambda - 0.96 & -0.01 \\ -0.04 & \lambda - 0.99 \end{bmatrix}$
    $= (\lambda - 0.96)(\lambda - 0.99) - (-0.01)(-0.04)$
    $= \lambda^2 - 1.95\lambda + 0.9504 - 0.0004$
    $= \lambda^2 - 1.95\lambda + 0.95 = (\lambda - 1)(\lambda - 0.95)$
    The eigenvalues are $1$ and $0.95$ [source:ma2001-lecture-chapter6-pdf#section-3].
*   For $B = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$:
    $\det(\lambda I - B) = \det \begin{bmatrix} \lambda - 1 & -2 & -1 \\ -2 & \lambda - 4 & -2 \\ -1 & -2 & \lambda - 1 \end{bmatrix} = \lambda^3 - 6\lambda^2 = \lambda^2(\lambda - 6)$.
    The eigenvalues are $6$ and $0$ (with algebraic multiplicity $2$ for $\lambda=0$) [source:ma2001-lecture-chapter6-pdf#section-3].
*   For $C = \begin{bmatrix} 0 & -1 & 0 \\ 0 & 0 & 2 \\ 1 & 1 & 1 \end{bmatrix}$:
    $\det(\lambda I - C) = \det \begin{bmatrix} \lambda & 1 & 0 \\ 0 & \lambda & -2 \\ -1 & -1 & \lambda - 1 \end{bmatrix} = \lambda^3 - \lambda^2 - 2\lambda + 2 = (\lambda - 1)(\lambda - \sqrt{2})(\lambda + \sqrt{2})$.
    The eigenvalues are $1$, $\sqrt{2}$, and $-\sqrt{2}$ [source:ma2001-lecture-chapter6-pdf#section-3].

**Invertible Matrices and Eigenvalues:**
A key property relates invertibility to eigenvalues: For an $n \times n$ matrix $A$, the following statements are equivalent:
1.  $A$ is invertible.
2.  The linear system $Ax = 0$ has only the trivial solution.
3.  The reduced row-echelon form of $A$ is an identity matrix.
4.  $A$ can be expressed as a product of elementary matrices.
5.  $\det(A) \neq 0$.
6.  The rows of $A$ form a basis for $\mathbb{R}^n$.
7.  The columns of $A$ form a basis for $\mathbb{R}^n$.
8.  $\text{rank}(A) = n$.
9.  $0$ is not an eigenvalue of $A$ [source:ma2001-lecture-chapter6-pdf#section-3].

The equivalence between $\det(A) \neq 0$ and $0$ not being an eigenvalue stems from the fact that if $\lambda = 0$ is an eigenvalue, then $\det(0I - A) = \det(-A) = (-1)^n \det(A) = 0$, implying $\det(A) = 0$ [source:ma2001-lecture-chapter6-pdf#section-3].

**Triangular Matrices:**
If $A$ is an $n \times n$ triangular matrix (upper or lower), its eigenvalues are its diagonal entries $a_{11}, a_{22}, \dots, a_{nn}$ [source:ma2001-lecture-chapter6-pdf#section-3]. This is because $\det(\lambda I - A)$ for a triangular matrix is simply the product of its diagonal entries: $(\lambda - a_{11})(\lambda - a_{22})\cdots(\lambda - a_{nn})$ [source:ma2001-lecture-chapter6-pdf#section-3].

**Warning:** In general, you cannot find eigenvalues by reducing $A$ to a triangular matrix using row operations, as row operations change the eigenvalues. However, you *can* use row operations to reduce $\lambda I - A$ to a triangular matrix to find $\det(\lambda I - A)$ [source:ma2001-lecture-chapter6-pdf#section-3].

### Eigenspaces
**Definition:**
Let $A$ be a square matrix of order $n$ and $\lambda$ an eigenvalue of $A$. The solution space of the linear system $(\lambda I - A)x = 0$ is called the **eigenspace** of $A$ associated with the eigenvalue $\lambda$. It is denoted by $E_\lambda$ (or $E_\lambda(A)$) [source:ma2001-lecture-chapter6-pdf#section-3]. If $u$ is a nonzero vector in $E_\lambda$, then $u$ is an eigenvector of $A$ associated with $\lambda$ [source:ma2001-lecture-chapter6-pdf#section-3]. The eigenspace $E_\lambda$ is the nullspace of the matrix $(\lambda I - A)$.

**Examples of finding Eigenspaces:**
*   For $A = \begin{bmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{bmatrix}$, with eigenvalues $1$ and $0.95$:
    *   For $\lambda = 1$: Solve $(1I - A)x = 0 \implies \begin{bmatrix} 0.04 & -0.01 \\ -0.04 & 0.01 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$.
        This simplifies to $0.04x - 0.01y = 0 \implies 4x = y$.
        The general solution is $x = t \begin{bmatrix} 0.25 \\ 1 \end{bmatrix}$ for some $t \in \mathbb{R}$.
        So, $E_1 = \text{span}\left\{ \begin{bmatrix} 0.25 \\ 1 \end{bmatrix} \right\}$ [source:ma2001-lecture-chapter6-pdf#section-3]. (Note: The provided lecture slide has a typo; it should be $0.25$ not $0$ in the first component of the vector).
    *   For $\lambda = 0.95$: Solve $(0.95I - A)x = 0 \implies \begin{bmatrix} -0.01 & -0.01 \\ -0.04 & -0.04 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$.
        This simplifies to $-0.01x - 0.01y = 0 \implies x = -y$.
        The general solution is $x = t \begin{bmatrix} -1 \\ 1 \end{bmatrix}$ for some $t \in \mathbb{R}$.
        So, $E_{0.95} = \text{span}\left\{ \begin{bmatrix} -1 \\ 1 \end{bmatrix} \right\}$ [source:ma2001-lecture-chapter6-pdf#section-3].

*   For $B = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$, with eigenvalues $6$ and $0$:
    *   For $\lambda = 6$: Solve $(6I - B)x = 0 \implies \begin{bmatrix} 5 & -2 & -1 \\ -2 & 2 & -2 \\ -1 & -2 & 5 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$.
        Row reducing yields a solution of the form $x = t \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}$ for some $t \in \mathbb{R}$.
        So, $E_6 = \text{span}\left\{ \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \right\}$ [source:ma2001-lecture-chapter6-pdf#section-3].
    *   For $\lambda = 0$: Solve $(0I - B)x = 0 \implies \begin{bmatrix} -1 & -2 & -1 \\ -2 & -4 & -2 \\ -1 & -2 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$.
        This simplifies to $-x - 2y - z = 0$.
        The general solution is $x = s \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix} + t \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$ for some $s, t \in \mathbb{R}$.
        So, $E_0 = \text{span}\left\{ \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \right\}$ [source:ma2001-lecture-chapter6-pdf#section-3].
        Tutorial 10 Problem 1(b) provides a slightly different basis for $E_0$: $\left\{ \begin{bmatrix} -1 \\ -1 \\ 1 \\ 0 \end{bmatrix} \right\}$ and for $E_{-1}$ of a 4x4 matrix $B$: $\left\{ \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix} \right\}$ [source:ma2001-tutorial-tutorial10sol-pdf#section-1]. These differences in basis vectors are common, as a span can have multiple bases.

## Diagonalization

**Definition:**
A square matrix $A$ is called **diagonalizable** if there exists an invertible matrix $P$ such that $P^{-1}AP$ is a diagonal matrix. The matrix $P$ is said to **diagonalize** $A$ [source:ma2001-lecture-chapter6-pdf#section-4].
If $P^{-1}AP = D$, then $A = PDP^{-1}$.

**Examples of Diagonalizable Matrices:**
*   $A = \begin{bmatrix} 0.96 & 0.01 \\ 0.04 & 0.99 \end{bmatrix}$ is diagonalizable, as shown earlier.
*   $B = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$ is diagonalizable. We found eigenvalues $6$ and $0$, and bases for $E_6$ and $E_0$. We can form $P$ from these eigenvectors (see Algorithm 6.2.4 below) [source:ma2001-lecture-chapter6-pdf#section-4].

**Example of a Non-Diagonalizable Matrix:**
Not all square matrices are diagonalizable. For instance, consider $M = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}$.
The eigenvalues are the diagonal entries, so $\lambda = 2$ (with algebraic multiplicity $2$) is the only eigenvalue.
Let's find the eigenspace for $\lambda = 2$:
$(2I - M)x = 0 \implies \begin{bmatrix} 0 & 0 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$.
This means $-x = 0 \implies x = 0$. So $E_2 = \text{span}\left\{ \begin{bmatrix} 0 \\ 1 \end{bmatrix} \right\}$.
The basis for $E_2$ has only one vector. If $M$ were diagonalizable, there would exist an invertible matrix $P = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ such that $P^{-1}MP = \begin{bmatrix} \lambda & 0 \\ 0 & \mu \end{bmatrix}$. This would imply $M$ has two linearly independent eigenvectors. Since we only found one, $M$ is not diagonalizable [source:ma2001-lecture-chapter6-pdf#section-4].

### Diagonalization and Eigenvectors
**Theorem:** An $n \times n$ matrix $A$ is diagonalizable if and only if $A$ has $n$ linearly independent eigenvectors [source:ma2001-lecture-chapter6-pdf#section-4].

**Proof (Outline):**
*   **($\Rightarrow$) Suppose $A$ is diagonalizable.** Then there exists an invertible matrix $P = [u_1 \ u_2 \ \cdots \ u_n]$ such that $P^{-1}AP = D$, where $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$ is a diagonal matrix.
    From $P^{-1}AP = D$, we have $AP = PD$.
    Writing this out: $A[u_1 \ u_2 \ \cdots \ u_n] = [u_1 \ u_2 \ \cdots \ u_n]D$.
    This means $[Au_1 \ Au_2 \ \cdots \ Au_n] = [\lambda_1 u_1 \ \lambda_2 u_2 \ \cdots \ \lambda_n u_n]$.
    Therefore, $Au_i = \lambda_i u_i$ for each $i = 1, \dots, n$. This shows that $u_i$ are eigenvectors of $A$ associated with eigenvalues $\lambda_i$. Since $P$ is invertible, its columns $u_1, \dots, u_n$ are linearly independent [source:ma2001-lecture-chapter6-pdf#section-4].
*   **($\Leftarrow$) Suppose $A$ has $n$ linearly independent eigenvectors $u_1, \dots, u_n$,** associated with eigenvalues $\lambda_1, \dots, \lambda_n$.
    Let $P = [u_1 \ u_2 \ \cdots \ u_n]$. Since $u_i$ are linearly independent, and there are $n$ of them in $\mathbb{R}^n$, they form a basis for $\mathbb{R}^n$. Thus, $P$ is an invertible matrix.
    Then $AP = A[u_1 \ u_2 \ \cdots \ u_n] = [Au_1 \ Au_2 \ \cdots \ Au_n] = [\lambda_1 u_1 \ \lambda_2 u_2 \ \cdots \ \lambda_n u_n]$.
    We can also write this as $P D$, where $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$.
    So $AP = PD$. Multiplying by $P^{-1}$ on the left, we get $P^{-1}AP = D$, which means $A$ is diagonalizable [source:ma2001-lecture-chapter6-pdf#section-4].

### Algorithm to Diagonalize a Matrix
To diagonalize an $n \times n$ matrix $A$:
**Step 1:** Find all distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_k$ by solving the characteristic equation $\det(\lambda I - A) = 0$ [source:ma2001-lecture-chapter6-pdf#section-4].
**Step 2:** For each eigenvalue $\lambda_i$, find a basis $S_{\lambda_i}$ for the eigenspace $E_{\lambda_i}$ [source:ma2001-lecture-chapter6-pdf#section-4].
**Step 3:** Let $S = S_{\lambda_1} \cup S_{\lambda_2} \cup \dots \cup S_{\lambda_k}$ be the union of all these bases.
    *   (a) If $|S| < n$ (i.e., the total number of linearly independent eigenvectors is less than $n$), then $A$ is not diagonalizable [source:ma2001-lecture-chapter6-pdf#section-4].
    *   (b) If $|S| = n$, say $S = \{u_1, u_2, \dots, u_n\}$, then $A$ is diagonalizable. Form the invertible matrix $P = [u_1 \ u_2 \ \dots \ u_n]$ whose columns are these $n$ linearly independent eigenvectors. This $P$ diagonalizes $A$. The diagonal matrix $D = P^{-1}AP$ will have the eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$ (in the order corresponding to the eigenvectors in $P$) on its diagonal [source:ma2001-lecture-chapter6-pdf#section-4].

**Remarks on Algorithm 6.2.4:**
*   Sometimes eigenvalues can be complex numbers, not just real numbers. The algorithm still applies, but $P$ might have complex entries [source:ma2001-lecture-chapter6-pdf#section-4]. For example, if $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$, $\det(\lambda I - A) = \det \begin{bmatrix} \lambda & 1 \\ -1 & \lambda \end{bmatrix} = \lambda^2 + 1 = 0$, so $\lambda = i, -i$ [source:ma2001-lecture-chapter6-pdf#section-4].
*   If the characteristic polynomial of $A$ is factored as $\det(\lambda I - A) = (\lambda - \lambda_1)^{r_1}(\lambda - \lambda_2)^{r_2}\cdots(\lambda - \lambda_k)^{r_k}$, where $\lambda_1, \dots, \lambda_k$ are distinct eigenvalues and $r_i$ are their algebraic multiplicities. Then for each $\lambda_i$, $\dim(E_{\lambda_i}) \le r_i$. A matrix $A$ is diagonalizable if and only if for each eigenvalue $\lambda_i$, $\dim(E_{\lambda_i}) = r_i$ (i.e., the geometric multiplicity equals the algebraic multiplicity). Also, the set $S$ formed in Step 3 is always linearly independent [source:ma2001-lecture-chapter6-pdf#section-4].

**Theorem:** If an $n \times n$ matrix $A$ has $n$ distinct eigenvalues, then $A$ is diagonalizable [source:ma2001-lecture-chapter6-pdf#section-5]. (This is a sufficient but not necessary condition; a matrix can have repeated eigenvalues and still be diagonalizable if geometric multiplicity equals algebraic multiplicity for all eigenvalues).

**Examples of Diagonalization:**
*   For $B = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$:
    *   **Step 1:** Eigenvalues are $6$ and $0$ (from earlier example) [source:ma2001-lecture-chapter6-pdf#section-4].
    *   **Step 2:** Bases for eigenspaces: $S_6 = \left\{ \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \right\}$ and $S_0 = \left\{ \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \right\}$ [source:ma2001-lecture-chapter6-pdf#section-4].
    *   **Step 3:** $S = \left\{ \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}, \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \right\}$. $|S|=3$, which is $n$. So $B$ is diagonalizable.
        Let $P = \begin{bmatrix} 1 & -2 & -1 \\ 2 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$. Then $P^{-1}BP = \begin{bmatrix} 6 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-4].
        If the order of columns in $P$ is rearranged (e.g., $Q = \begin{bmatrix} -2 & 1 & -1 \\ 1 & 2 & 0 \\ 0 & 1 & 1 \end{bmatrix}$), the diagonal matrix $Q^{-1}BQ$ will have the eigenvalues in a corresponding rearranged order: $\begin{bmatrix} 0 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 0 \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-4].

*   For $A = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 2 & 0 \\ -3 & 5 & 2 \end{bmatrix}$:
    *   **Step 1:** $A$ is a lower triangular matrix, so its eigenvalues are its diagonal entries: $1$ and $2$ (with algebraic multiplicity $2$ for $\lambda=2$) [source:ma2001-lecture-chapter6-pdf#section-4].
    *   **Step 2:**
        *   For $\lambda = 1$: Solve $(1I - A)x = 0 \implies \begin{bmatrix} 0 & 0 & 0 \\ -1 & -1 & 0 \\ 3 & -5 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$.
            Row reducing leads to $S_1 = \left\{ \begin{bmatrix} 1 \\ -1 \\ 8 \end{bmatrix} \right\}$.
        *   For $\lambda = 2$: Solve $(2I - A)x = 0 \implies \begin{bmatrix} 1 & 0 & 0 \\ -1 & 0 & 0 \\ 3 & -5 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$.
            Row reducing leads to $S_2 = \left\{ \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \right\}$.
    *   **Step 3:** $S = \left\{ \begin{bmatrix} 1 \\ -1 \\ 8 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \right\}$. $|S|=2$, which is less than $n=3$. Therefore, $A$ is not diagonalizable [source:ma2001-lecture-chapter6-pdf#section-4].
        The characteristic polynomial of $A$ is $\det(\lambda I - A) = (\lambda - 1)(\lambda - 2)^2$. The algebraic multiplicity of $\lambda=2$ is $2$, but the geometric multiplicity (dimension of $E_2$) is $1$. Since $1 \neq 2$, $A$ is not diagonalizable.

## Power of Matrices
Diagonalization is particularly useful for computing integer powers of a matrix $A$ [source:ma2001-lecture-chapter6-pdf#section-5].
If $A = PDP^{-1}$ for some diagonal matrix $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$, then for any positive integer $m$:
$A^m = PD^m P^{-1} = P \begin{bmatrix} \lambda_1^m & 0 & \dots & 0 \\ 0 & \lambda_2^m & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n^m \end{bmatrix} P^{-1}$ [source:ma2001-lecture-chapter6-pdf#section-5].

If $A$ is invertible (meaning none of its eigenvalues are zero, by Theorem 6.1.8), then for any positive integer $m$:
$A^{-1} = PD^{-1}P^{-1} = P \begin{bmatrix} \lambda_1^{-1} & 0 & \dots & 0 \\ 0 & \lambda_2^{-1} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n^{-1} \end{bmatrix} P^{-1}$
$A^{-m} = PD^{-m}P^{-1} = P \begin{bmatrix} \lambda_1^{-m} & 0 & \dots & 0 \\ 0 & \lambda_2^{-m} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n^{-m} \end{bmatrix} P^{-1}$ [source:ma2001-lecture-chapter6-pdf#section-5].

**Example:**
Let $A = \begin{bmatrix} -4 & 0 & -6 \\ 2 & 1 & 2 \\ 3 & 0 & 5 \end{bmatrix}$. Following Algorithm 6.2.4, we find $P = \begin{bmatrix} -2 & 0 & -1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$ such that $P^{-1}AP = D = \begin{bmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-5].
Then $A^m = P \begin{bmatrix} (-1)^m & 0 & 0 \\ 0 & 1^m & 0 \\ 0 & 0 & 2^m \end{bmatrix} P^{-1}$ [source:ma2001-lecture-chapter6-pdf#section-5].
For instance, $A^{10} = \begin{bmatrix} -2 & 0 & -1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix} \begin{bmatrix} (-1)^{10} & 0 & 0 \\ 0 & 1^{10} & 0 \\ 0 & 0 & 2^{10} \end{bmatrix} \begin{bmatrix} -2 & 0 & -1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}^{-1} = \begin{bmatrix} -1022 & 0 & -2046 \\ 0 & 1 & 0 \\ 1023 & 0 & 2047 \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-5].

**Application to Fibonacci Numbers:**
Fibonacci numbers are defined by the sequence $(a_0, a_1, a_2, \dots)$ where $a_0=0, a_1=1$, and $a_n = a_{n-1} + a_{n-2}$ for $n \ge 2$ [source:ma2001-lecture-chapter6-pdf#section-5].
This can be formulated as a matrix equation:
$\begin{bmatrix} a_n \\ a_{n+1} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} a_{n-1} \\ a_n \end{bmatrix}$.
Let $x_n = \begin{bmatrix} a_n \\ a_{n+1} \end{bmatrix}$ and $A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$. Then $x_n = Ax_{n-1}$, which means $x_n = A^n x_0$ where $x_0 = \begin{bmatrix} a_0 \\ a_1 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-5].
To compute $A^n$, we diagonalize $A$. The eigenvalues of $A$ are $\frac{1+\sqrt{5}}{2}$ and $\frac{1-\sqrt{5}}{2}$.
We find an invertible matrix $P = \begin{bmatrix} 1 & 1 \\ \frac{1+\sqrt{5}}{2} & \frac{1-\sqrt{5}}{2} \end{bmatrix}$ such that $P^{-1}AP = D = \begin{bmatrix} \frac{1+\sqrt{5}}{2} & 0 \\ 0 & \frac{1-\sqrt{5}}{2} \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-5].
Then $A^n = PD^nP^{-1}$. Computing $A^n x_0$ allows us to find a closed-form expression for $a_n$, which is Binet's formula: $a_n = \frac{1}{\sqrt{5}} \left[ \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right]$ [source:ma2001-lecture-chapter6-pdf#section-5].

## Orthogonal Diagonalization

**Definition:**
A square matrix $A$ is called **orthogonally diagonalizable** if there exists an **orthogonal matrix** $P$ such that $P^TAP$ is a diagonal matrix. The matrix $P$ is said to orthogonally diagonalize $A$ [source:ma2001-lecture-chapter6-pdf#section-6].
Recall that an orthogonal matrix $P$ satisfies $P^{-1} = P^T$. So, for an orthogonally diagonalizable matrix, $P^{-1}AP = P^TAP$ [source:ma2001-lecture-chapter6-pdf#section-6].

**Theorem:** An $n \times n$ matrix $A$ is orthogonally diagonalizable if and only if $A$ is symmetric (i.e., $A^T = A$) [source:ma2001-lecture-chapter6-pdf#section-6].

**Proof (Outline for "only if" part):**
Suppose $A$ is orthogonally diagonalizable. Then there exists an orthogonal matrix $P$ such that $P^TAP = D$, where $D$ is a diagonal matrix.
Since $P$ is orthogonal, $P^{-1} = P^T$. Thus, $A = PDP^{-1} = PDP^T$.
Now, consider $A^T$:
$A^T = (PDP^T)^T = (P^T)^T D^T P^T = PD^T P^T$.
Since $D$ is a diagonal matrix, $D^T = D$.
So, $A^T = PDP^T = A$. Thus, $A$ is symmetric [source:ma2001-lecture-chapter6-pdf#section-6].

**Properties of Symmetric Matrices relevant to Diagonalization:**
*   The eigenvalues of a symmetric matrix are always real numbers [source:ma2001-lecture-chapter6-pdf#section-6].
*   For a symmetric matrix $A$, eigenvectors from different eigenspaces are always orthogonal to each other [source:ma2001-lecture-chapter6-pdf#section-6].
    *   Proof: Let $u$ and $v$ be eigenvectors from eigenspaces $E_\lambda$ and $E_\mu$ respectively, with $\lambda \neq \mu$.
        Then $Au = \lambda u$ and $Av = \mu v$.
        Consider $(Au) \cdot v = (Au)^T v = u^T A^T v$. Since $A$ is symmetric, $A^T = A$, so $u^T A v = u^T (Av) = u \cdot (Av)$.
        Thus, $\lambda (u \cdot v) = u \cdot (\mu v) = \mu (u \cdot v)$.
        This implies $(\lambda - \mu)(u \cdot v) = 0$. Since $\lambda \neq \mu$, we must have $u \cdot v = 0$. Hence $u$ and $v$ are orthogonal [source:ma2001-lecture-chapter6-pdf#section-6].
*   For each eigenvalue $\lambda_i$ of a symmetric matrix $A$, the geometric multiplicity $\dim(E_{\lambda_i})$ equals its algebraic multiplicity $r_i$ [source:ma2001-lecture-chapter6-pdf#section-6].

### Algorithm to Orthogonally Diagonalize a Symmetric Matrix
To orthogonally diagonalize an $n \times n$ symmetric matrix $A$:
**Step 1:** Find all distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_k$ by solving the characteristic equation $\det(\lambda I - A) = 0$ [source:ma2001-lecture-chapter6-pdf#section-6].
**Step 2:** For each eigenvalue $\lambda_i$:
    *   (a) Find a basis $S_{\lambda_i}$ for the eigenspace $E_{\lambda_i}$ [source:ma2001-lecture-chapter6-pdf#section-6].
    *   (b) Use the [[gram-schmidt-process|Gram-Schmidt Process]] to transform $S_{\lambda_i}$ into an orthonormal basis $T_{\lambda_i}$ [source:ma2001-lecture-chapter6-pdf#section-6].
**Step 3:** Let $T = T_{\lambda_1} \cup T_{\lambda_2} \cup \dots \cup T_{\lambda_k}$ be the union of all these orthonormal bases. Since eigenvectors from distinct eigenspaces of a symmetric matrix are orthogonal, the set $T$ will be an orthonormal set of $n$ vectors.
Form the matrix $P = [v_1 \ v_2 \ \dots \ v_n]$ whose columns are the vectors in $T$. This $P$ will be an orthogonal matrix that orthogonally diagonalizes $A$ [source:ma2001-lecture-chapter6-pdf#section-6].

**Examples of Orthogonal Diagonalization:**
*   Let $A = \begin{bmatrix} 1 & -1/2 \\ -1/2 & 1 \end{bmatrix}$. This matrix is symmetric.
    *   **Step 1:** $\det(\lambda I - A) = \det \begin{bmatrix} \lambda-1 & 1/2 \\ 1/2 & \lambda-1 \end{bmatrix} = (\lambda-1)^2 - (1/2)^2 = \lambda^2 - 2\lambda + 1 - 1/4 = \lambda^2 - 2\lambda + 3/4 = (\lambda - 1/2)(\lambda - 3/2)$.
        Eigenvalues are $1/2$ and $3/2$ [source:ma2001-lecture-chapter6-pdf#section-6].
    *   **Step 2:**
        *   For $\lambda = 1/2$: Solve $(1/2 I - A)x = 0 \implies \begin{bmatrix} -1/2 & 1/2 \\ 1/2 & -1/2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies -x+y=0 \implies y=x$.
            $S_{1/2} = \left\{ \begin{bmatrix} 1 \\ 1 \end{bmatrix} \right\}$. Normalizing gives $T_{1/2} = \left\{ \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix} \right\}$.
        *   For $\lambda = 3/2$: Solve $(3/2 I - A)x = 0 \implies \begin{bmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies x+y=0 \implies y=-x$.
            $S_{3/2} = \left\{ \begin{bmatrix} -1 \\ 1 \end{bmatrix} \right\}$. Normalizing gives $T_{3/2} = \left\{ \frac{1}{\sqrt{2}} \begin{bmatrix} -1 \\ 1 \end{bmatrix} \right\}$.
    *   **Step 3:** Form $P$ using the orthonormal eigenvectors: $P = \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$.
        Then $P^TAP = \begin{bmatrix} 1/2 & 0 \\ 0 & 3/2 \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-6].

## Quadratic Forms and Conic Sections

Orthogonal diagonalization has important applications in simplifying quadratic forms and classifying conic sections [source:ma2001-lecture-chapter6-pdf#section-6].

**Definition: Quadratic Form**
An expression of the form $Q(x_1, x_2, \dots, x_n) = \sum_{i=1}^n \sum_{j=i}^n q_{ij} x_i x_j$ is called a **quadratic form** in $n$ variables $x_1, x_2, \dots, x_n$, where $q_{ij}$ are real numbers [source:ma2001-lecture-chapter6-pdf#section-7].
A quadratic form can be written in matrix form as $Q(x) = x^T A x$, where $x = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$ and $A = (a_{ij})$ is an $n \times n$ symmetric matrix defined by:
$a_{ii} = q_{ii}$
$a_{ij} = a_{ji} = \frac{1}{2}q_{ij}$ for $i < j$ [source:ma2001-lecture-chapter6-pdf#section-7].

**Examples of Quadratic Forms:**
*   $Q_1(x,y) = x^2 - xy + y^2$. This can be written as $[x \ y] \begin{bmatrix} 1 & -1/2 \\ -1/2 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-7].
*   $Q_2(x,y,z) = x^2 + 2y^2 + z^2 + 2xz$. This can be written as $[x \ y \ z] \begin{bmatrix} 1 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-7].

**Simplifying Quadratic Forms:**
Since the matrix $A$ in $Q(x) = x^T A x$ is symmetric, it is orthogonally diagonalizable (by Theorem 6.3.4). We can find an orthogonal matrix $P$ such that $P^TAP = D$, where $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$ contains the eigenvalues of $A$ [source:ma2001-lecture-chapter6-pdf#section-7].
By defining new variables $y = P^T x$ (which implies $x = Py$ since $P^T = P^{-1}$), we can transform the quadratic form:
$Q(x) = x^T A x = (Py)^T A (Py) = y^T P^T A P y = y^T D y$.
So, in the new coordinates $y = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}$, the quadratic form simplifies to $Q(y) = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \dots + \lambda_n y_n^2$ [source:ma2001-lecture-chapter6-pdf#section-7]. This transformation eliminates the cross-product terms.

**Example of Simplifying Quadratic Forms:**
*   Consider $Q_1(x,y) = x^2 - xy + y^2$. The associated matrix is $A = \begin{bmatrix} 1 & -1/2 \\ -1/2 & 1 \end{bmatrix}$.
    From the previous orthogonal diagonalization example, we have $P = \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$ and $D = \begin{bmatrix} 1/2 & 0 \\ 0 & 3/2 \end{bmatrix}$.
    Defining new variables $\begin{bmatrix} x' \\ y' \end{bmatrix} = P^T \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} (x+y)/\sqrt{2} \\ (-x+y)/\sqrt{2} \end{bmatrix}$, the quadratic form becomes $Q_1(x',y') = \frac{1}{2}(x')^2 + \frac{3}{2}(y')^2$ [source:ma2001-lecture-chapter6-pdf#section-7].

### Conic Sections
Algebraically, a conic section can be defined by a quadratic equation $ax^2 + bxy + cy^2 + dx + ey = f$ [source:ma2001-lecture-chapter6-pdf#section-8].
This equation can be rewritten in matrix form as $x^T A x + b^T x = f$, where $x = \begin{bmatrix} x \\ y \end{bmatrix}$, $A = \begin{bmatrix} a & b/2 \\ b/2 & c \end{bmatrix}$, and $b = \begin{bmatrix} d \\ e \end{bmatrix}$ [source:ma2001-lecture-chapter6-pdf#section-8].
To identify the type of conic section, we change coordinates using orthogonal diagonalization of the symmetric matrix $A$. This rotates the coordinate system to align with the principal axes of the conic section, eliminating the $xy$ term.

If $P^TAP = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix}$, and we define new variables $y = P^Tx = \begin{bmatrix} x' \\ y' \end{bmatrix}$, the equation becomes $\lambda_1(x')^2 + \lambda_2(y')^2 + gx' + hy' = f$, where $[g \ h] = b^T P$ [source:ma2001-lecture-chapter6-pdf#section-8].

The type of non-degenerate conic section is determined by the eigenvalues $\lambda_1, \lambda_2$:
*   If either $\lambda_1 = 0$ or $\lambda_2 = 0$ (but not both), the curve is a **parabola** [source:ma2001-lecture-chapter6-pdf#section-8].
*   If $\lambda_1 = \lambda_2$, the curve is a **circle** [source:ma2001-lecture-chapter6-pdf#section-8].
*   If $\lambda_1 \lambda_2 > 0$ (i.e., both have the same sign), the curve is an **ellipse** (or a circle if $\lambda_1 = \lambda_2$) [source:ma2001-lecture-chapter6-pdf#section-8].
*   If $\lambda_1 \lambda_2 < 0$ (i.e., they have opposite signs), the curve is a **hyperbola** [source:ma2001-lecture-chapter6-pdf#section-8].

**Standard Forms of Conic Sections:**
*   **Circle/Ellipse:** $\frac{x^2}{\alpha^2} + \frac{y^2}{\beta^2} = 1$ [source:ma2001-lecture-chapter6-pdf#section-8].
*   **Hyperbola:** $\frac{x^2}{\alpha^2} - \frac{y^2}{\beta^2} = 1$ or $-\frac{x^2}{\alpha^2} + \frac{y^2}{\beta^2} = 1$ [source:ma2001-lecture-chapter6-pdf#section-8].
*   **Parabola:** $x^2 = ay$ or $y^2 = ax$ [source:ma2001-lecture-chapter6-pdf#section-8].

**Degenerate Conic Sections:**
A conic section is called **degenerate** if its solution set is an empty set, a single point, a line, or a pair of lines. Conic sections that are not degenerate are called non-degenerate [source:ma2001-lecture-chapter6-pdf#section-8].
Examples of degenerate conic sections:
*   $x^2 + y^2 = -1$ (empty set)
*   $x^2 + y^2 = 0$ (point $(0,0)$)
*   $x^2 - 4y^2 = 0 \implies (x+2y)(x-2y)=0$ (pair of lines $x+2y=0$ and $x-2y=0$)
*   $x^2 + 2xy + y^2 = 0 \implies (x+y)^2=0$ (line $x+y=0$) [source:ma2001-lecture-chapter6-pdf#section-8].

**Example of Classifying a Conic Section:**
Consider the quadratic equation $x^2 - xy + y^2 - x - y = 1$ [source:ma2001-lecture-chapter6-pdf#section-8].
This is $x^T A x + b^T x = f$ with $A = \begin{bmatrix} 1 & -1/2 \\ -1/2 & 1 \end{bmatrix}$ and $b = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$.
From a previous example, $P = \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$ and $P^TAP = D = \begin{bmatrix} 1/2 & 0 \\ 0 & 3/2 \end{bmatrix}$.
The new variables are $\begin{bmatrix} x' \\ y' \end{bmatrix} = P^T \begin{bmatrix} x \\ y \end{bmatrix}$.
The original equation becomes $\frac{1}{2}(x')^2 + \frac{3}{2}(y')^2 + [-1 \ -1]P \begin{bmatrix} x' \\ y' \end{bmatrix} = 1$.
$[-1 \ -1]P = [-1 \ -1]\begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix} = [-2/\sqrt{2} \ 0] = [-\sqrt{2} \ 0]$.
So, the equation is $\frac{1}{2}(x')^2 + \frac{3}{2}(y')^2 - \sqrt{2}x' = 1$ [source:ma2001-lecture-chapter6-pdf#section-8].
Completing the square for $x'$: $\frac{1}{2}((x')^2 - 2\sqrt{2}x') + \frac{3}{2}(y')^2 = 1$.
$\frac{1}{2}((x' - \sqrt{2})^2 - 2) + \frac{3}{2}(y')^2 = 1$.
$\frac{1}{2}(x' - \sqrt{2})^2 + \frac{3}{2}(y')^2 = 2$.
Dividing by $2$: $\frac{(x' - \sqrt{2})^2}{4} + \frac{y'^2}{4/3} = 1$ [source:ma2001-lecture-chapter6-pdf#section-8].
This is the standard form of an **ellipse**, centered at $(\sqrt{2}, 0)$ in the $(x', y')$ coordinate system.

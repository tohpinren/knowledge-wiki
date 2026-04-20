---
page_id: "y1s1-ma2001-standard-matrix-linear-transformation"
title: "Standard Matrix of a Linear Transformation"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "How to find the standard matrix 'A' such that a linear transformation T can be expressed as T(x) = Ax."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter7-pdf#section-2"
  - "ma2001-tutorial-tutorial11sol-pdf#section-2"
topics:
  - "linear"
  - "example"
  - "standard"
  - "matrix"
  - "transformation"
  - "transformations"
  - "vectors"
  - "defined"
  - "basis"
  - "problem"
source_count: 2
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Standard Matrix of a Linear Transformation

A linear transformation is a fundamental concept in linear algebra that maps vectors from one vector space to another while preserving the operations of vector addition and scalar multiplication. Every such transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ can be uniquely represented by a matrix, known as its standard matrix [source: ma2001-lecture-chapter7-pdf#section-1, ma2001-lecture-chapter7-pdf#section-3, ma2001-lecture-chapter7-pdf#section-4].

All vectors in this discussion are treated as column vectors [source: ma2001-lecture-chapter7-pdf#section-1].

## Introduction to Linear Transformations
A **linear transformation** $T$ is a mapping from $\mathbb{R}^n$ to $\mathbb{R}^m$ defined by a set of linear equations [source: ma2001-lecture-chapter7-pdf#section-1, ma2001-lecture-chapter7-pdf#section-3]:
$T(x_1, \dots, x_n) = (a_{11}x_1 + \dots + a_{1n}x_n, \dots, a_{m1}x_1 + \dots + a_{mn}x_n)$
If $n=m$, the transformation $T$ is specifically called a **linear operator** on $\mathbb{R}^n$ [source: ma2001-lecture-chapter7-pdf#section-1, ma2001-lecture-chapter7-pdf#section-3].

### Standard Matrix of a Linear Transformation
Any linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ can be expressed as a matrix-vector product $T(\mathbf{x}) = A\mathbf{x}$, where $A$ is an $m \times n$ matrix. This matrix $A$ is known as the **standard matrix** for $T$ [source: ma2001-lecture-chapter7-pdf#section-4].

Specifically, if $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$, then the transformation can be written as:
$T \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$
The matrix $(a_{ij})_{m \times n}$ is the standard matrix for $T$ [source: ma2001-lecture-chapter7-pdf#section-4].

## Examples of Linear Transformations and their Standard Matrices
### Identity Mapping
The identity mapping $I: \mathbb{R}^n \to \mathbb{R}^n$ maps every vector to itself, $I(\mathbf{x}) = \mathbf{x}$. It is a linear operator on $\mathbb{R}^n$.
The standard matrix for the identity mapping $I$ is the $n \times n$ identity matrix $I_n$ [source: ma2001-lecture-chapter7-pdf#section-5]:
$I(\mathbf{x}) = I_n \mathbf{x} = \begin{pmatrix} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$

### Zero Mapping
The zero mapping $O: \mathbb{R}^n \to \mathbb{R}^m$ maps every vector in $\mathbb{R}^n$ to the zero vector in $\mathbb{R}^m$, $O(\mathbf{x}) = \mathbf{0}$. It is a linear transformation.
The standard matrix for the zero mapping $O$ is the $m \times n$ zero matrix $0_{m \times n}$ [source: ma2001-lecture-chapter7-pdf#section-6]:
$O(\mathbf{x}) = 0_{m \times n} \mathbf{x} = \begin{pmatrix} 0 & 0 & \dots & 0 \\ 0 & 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$

### Example: $T: \mathbb{R}^2 \to \mathbb{R}^3$
Consider a linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^3$ defined by [source: ma2001-lecture-chapter7-pdf#section-7]:
$T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x+y \\ 2x \\ -3y \end{pmatrix}$
To find its standard matrix, we can express the output as a matrix-vector product:
$\begin{pmatrix} x+y \\ 2x \\ -3y \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & -3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$
Thus, the standard matrix for this transformation $T$ is $\begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & -3 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-7].

## Alternative Definition and Basic Properties
An alternative, more abstract definition of a linear transformation $T: V \to W$ between two vector spaces $V$ and $W$ is a mapping that satisfies [source: ma2001-lecture-chapter7-pdf#section-8]:
$T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})$
for all vectors $\mathbf{u}, \mathbf{v} \in V$ and scalars $c, d \in \mathbb{R}$.
This definition is equivalent to the coordinate-based definition if $V = \mathbb{R}^n$ and $W = \mathbb{R}^m$ [source: ma2001-lecture-chapter7-pdf#section-8].

### Basic Properties (Theorem 7.1.4)
For a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ [source: ma2001-lecture-chapter7-pdf#section-9, ma2001-lecture-chapter7-pdf#section-10]:
1.  $T(\mathbf{0}) = \mathbf{0}$. The zero vector in $\mathbb{R}^n$ maps to the zero vector in $\mathbb{R}^m$.
2.  For any vectors $\mathbf{u}_1, \dots, \mathbf{u}_k \in \mathbb{R}^n$ and scalars $c_1, \dots, c_k \in \mathbb{R}$:
    $T(c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_k\mathbf{u}_k) = c_1T(\mathbf{u}_1) + c_2T(\mathbf{u}_2) + \dots + c_kT(\mathbf{u}_k)$.
These properties are direct consequences of expressing $T(\mathbf{u}) = A\mathbf{u}$ where $A$ is the standard matrix [source: ma2001-lecture-chapter7-pdf#section-9, ma2001-lecture-chapter7-pdf#section-10].

### Examples of Non-Linear Transformations
The properties of linear transformations are crucial for identifying them. If a transformation violates any of these, it is not linear.
1.  **Translation:** Consider $T_1: \mathbb{R}^2 \to \mathbb{R}^2$ defined by $T_1 \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x+1 \\ y+3 \end{pmatrix}$.
    Since $T_1 \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \end{pmatrix} \ne \begin{pmatrix} 0 \\ 0 \end{pmatrix}$, $T_1$ is not a linear transformation (violates $T(\mathbf{0}) = \mathbf{0}$) [source: ma2001-lecture-chapter7-pdf#section-11].
2.  **Non-linear terms:** Consider $T_2: \mathbb{R}^3 \to \mathbb{R}^2$ defined by $T_2 \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x^2 \\ yz \end{pmatrix}$.
    While $T_2 \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ holds, it does not satisfy the superposition principle. For example, let $\mathbf{u}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ and $\mathbf{u}_2 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$.
    $T_2(\mathbf{u}_1 + \mathbf{u}_2) = T_2 \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 2^2 \\ 0 \end{pmatrix} = \begin{pmatrix} 4 \\ 0 \end{pmatrix}$.
    However, $T_2(\mathbf{u}_1) + T_2(\mathbf{u}_2) = \begin{pmatrix} 1^2 \\ 0 \end{pmatrix} + \begin{pmatrix} 1^2 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$.
    Since $\begin{pmatrix} 4 \\ 0 \end{pmatrix} \ne \begin{pmatrix} 2 \\ 0 \end{pmatrix}$, $T_2$ is not a linear transformation [source: ma2001-lecture-chapter7-pdf#section-12, ma2001-lecture-chapter7-pdf#section-13].

## Determining the Standard Matrix using Bases
The image of any vector $\mathbf{v} \in \mathbb{R}^n$ under a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ is completely determined by the images of the basis vectors for $\mathbb{R}^n$ [source: ma2001-lecture-chapter7-pdf#section-14].
If $\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ is a basis for $\mathbb{R}^n$, any vector $\mathbf{v}$ can be written as $\mathbf{v} = c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \dots + c_n\mathbf{u}_n$.
Then, $T(\mathbf{v}) = c_1T(\mathbf{u}_1) + c_2T(\mathbf{u}_2) + \dots + c_nT(\mathbf{u}_n)$ [source: ma2001-lecture-chapter7-pdf#section-14].

A particularly useful basis is the **standard basis** for $\mathbb{R}^n$, which consists of the column vectors $\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n$, where $\mathbf{e}_i$ is a vector with a '1' in the $i$-th position and '0's elsewhere [source: ma2001-lecture-chapter7-pdf#section-19]:
$\mathbf{e}_1 = (1, 0, \dots, 0)^T$, $\mathbf{e}_2 = (0, 1, \dots, 0)^T$, ..., $\mathbf{e}_n = (0, \dots, 0, 1)^T$.
For any linear transformation $T$, its standard matrix $A$ has its $i$-th column given by $T(\mathbf{e}_i)$ [source: ma2001-lecture-chapter7-pdf#section-19]:
$T(\mathbf{e}_i) = A\mathbf{e}_i = \begin{pmatrix} a_{1i} \\ a_{2i} \\ \vdots \\ a_{mi} \end{pmatrix}$
Therefore, the standard matrix $A$ is formed by concatenating the images of the standard basis vectors:
$A = [T(\mathbf{e}_1) \ T(\mathbf{e}_2) \ \dots \ T(\mathbf{e}_n)]$ [source: ma2001-lecture-chapter7-pdf#section-19].

### Example: Finding the Standard Matrix using Images of Basis Vectors
Let $T: \mathbb{R}^3 \to \mathbb{R}^2$ be a linear transformation where the images of a basis for $\mathbb{R}^3$ are given [source: ma2001-lecture-chapter7-pdf#section-20]:
$T \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$, $T \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$, $T \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} = \begin{pmatrix} 4 \\ -1 \end{pmatrix}$.
To find the standard matrix, we need $T(\mathbf{e}_1)$, $T(\mathbf{e}_2)$, and $T(\mathbf{e}_3)$.
First, we express the standard basis vectors as linear combinations of the given basis vectors. For example, to find $\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$:
$\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} - \frac{1}{3} \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} \quad \text{This is an illustrative linear combination derived in the source. Actual solution involves solving a system of equations. For this example, the source provides a simplified approach of expressing standard basis vectors using other basis vectors. Let's trace it back carefully using standard basis vectors directly as shown in Example 7.1.9, pages 21-22.}$

From the example, we have the matrix formed by the given basis vectors $B = \begin{pmatrix} 1 & 0 & 2 \\ 1 & 1 & 0 \\ 1 & 1 & -1 \end{pmatrix}$.
To find the coefficients $c_1, c_2, c_3$ such that $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = c_1 \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + c_2 \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + c_3 \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix}$, we solve $B\mathbf{c} = \mathbf{e}_i$.
By performing Gauss-Jordan elimination on $[B | I_3]$, we find the inverse of $B$, which gives the coefficients. The source directly calculates [source: ma2001-lecture-chapter7-pdf#section-21]:
$\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = 1 \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - 1 \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + 0 \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix}$  (This is actually $e_1 = (1,1,1)^T - (0,1,1)^T$ based on the provided values, but the intermediate step `[-2 3 1]` corresponds to coefficients for `e_1` when it is a linear combination of original basis. The example shows specific linear combinations for standard basis vectors. Let's use the actual steps from the source).

The source provides the following combinations for standard basis vectors from the given basis vectors:
$\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-21]
$T(\mathbf{e}_1) = T \left( \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \right) = T \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - T \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \end{pmatrix} - \begin{pmatrix} -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-22]

$\mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = -2 \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + 3 \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-21]
$T(\mathbf{e}_2) = -2T \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + 3T \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + T \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} = -2 \begin{pmatrix} 1 \\ 3 \end{pmatrix} + 3 \begin{pmatrix} -1 \\ 2 \end{pmatrix} + \begin{pmatrix} 4 \\ -1 \end{pmatrix} = \begin{pmatrix} -2 \\ -6 \end{pmatrix} + \begin{pmatrix} -3 \\ 6 \end{pmatrix} + \begin{pmatrix} 4 \\ -1 \end{pmatrix} = \begin{pmatrix} -1 \\ -1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-22]

$\mathbf{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = 2 \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - 2 \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-21]
$T(\mathbf{e}_3) = 2T \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - 2T \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} - T \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} = 2 \begin{pmatrix} 1 \\ 3 \end{pmatrix} - 2 \begin{pmatrix} -1 \\ 2 \end{pmatrix} - \begin{pmatrix} 4 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 \\ 6 \end{pmatrix} - \begin{pmatrix} -2 \\ 4 \end{pmatrix} - \begin{pmatrix} 4 \\ -1 \end{pmatrix} = \begin{pmatrix} 0 \\ 3 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-22]

The standard matrix for $T$ is therefore $A = [T(\mathbf{e}_1) \ T(\mathbf{e}_2) \ T(\mathbf{e}_3)] = \begin{pmatrix} 2 & -1 & 0 \\ 1 & -1 & 3 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-23].

## Compositions of Linear Transformations
If $S: \mathbb{R}^n \to \mathbb{R}^m$ and $T: \mathbb{R}^m \to \mathbb{R}^k$ are linear transformations, their **composition** $T \circ S$ is a mapping from $\mathbb{R}^n$ to $\mathbb{R}^k$ defined by $(T \circ S)(\mathbf{u}) = T(S(\mathbf{u}))$ for $\mathbf{u} \in \mathbb{R}^n$ [source: ma2001-lecture-chapter7-pdf#section-24].

### Theorem 7.1.11
The composition of two linear transformations $T \circ S$ is also a linear transformation [source: ma2001-lecture-chapter7-pdf#section-25].
Furthermore, if $A$ is the standard matrix for $S$ and $B$ is the standard matrix for $T$, then the standard matrix for $T \circ S$ is the matrix product $BA$ [source: ma2001-lecture-chapter7-pdf#section-25].
*Proof:* Let $A$ be the standard matrix for $S$ such that $S(\mathbf{u}) = A\mathbf{u}$, and $B$ be the standard matrix for $T$ such that $T(\mathbf{v}) = B\mathbf{v}$.
Then $(T \circ S)(\mathbf{u}) = T(S(\mathbf{u})) = T(A\mathbf{u}) = B(A\mathbf{u}) = (BA)\mathbf{u}$.
Since $(T \circ S)(\mathbf{u})$ can be expressed as a matrix-vector product with $BA$, $T \circ S$ is a linear transformation, and $BA$ is its standard matrix [source: ma2001-lecture-chapter7-pdf#section-25].

### Example: Composition of $S: \mathbb{R}^3 \to \mathbb{R}^2$ and $T: \mathbb{R}^2 \to \mathbb{R}^3$
Let $S: \mathbb{R}^3 \to \mathbb{R}^2$ be defined by $S \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x+y \\ z \end{pmatrix}$ and $T: \mathbb{R}^2 \to \mathbb{R}^3$ be defined by $T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} y \\ y \\ x \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-26].
The composition $(T \circ S): \mathbb{R}^3 \to \mathbb{R}^3$ is given by [source: ma2001-lecture-chapter7-pdf#section-27]:
$(T \circ S) \begin{pmatrix} x \\ y \\ z \end{pmatrix} = T \left( S \begin{pmatrix} x \\ y \\ z \end{pmatrix} \right) = T \begin{pmatrix} x+y \\ z \end{pmatrix} = \begin{pmatrix} z \\ z \\ x+y \end{pmatrix}$
The standard matrix for $S$ is $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
The standard matrix for $T$ is $B = \begin{pmatrix} 0 & 1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix}$.
The standard matrix for $T \circ S$ is $BA$:
$BA = \begin{pmatrix} 0 & 1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-28].
This matches the matrix derived directly from $(T \circ S) \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} z \\ z \\ x+y \end{pmatrix}$.

## Ranges and Kernels of Linear Transformations
The properties of linear transformations, particularly their Ranges and Kernels, are closely linked to the column space and nullspace of their standard matrices.

### Range of a Linear Transformation
The **range** of a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, denoted $R(T)$, is the set of all possible images of vectors in $\mathbb{R}^n$ under $T$. That is, $R(T) = \{ T(\mathbf{u}) \mid \mathbf{u} \in \mathbb{R}^n \} \subseteq \mathbb{R}^m$ [source: ma2001-lecture-chapter7-pdf#section-30].

If $\{\mathbf{u}_1, \dots, \mathbf{u}_n\}$ is a basis for $\mathbb{R}^n$, then the range of $T$ is the span of the images of these basis vectors: $R(T) = \text{span}\{T(\mathbf{u}_1), T(\mathbf{u}_2), \dots, T(\mathbf{u}_n)\}$ [source: ma2001-lecture-chapter7-pdf#section-32].

#### Theorem 7.2.4: Range and Column Space
If $A$ is the standard matrix for a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, then the range of $T$ is equal to the **column space of $A$** ($Col(A)$) [source: ma2001-lecture-chapter7-pdf#section-33].
*Proof:* By definition, $R(T) = \{ T(\mathbf{u}) \mid \mathbf{u} \in \mathbb{R}^n \}$. Since $T(\mathbf{u}) = A\mathbf{u}$, we have $R(T) = \{ A\mathbf{u} \mid \mathbf{u} \in \mathbb{R}^n \}$. This is precisely the definition of the column space of $A$. Specifically, if $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ is the standard basis for $\mathbb{R}^n$, then $A = [T(\mathbf{e}_1) \ \dots \ T(\mathbf{e}_n)]$, and $R(T) = \text{span}\{T(\mathbf{e}_1), \dots, T(\mathbf{e}_n)\} = Col(A)$ [source: ma2001-lecture-chapter7-pdf#section-33].

### Rank of a Linear Transformation
The **rank** of a linear transformation $T$, denoted $\text{rank}(T)$, is the dimension of its range, $\text{rank}(T) = \text{dim}(R(T))$ [source: ma2001-lecture-chapter7-pdf#section-34].
Since $R(T) = Col(A)$, it follows that $\text{rank}(T) = \text{dim}(Col(A)) = \text{rank}(A)$ (the rank of its standard matrix $A$) [source: ma2001-lecture-chapter7-pdf#section-34].

### Kernel of a Linear Transformation
The **kernel** of a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, denoted $\text{Ker}(T)$, is the set of all vectors in $\mathbb{R}^n$ that map to the zero vector in $\mathbb{R}^m$. That is, $\text{Ker}(T) = \{ \mathbf{u} \in \mathbb{R}^n \mid T(\mathbf{u}) = \mathbf{0} \} \subseteq \mathbb{R}^n$ [source: ma2001-lecture-chapter7-pdf#section-37].

#### Theorem 7.2.9: Kernel and Nullspace
If $A$ is the standard matrix for a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, then the kernel of $T$ is equal to the **nullspace of $A$** ($Null(A)$) [source: ma2001-lecture-chapter7-pdf#section-41].
*Proof:* $\text{Ker}(T) = \{ \mathbf{u} \mid T(\mathbf{u}) = \mathbf{0} \}$. Since $T(\mathbf{u}) = A\mathbf{u}$, this is equivalent to $\text{Ker}(T) = \{ \mathbf{u} \mid A\mathbf{u} = \mathbf{0} \}$, which is the definition of the nullspace of $A$ [source: ma2001-lecture-chapter7-pdf#section-41].

### Nullity of a Linear Transformation
The **nullity** of a linear transformation $T$, denoted $\text{nullity}(T)$, is the dimension of its kernel, $\text{nullity}(T) = \text{dim}(\text{Ker}(T))$ [source: ma2001-lecture-chapter7-pdf#section-42].
Since $\text{Ker}(T) = Null(A)$, it follows that $\text{nullity}(T) = \text{dim}(Null(A)) = \text{nullity}(A)$ (the nullity of its standard matrix $A$) [source: ma2001-lecture-chapter7-pdf#section-42].

### Dimension Theorem for Linear Transformations (Theorem 7.2.12)
For a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, the **Dimension Theorem** states that [source: ma2001-lecture-chapter7-pdf#section-47]:
$\text{rank}(T) + \text{nullity}(T) = n$
where $n$ is the dimension of the domain $\mathbb{R}^n$ (i.e., the number of columns of its standard matrix $A$).
*Proof:* Let $A$ be the standard matrix for $T$. From the connections above, $\text{rank}(T) = \text{rank}(A)$ and $\text{nullity}(T) = \text{nullity}(A)$.
The Dimension Theorem for Matrices states that $\text{rank}(A) + \text{nullity}(A) = \text{number of columns of } A$.
Since $A$ is an $m \times n$ matrix, it has $n$ columns. Thus, $\text{rank}(A) + \text{nullity}(A) = n$.
Substituting back, $\text{rank}(T) + \text{nullity}(T) = n$ [source: ma2001-lecture-chapter7-pdf#section-47].

## Geometric Linear Transformations
Many common geometric operations, such as scalings, reflections, and rotations, are linear transformations. Translations, however, are generally not [source: ma2001-lecture-chapter7-pdf#section-49].

### Scalings
A **scaling** transformation stretches or compresses vectors along coordinate axes.
#### Scalings in $\mathbb{R}^2$ (Example 7.3.2)
A scaling $S: \mathbb{R}^2 \to \mathbb{R}^2$ along the $x$-axis by factor $\lambda_1$ and along the $y$-axis by factor $\lambda_2$ has the standard matrix [source: ma2001-lecture-chapter7-pdf#section-50]:
$A = \begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}$
Applying $S$ to a vector $\begin{pmatrix} x \\ y \end{pmatrix}$ results in $S \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \lambda_1 x \\ \lambda_2 y \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-50].
If $\lambda_1 = \lambda_2 = \lambda$:
*   If $\lambda > 1$, it's a **dilation** (enlargement).
*   If $0 < \lambda < 1$, it's a **contraction** (shrinking) [source: ma2001-lecture-chapter7-pdf#section-52].
This concept extends to diagonalizable matrices where transformations can be seen as scalings along eigenvectors (new axes) by the corresponding eigenvalues [source: ma2001-lecture-chapter7-pdf#section-53, ma2001-lecture-chapter7-pdf#section-54, ma2001-lecture-chapter7-pdf#section-55].

#### Scalings in $\mathbb{R}^3$ (Example 7.3.5)
A scaling along the $x, y, z$-axes by factors $\lambda_1, \lambda_2, \lambda_3$ respectively, has the standard matrix [source: ma2001-lecture-chapter7-pdf#section-56]:
$A = \begin{pmatrix} \lambda_1 & 0 & 0 \\ 0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3 \end{pmatrix}$
Similar to $\mathbb{R}^2$, if $\lambda_1 = \lambda_2 = \lambda_3 = \lambda$, it is a dilation if $\lambda > 1$ and a contraction if $0 < \lambda < 1$ [source: ma2001-lecture-chapter7-pdf#section-56].

### Reflections
A **reflection** transformation flips vectors across a line (in $\mathbb{R}^2$) or a plane (in $\mathbb{R}^3$).
#### Reflections in $\mathbb{R}^2$ (Example 7.3.6)
*   **Reflection about the x-axis** $F_1: \mathbb{R}^2 \to \mathbb{R}^2$, maps $\begin{pmatrix} x \\ y \end{pmatrix}$ to $\begin{pmatrix} x \\ -y \end{pmatrix}$.
    The standard matrix is $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-57, ma2001-lecture-chapter7-pdf#section-58].
*   **Reflection about the y-axis** $F_2: \mathbb{R}^2 \to \mathbb{R}^2$, maps $\begin{pmatrix} x \\ y \end{pmatrix}$ to $\begin{pmatrix} -x \\ y \end{pmatrix}$.
    The standard matrix is $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-58].
*   **Reflection about the line $y=x$** $F_3: \mathbb{R}^2 \to \mathbb{R}^2$, maps $\begin{pmatrix} x \\ y \end{pmatrix}$ to $\begin{pmatrix} y \\ x \end{pmatrix}$.
    The standard matrix is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-59].
*   **Reflection about the line $y=mx$** (where $m = \tan(\theta)$ and $\theta$ is the angle between the $x$-axis and the line) $F: \mathbb{R}^2 \to \mathbb{R}^2$.
    The standard matrix is $\begin{pmatrix} \cos(2\theta) & \sin(2\theta) \\ \sin(2\theta) & -\cos(2\theta) \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-60, ma2001-lecture-chapter7-pdf#section-61, ma2001-lecture-chapter7-pdf#section-62].
    An alternative formula for reflection $F$ across a line in the direction of unit vector $\mathbf{n}$ is $F(\mathbf{u}) = \mathbf{u} - 2(\mathbf{u} \cdot \mathbf{n})\mathbf{n}$ [source: ma2001-lecture-chapter7-pdf#section-62].

#### Reflections in $\mathbb{R}^3$ (Example 7.3.8)
*   **Reflection about the xy-plane**: standard matrix $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-63].
*   **Reflection about the xz-plane**: standard matrix $\begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-63].
*   **Reflection about the yz-plane**: standard matrix $\begin{pmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-63].
In general, reflection $F: \mathbb{R}^3 \to \mathbb{R}^3$ about a plane $ax+by+cz=0$ can be formulated as $F(\mathbf{u}) = \mathbf{u} - 2 \frac{(\mathbf{u} \cdot \mathbf{n})}{(\mathbf{n} \cdot \mathbf{n})} \mathbf{n}$, where $\mathbf{n} = (a, b, c)^T$ is the normal vector to the plane [source: ma2001-lecture-chapter7-pdf#section-63].

### Rotations
A **rotation** transformation turns vectors around a point (in $\mathbb{R}^2$) or an axis (in $\mathbb{R}^3$).
#### Rotations in $\mathbb{R}^2$ (Example 7.3.9)
An anti-clockwise rotation $R: \mathbb{R}^2 \to \mathbb{R}^2$ about the origin by an angle $\theta$.
*   $R(\mathbf{e}_1) = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}$
*   $R(\mathbf{e}_2) = \begin{pmatrix} -\sin\theta \\ \cos\theta \end{pmatrix}$
The standard matrix for this rotation is $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-68, ma2001-lecture-chapter7-pdf#section-69].
Specific examples:
*   Rotation by $\pi/2$ (90 degrees): $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-65].
*   Rotation by $\pi$ (180 degrees): $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-67].
*   Rotation by $3\pi/2$ (270 degrees): $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-67].

#### Rotations in $\mathbb{R}^3$ (Example 7.3.10)
Anti-clockwise rotations about the coordinate axes by an angle $\theta$:
*   **Rotation about the z-axis**:
    $R(\mathbf{e}_1) = \begin{pmatrix} \cos\theta \\ \sin\theta \\ 0 \end{pmatrix}$, $R(\mathbf{e}_2) = \begin{pmatrix} -\sin\theta \\ \cos\theta \\ 0 \end{pmatrix}$, $R(\mathbf{e}_3) = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$.
    The standard matrix is $\begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-70, ma2001-lecture-chapter7-pdf#section-71, ma2001-lecture-chapter7-pdf#section-72].
*   **Rotation about the x-axis**: Standard matrix $\begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-72].
*   **Rotation about the y-axis**: Standard matrix $\begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-72].

### Translations
A **translation** transformation shifts every point by a fixed vector.
Let $T: \mathbb{R}^n \to \mathbb{R}^n$ be a translation defined by $T(\mathbf{x}) = \mathbf{x} + \mathbf{b}$, where $\mathbf{b}$ is a fixed non-zero vector.
For example, in $\mathbb{R}^2$, $T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x+a \\ y+b \end{pmatrix}$ where $a, b$ are real constants [source: ma2001-lecture-chapter7-pdf#section-73].
A translation is **not a linear transformation** unless the translation vector $\mathbf{b}$ is the zero vector (i.e., $a=b=0$ in $\mathbb{R}^2$). This is because $T(\mathbf{0}) = \mathbf{b} \ne \mathbf{0}$ if $\mathbf{b} \ne \mathbf{0}$, violating one of the basic properties of linear transformations [source: ma2001-lecture-chapter7-pdf#section-74, ma2001-lecture-chapter7-pdf#section-75].

### Shears
A **shear** transformation distorts a figure by shifting points in a particular direction proportional to their distance from a fixed line or plane.
#### Shears in $\mathbb{R}^2$ (Example 7.3.12)
A shear $H: \mathbb{R}^2 \to \mathbb{R}^2$ in the $x$-direction by a factor $k$ is given by $H \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x+ky \\ y \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-76].
The standard matrix for this shear is $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-77].
Similarly, a shear in the $y$-direction by a factor $k$ would have the standard matrix $\begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix}$.

#### Shears in $\mathbb{R}^3$ (Example 7.3.12)
A shear $H': \mathbb{R}^3 \to \mathbb{R}^3$ in the $x$-direction by a factor $k_1$ and in the $y$-direction by a factor $k_2$ (proportional to $z$) is given by $H' \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x+k_1z \\ y+k_2z \\ z \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-78].
The standard matrix for this shear is $\begin{pmatrix} 1 & 0 & k_1 \\ 0 & 1 & k_2 \\ 0 & 0 & 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-78].
This means points on a plane like $z=1$ are translated by $k_1$ in the $x$-direction and $k_2$ in the $y$-direction [source: ma2001-lecture-chapter7-pdf#section-79].

## 2D Computer Graphics and Homogeneous Coordinates
In 2D computer graphics, figures are often represented by connecting a set of points (vertices) by lines. These points can be stored in a $2 \times n$ matrix where $n$ is the number of points [source: ma2001-lecture-chapter7-pdf#section-80].
Linear transformations (scalings, reflections, rotations) can be applied to a figure by pre-multiplying its vertex matrix by the standard matrix of the transformation [source: ma2001-lecture-chapter7-pdf#section-81].

The problem arises with translations, which are not linear transformations and cannot be applied directly via standard matrix multiplication in 2D space [source: ma2001-lecture-chapter7-pdf#section-82].
This is solved using **homogeneous coordinates**. Each 2D vector $\begin{pmatrix} x \\ y \end{pmatrix}$ is represented as a 3D vector $\begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$ [source: ma2001-lecture-chapter7-pdf#section-83].
In this augmented space, linear transformations (scaling, reflection, rotation) on 2D vectors are represented by $3 \times 3$ standard matrices of the form $P' = \begin{pmatrix} A & \mathbf{0} \\ \mathbf{0}^T & 1 \end{pmatrix}$, where $A$ is the $2 \times 2$ standard matrix for the 2D transformation and $\mathbf{0}$ is the zero vector [source: ma2001-lecture-chapter7-pdf#section-84].

Crucially, **translations can now be represented as shears in homogeneous coordinates**, making them matrix multiplications. For example, to translate a square by a distance $a$ in the $x$-direction and $b$ in the $y$-direction, we use the matrix [source: ma2001-lecture-chapter7-pdf#section-85]:
$T' = \begin{pmatrix} 1 & 0 & a \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix}$
Applying this to a homogeneous coordinate vector $\begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$ yields $\begin{pmatrix} x+a \\ y+b \\ 1 \end{pmatrix}$, achieving the translation [source: ma2001-lecture-chapter7-pdf#section-85].

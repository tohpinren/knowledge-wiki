---
page_id: "y1s1-ma2001-linear-transformations-intro"
title: "Introduction to Linear Transformations"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Definition and properties of linear transformations between vector spaces, and their representation."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter7-pdf#section-1"
  - "ma2001-tutorial-tutorial11-pdf#section-1"
topics:
  - "linear"
  - "example"
  - "standard"
  - "matrix"
  - "transformation"
  - "transformations"
  - "vectors"
  - "defined"
  - "such"
  - "where"
source_count: 2
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Introduction to Linear Transformations

Linear transformations are fundamental concepts in linear algebra, describing mappings between vector spaces that preserve the operations of vector addition and scalar multiplication. In this module, all vectors are written as column vectors [source:ma2001-lecture-chapter7-pdf#section-1].

---

## Linear Transformations from $\mathbb{R}^n$ to $\mathbb{R}^m$

A **linear transformation** $T$ is a mapping from $\mathbb{R}^n$ to $\mathbb{R}^m$ defined by:
$T(x_1, \ldots, x_n) = (a_{11}x_1 + \ldots + a_{1n}x_n, \ldots, a_{m1}x_1 + \ldots + a_{mn}x_n)$
for any $(x_1, x_2, \ldots, x_n)^T \in \mathbb{R}^n$ [source:ma2001-lecture-chapter7-pdf#section-3].

If $n=m$, $T$ is called a **linear operator** on $\mathbb{R}^n$ [source:ma2001-lecture-chapter7-pdf#section-3].

This definition can be rewritten in matrix form as $T(\mathbf{x}) = A\mathbf{x}$, where $\mathbf{x} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$ and $A = \begin{pmatrix} a_{11} & a_{12} & \ldots & a_{1n} \\ a_{21} & a_{22} & \ldots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \ldots & a_{mn} \end{pmatrix}$. The matrix $A_{(m \times n)}$ is known as the **standard matrix** for $T$ [source:ma2001-lecture-chapter7-pdf#section-4].

### Examples of Linear Transformations

1.  **Identity Mapping** $I: \mathbb{R}^n \to \mathbb{R}^n$:
    Defined by $I(\mathbf{x}) = \mathbf{x}$. The standard matrix for $I$ is the identity matrix $I_n$ [source:ma2001-lecture-chapter7-pdf#section-5].
    $\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} 1 & 0 & \ldots & 0 \\ 0 & 1 & \ldots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ldots & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$
    The identity mapping is a linear operator on $\mathbb{R}^n$ [source:ma2001-lecture-chapter7-pdf#section-5].

2.  **Zero Mapping** $O: \mathbb{R}^n \to \mathbb{R}^m$:
    Defined by $O(\mathbf{x}) = \mathbf{0}$. The standard matrix for $O$ is the zero matrix $O_{m \times n}$ [source:ma2001-lecture-chapter7-pdf#section-6].
    $\begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & \ldots & 0 \\ 0 & 0 & \ldots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ldots & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$
    The zero mapping is a linear transformation [source:ma2001-lecture-chapter7-pdf#section-6].

3.  **Example Mapping** $T: \mathbb{R}^2 \to \mathbb{R}^3$:
    Defined by $T\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x+y \\ 2x \\ -3y \end{pmatrix}$.
    This is a linear transformation with standard matrix $A = \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & -3 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-7].

### Alternative Definition (for Abstract Vector Spaces)

A mapping $T: V \to W$ between two vector spaces $V$ and $W$ is a linear transformation if and only if for all $\mathbf{u}, \mathbf{v} \in V$ and scalars $c, d \in \mathbb{R}$:
$T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})$ [source:ma2001-lecture-chapter7-pdf#section-8].
This is the general definition of a linear transformation in abstract linear algebra. The two definitions are equivalent if $V = \mathbb{R}^n$ and $W = \mathbb{R}^m$ [source:ma2001-lecture-chapter7-pdf#section-8].

### Basic Properties of Linear Transformations

For a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ [source:ma2001-lecture-chapter7-pdf#section-9]:
1.  $T(\mathbf{0}) = \mathbf{0}$.
2.  For any vectors $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_k \in \mathbb{R}^n$ and scalars $c_1, c_2, \ldots, c_k \in \mathbb{R}$:
    $T(c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \ldots + c_k\mathbf{u}_k) = c_1T(\mathbf{u}_1) + c_2T(\mathbf{u}_2) + \ldots + c_kT(\mathbf{u}_k)$ [source:ma2001-lecture-chapter7-pdf#section-9, ma2001-lecture-chapter7-pdf#section-10].

These properties can be proven by using the standard matrix $A$ for $T$, such that $T(\mathbf{u}) = A\mathbf{u}$ [source:ma2001-lecture-chapter7-pdf#section-9].
1.  $T(\mathbf{0}) = A\mathbf{0} = \mathbf{0}$.
2.  $T(c_1\mathbf{u}_1 + \ldots + c_k\mathbf{u}_k) = A(c_1\mathbf{u}_1 + \ldots + c_k\mathbf{u}_k) = c_1A\mathbf{u}_1 + \ldots + c_kA\mathbf{u}_k = c_1T(\mathbf{u}_1) + \ldots + c_kT(\mathbf{u}_k)$.

### Identifying Non-Linear Transformations

A function is *not* a linear transformation if it violates any of the basic properties.

**Example 1: Translation**
Let $T_1: \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $T_1\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x+1 \\ y+3 \end{pmatrix}$.
Here, $T_1\begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \end{pmatrix} \ne \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.
Since $T_1(\mathbf{0}) \ne \mathbf{0}$, $T_1$ is not a linear transformation [source:ma2001-lecture-chapter7-pdf#section-11].

**Example 2: Non-linear terms**
Let $T_2: \mathbb{R}^3 \to \mathbb{R}^2$ be defined by $T_2\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x^2 \\ yz \end{pmatrix}$.
While $T_2(\mathbf{0}) = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ is satisfied, consider $T_2(c\mathbf{u}) = cT_2(\mathbf{u})$.
Let $\mathbf{u} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$. Then $T_2\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1^2 \\ 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
Now, $c\mathbf{u} = \begin{pmatrix} c \\ 0 \\ 0 \end{pmatrix}$. So $T_2\begin{pmatrix} c \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} c^2 \\ 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} c^2 \\ 0 \end{pmatrix}$.
For $T_2$ to be linear, $T_2(c\mathbf{u})$ must equal $cT_2(\mathbf{u})$, meaning $\begin{pmatrix} c^2 \\ 0 \end{pmatrix} = c\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} c \\ 0 \end{pmatrix}$. This implies $c^2 = c$, which is only true for $c=0$ or $c=1$. Thus, it is not generally true for all scalars $c$.
Alternatively, consider $T_2(\mathbf{u} + \mathbf{v}) = T_2(\mathbf{u}) + T_2(\mathbf{v})$.
Let $\mathbf{u} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ and $\mathbf{v} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$. Then $\mathbf{u} + \mathbf{v} = \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}$.
$T_2(\mathbf{u} + \mathbf{v}) = T_2\begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 2^2 \\ 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 4 \\ 0 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-13].
$T_2(\mathbf{u}) + T_2(\mathbf{v}) = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-13].
Since $\begin{pmatrix} 4 \\ 0 \end{pmatrix} \ne \begin{pmatrix} 2 \\ 0 \end{pmatrix}$, $T_2$ is not a linear transformation [source:ma2001-lecture-chapter7-pdf#section-13].

### Standard Matrix of a Linear Transformation

If $\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n\}$ is a basis for $\mathbb{R}^n$, then the image $T(\mathbf{v})$ of any vector $\mathbf{v} \in \mathbb{R}^n$ is completely determined by the images $T(\mathbf{u}_1), T(\mathbf{u}_2), \ldots, T(\mathbf{u}_n)$ of these basis vectors [source:ma2001-lecture-chapter7-pdf#section-14].
This is because any $\mathbf{v}$ can be written as a linear combination $\mathbf{v} = c_1\mathbf{u}_1 + c_2\mathbf{u}_2 + \ldots + c_n\mathbf{u}_n$. Then, by the linearity property, $T(\mathbf{v}) = c_1T(\mathbf{u}_1) + c_2T(\mathbf{u}_2) + \ldots + c_nT(\mathbf{u}_n)$ [source:ma2001-lecture-chapter7-pdf#section-14].

A particularly useful basis is the **standard basis** $\{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n\}$ for $\mathbb{R}^n$, where $\mathbf{e}_i$ is the vector with 1 in the $i$-th position and 0 elsewhere.
For a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, its standard matrix $A$ is given by $A = [T(\mathbf{e}_1) \ T(\mathbf{e}_2) \ \ldots \ T(\mathbf{e}_n)]$. In other words, the $i$-th column of $A$ is $T(\mathbf{e}_i)$ [source:ma2001-lecture-chapter7-pdf#section-19].

**Example:** Let $T: \mathbb{R}^3 \to \mathbb{R}^2$ be a linear transformation such that:
$T\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$, $T\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$, $T\begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} = \begin{pmatrix} 4 \\ -1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-20].
To find the standard matrix of $T$, we need to find $T(\mathbf{e}_1)$, $T(\mathbf{e}_2)$, and $T(\mathbf{e}_3)$.
We can express the standard basis vectors as linear combinations of the given basis vectors:
$\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-21].
$T\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = T\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - T\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \end{pmatrix} - \begin{pmatrix} -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-22].
Similarly, we find $T(\mathbf{e}_2) = \begin{pmatrix} -1 \\ -1 \end{pmatrix}$ and $T(\mathbf{e}_3) = \begin{pmatrix} 0 \\ 3 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-22].
Thus, the standard matrix for $T$ is $A = \begin{pmatrix} 2 & -1 & 0 \\ 1 & -1 & 3 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-23].

### Compositions of Mappings

Let $S: \mathbb{R}^n \to \mathbb{R}^m$ and $T: \mathbb{R}^m \to \mathbb{R}^k$ be linear transformations. The **composition** of $T$ with $S$, denoted by $T \circ S$, is a mapping from $\mathbb{R}^n$ to $\mathbb{R}^k$ defined by $(T \circ S)(\mathbf{u}) = T(S(\mathbf{u}))$ for all $\mathbf{u} \in \mathbb{R}^n$ [source:ma2001-lecture-chapter7-pdf#section-24].

**Theorem:** If $S: \mathbb{R}^n \to \mathbb{R}^m$ and $T: \mathbb{R}^m \to \mathbb{R}^k$ are linear transformations, then $T \circ S$ is also a linear transformation. Furthermore, if $A$ and $B$ are the standard matrices for $S$ and $T$ respectively, then the standard matrix for $T \circ S$ is the matrix product $BA$ [source:ma2001-lecture-chapter7-pdf#section-25].
*Proof:* For any $\mathbf{u} \in \mathbb{R}^n$, we have $S(\mathbf{u}) = A\mathbf{u}$. Then $(T \circ S)(\mathbf{u}) = T(S(\mathbf{u})) = T(A\mathbf{u}) = B(A\mathbf{u}) = (BA)\mathbf{u}$. This shows that $T \circ S$ is a linear transformation and its standard matrix is $BA$ [source:ma2001-lecture-chapter7-pdf#section-25].

---

## Ranges and Kernels

Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation.

### Range of $T$
The **range** of $T$, denoted by $R(T)$ or Im($T$), is the set of all possible images of vectors in $\mathbb{R}^n$ under $T$.
$R(T) = \{ T(\mathbf{u}) \mid \mathbf{u} \in \mathbb{R}^n \} \subseteq \mathbb{R}^m$ [source:ma2001-lecture-chapter7-pdf#section-30].

**Theorem:** If $A$ is the standard matrix for $T$, then $R(T)$ is equal to the [column space of $A$](ma2001-row-column-nullspace#column-space) [source:ma2001-lecture-chapter7-pdf#section-33].
*Proof:* Let $\{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n\}$ be the standard basis for $\mathbb{R}^n$. Any vector $\mathbf{v} \in \mathbb{R}^n$ can be written as $\mathbf{v} = c_1\mathbf{e}_1 + \ldots + c_n\mathbf{e}_n$.
Then $T(\mathbf{v}) = c_1T(\mathbf{e}_1) + \ldots + c_nT(\mathbf{e}_n)$.
Since the columns of $A$ are $T(\mathbf{e}_1), \ldots, T(\mathbf{e}_n)$, $T(\mathbf{v})$ is a linear combination of the columns of $A$. Therefore, $R(T) = \text{span}\{T(\mathbf{e}_1), \ldots, T(\mathbf{e}_n)\} = \text{Col}(A)$ [source:ma2001-lecture-chapter7-pdf#section-32, ma2001-lecture-chapter7-pdf#section-33].

### Rank of $T$
The **rank** of $T$, denoted by $\text{rank}(T)$, is the dimension of the range of $T$, i.e., $\text{rank}(T) = \text{dim}(R(T))$ [source:ma2001-lecture-chapter7-pdf#section-34].
If $A$ is the standard matrix for $T$, then $\text{rank}(T) = \text{dim}(\text{Col}(A)) = \text{rank}(A)$ [source:ma2001-lecture-chapter7-pdf#section-34].

**Example:** Let $T: \mathbb{R}^4 \to \mathbb{R}^4$ be defined by $T\begin{pmatrix} w \\ x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x+2y+z \\ x+3y \\ x+4y-z \\ y-z \end{pmatrix}$.
The standard matrix for $T$ is $A = \begin{pmatrix} 0 & 1 & 2 & 1 \\ 0 & 1 & 3 & 0 \\ 0 & 1 & 4 & -1 \\ 0 & 0 & 1 & -1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-35].
To find the rank, we reduce $A$ to its row echelon form using [Gaussian elimination](ma2001-gaussian-elimination-rref):
$A = \begin{pmatrix} 0 & 1 & 2 & 1 \\ 0 & 1 & 3 & 0 \\ 0 & 1 & 4 & -1 \\ 0 & 0 & 1 & -1 \end{pmatrix} \xrightarrow{\text{Gauss-Jordan Elimination}} \begin{pmatrix} 0 & 1 & 2 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-36].
The pivot columns are the 2nd and 3rd columns. The corresponding columns from the original matrix $A$ form a basis for $\text{Col}(A)$. So, a basis for $R(T)$ can be found using the linearly independent columns of $A$ (which correspond to the pivot columns of the RREF).
For $A$ given, a basis for the column space is $\{(1,1,1,0)^T, (2,3,4,1)^T\}$ (using the original columns corresponding to pivots, but here it seems the example is implicitly taking $(1,1,1,0)^T$ as related to the second column, and $(2,3,4,1)^T$ as related to the third column after some operations). The actual basis for Col(A) from the given A would be its pivot columns, i.e., columns 2 and 3: $\{ (1,1,1,0)^T, (2,3,4,1)^T \}$ or more precisely using the original matrix, the second and third columns of $A$: $\{ \begin{pmatrix} 1 \\ 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 3 \\ 4 \\ 1 \end{pmatrix} \}$.
The number of vectors in this basis is 2, so $\text{rank}(T) = \text{dim}(R(T)) = 2$ [source:ma2001-lecture-chapter7-pdf#section-36].

### Kernel of $T$
The **kernel** of $T$, denoted by $\text{Ker}(T)$ or Null($T$), is the set of all vectors in $\mathbb{R}^n$ whose image under $T$ is the zero vector in $\mathbb{R}^m$.
$\text{Ker}(T) = \{ \mathbf{u} \mid T(\mathbf{u}) = \mathbf{0} \} \subseteq \mathbb{R}^n$ [source:ma20001-lecture-chapter7-pdf#section-37].

**Theorem:** If $A$ is the standard matrix for $T$, then $\text{Ker}(T)$ is equal to the [nullspace of $A$](ma2001-row-column-nullspace#nullspace) [source:ma2001-lecture-chapter7-pdf#section-41].
*Proof:* $\text{Ker}(T) = \{ \mathbf{u} \mid T(\mathbf{u}) = \mathbf{0} \} = \{ \mathbf{u} \mid A\mathbf{u} = \mathbf{0} \}$, which is the definition of the nullspace of $A$ [source:ma2001-lecture-chapter7-pdf#section-41].

### Nullity of $T$
The **nullity** of $T$, denoted by $\text{nullity}(T)$, is the dimension of the kernel of $T$, i.e., $\text{nullity}(T) = \text{dim}(\text{Ker}(T))$ [source:ma2001-lecture-chapter7-pdf#section-42].
If $A$ is the standard matrix for $T$, then $\text{nullity}(T) = \text{dim}(\text{Null}(A)) = \text{nullity}(A)$ [source:ma2001-lecture-chapter7-pdf#section-42].

**Example 1:** Let $T_1: \mathbb{R}^3 \to \mathbb{R}^4$ be defined by $T_1\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 2x-y \\ x-y+3z \\ -5x+y \\ x-z \end{pmatrix}$.
To find $\text{Ker}(T_1)$, we set $T_1(\mathbf{x}) = \mathbf{0}$:
$\begin{pmatrix} 2x-y \\ x-y+3z \\ -5x+y \\ x-z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}$
This forms a system of linear equations. The standard matrix for $T_1$ is $A_1 = \begin{pmatrix} 2 & -1 & 0 \\ 1 & -1 & 3 \\ -5 & 1 & 0 \\ 1 & 0 & -1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-38].
Solving $A_1\mathbf{x} = \mathbf{0}$ yields only the trivial solution $x=0, y=0, z=0$ [source:ma2001-lecture-chapter7-pdf#section-39].
Thus, $\text{Ker}(T_1) = \{ \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \}$ and $\text{nullity}(T_1) = \text{dim}(\text{Ker}(T_1)) = 0$ [source:ma2001-lecture-chapter7-pdf#section-39, ma2001-lecture-chapter7-pdf#section-43].

**Example 2:** Let $T_2: \mathbb{R}^3 \to \mathbb{R}^3$ be defined by $T_2\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} z-y \\ 0 \\ x \end{pmatrix}$.
To find $\text{Ker}(T_2)$, we set $T_2(\mathbf{x}) = \mathbf{0}$:
$\begin{pmatrix} z-y \\ 0 \\ x \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$
This implies $x=0$ and $z-y=0 \Rightarrow z=y$.
So, vectors in $\text{Ker}(T_2)$ are of the form $\begin{pmatrix} 0 \\ t \\ t \end{pmatrix} = t \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$ for $t \in \mathbb{R}$ [source:ma2001-lecture-chapter7-pdf#section-40].
Thus, $\text{Ker}(T_2) = \text{span}\{ \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \}$ and $\text{nullity}(T_2) = \text{dim}(\text{Ker}(T_2)) = 1$ [source:ma2001-lecture-chapter7-pdf#section-40, ma2001-lecture-chapter7-pdf#section-44].

### Dimension Theorem for Linear Transformation (Rank-Nullity Theorem)

Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation. Then:
$\text{rank}(T) + \text{nullity}(T) = n$ [source:ma2001-lecture-chapter7-pdf#section-47].
*Proof:* Let $A$ be the standard matrix for $T$. By the [Dimension Theorem for Matrices](ma2001-dimension-rank-nullity#dimension-theorem-for-matrices), $\text{rank}(A) + \text{nullity}(A) = \text{number of columns of } A$.
Since $A$ is an $m \times n$ matrix, the number of columns is $n$.
Also, $\text{rank}(T) = \text{rank}(A)$ and $\text{nullity}(T) = \text{nullity}(A)$.
Therefore, $\text{rank}(T) + \text{nullity}(T) = n$ [source:ma2001-lecture-chapter7-pdf#section-47].

---

## Geometric Linear Transformations

Several well-known geometric transformations in $\mathbb{R}^2$ and $\mathbb{R}^3$ are linear transformations, including scalings, reflections about lines and planes through the origin, and rotations about the origin [source:ma2001-lecture-chapter7-pdf#section-49].

### Scalings
A scaling transformation stretches or compresses vectors along axes.
For $S: \mathbb{R}^2 \to \mathbb{R}^2$, a scaling transformation along the $x$-axis by factor $\lambda_1$ and $y$-axis by factor $\lambda_2$ has the standard matrix:
$A = \begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-50].
-   If $\lambda_1 = \lambda_2 = \lambda$:
    -   A **dilation** occurs if $\lambda > 1$.
    -   A **contraction** occurs if $\lambda < 1$ [source:ma2001-lecture-chapter7-pdf#section-52].
For $S: \mathbb{R}^3 \to \mathbb{R}^3$, a scaling along the $x, y, z$-axes by factors $\lambda_1, \lambda_2, \lambda_3$ respectively has the standard matrix:
$A = \begin{pmatrix} \lambda_1 & 0 & 0 \\ 0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-56].

If a matrix $A$ is [diagonalizable](ma2001-diagonalization#diagonalization), the transformation $T(\mathbf{x}) = A\mathbf{x}$ can be viewed as a scaling along the directions of its eigenvectors by factors equal to the corresponding eigenvalues [source:ma2001-lecture-chapter7-pdf#section-53, ma2001-lecture-chapter7-pdf#section-54]. The "new axes" (eigenvector directions) may not be perpendicular to each other [source:ma2001-lecture-chapter7-pdf#section-53].

### Reflections
A reflection transformation flips vectors across a line or plane.

**Reflections in $\mathbb{R}^2$:**
1.  **About the $x$-axis:** $F_1\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ -y \end{pmatrix}$. Standard matrix: $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-57, ma2001-lecture-chapter7-pdf#section-58].
2.  **About the $y$-axis:** $F_2\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} -x \\ y \end{pmatrix}$. Standard matrix: $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-58].
3.  **About the line $y=x$:** $F_3\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} y \\ x \end{pmatrix}$. Standard matrix: $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-59].
4.  **About the line $y=mx$ (where $m = \tan(\theta)$):** The standard matrix for this reflection $F$ is $\begin{pmatrix} \cos(2\theta) & \sin(2\theta) \\ \sin(2\theta) & -\cos(2\theta) \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-60, ma2001-lecture-chapter7-pdf#section-61, ma2001-lecture-chapter7-pdf#section-62].
    An alternative formula for reflection $F$ about the line $y=mx$ (or vector $\mathbf{n}$) is $F(\mathbf{u}) = \mathbf{u} - 2(\mathbf{u} \cdot \mathbf{n})\mathbf{n}$ where $\mathbf{n} = (\sin(\theta), -\cos(\theta))^T$ is a unit normal vector to the line [source:ma2001-lecture-chapter7-pdf#section-62].

**Reflections in $\mathbb{R}^3$:**
1.  **About the $xy$-plane:** Standard matrix: $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-63].
2.  **About the $xz$-plane:** Standard matrix: $\begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-63].
3.  **About the $yz$-plane:** Standard matrix: $\begin{pmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-63].
In general, reflection $F: \mathbb{R}^3 \to \mathbb{R}^3$ about a plane $ax+by+cz=0$ (with normal vector $\mathbf{n} = (a, b, c)^T$) can be formulated as $F(\mathbf{u}) = \mathbf{u} - 2\left(\frac{\mathbf{u} \cdot \mathbf{n}}{\mathbf{n} \cdot \mathbf{n}}\right)\mathbf{n}$ [source:ma2001-lecture-chapter7-pdf#section-63].

### Rotations
A rotation transformation rotates vectors around the origin.

**Rotations in $\mathbb{R}^2$:**
An anti-clockwise rotation $R$ about the origin through an angle $\theta$ has the standard matrix:
$R = \begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-68, ma2001-lecture-chapter7-pdf#section-69].
Specific examples:
-   Rotation by $\pi/2$: $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-65].
-   Rotation by $\pi$: $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-67].
-   Rotation by $3\pi/2$: $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-67].

**Rotations in $\mathbb{R}^3$:**
1.  **Anti-clockwise rotation about the $z$-axis through angle $\theta$**:
    $R_z = \begin{pmatrix} \cos(\theta) & -\sin(\theta) & 0 \\ \sin(\theta) & \cos(\theta) & 0 \\ 0 & 0 & 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-70, ma2001-lecture-chapter7-pdf#section-71, ma2001-lecture-chapter7-pdf#section-72].
2.  **Anti-clockwise rotation about the $x$-axis through angle $\theta$**:
    $R_x = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos(\theta) & -\sin(\theta) \\ 0 & \sin(\theta) & \cos(\theta) \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-72].
3.  **Anti-clockwise rotation about the $y$-axis through angle $\theta$**:
    $R_y = \begin{pmatrix} \cos(\theta) & 0 & \sin(\theta) \\ 0 & 1 & 0 \\ -\sin(\theta) & 0 & \cos(\theta) \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-72].

### Translations (Not Linear Transformations)
A translation transformation shifts vectors by a constant amount.
For $T: \mathbb{R}^2 \to \mathbb{R}^2$ defined by $T\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x+a \\ y+b \end{pmatrix}$, where $a, b$ are real constants. This is generally *not* a linear transformation, unless $a=0$ and $b=0$ (the zero translation) [source:ma2001-lecture-chapter7-pdf#section-73, ma2001-lecture-chapter7-pdf#section-74].
Similarly, for $T': \mathbb{R}^3 \to \mathbb{R}^3$ defined by $T'\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x+a \\ y+b \\ z+c \end{pmatrix}$, it is not a linear transformation unless $a=b=c=0$ [source:ma2001-lecture-chapter7-pdf#section-75].

### Shears
A shear transformation skews vectors in a certain direction.
1.  **Shear in $\mathbb{R}^2$ in the $x$-direction by a factor $k$**:
    $H\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x+ky \\ y \end{pmatrix}$. Standard matrix: $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-76, ma2001-lecture-chapter7-pdf#section-77].
2.  **Shear in $\mathbb{R}^3$ in the $x$-direction by $k_1$ and $y$-direction by $k_2$ (dependent on $z$)**:
    $H'\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x+k_1z \\ y+k_2z \\ z \end{pmatrix}$. Standard matrix: $\begin{pmatrix} 1 & 0 & k_1 \\ 0 & 1 & k_2 \\ 0 & 0 & 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-78, ma2001-lecture-chapter7-pdf#section-79].
    This means every point on a plane $z=C$ is translated by $(k_1C, k_2C)$ [source:ma2001-lecture-chapter7-pdf#section-79].

### 2D Computer Graphics and Homogeneous Coordinates
In 2D computer graphics, figures are drawn by connecting points (vertices) by lines. These points can be stored as a $2 \times n$ matrix for $n$ points [source:ma2001-lecture-chapter7-pdf#section-80].
Linear transformations (scalings, reflections, rotations) can be applied to a figure by pre-multiplying the figure's matrix with the standard matrix of the transformation [source:ma2001-lecture-chapter7-pdf#section-81].
However, translations are not linear transformations [source:ma2001-lecture-chapter7-pdf#section-82]. This problem is solved using **homogeneous coordinates** [source:ma2001-lecture-chapter7-pdf#section-82].
In homogeneous coordinates, each vector $\begin{pmatrix} x \\ y \end{pmatrix} \in \mathbb{R}^2$ is represented as a vector $\begin{pmatrix} x \\ y \\ 1 \end{pmatrix} \in \mathbb{R}^3$ [source:ma2001-lecture-chapter7-pdf#section-83].
A geometric linear transformation on $\mathbb{R}^2$ (like scaling or rotation) can be represented by a $3 \times 3$ standard matrix $P'$ acting on these homogeneous coordinates [source:ma2001-lecture-chapter7-pdf#section-84].
A translation in $\mathbb{R}^2$ can then be achieved using a shear transformation in $\mathbb{R}^3$ on the homogeneous coordinates [source:ma2001-lecture-chapter7-pdf#section-85]. For example, translating a square by distance $a$ in $x$-direction and $b$ in $y$-direction uses the shear matrix $\begin{pmatrix} 1 & 0 & a \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix}$ [source:ma2001-lecture-chapter7-pdf#section-85].

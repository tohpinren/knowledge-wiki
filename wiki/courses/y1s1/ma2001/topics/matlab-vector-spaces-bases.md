---
page_id: "y1s1-ma2001-matlab-vector-spaces-bases"
title: "MATLAB for Vector Spaces and Bases"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Applying MATLAB commands to determine linear combinations, linear independence, span, and find bases for vector spaces."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lab-lab3-pdf#section-1"
  - "ma2001-lab-lab3sol-pdf#section-1"
topics:
  - "vectors"
  - "linear"
  - "form"
  - "span"
  - "rref"
  - "basis"
  - "question"
  - "how"
  - "matrix"
  - "columns"
source_count: 2
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# MATLAB for Vector Spaces and Bases

This page provides a guide to using MATLAB's `rref` (reduced row-echelon form) command to solve fundamental problems in linear algebra related to vector spaces, including linear combinations, linear independence, span, bases, and dimension. This approach leverages the computational power of MATLAB to reinforce theoretical understanding [source:ma2001-lab-lab3-pdf#section-1].

Before starting, it is recommended to type `format rat` in the MATLAB workspace. This command ensures that all matrix entries are displayed as rational numbers (fractions) for easier interpretation [source:ma2001-lab-lab3-pdf#section-1].

## 1. Linear Combinations

To determine if a vector $\mathbf{v}$ is a linear combination of a given set of vectors $\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_k\}$, you need to check if the system of linear equations $x_1\mathbf{u}_1 + x_2\mathbf{u}_2 + \ldots + x_k\mathbf{u}_k = \mathbf{v}$ has a solution. This can be expressed as an augmented matrix equation $A\mathbf{x} = \mathbf{v}$, where $A = [\mathbf{u}_1 \ \mathbf{u}_2 \ \ldots \ \mathbf{u}_k]$ [source:ma2001-lab-lab3-pdf#section-1].

### MATLAB Steps

1.  **Input Vectors**: Enter the vectors $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_k$ and $\mathbf{v}$ into MATLAB as column matrices [source:ma2001-lab-lab3-pdf#section-1].
    ```matlab
    u1 = [1; 0; 1; 2; 3];
    u2 = [2; -1; 1; 1; -3];
    u3 = [1; 1; -1; -2; 1];
    u4 = [1; 2; 1; 3; 1];
    v_test1 = [2; 0; 0; 1; 0];
    v_test2 = [-2; -1; 1; -1; 0];
    ```
2.  **Form Matrix A**: Combine the vectors $\mathbf{u}_1, \ldots, \mathbf{u}_k$ into a single matrix $A$ where they form the columns [source:ma2001-lab-lab3-pdf#section-1].
    ```matlab
    A = [u1, u2, u3, u4];
    ```
3.  **Form Augmented Matrix**: Create the augmented matrix $[A \ | \ \mathbf{v}]$ by appending $\mathbf{v}$ as the last column [source:ma2001-lab-lab3-pdf#section-1].
    ```matlab
    Augmented_Matrix_1 = [A, v_test1];
    Augmented_Matrix_2 = [A, v_test2];
    ```
4.  **Compute RREF**: Apply the `rref` command to the augmented matrix [source:ma2001-lab-lab3-pdf#section-2].
    ```matlab
    rref_Augmented_Matrix_1 = rref(Augmented_Matrix_1);
    rref_Augmented_Matrix_2 = rref(Augmented_Matrix_2);
    ```

### Interpretation of Results

*   **Inconsistent System**: If the reduced row-echelon form of $[A \ | \ \mathbf{v}]$ contains a row of the form `[0 0 ... 0 | 1]`, the system is inconsistent, meaning $\mathbf{v}$ is **not** a linear combination of $\mathbf{u}_1, \ldots, \mathbf{u}_k$ [source:ma2001-lab-lab3sol-pdf#section-1].
    *   **Example 1**: For `v_test1`, `rref(Augmented_Matrix_1)` might yield:
        ```
        rref_Augmented_Matrix_1 =
            1     0    -1     0     0
            0     1     1     0     0
            0     0     0     1     0
            0     0     0     0     1
            0     0     0     0     0
        ```
        The fourth row `[0 0 0 0 | 1]` indicates inconsistency. Thus, `v_test1` is not a linear combination of `u1, u2, u3, u4` [source:ma2001-lab-lab3sol-pdf#section-1].
*   **Consistent System**: If no such row exists, the system is consistent, and $\mathbf{v}$ **is** a linear combination of $\mathbf{u}_1, \ldots, \mathbf{u}_k$ [source:ma2001-lab-lab3sol-pdf#section-1].
    *   **Example 2**: For `v_test2`, `rref(Augmented_Matrix_2)` might yield:
        ```
        rref_Augmented_Matrix_2 =
            1     0    -1     0     0
            0     1     1     0    -1
            0     0     0     1     0
            0     0     0     0     0
            0     0     0     0     0
        ```
        Since there is no row `[0 0 0 0 | 1]`, the system is consistent. Thus, `v_test2` is a linear combination of `u1, u2, u3, u4` [source:ma2001-lab-lab3sol-pdf#section-1].

---

## 2. Linear Independence

To check if a given set of vectors $\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_k\}$ is linearly independent, you need to determine if the homogeneous system $x_1\mathbf{u}_1 + x_2\mathbf{u}_2 + \ldots + x_k\mathbf{u}_k = \mathbf{0}$ (or $A\mathbf{x} = \mathbf{0}$) has only the trivial solution ($\mathbf{x} = \mathbf{0}$). Non-trivial solutions imply linear dependence [source:ma2001-lab-lab3-pdf#section-2].

### MATLAB Steps

1.  **Input Vectors**: Enter the vectors $\mathbf{u}_1, \ldots, \mathbf{u}_k$ into MATLAB as column matrices [source:ma2001-lab-lab3-pdf#section-2].
2.  **Form Matrix A**: Combine the vectors into a matrix $A = [\mathbf{u}_1 \ \mathbf{u}_2 \ \ldots \ \mathbf{u}_k]$ [source:ma2001-lab-lab3-pdf#section-2].
3.  **Compute RREF**: Apply the `rref` command to matrix $A$. Although you can form `rref([A, z])` where `z` is the zero vector, `rref(A)` is sufficient because appending a zero column does not change the pivot structure [source:ma2001-lab-lab3-pdf#section-3, ma2001-lab-lab3sol-pdf#section-2].
    ```matlab
    % Example vectors
    u1 = [0; 0; 0; 1; 3; 1]; u2 = [1; 0; 2; 0; 2; 1]; u3 = [1; 1; -3; 8; -6; 1];
    u4 = [2; 2; 1; 3; 4; 1]; u5 = [0; 1; 1; -2; 1; 1]; u6 = [1; 1; 1; 1; 1; 1];
    A_linear_independence = [u1, u2, u3, u4, u5, u6];
    rref_A_independence = rref(A_linear_independence);
    ```

### Interpretation of Results

*   **Linearly Dependent**: If `rref(A)` has any non-pivot columns (columns without a leading `1`), it means there are free variables in the system $A\mathbf{x}=\mathbf{0}$. This leads to non-trivial solutions, and thus the set of vectors is **linearly dependent** [source:ma2001-lab-lab3sol-pdf#section-2].
    *   **Example**: For `A_linear_independence`, `rref_A_independence` might yield:
        ```
        rref_A_independence =
            1     0     4     0     4/5     0
            0     1    -3     0    -3/5     0
            0     0     0     1    -1/5     0
            0     0     0     0     0     1
            0     0     0     0     0     0
            0     0     0     0     0     0
        ```
        Columns 3 and 5 are non-pivot columns. Therefore, the set $\{\mathbf{u}_1, \ldots, \mathbf{u}_6\}$ is linearly dependent [source:ma2001-lab-lab3sol-pdf#section-2].
*   **Linearly Independent**: If all columns in `rref(A)` are pivot columns, the only solution to $A\mathbf{x}=\mathbf{0}$ is the trivial solution ($\mathbf{x} = \mathbf{0}$). This means the set of vectors is **linearly independent** [source:ma2001-lab-lab3sol-pdf#section-2].
    *   **Example**: For a set of vectors `v1, ..., v5` which form matrix `B`:
        ```matlab
        v1 = [1;2;0;0;3]; v2 = [1;-1;0;2;2]; v3 = [1;2;3;4;1];
        v4 = [2;1;1;1;1]; v5 = [0;1;1;1;0];
        B_independence = [v1, v2, v3, v4, v5];
        rref_B_independence = rref(B_independence);
        ```
        `rref_B_independence` might yield:
        ```
        rref_B_independence =
            1     0     0     0     0
            0     1     0     0     0
            0     0     1     0     0
            0     0     0     1     0
            0     0     0     0     1
        ```
        All columns are pivot columns. Thus, the set $\{\mathbf{v}_1, \ldots, \mathbf{v}_5\}$ is linearly independent [source:ma2001-lab-lab3sol-pdf#section-2].

---

## 3. Redundant Vectors

Redundant vectors in a set are those that can be expressed as linear combinations of other vectors in the set. Identifying these is crucial for finding a basis.

### MATLAB Steps

1.  **Form Matrix A**: Combine the vectors into a matrix $A = [\mathbf{u}_1 \ \mathbf{u}_2 \ \ldots \ \mathbf{u}_k]$ [source:ma2001-lab-lab3-pdf#section-3].
2.  **Compute RREF**: Apply the `rref` command to matrix $A$ [source:ma2001-lab-lab3-pdf#section-3].

### Interpretation of Results

*   **Identify Redundant Vectors**: The columns in the original matrix $A$ that correspond to the non-pivot columns in `rref(A)` are the redundant vectors [source:ma2001-lab-lab3sol-pdf#section-3].
    *   **Example**: Using `A_linear_independence` from the previous section:
        ```
        rref_A_independence =
            1     0     4     0     4/5     0
            0     1    -3     0    -3/5     0
            0     0     0     1    -1/5     0
            0     0     0     0     0     1
            0     0     0     0     0     0
            0     0     0     0     0     0
        ```
        Columns 3 and 5 are non-pivot columns. Therefore, $\mathbf{u}_3$ and $\mathbf{u}_5$ are redundant vectors in the set $\{\mathbf{u}_1, \ldots, \mathbf{u}_6\}$ [source:ma2001-lab-lab3sol-pdf#section-3].
*   **Express Redundant Vectors as Linear Combinations**: The entries in the non-pivot columns of `rref(A)` provide the coefficients to express the corresponding redundant vectors as linear combinations of the *pivot column vectors* [source:ma2001-lab-lab3-pdf#section-3].
    *   From `rref_A_independence`, column 3 (non-pivot) has entries $(4, -3, 0, 0, 0, 0)^T$ relative to the pivot columns (1, 2, 4, 6). So, $\mathbf{u}_3 = 4\mathbf{u}_1 - 3\mathbf{u}_2$.
    *   Similarly, column 5 (non-pivot) has entries $(4/5, -3/5, -1/5, 0, 0, 0)^T$ relative to the pivot columns (1, 2, 4, 6), considering the respective positions of the leading 1s. So, $\mathbf{u}_5 = \frac{4}{5}\mathbf{u}_1 - \frac{3}{5}\mathbf{u}_2 - \frac{1}{5}\mathbf{u}_4$ [source:ma2001-lab-lab3sol-pdf#section-3].
    *   You can verify these relations in MATLAB (be aware of potential round-off errors with floating-point arithmetic).

---

## 4. Linear Spans

To determine relationships between the span of two sets of vectors, $S = \{\mathbf{u}_1, \ldots, \mathbf{u}_m\}$ and $T = \{\mathbf{v}_1, \ldots, \mathbf{v}_n\}$, we use the concept of linear combinations.

### Checking if $\text{span}(S) \subseteq \text{span}(T)$

This means every vector in $S$ must be a linear combination of vectors in $T$. This is equivalent to checking if the systems $B\mathbf{x} = \mathbf{u}_i$ are consistent for all $\mathbf{u}_i \in S$, where $B = [\mathbf{v}_1 \ \ldots \ \mathbf{v}_n]$ [source:ma2001-lab-lab3-pdf#section-4].

#### MATLAB Steps

1.  **Input Vectors**: Enter vectors from sets $S$ and $T$ [source:ma2001-lab-lab3-pdf#section-4].
    ```matlab
    % Example vectors from Question 4, Lab3
    u1 = [1; 2; 2; 3]; u2 = [1; 0; 3; 0]; u3 = [1; 1; 1; 1];
    v1 = [3; 2; 1; 7]; v2 = [0; 0; 1; 2]; v3 = [2; -1; 1; 0]; v4 = [-1; 1; 3; -5];
    ```
2.  **Form Matrices**: Create matrices $A = [\mathbf{u}_1 \ \mathbf{u}_2 \ \mathbf{u}_3]$ and $B = [\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{v}_3 \ \mathbf{v}_4]$ [source:ma2001-lab-lab3-pdf#section-4].
    ```matlab
    A_span = [u1, u2, u3];
    B_span = [v1, v2, v3, v4];
    ```
3.  **Compute RREF**: Apply `rref([B, A])`. This effectively solves the systems $B\mathbf{x} = \mathbf{u}_1$, $B\mathbf{x} = \mathbf{u}_2$, and $B\mathbf{x} = \mathbf{u}_3$ simultaneously [source:ma2001-lab-lab3-pdf#section-5].
    ```matlab
    rref_B_A = rref([B_span, A_span]);
    ```

#### Interpretation of Results

*   **$\text{span}(S) \subseteq \text{span}(T)$**: If none of the augmented columns corresponding to vectors in $S$ (i.e., the columns derived from $A$) result in a pivot position in a row `[0 0 ... 0 | 1]`, then all systems $B\mathbf{x} = \mathbf{u}_i$ are consistent. This implies that every $\mathbf{u}_i \in S$ is in $\text{span}(T)$, and thus $\text{span}(S) \subseteq \text{span}(T)$ [source:ma2001-lab-lab3sol-pdf#section-4].
    *   **Example**: `rref_B_A` might yield:
        ```
        rref_B_A =
            1     0     0     2     0     1
            0     1     0   -9/2    3/2    1/2
            0     0     1   -5/2    1/2    1/2
            0     0     0     0     0     0
            0     0     0     0     0     0
        ```
        The last three augmented columns (representing `u1, u2, u3`) do not have a pivot `1` in a row of all zeros to their left. This indicates consistency for all `u_i`. Hence, `span(S) ⊆ span(T)` [source:ma2001-lab-lab3sol-pdf#section-4].

### Checking if $\text{span}(S) = \text{span}(T)$

For the spans to be equal, we need $\text{span}(S) \subseteq \text{span}(T)$ AND $\text{span}(T) \subseteq \text{span}(S)$.

#### MATLAB Steps

1.  After checking $\text{span}(S) \subseteq \text{span}(T)$ (using `rref([B, A])`), you must also check if $\text{span}(T) \subseteq \text{span}(S)$ [source:ma2001-lab-lab3-pdf#section-5].
2.  **Compute RREF**: Apply `rref([A, B])` [source:ma2001-lab-lab3-pdf#section-5].
    ```matlab
    rref_A_B = rref([A_span, B_span]);
    ```

#### Interpretation of Results

*   **$\text{span}(T) \subseteq \text{span}(S)$**: If `rref([A, B])` shows that all systems $A\mathbf{x} = \mathbf{v}_i$ are consistent, then $\text{span}(T) \subseteq \text{span}(S)$ [source:ma2001-lab-lab3sol-pdf#section-5].
    *   **Example**: `rref_A_B` might yield:
        ```
        rref_A_B =
            1     0     0     1     1     -1     0
            0     1     0     1     0     0     2
            0     0     1     1    -1     3     -1
            0     0     0     0     0     0     0
            0     0     0     0     0     0     0
        ```
        All four augmented columns (corresponding to `v1, v2, v3, v4`) are consistent. Hence, `span(T) ⊆ span(S)` [source:ma2001-lab-lab3sol-pdf#section-5].
*   **Conclusion**: If both `rref([B, A])` and `rref([A, B])` indicate consistency for all respective vectors, then $\text{span}(S) = \text{span}(T)$ [source:ma2001-lab-lab3sol-pdf#section-5].

### Checking if $\text{span}(T) \not\subseteq \text{span}(S)$

This occurs if at least one vector in $T$ is *not* a linear combination of vectors in $S$.

#### MATLAB Steps

1.  Use the same vectors as above, but with a modified `v4` for instance [source:ma2001-lab-lab3-pdf#section-6].
    ```matlab
    v4_new = [1; -1; 3; -1; 0]; % assuming 5-dim vectors for this example
    B_span_new = [v1, v2, v3, v4_new];
    rref_A_B_new = rref([A_span, B_span_new]);
    ```

#### Interpretation of Results

*   **$\text{span}(T) \not\subseteq \text{span}(S)$**: If `rref([A, B])` produces a row like `[0 0 ... 0 | 1]` for any of the columns from $B$, then the corresponding vector from $T$ is not in $\text{span}(S)$.
    *   **Example**: `rref_A_B_new` might yield:
        ```
        rref_A_B_new =
            1     0     0     1     1     -1     0
            0     1     0     1     0     0     0
            0     0     1     1    -1     3     0
            0     0     0     0     0     0     1
            0     0     0     0     0     0     0
        ```
        The last augmented column (corresponding to `v4_new`) has a pivot `1` in the fourth row, implying inconsistency. This means $A\mathbf{x} = \mathbf{v}_{\text{4_new}}$ is inconsistent, so $\mathbf{v}_{\text{4_new}}$ is not in $\text{span}(S)$, and therefore $\text{span}(T) \not\subseteq \text{span}(S)$ [source:ma2001-lab-lab3sol-pdf#section-6].

---

## 5. Bases and Dimensions

A basis for a subspace $V$ is a linearly independent set of vectors that spans $V$. The dimension of $V$ is the number of vectors in any basis for $V$ [[linear-independence-bases#basis-of-a-vector-space], [dimension-rank-nullity#dimension]].

### Finding a Basis for $V = \text{span}(S)$

To find a basis for a subspace $V$ spanned by a set of vectors $S = \{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$, we identify the linearly independent vectors within $S$.

#### MATLAB Steps

1.  **Input Vectors**: Enter the vectors from set $S$ [source:ma2001-lab-lab3-pdf#section-7].
    ```matlab
    % Example vectors from Question 7, Lab3
    u1 = [1; 1; 1; 1; 1]; u2 = [1; -1; 2; 3; 0];
    u3 = [-1; -3; 1; -2; 0]; u4 = [0; 1; -1; -1; 1];
    ```
2.  **Form Matrix A**: Create matrix $A = [\mathbf{u}_1 \ \mathbf{u}_2 \ \mathbf{u}_3 \ \mathbf{u}_4]$ [source:ma2001-lab-lab3-pdf#section-7].
    ```matlab
    A_basis = [u1, u2, u3, u4];
    ```
3.  **Compute RREF**: Apply `rref(A)` [source:ma2001-lab-lab3-pdf#section-7].
    ```matlab
    rref_A_basis = rref(A_basis);
    ```

#### Interpretation of Results

*   **Identify Pivot Columns**: Identify the columns in `rref(A)` that contain a leading `1` (pivot columns) [source:ma2001-lab-lab3-pdf#section-7].
    *   **Example**: `rref_A_basis` might yield:
        ```
        rref_A_basis =
            1     0    -2     0
            0     1     1     0
            0     0     0     1
            0     0     0     0
            0     0     0     0
        ```
        Columns 1, 2, and 4 are pivot columns [source:ma2001-lab-lab3sol-pdf#section-7].
*   **Form a Basis**: The columns in the *original* matrix $A$ corresponding to these pivot columns form a basis for $V = \text{span}(S)$. This is the largest set of linearly independent vectors from $S$ [source:ma2001-lab-lab3sol-pdf#section-7].
    *   Based on the example, $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_4\}$ is a basis for $V$ [source:ma2001-lab-lab3sol-pdf#section-7].
*   **Determine Dimension**: The dimension of $V$ is the number of vectors in this basis, which is equal to the number of pivot columns [source:ma2001-lab-lab3sol-pdf#section-7].
    *   In the example, there are 3 pivot columns, so $\text{dim}(V) = 3$ [source:ma2001-lab-lab3sol-pdf#section-7].

### Showing a Set $T$ is a Basis for $V$

To confirm that a given set $T = \{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ is a basis for a subspace $V = \text{span}(S)$, two conditions must be met [source:ma2001-lab-lab3-pdf#section-8]:
1.  $T$ must be linearly independent.
2.  $T$ must span $V$ (i.e., $\text{span}(T) = \text{span}(S)$).

#### MATLAB Steps

1.  **Check Linear Independence of $T$**:
    *   Form matrix $B = [\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{v}_3]$.
    *   Compute `rref(B)`. If all columns are pivot columns, $T$ is linearly independent [source:ma2001-lab-lab3sol-pdf#section-8].
2.  **Check if $\text{span}(T) = \text{span}(S)$**:
    *   Use the method from Section 4 by computing `rref([A, B])` and `rref([B, A])`. Both must yield consistent systems for all respective vectors [source:ma2001-lab-lab3sol-pdf#section-8].

#### Conclusion

If both conditions are satisfied, then $T$ is a basis for $V$ [source:ma2001-lab-lab3sol-pdf#section-8].

---

## 6. Expressing a Vector as a Linear Combination of a Basis (Coordinate Vector)

To express a vector $\mathbf{v}$ as a linear combination of a given basis $T = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ for a subspace $V$, you need to find the coefficients $c_1, c_2, c_3$ such that $\mathbf{v} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3$. These coefficients form the coordinate vector $[\mathbf{v}]_T$ [source:ma2001-lab-lab3-pdf#section-9].

### MATLAB Steps

1.  **Input Vectors**: Enter the basis vectors $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ and the vector $\mathbf{v}$ [source:ma2001-lab-lab3-pdf#section-9].
    ```matlab
    % Example basis T = {v1, v2, v3} and vector v from Question 8 & 9, Lab3
    v1_basis = [2; 0; 3; 4; 1]; v2_basis = [1; 0; 3; 2; -1]; v3_basis = [1; 2; 2; 0; 0];
    v_target = [-1; -3; 0; 1; -2];
    ```
2.  **Form Augmented Matrix**: Create the augmented matrix $[B \ | \ \mathbf{v}]$, where $B = [\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{v}_3]$ [source:ma2001-lab-lab3-pdf#section-9].
    ```matlab
    B_augmented_v = [v1_basis, v2_basis, v3_basis, v_target];
    ```
3.  **Compute RREF**: Apply `rref([B, v])` [source:ma2001-lab-lab3-pdf#section-9].
    ```matlab
    rref_B_v = rref(B_augmented_v);
    ```

### Interpretation of Results

*   **Identify Coefficients**: The last column of `rref([B, v])` provides the coefficients $c_1, c_2, c_3$ for the linear combination [source:ma2001-lab-lab3sol-pdf#section-9].
    ```
    rref_B_v =
        1     0     0    -1/2
        0     1     0     3/2
        0     0     1    -3/2
        0     0     0     0
        0     0     0     0
    ```
    From this, we can see that $\mathbf{v} = (-\frac{1}{2})\mathbf{v}_1 + (\frac{3}{2})\mathbf{v}_2 + (-\frac{3}{2})\mathbf{v}_3$ [source:ma2001-lab-lab3sol-pdf#section-9].
*   **Coordinate Vector**: The coordinate vector of $\mathbf{v}$ with respect to the basis $T$ is $[\mathbf{v}]_T = \begin{bmatrix} -1/2 \\ 3/2 \\ -3/2 \end{bmatrix}$ [source:ma2001-lab-lab3sol-pdf#section-9].

---

## 7. Practice Exercises

This section outlines how to approach common problems using the MATLAB techniques discussed above [source:ma2001-lab-lab3-pdf#section-10].

### Determining Relationships Between Spans ($\text{span}(S)$ and $\text{span}(T)$)

To determine if $\text{span}(S) = \text{span}(T)$, $\text{span}(S) \subseteq \text{span}(T)$, $\text{span}(T) \subseteq \text{span}(S)$, or neither:
1.  Form matrix $A$ from vectors in $S$ and matrix $B$ from vectors in $T$.
2.  Compute `rref([A, B])`. If this system is consistent (no `[0...0|1]` rows for any of $B$'s columns), then $\text{span}(T) \subseteq \text{span}(S)$.
3.  Compute `rref([B, A])`. If this system is consistent (no `[0...0|1]` rows for any of $A$'s columns), then $\text{span}(S) \subseteq \text{span}(T)$.
4.  Combine conclusions:
    *   If both are consistent, then $\text{span}(S) = \text{span}(T)$.
    *   If `rref([B, A])` is consistent but `rref([A, B])` is inconsistent for some columns, then $\text{span}(S) \subseteq \text{span}(T)$ but $\text{span}(S) \neq \text{span}(T)$.
    *   (And vice-versa for the other case) [source:ma2001-lab-lab3sol-pdf#section-10].

### Finding a Basis and Dimension of a Subspace

Given $V = \text{span}(T)$ for a set $T = \{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$:
1.  Form matrix $B = [\mathbf{v}_1 \ \ldots \ \mathbf{v}_k]$.
2.  Compute `rref(B)`.
3.  **Basis**: The columns in the original matrix $B$ that correspond to the pivot columns in `rref(B)` form a basis for $V$.
4.  **Dimension**: The number of pivot columns in `rref(B)` is the dimension of $V$.
5.  **Redundant Vectors**: The columns in the original matrix $B$ corresponding to the non-pivot columns in `rref(B)` are the redundant vectors. Use the entries of the non-pivot columns in `rref(B)` to express these redundant vectors as linear combinations of the basis vectors.
6.  **Coordinate Vectors**: Once a redundant vector is expressed as a linear combination of the basis vectors $W = \{\mathbf{w}_1, \ldots, \mathbf{w}_p\}$, the coefficients form its coordinate vector $[\mathbf{v}_j]_W$ [source:ma2001-lab-lab3sol-pdf#section-10].

### Checking if a Set is a Basis for $\mathbb{R}^n$

To check if a set $S$ is a basis for $\mathbb{R}^n$:
1.  Count the number of vectors in $S$. If it is not equal to $n$, $S$ cannot be a basis for $\mathbb{R}^n$.
2.  If the number of vectors in $S$ *is* $n$, then $S$ forms a basis for $\mathbb{R}^n$ if and only if $S$ is linearly independent (or equivalently, if it spans $\mathbb{R}^n$).
3.  Form matrix $A$ from the vectors in $S$.
4.  Compute `rref(A)`. If `rref(A)` is the identity matrix, then $A$ is invertible, the columns are linearly independent, and they span $\mathbb{R}^n$. Therefore, $S$ is a basis for $\mathbb{R}^n$ [source:ma2001-lab-lab3sol-pdf#section-10].

---
page_id: "y1s1-ma2001-gaussian-elimination-rref"
title: "Gaussian Elimination and Row Echelon Form"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Methodology for solving linear systems using elementary row operations to achieve row-echelon and reduced row-echelon forms."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter1-pdf#section-2"
  - "ma2001-hw1-ma2001-hw1-pdf#section-1"
  - "ma2001-hw1-hw1-q-pdf#section-1"
  - "ma2001-tutorial-tutorial1sol-pdf#section-1"
  - "ma2001-revision-pdf#section-1"
topics:
  - "solution"
  - "solutions"
  - "row-echelon"
  - "linear"
  - "row"
  - "form"
  - "system"
  - "systems"
  - "part"
  - "matrix"
source_count: 5
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Gaussian Elimination and Row Echelon Form

This page introduces Gaussian Elimination, a fundamental algorithm for solving systems of linear equations. It details the steps to transform an augmented matrix into a row-echelon form and a reduced row-echelon form, which simplifies finding solutions.

---

### 1. Introduction to Linear Systems and Their Solutions

A **linear equation** in `n` variables (or unknowns) $x_1, x_2, \ldots, x_n$ is an equation of the form $a_1x_1 + a_2x_2 + \cdots + a_nx_n = b$, where $a_1, a_2, \ldots, a_n$ and $b$ are real constants [source: ma2001-lecture-chapter1-pdf#section-1, ma2001-lecture-chapter1-pdf#section-2].
*   If all coefficients $a_1, \ldots, a_n$ and $b$ are zero, it is called a **zero equation**. Otherwise, it's a **non-zero equation** [source: ma2001-lecture-chapter1-pdf#section-2].

**Examples:**
*   **Linear equations**: $x + 3y = 7$, $x_1 + 2x_2 + 2x_3 + x_4 = x_5$, $y = x - \frac{1}{2}z + 4.5$ [source: ma2001-lecture-chapter1-pdf#section-3].
*   **Non-linear equations**: $xy = 2$, $\sin(\theta) + \cos(\phi) = 0.2$, $x_1^2 + x_2^2 + \cdots + x_n^2 = 1$, $x = e^y$ [source: ma2001-lecture-chapter1-pdf#section-3].

**Geometrical Interpretation:**
*   In the $xy$-plane, a linear equation $ax + by = c$ (where $a, b$ are not both zero) represents a straight line [source: ma2001-lecture-chapter1-pdf#section-1, ma2001-lecture-chapter1-pdf#section-2].
*   In 3D space, a linear equation $ax + by + cz = d$ (where $a, b, c$ are not all zero) represents a plane. For example, $z=0$ (i.e., $0x + 0y + z = 0$) represents the $xy$-plane [source: ma2001-lecture-chapter1-pdf#section-4].

#### Solutions of a Linear Equation

Given $n$ real numbers $s_1, s_2, \ldots, s_n$, we say that $(x_1, x_2, \ldots, x_n) = (s_1, s_2, \ldots, s_n)$ is a **solution** to a linear equation $a_1x_1 + a_2x_2 + \cdots + a_nx_n = b$ if the equation is satisfied when these values are substituted [source: ma2001-lecture-chapter1-pdf#section-4].
*   The set of all solutions to the equation is called the **solution set**.
*   An expression that gives all solutions is called the **general solution** [source: ma2001-lecture-chapter1-pdf#section-4]. This often involves one or more **arbitrary parameters** (e.g., $t, s, r$) [source: ma2001-lecture-chapter1-pdf#section-5].

**Examples of General Solutions:**
*   For $4x - 2y = 1$, the general solution can be $x = t, y = 2t - \frac{1}{2}$ for an arbitrary parameter $t$. This represents infinitely many solutions [source: ma2001-lecture-chapter1-pdf#section-5].
*   For $x_1 - 4x_2 + 7x_3 = 5$, the general solution is $x_1 = 5 + 4s - 7t, x_2 = s, x_3 = t$ for arbitrary parameters $s, t$ [source: ma2001-lecture-chapter1-pdf#section-5].
*   The zero linear equation $0x_1 + \cdots + 0x_n = 0$ has infinitely many solutions, where $x_i = t_i$ are arbitrary parameters [source: ma2001-lecture-chapter1-pdf#section-5].
*   A linear equation $0x_1 + \cdots + 0x_n = b$ where $b \neq 0$ has no solution [source: ma2001-lecture-chapter1-pdf#section-5].

#### Systems of Linear Equations

A **system of linear equations** (or a **linear system**) is a finite set of linear equations in the same variables $x_1, \ldots, x_n$ [source: ma2001-lecture-chapter1-pdf#section-6, ma2001-revision-pdf#section-1].
*   A solution to a linear system is a set of values $(s_1, \ldots, s_n)$ that is a solution to *every* equation in the system [source: ma2001-lecture-chapter1-pdf#section-6].
*   The **solution set** and **general solution** for a system are defined similarly to single equations [source: ma2001-lecture-chapter1-pdf#section-6].

**Consistency of Linear Systems:**
Every system of linear equations can have one of three possibilities [source: ma2001-lecture-chapter1-pdf#section-7]:
1.  **No solution**: The system is **inconsistent** [source: ma2001-lecture-chapter1-pdf#section-7].
2.  **Exactly one solution**: The system is **consistent** [source: ma2001-lecture-chapter1-pdf#section-7].
3.  **Infinitely many solutions**: The system is **consistent** [source: ma2001-lecture-chapter1-pdf#section-7].

**Geometrical Interpretation of Systems:**
*   **In 2D ($xy$-plane)**: A system of two linear equations represents two lines ($L_1, L_2$).
    *   **No solution**: $L_1$ and $L_2$ are different but parallel lines (they do not intersect) [source: ma2001-lecture-chapter1-pdf#section-8].
    *   **Only one solution**: $L_1$ and $L_2$ are not parallel (they intersect at a single point) [source: ma2001-lecture-chapter1-pdf#section-8].
    *   **Infinitely many solutions**: $L_1$ and $L_2$ are the same line [source: ma2001-lecture-chapter1-pdf#section-8].
*   **In 3D ($xyz$-space)**: A system of two linear equations represents two planes ($P_1, P_2$).
    *   **No solution**: $P_1$ and $P_2$ are different but parallel planes [source: ma2001-lecture-chapter1-pdf#section-8].
    *   **Cannot have only one solution**: Two planes can't intersect at a single point; they either intersect at a line or are parallel [source: ma2001-lecture-chapter1-pdf#section-8].
    *   **Infinitely many solutions**: $P_1$ and $P_2$ intersect at a line, or they are the same plane [source: ma2001-lecture-chapter1-pdf#section-8].
    *   For three equations in 3D, the solutions correspond to the relative positions of three planes (e.g., intersecting at a single point, a line, or no common intersection) [source: ma2001-lecture-chapter1-pdf#section-8].

### 2. Elementary Row Operations

A system of linear equations can be represented by a rectangular array of numbers called an **augmented matrix** [source: ma2001-lecture-chapter1-pdf#section-8, ma2001-revision-pdf#section-1].
*   For a system:
    $a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1$
    $a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2$
    $\vdots$
    $a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m$
    The augmented matrix is:
    $\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-8, ma2001-revision-pdf#section-3].

**Elementary Row Operations (EROs):**
These are the basic techniques used to solve linear systems and transform augmented matrices [source: ma2001-lecture-chapter1-pdf#section-8, ma2001-revision-pdf#section-1].
1.  **Multiply a row by a non-zero constant** ($cR_i$): This corresponds to multiplying an equation by a non-zero constant [source: ma2001-lecture-chapter1-pdf#section-8, ma2001-revision-pdf#section-1].
2.  **Interchange two rows** ($R_i \leftrightarrow R_j$): This corresponds to interchanging two equations [source: ma2001-lecture-chapter1-pdf#section-8, ma2001-revision-pdf#section-1].
3.  **Add a multiple of one row to another row** ($R_i + cR_j$): This corresponds to adding a multiple of one equation to another equation [source: ma2001-lecture-chapter1-pdf#section-8, ma2001-revision-pdf#section-1].

**Row Equivalent Matrices:**
Two augmented matrices are **row equivalent** if one can be obtained from the other by a series of elementary row operations [source: ma2001-lecture-chapter1-pdf#section-9]. If two augmented matrices are row equivalent, their corresponding linear systems have the **same set of solutions** [source: ma2001-lecture-chapter1-pdf#section-9].

### 3. Row-Echelon Forms

An augmented matrix is in **row-echelon form (REF)** if it satisfies the following properties [source: ma2001-lecture-chapter1-pdf#section-9]:
1.  Any rows that consist entirely of zeros are grouped together at the bottom of the matrix [source: ma2001-lecture-chapter1-pdf#section-9].
2.  In any two successive non-zero rows, the first non-zero number in the lower row (called the **leading entry**) occurs farther to the right than the leading entry of the higher row [source: ma2001-lecture-chapter1-pdf#section-9].

**Key Terminology:**
*   **Leading Entry**: The first non-zero number in a row [source: ma2001-lecture-chapter1-pdf#section-9].
*   **Pivot Point**: The leading entries of non-zero rows are called pivot points [source: ma2001-lecture-chapter1-pdf#section-9].
*   **Pivot Column**: A column that contains a pivot point [source: ma2001-lecture-chapter1-pdf#section-9].
*   **Non-Pivot Column**: A column that does not contain a pivot point [source: ma2001-lecture-chapter1-pdf#section-9].

**Reduced Row-Echelon Form (RREF):**
An augmented matrix is in **reduced row-echelon form (RREF)** if it is already in row-echelon form and satisfies two additional properties [source: ma2001-lecture-chapter1-pdf#section-9]:
3.  The leading entry of every non-zero row is 1 [source: ma2001-lecture-chapter1-pdf#section-9].
4.  In each pivot column, all other entries (except the pivot point itself) are zero [source: ma2001-lecture-chapter1-pdf#section-9].

**Examples:**
*   **Matrices in RREF**:
    $\begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$, $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 3 \end{pmatrix}$, $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 0 & 1 & 2 & 0 & 1 \\ 0 & 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-9].
*   **Matrices in REF but not RREF**:
    $\begin{pmatrix} 3 & 2 & 1 \end{pmatrix}$, $\begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 2 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, $\begin{pmatrix} -1 & 2 & 3 & 4 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & 2 & 3 \end{pmatrix}$, $\begin{pmatrix} 0 & 1 & 2 & 8 & 1 \\ 0 & 0 & 0 & 4 & 3 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-9].

#### Solving Systems from Row-Echelon Forms

If the augmented matrix of a linear system is in REF or RREF, the solutions can be easily obtained [source: ma2001-lecture-chapter1-pdf#section-9].

*   **From RREF**: The solutions can often be read directly. For example, $\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 3 \end{pmatrix}$ implies $x_1=1, x_2=2, x_3=3$, a unique solution [source: ma2001-lecture-chapter1-pdf#section-9].
*   **From REF (using Back Substitution)**: For a matrix in REF, variables corresponding to non-pivot columns are set as arbitrary parameters. Then, starting from the last non-zero equation, solve for variables and substitute them into the equations above. This is called **back substitution** [source: ma2001-lecture-chapter1-pdf#section-9].

    *   **Example (infinitely many solutions via back substitution)**:
        Consider $\begin{pmatrix} 0 & 2 & 2 & 1 & -2 & 2 \\ 0 & 0 & 1 & 1 & 1 & 3 \\ 0 & 0 & 0 & 0 & 2 & 4 \end{pmatrix}$.
        This corresponds to the system:
        $2x_2 + 2x_3 + x_4 - 2x_5 = 2$
        $x_3 + x_4 + x_5 = 3$
        $2x_5 = 4$
        From $2x_5=4$, $x_5=2$.
        $x_1$ is arbitrary (as its coefficient is zero in all equations). Let $x_1 = s$.
        $x_4$ is a non-pivot column variable. Let $x_4 = t$.
        Substitute $x_5=2$ into the second equation: $x_3 + t + 2 = 3 \Rightarrow x_3 = 1-t$.
        Substitute $x_3=1-t, x_4=t, x_5=2$ into the first equation: $2x_2 + 2(1-t) + t - 2(2) = 2 \Rightarrow 2x_2 + 2 - 2t + t - 4 = 2 \Rightarrow 2x_2 - t - 2 = 2 \Rightarrow 2x_2 = 4 + t \Rightarrow x_2 = 2 + \frac{1}{2}t$.
        The general solution is $x_1=s, x_2=2+\frac{1}{2}t, x_3=1-t, x_4=t, x_5=2$ (infinitely many solutions) [source: ma2001-lecture-chapter1-pdf#section-9].

    *   **Example (no solution)**:
        Consider $\begin{pmatrix} 3 & 1 & 4 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{pmatrix}$.
        The third row corresponds to $0x_1 + 0x_2 = 1$, which is $0=1$. This is a contradiction, so the system has no solution [source: ma2001-lecture-chapter1-pdf#section-9].

### 4. Gaussian Elimination

**Gaussian Elimination** is an algorithm that uses elementary row operations to reduce an augmented matrix to a row-echelon form [source: ma2001-lecture-chapter1-pdf#section-10, ma2001-revision-pdf#section-8].

**Algorithm Steps (to achieve REF) [source: ma2001-lecture-chapter1-pdf#section-10]:**
1.  Locate the leftmost column that does not consist entirely of zeros.
2.  Interchange the top row with another row, if necessary, to bring a non-zero entry to the top of the column found in Step 1.
3.  For each row below the top row, add a suitable multiple of the top row to it so that the entry below the leading entry of the top row becomes zero.
4.  Now cover the top row and begin again with Step 1 applied to the submatrix that remains. Continue until the entire matrix is in row-echelon form.

**Gauss-Jordan Elimination:**
**Gauss-Jordan Elimination** is an algorithm that uses elementary row operations to reduce an augmented matrix to its **reduced row-echelon form** [source: ma2001-lecture-chapter1-pdf#section-10, ma2001-revision-pdf#section-9]. It builds upon Gaussian Elimination.

**Algorithm Steps (to achieve RREF, following REF completion) [source: ma2001-lecture-chapter1-pdf#section-10]:**
5.  Multiply each row by a suitable constant so that all leading entries become 1.
6.  Beginning with the last pivot column and working backward, add suitable multiples of each row to the rows above to introduce zeros above each pivot point. (This eliminates non-zero entries above the pivots).

**Remarks on Gaussian and Gauss-Jordan Elimination:**
*   Every matrix has a **unique RREF**, but can have many different REFs [source: ma2001-lecture-chapter1-pdf#section-10].
*   In practice, implementations of these algorithms may be modified to avoid round-off errors [source: ma2001-lecture-chapter1-pdf#section-10].

#### Solving Linear Systems using Elimination

The process of solving a linear system typically involves these steps [source: ma2001-lecture-chapter1-pdf#section-10]:
1.  Represent the given linear system as an augmented matrix.
2.  Use Gaussian Elimination to reduce the augmented matrix to a row-echelon form, or Gauss-Jordan Elimination to reduce it to a reduced row-echelon form.
3.  Solve the system corresponding to the row-echelon form (using back substitution) or read solutions directly from the reduced row-echelon form.

**General Solution from REF vs. RREF:**
*   **From REF**: Set variables corresponding to non-pivot columns to arbitrary parameters. Use back substitution for the other variables [source: ma2001-lecture-chapter1-pdf#section-10].
*   **From RREF**: Set variables corresponding to non-pivot columns to arbitrary parameters. The other variables can be directly equated to an expression involving these parameters [source: ma2001-lecture-chapter1-pdf#section-10].

#### Determining Solution Types from REF

Once a matrix is in row-echelon form, the type of solution can be determined by examining the pivot columns and the last column [source: ma2001-lecture-chapter1-pdf#section-10, ma2001-revision-pdf#section-11, ma2001-revision-pdf#section-12, ma2001-revision-pdf#section-13].

1.  **No Solution (Inconsistent System)**:
    *   Occurs if the last column of the row-echelon form of the augmented matrix is a pivot column. This implies a row of the form $\begin{pmatrix} 0 & 0 & \cdots & 0 & | & b \end{pmatrix}$ where $b \neq 0$ [source: ma2001-lecture-chapter1-pdf#section-10, ma2001-revision-pdf#section-11].
    *   *Example*: $\begin{pmatrix} 3 & 2 & 3 & 4 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 2 \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-10].

2.  **Unique Solution (Consistent System)**:
    *   Occurs if the last column is NOT a pivot column, and every other column (excluding the last) of the row-echelon form of the augmented matrix IS a pivot column [source: ma2001-lecture-chapter1-pdf#section-10, ma2001-revision-pdf#section-12].
    *   This means there are no free variables.
    *   *Example*: $\begin{pmatrix} 1 & 2 & 3 & 4 \\ 0 & 2 & 0 & 1 \\ 0 & 0 & -1 & 2 \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-10].

3.  **Infinitely Many Solutions (Consistent System)**:
    *   Occurs if the last column is NOT a pivot column, and there is at least one other non-pivot column in the row-echelon form of the augmented matrix [source: ma2001-lecture-chapter1-pdf#section-10, ma2001-revision-pdf#section-13].
    *   These non-pivot columns correspond to arbitrary parameters in the general solution.
    *   *Example*: $\begin{pmatrix} 5 & 1 & 2 & 3 & 4 \\ 0 & 0 & -1 & 0 & 1 \\ 0 & 0 & 0 & 1 & 2 \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-10].

#### Notation for Elementary Row Operations

When performing elementary row operations, the following notation is used [source: ma2001-lecture-chapter1-pdf#section-10]:
1.  $cR_i$: Multiply the $i^{th}$ row by the constant $c$.
2.  $R_i \leftrightarrow R_j$: Interchange the $i^{th}$ and $j^{th}$ rows.
3.  $R_i + cR_j$: Add $c$ times the $j^{th}$ row to the $i^{th}$ row.

#### Example: Conditions for Solutions Based on Parameters

Consider a system:
$x + 2y + z = 1$
$2x + by + 2z = 2$
$4x + 8y + b^2z = 2b$

Its augmented matrix is $\begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & b & 2 & 2 \\ 4 & 8 & b^2 & 2b \end{pmatrix}$.
Applying row operations $R_2 - 2R_1$ and $R_3 - 4R_1$ leads to:
$\begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & b-4 & 0 & 0 \\ 0 & 0 & b^2-4 & 2b-4 \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-10].

Now we analyze cases based on the values of $b$:
1.  **No Solution**: This occurs if there is a row $\begin{pmatrix} 0 & 0 & \cdots & 0 & | & k \end{pmatrix}$ where $k \neq 0$.
    *   From the second row, $0 = 0$ if $b-4=0 \Rightarrow b=4$.
    *   If $b \neq 4$, the leading entry of the second row is $b-4$.
    *   From the third row, we need $b^2-4=0$ AND $2b-4 \neq 0$.
        *   $b^2-4=0 \Rightarrow (b-2)(b+2)=0 \Rightarrow b=2$ or $b=-2$.
        *   If $b=2$, then $2b-4 = 2(2)-4 = 0$.
        *   If $b=-2$, then $2b-4 = 2(-2)-4 = -8 \neq 0$.
    *   So, the system has **no solution** if $b=-2$ [source: ma2001-lecture-chapter1-pdf#section-10].

2.  **Unique Solution**: This occurs if there are no zero rows on the left side, and the number of pivot columns equals the number of variables, and the last column is not a pivot column.
    *   This requires $b-4 \neq 0$ and $b^2-4 \neq 0$.
    *   So, $b \neq 4$ AND $b \neq \pm 2$.
    *   The system has a **unique solution** if $b \neq 4$ and $b \neq \pm 2$ [source: ma2001-lecture-chapter1-pdf#section-10].

3.  **Infinitely Many Solutions**: This occurs if there are no rows like $\begin{pmatrix} 0 & 0 & \cdots & 0 & | & k \end{pmatrix}$ with $k \neq 0$, and there are non-pivot columns (free variables).
    *   We need $b-4=0$ (so $b=4$) AND $b^2-4=0$ (so $b=\pm 2$) AND $2b-4=0$ (so $b=2$). These conditions are contradictory ($b$ cannot be 4 and $\pm 2$ simultaneously).
    *   Let's check when $b^2-4=0$ and $2b-4=0$. This holds for $b=2$. In this case, the matrix becomes $\begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & -2 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$. This system has free variables ($z$ corresponding to a non-pivot column), leading to **infinitely many solutions** [source: ma2001-lecture-chapter1-pdf#section-10].

### 5. Homogeneous Linear Systems

A system of linear equations is **homogeneous** if all the constant terms $b_i$ are zero [source: ma2001-lecture-chapter1-pdf#section-11, ma2001-revision-pdf#section-14].
*   Form:
    $a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = 0$
    $a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = 0$
    $\vdots$
    $a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = 0$

*   The solution $x_1=0, x_2=0, \ldots, x_n=0$ is always a solution to a homogeneous system and is called the **trivial solution** [source: ma2001-lecture-chapter1-pdf#section-11, ma2001-revision-pdf#section-14].
*   Any other solution is called a **non-trivial solution** [source: ma2001-lecture-chapter1-pdf#section-11].

**Geometrical Interpretation of Homogeneous Systems:**
*   In the $xy$-plane, homogeneous equations $a_1x + b_1y = 0$ represent lines passing through the origin $(0,0)$ [source: ma2001-lecture-chapter1-pdf#section-11].
    *   If lines are not parallel, there's only one solution (the trivial solution $(0,0)$).
    *   If lines are the same, there are infinitely many solutions.
*   In $xyz$-space, homogeneous equations $a_1x + b_1y + c_1z = 0$ represent planes containing the origin $(0,0,0)$ [source: ma2001-lecture-chapter1-pdf#section-11].
    *   Such a system always has the trivial solution.
    *   It cannot have a unique non-trivial solution; it either has only the trivial solution or infinitely many solutions.
    *   Two planes through the origin will always intersect in a line through the origin (infinitely many solutions).

**Solutions of Homogeneous Systems:**
A homogeneous system of linear equations has either [source: ma2001-lecture-chapter1-pdf#section-11, ma2001-revision-pdf#section-14]:
1.  Only the trivial solution.
2.  Infinitely many solutions (including the trivial solution).

**Theorem:** A homogeneous system of linear equations with **more unknowns than equations** always has **infinitely many solutions** [source: ma2001-lecture-chapter1-pdf#section-11].

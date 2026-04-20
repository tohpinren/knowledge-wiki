---
page_id: "y1s1-ma2001-linear-systems-solution-types"
title: "Types of Solutions for Linear Systems"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Exploring unique, infinite, and no-solution scenarios for linear systems, including homogeneous systems."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lecture-chapter1-pdf#section-3"
  - "ma2001-tutorial-tutorial1-pdf#section-2"
  - "ma2001-ma2001-pdf#section-1"
topics:
  - "solution"
  - "solutions"
  - "row-echelon"
  - "linear"
  - "row"
  - "form"
  - "system"
  - "systems"
  - "equations"
  - "question"
source_count: 3
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# Types of Solutions for Linear Systems

Linear systems can have a single solution, an infinite number of solutions, or no solutions at all. Understanding these possibilities is fundamental to linear algebra, with distinct implications for systems and their geometric interpretations [source: ma2001-lecture-chapter1-pdf#section-5, ma2001-ma2001-pdf#section-1].

---

### Solutions of a Single Linear Equation

A **linear equation** in $n$ variables $x_1, \dots, x_n$ is an equation of the form $a_1x_1 + a_2x_2 + \dots + a_nx_n = b$, where $a_1, \dots, a_n$ and $b$ are real constants. The variables $x_1, \dots, x_n$ are also called **unknowns** [source: ma2001-lecture-chapter1-pdf#section-1].
If all coefficients $a_i$ and the constant $b$ are zero, it is a **zero equation**; otherwise, it is a **non-zero equation** [source: ma2001-lecture-chapter1-pdf#section-1].

A set of $n$ real numbers $(s_1, s_2, \dots, s_n)$ is a **solution** to a linear equation if substituting $x_i = s_i$ into the equation satisfies it ($a_1s_1 + a_2s_2 + \dots + a_ns_n = b$). The collection of all such solutions is called the **solution set**, and an expression that describes all solutions is known as the **general solution** [source: ma2001-lecture-chapter1-pdf#section-2].

For example:
*   For the equation $4x - 2y = 1$, a general solution can be written as $x = t$, $y = 2t - \frac{1}{2}$ for any arbitrary parameter $t \in \mathbb{R}$ [source: ma2001-lecture-chapter1-pdf#section-3]. This equation has infinitely many solutions.
*   The equation $0x_1 + 0x_2 + \dots + 0x_n = 0$ has infinitely many solutions, as any values for $x_1, \dots, x_n$ will satisfy it. The general solution is $x_i = t_i$ for arbitrary parameters $t_i \in \mathbb{R}$ [source: ma2001-lecture-chapter1-pdf#section-5].
*   The equation $0x_1 + 0x_2 + \dots + 0x_n = b$ where $b$ is non-zero has no solution, as no values for $x_i$ can satisfy it [source: ma2001-lecture-chapter1-pdf#section-5].

### Systems of Linear Equations and Their Solutions

A **system of linear equations** (or **linear system**) is a finite set of linear equations involving the same variables [source: ma2001-lecture-chapter1-pdf#section-5]. A solution to a linear system is a set of values for the variables that satisfies *every* equation in the system simultaneously [source: ma2001-lecture-chapter1-pdf#section-5]. Like single equations, a system has a **solution set** (all solutions) and a **general solution** (an expression describing all solutions) [source: ma2001-lecture-chapter1-pdf#section-5].

#### Types of Solutions for Linear Systems

Every system of linear equations must fall into one of three categories:
1.  **No solution:** The system is **inconsistent** [source: ma2001-lecture-chapter1-pdf#section-5, ma2001-ma2001-pdf#section-1].
2.  **Exactly one solution:** The system is **consistent** [source: ma2001-lecture-chapter1-pdf#section-5, ma2001-ma2001-pdf#section-1].
3.  **Infinitely many solutions:** The system is **consistent** [source: ma2001-lecture-chapter1-pdf#section-5, ma2001-ma2001-pdf#section-1].

An example of a system with no solution is $\begin{cases} x + y = 4 \\ 2x + 2y = 6 \end{cases}$, because the first equation implies $2x + 2y = 8$, which contradicts the second equation [source: ma2001-lecture-chapter1-pdf#section-5].

#### Geometrical Interpretation

The types of solutions have clear geometric interpretations in 2D and 3D spaces.

**In the $xy$-plane (2D):**
A linear equation $ax + by = c$ represents a straight line. For a system of two linear equations:
*   **No solution:** The lines are different but parallel. They never intersect [source: ma2001-lecture-chapter1-pdf#section-5].
*   **Exactly one solution:** The lines intersect at a single point, and they are not parallel [source: ma2001-lecture-chapter1-pdf#section-5].
*   **Infinitely many solutions:** The lines are the same (coincident). Every point on the line is a solution [source: ma2001-lecture-chapter1-pdf#section-5].

**In $xyz$-space (3D):**
A linear equation $ax + by + cz = d$ represents a plane. For a system of two linear equations:
*   **No solution:** The planes are different but parallel [source: ma2001-lecture-chapter1-pdf#section-5].
*   **Infinitely many solutions:** The planes either intersect at a line, or they are the same plane [source: ma2001-lecture-chapter1-pdf#section-5].
    *   It is crucial to note that a system of only two linear equations representing planes in 3D space *cannot* have exactly one solution. They will always have either no solution or infinitely many solutions [source: ma2001-lecture-chapter1-pdf#section-5].
For a system of three linear equations, representing three planes:
*   **No solution:** The three planes might be parallel, two parallel planes intersected by a third, or they intersect pairwise but with no common intersection point (forming a triangular prism).
*   **Exactly one solution:** The three planes intersect at a single point.
*   **Infinitely many solutions:** The three planes intersect along a common line, or all three planes are the same.

### Determining Solution Types from Row-Echelon Form

The type of solution for a linear system can be easily determined by converting its augmented matrix into a [**row-echelon form**](ma2001-gaussian-elimination-rref) (REF) or [**reduced row-echelon form**](ma2001-gaussian-elimination-rref) (RREF) using [**elementary row operations**](ma2001-gaussian-elimination-rref) [source: ma2001-lecture-chapter1-pdf#section-4, ma2001-lecture-chapter1-pdf#section-8]. A **pivot column** is a column containing a leading entry (also called a pivot point) in an REF/RREF matrix [source: ma2001-lecture-chapter1-pdf#section-3].

Let $m$ be the number of non-zero rows (or pivot points) in the row-echelon form, and $n$ be the number of variables in the system.

1.  **No Solution (Inconsistent System):**
    *   This occurs if, after reduction to row-echelon form, there is a row that looks like `[0 0 ... 0 | b]` where `b` is a non-zero constant (e.g., `0 = 1`).
    *   In terms of pivot columns, the last column of the augmented matrix (the constant column) is a pivot column [source: ma2001-lecture-chapter1-pdf#section-8, ma2001-ma2001-pdf#section-1].
    *   Example: An augmented matrix in REF such as $\begin{pmatrix} 3 & 2 & 3 & 4 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 2 \end{pmatrix}$ represents an inconsistent system because the last row corresponds to $0x_1 + 0x_2 + 0x_3 = 2$, which is impossible [source: ma2001-lecture-chapter1-pdf#section-8].

2.  **Exactly One Solution (Consistent System):**
    *   This occurs if the system is consistent (no `0 = b` row with `b != 0`) and the number of non-zero rows equals the number of variables ($m = n$) [source: ma2001-ma2001-pdf#section-1].
    *   In terms of pivot columns, every column of the coefficient matrix (i.e., every column *except* the last column of the augmented matrix) is a pivot column [source: ma2001-lecture-chapter1-pdf#section-8]. This means there are no "free variables."
    *   Example: An augmented matrix in RREF like $\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 3 \end{pmatrix}$ has a unique solution $x_1=1, x_2=2, x_3=3$ [source: ma2001-lecture-chapter1-pdf#section-4]. For three variables, there are three pivot columns in the coefficient part.

3.  **Infinitely Many Solutions (Consistent System):**
    *   This occurs if the system is consistent and the number of non-zero rows is less than the number of variables ($m < n$) [source: ma2001-ma2001-pdf#section-1].
    *   In terms of pivot columns, apart from the last column, there is at least one non-pivot column in the coefficient matrix. Each non-pivot column corresponds to a "free variable" that can be assigned an arbitrary parameter [source: ma2001-lecture-chapter1-pdf#section-8, ma2001-ma2001-pdf#section-1].
    *   The number of arbitrary parameters is equal to $n - m$ (number of variables - number of non-zero rows) [source: ma2001-ma2001-pdf#section-1].
    *   Example: An augmented matrix in REF like $\begin{pmatrix} 0 & 2 & 2 & 1 & -2 & 2 \\ 0 & 0 & 1 & 1 & 1 & 3 \\ 0 & 0 & 0 & 0 & 2 & 4 \end{pmatrix}$ has 5 variables ($x_1, \dots, x_5$) but only 3 non-zero rows. $x_1$ and $x_4$ are arbitrary parameters, leading to infinitely many solutions [source: ma2001-lecture-chapter1-pdf#section-4].

### Homogeneous Linear Systems

A system of linear equations is **homogeneous** if all the constant terms ($b_i$) are zero. That is, $a_{11}x_1 + \dots + a_{1n}x_n = 0$, $a_{21}x_1 + \dots + a_{2n}x_n = 0$, etc. [source: ma2001-lecture-chapter1-pdf#section-5].

Homogeneous systems have special properties:
*   **Always Consistent:** A homogeneous system always has at least one solution: the **trivial solution**, where all variables are zero ($x_1 = 0, x_2 = 0, \dots, x_n = 0$) [source: ma2001-lecture-chapter1-pdf#section-5, ma2001-ma2001-pdf#section-1].
*   **Two possibilities for solutions:** A homogeneous system either has:
    1.  **Only the trivial solution.**
    2.  **Infinitely many solutions**, which include the trivial solution and other **non-trivial solutions** [source: ma2001-lecture-chapter1-pdf#section-5, ma2001-ma2001-pdf#section-1].
*   **More unknowns than equations:** If a homogeneous linear system has more unknowns than equations ($n > m$), it is guaranteed to have infinitely many solutions (i.e., non-trivial solutions) [source: ma2001-lecture-chapter1-pdf#section-5, ma2001-ma2001-pdf#section-1].

Geometrically, for homogeneous systems, the lines or planes always pass through the origin $(0,0)$ or $(0,0,0)$ respectively.
*   In 2D, two homogeneous linear equations represent lines through the origin. They either intersect only at the origin (unique trivial solution) or are the same line (infinitely many solutions) [source: ma2001-lecture-chapter1-pdf#section-5].
*   In 3D, two homogeneous linear equations represent planes containing the origin. They either intersect along a line through the origin (infinitely many solutions) or are the same plane (infinitely many solutions) [source: ma2001-lecture-chapter1-pdf#section-5].

### Examples

Consider the following examples to determine conditions for different solution types for a linear system based on parameters $a, b, c$ [source: ma2001-lecture-chapter1-pdf#section-4]:

**Example 1:** Determine conditions on $a, b, c$ for the system to have at least one solution:
$\begin{cases} x + 2y - 3z = a \\ 2x + 6y - 11z = b \\ x - 2y + 7z = c \end{cases}$

After Gaussian Elimination, the augmented matrix becomes:
$\begin{pmatrix} 1 & 2 & -3 & a \\ 0 & 2 & -5 & b - 2a \\ 0 & 0 & 0 & 2b + c - 5a \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-4]

For the system to have a solution (either unique or infinitely many), the last row cannot be of the form `[0 0 0 | non-zero]`. Therefore, $2b + c - 5a$ must be zero. If $2b + c - 5a = 0$, the system will have infinitely many solutions since there are 3 variables but only 2 effective non-zero rows (the last row becomes all zeros) [source: ma2001-lecture-chapter1-pdf#section-4].

**Example 2:** Determine values of $b$ for the system to have (a) no solution, (b) a unique solution, and (c) infinitely many solutions:
$\begin{cases} x + 2y + z = 1 \\ 2x + by + 2z = 2 \\ 4x + 8y + b^2z = 2b \end{cases}$

After Gaussian Elimination, the augmented matrix is reduced to:
$\begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & b - 4 & 0 & 0 \\ 0 & 0 & b^2 - 4 & 2b - 4 \end{pmatrix}$ [source: ma2001-lecture-chapter1-pdf#section-4]

We analyze the last two rows:
*   $(b-4)y = 0$
*   $(b^2-4)z = 2b-4$

(a) **No Solution:**
    This occurs if a row of the form `[0 0 ... 0 | non-zero]` exists.
    From the last row, if $b^2 - 4 = 0$ AND $2b - 4 \ne 0$.
    $b^2 - 4 = (b-2)(b+2) = 0 \Rightarrow b = 2$ or $b = -2$.
    If $b = 2$, then $2b - 4 = 2(2) - 4 = 0$. This gives `0z = 0`, so it doesn't lead to no solution.
    If $b = -2$, then $2b - 4 = 2(-2) - 4 = -8 \ne 0$. This gives `0z = -8`, which implies no solution.
    Also, if $b-4=0 \Rightarrow b=4$, and $(b^2-4)=12 \ne 0$ and $2b-4 = 4 \ne 0$, this is a unique solution (see (b)).
    Therefore, the system has no solution if $b = -2$ [source: ma2001-lecture-chapter1-pdf#section-4].

(b) **Unique Solution:**
    This occurs if all coefficient columns (excluding the augmented column) are pivot columns. This requires $b-4 \ne 0$ and $b^2 - 4 \ne 0$.
    So, $b \ne 4$ and $b \ne \pm 2$.
    Thus, the system has a unique solution if $b \ne 4$ and $b \ne \pm 2$ [source: ma2001-lecture-chapter1-pdf#section-4].

(c) **Infinitely Many Solutions:**
    This occurs if the system is consistent and has free variables.
    Case 1: $b-4=0 \Rightarrow b=4$. The matrix becomes $\begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 12 & 4 \end{pmatrix}$. This system has 3 variables and effectively 2 non-zero rows ($x+2y+z=1$, $12z=4$). This implies $z = 1/3$, and $x+2y = 1-1/3 = 2/3$. $y$ can be a free variable, so infinitely many solutions.
    Case 2: $b^2-4=0$ and $2b-4=0$. This means $b=2$. The matrix becomes $\begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & -2 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$. This system has 3 variables and 2 non-zero rows ($x+2y+z=1$, $-2y=0 \Rightarrow y=0$). $x+z=1$. Here, $z$ can be a free variable, so infinitely many solutions.
    Combining these, the system has infinitely many solutions if $b=4$ or $b=2$ [source: ma2001-lecture-chapter1-pdf#section-4].

Summary for Example 2:
*   **No solution:** $b = -2$
*   **Unique solution:** $b \ne 4$ and $b \ne \pm 2$
*   **Infinitely many solutions:** $b = 2$ or $b = 4$

This comprehensive analysis based on row-echelon forms allows for a systematic determination of solution types for linear systems, including those with parameters.

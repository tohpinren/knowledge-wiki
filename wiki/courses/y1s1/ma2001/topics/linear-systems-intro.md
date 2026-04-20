---
page_id: "y1s1-ma2001-linear-systems-intro"
title: "Introduction to Linear Systems"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Definitions of linear equations and systems, their representation, and basic geometric interpretations in 2D/3D."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
  - "y1s1-cs1231s-lecture-01-mathematical-language"
source_refs:
  - "ma2001-lecture-chapter1-pdf#section-1"
  - "ma2001-tutorial-tutorial1-pdf#section-1"
  - "ma2001-linear-algebra-pdf-pdf#section-1"
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
# Introduction to Linear Systems

This page introduces the fundamental concepts of linear equations and systems, their various representations, and their basic geometric interpretations in two and three dimensions. These foundational ideas are crucial for understanding more advanced topics in linear algebra, including solution methods like Gaussian elimination and the classification of solution types.

---

## Linear Equations

A **linear equation** is an algebraic equation where each term is either a constant or the product of a constant and a single variable (to the first power). The variables in a linear equation are often referred to as **unknowns** [source: ma2001-lecture-chapter1-pdf#section-4].

### In Two Variables

In the $xy$-plane, a line can be algebraically represented by an equation of the form:
$ax + by = c$
where $a$ and $b$ are not both zero. An equation of this kind is known as a linear equation in the variables $x$ and $y$ [source: ma2001-lecture-chapter1-pdf#section-3].

### In $n$ Variables

More generally, a linear equation in $n$ variables $x_1, x_2, \dots, x_n$ has the form:
$a_1x_1 + a_2x_2 + \dots + a_nx_n = b$
where $a_1, a_2, \dots, a_n$ and $b$ are real constants [source: ma2001-lecture-chapter1-pdf#section-4].

*   If all coefficients $a_1, a_2, \dots, a_n$ and the constant $b$ are zero, the equation is called a **zero equation** [source: ma2001-lecture-chapter1-pdf#section-4].
*   Otherwise, it is a **non-zero equation** [source: ma2001-lecture-chapter1-pdf#section-4].

### Examples of Linear and Non-Linear Equations

**Linear Equations:**
*   $x + 3y = 7$ [source: ma2001-lecture-chapter1-pdf#section-5]
*   $x_1 + 2x_2 + 2x_3 + x_4 = x_5$ [source: ma2001-lecture-chapter1-pdf#section-5]
*   $y = x - \frac{1}{2}z + 4.5$ [source: ma2001-lecture-chapter1-pdf#section-5]
*   $x_1 + x_2 + \dots + x_n = 1$ [source: ma2001-lecture-chapter1-pdf#section-5]

**Non-Linear Equations:**
*   $xy = 2$ (product of variables) [source: ma2001-lecture-chapter1-pdf#section-5]
*   $\sin(\theta) + \cos(\phi) = 0.2$ (trigonometric functions of variables) [source: ma2001-lecture-chapter1-pdf#section-5]
*   $x_1^2 + x_2^2 + \dots + x_n^2 = 1$ (variables raised to power other than 1) [source: ma2001-lecture-chapter1-pdf#section-5]
*   $x = e^y$ (exponential function of a variable) [source: ma2001-lecture-chapter1-pdf#section-5]

### Geometric Interpretation of Single Linear Equations

*   **In 2D ($xy$-plane):** A linear equation $ax + by = c$ represents a **line** [source: ma2001-lecture-chapter1-pdf#section-3].
*   **In 3D ($xyz$-space):** A linear equation $ax + by + cz = d$, where $a, b, c, d$ are constants and not all $a, b, c$ are zero, represents a **plane**. For example, the equation $z=0$ (or $0x + 0y + z = 0$) represents the $xy$-plane within the three-dimensional space [source: ma2001-lecture-chapter1-pdf#section-6].

## Solutions of a Linear Equation

Given $n$ real numbers $s_1, s_2, \dots, s_n$, we say that $(x_1, x_2, \dots, x_n) = (s_1, s_2, \dots, s_n)$ is a **solution** to a linear equation $a_1x_1 + a_2x_2 + \dots + a_nx_n = b$ if the equation is satisfied when these values are substituted, i.e., $a_1s_1 + a_2s_2 + \dots + a_ns_n = b$ [source: ma2001-lecture-chapter1-pdf#section-7].

*   The set of all solutions to the equation is called the **solution set** [source: ma2001-lecture-chapter1-pdf#section-7].
*   An expression that describes all solutions to the equation is called the **general solution** [source: ma2001-lecture-chapter1-pdf#section-7].

### Examples of General Solutions

1.  **Equation: $4x - 2y = 1$ (2 variables)**
    One way to express the general solution is to set $x = t$ (an arbitrary parameter). Substituting this into the equation:
    $4t - 2y = 1 \Rightarrow -2y = 1 - 4t \Rightarrow y = 2t - \frac{1}{2}$
    So, the general solution is $x=t$, $y = 2t - \frac{1}{2}$ [source: ma2001-lecture-chapter1-pdf#section-8].
    Alternatively, setting $y = s$ (an arbitrary parameter):
    $4x - 2s = 1 \Rightarrow 4x = 1 + 2s \Rightarrow x = \frac{1}{4} + \frac{1}{2}s$
    So, the general solution can also be written as $x = \frac{1}{4} + \frac{1}{2}s$, $y=s$ [source: ma2001-lecture-chapter1-pdf#section-8].
    These expressions represent the same set of solutions, for example:
    *   If $t=1$, then $(x, y) = (1, 1.5)$
    *   If $s=1.5$, then $(x, y) = (1, 1.5)$
    This equation has **infinitely many solutions** [source: ma2001-lecture-chapter1-pdf#section-8].

2.  **Equation: $x_1 - 4x_2 + 7x_3 = 5$ (3 variables)**
    We can choose $x_2 = s$ and $x_3 = t$ as arbitrary parameters. Substituting these into the equation:
    $x_1 - 4s + 7t = 5 \Rightarrow x_1 = 5 + 4s - 7t$
    The general solution is $x_1 = 5 + 4s - 7t$, $x_2 = s$, $x_3 = t$, where $s$ and $t$ are arbitrary parameters [source: ma2001-lecture-chapter1-pdf#section-9].
    This equation also has **infinitely many solutions**.

### Geometric Interpretation of Solutions for Single Equations

*   **In 2D:** For $x+y=1$, the solutions are points $(x,y)=(1-s,s)$ where $s$ is any real number. These points form a straight line in the $xy$-plane [source: ma2001-lecture-chapter1-pdf#section-10].
*   **In 3D:** For $x+y=1$ (which can be written as $x+y+0z=1$), the solutions are points $(x,y,z)=(1-s,s,t)$ where $s$ and $t$ are any real numbers. These points form a plane in the $xyz$-space [source: ma2001-lecture-chapter1-pdf#section-11].

### Solutions for Zero and Non-Zero Equations

*   **Zero equation:** For $0x_1 + 0x_2 + \dots + 0x_n = 0$, any values of $x_1, \dots, x_n$ will satisfy the equation. Thus, its general solution is $x_1=t_1, x_2=t_2, \dots, x_n=t_n$ where $t_1, \dots, t_n$ are arbitrary parameters, yielding **infinitely many solutions** [source: ma2001-lecture-chapter1-pdf#section-12].
*   **Non-zero equation with all zero coefficients:** For $0x_1 + 0x_2 + \dots + 0x_n = b$ where $b$ is non-zero, no values of $x_1, \dots, x_n$ can satisfy the equation. Thus, there is **no solution** [source: ma2001-lecture-chapter1-pdf#section-12].

## Systems of Linear Equations

A **system of linear equations** (or a **linear system**) is a finite set of linear equations in the same variables $x_1, x_2, \dots, x_n$ [source: ma2001-lecture-chapter1-pdf#section-13].

A general linear system of $m$ equations in $n$ variables can be written as:
$a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1$
$a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2$
$\vdots$
$a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m$
where $a_{ij}$ and $b_i$ are real constants [source: ma2001-lecture-chapter1-pdf#section-13].

### Solutions of a Linear System

A solution $(x_1, x_2, \dots, x_n) = (s_1, s_2, \dots, s_n)$ to a linear system is a set of values that satisfies **every equation** in the system [source: ma2001-lecture-chapter1-pdf#section-14].

*   The set of all such solutions is the **solution set** of the system [source: ma2001-lecture-chapter1-pdf#section-14].
*   An expression that gives all solutions to the system is the **general solution** of the system [source: ma2001-lecture-chapter1-pdf#section-14].

**Example:**
Consider the system:
$4x_1 - x_2 + 3x_3 = -1$
$3x_1 + x_2 + 9x_3 = -4$

*   $(x_1, x_2, x_3) = (1, 2, -1)$ is a solution because:
    $4(1) - (2) + 3(-1) = 4 - 2 - 3 = -1$
    $3(1) + (2) + 9(-1) = 3 + 2 - 9 = -4$
    Both equations are satisfied [source: ma2001-lecture-chapter1-pdf#section-15].
*   $(x_1, x_2, x_3) = (1, 8, 1)$ is not a solution because:
    $4(1) - (8) + 3(1) = 4 - 8 + 3 = -1$
    $3(1) + (8) + 9(1) = 3 + 8 + 9 = 20 \neq -4$
    The second equation is not satisfied [source: ma2001-lecture-chapter1-pdf#section-15].

Not all systems of linear equations have solutions. For example, the system below has no solution because it's impossible to satisfy both equations simultaneously:
$x + y = 4$
$2x + 2y = 6$
(This simplifies to $x+y=4$ and $x+y=3$, which is a contradiction) [source: ma2001-lecture-chapter1-pdf#section-15].

### Consistent and Inconsistent Systems

*   A system of linear equations that has **no solution** is called **inconsistent** [source: ma2001-lecture-chapter1-pdf#section-16].
*   A system that has **at least one solution** is called **consistent** [source: ma2001-lecture-chapter1-pdf#section-16].

Every system of linear equations will fall into one of three categories:
1.  **No solution** (inconsistent) [source: ma2001-lecture-chapter1-pdf#section-16].
2.  **Exactly one solution** (consistent) [source: ma2001-lecture-chapter1-pdf#section-16].
3.  **Infinitely many solutions** (consistent) [source: ma2001-lecture-chapter1-pdf#section-16].

## Geometric Interpretation of Linear Systems

The nature of solutions to a linear system can be visualized geometrically, especially in 2D and 3D spaces.

### In the $xy$-plane (2D)

A system of two linear equations in two variables, $x$ and $y$, represents two straight lines ($L_1$ and $L_2$) in the $xy$-plane. A solution to the system corresponds to a point of intersection of these two lines [source: ma2001-lecture-chapter1-pdf#section-17].

1.  **No Solution (Inconsistent):** The system has no solution if and only if $L_1$ and $L_2$ are different but **parallel lines**. This means they never intersect [source: ma2001-lecture-chapter1-pdf#section-17].
2.  **Exactly One Solution (Consistent):** The system has only one solution if and only if $L_1$ and $L_2$ are **not parallel lines**. This means they intersect at a single, unique point [source: ma2001-lecture-chapter1-pdf#section-18].
3.  **Infinitely Many Solutions (Consistent):** The system has infinitely many solutions if and only if $L_1$ and $L_2$ are the **same line**. In this case, all points on the line are solutions [source: ma20001-lecture-chapter1-pdf#section-19].

### In $xyz$-space (3D)

A system of two linear equations in three variables, $x, y$, and $z$, represents two planes ($P_1$ and $P_2$) in the $xyz$-space. A solution to the system is a point of intersection of these two planes [source: ma2001-lecture-chapter1-pdf#section-20].

1.  **No Solution (Inconsistent):** The system has no solution if and only if $P_1$ and $P_2$ are different but **parallel planes**. They never intersect [source: ma2001-lecture-chapter1-pdf#section-20].
2.  **Infinitely Many Solutions (Consistent):** The system has infinitely many solutions if and only if either:
    *   $P_1$ and $P_2$ intersect at a **line**.
    *   $P_1$ and $P_2$ are the **same plane** [source: ma2001-lecture-chapter1-pdf#section-21].
    It is important to note that a system of two linear equations representing two planes **cannot have only one solution** [source: ma2001-lecture-chapter1-pdf#section-21].

### Exercise: Relative Positions of Three Planes

Consider a linear system with three equations in $xyz$-space:
$a_1x + b_1y + c_1z = d_1$ ($P_1$)
$a_2x + b_2y + c_2z = d_2$ ($P_2$)
$a_3x + b_3y + c_3z = d_3$ ($P_3$)
where for each $i$, $a_i, b_i, c_i$ are not all zero, representing three planes. The discussion of the relative positions of these three planes corresponds to the three types of solutions for the linear system [source: ma2001-lecture-chapter1-pdf#section-22, ma2001-tutorial-tutorial1-pdf#section-3].

1.  **No Solution:**
    *   All three planes are parallel and distinct.
    *   Two planes are parallel and distinct, and the third intersects them.
    *   The three planes intersect pairwise, forming a triangular prism (no common intersection point).
2.  **Only One Solution:** The three planes intersect at a single, unique point.
3.  **Infinitely Many Solutions:**
    *   Two planes are identical and the third intersects them in a line.
    *   All three planes intersect along a common line.
    *   All three planes are identical.

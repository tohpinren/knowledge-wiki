---
page_id: "y1s1-ma2001-matlab-row-operations-geometry"
title: "MATLAB for Row Operations and Geometric Interpretation"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "Using MATLAB to visualize and understand the geometric effects of elementary row operations on linear systems."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lab-lab2-pdf#section-1"
  - "ma2001-lab-lab2sol-pdf#section-1"
topics:
  - "activity"
  - "elementary"
  - "matrices"
  - "matrix"
  - "geometrical"
  - "row"
  - "operations"
  - "matlab"
  - "plane"
  - "via"
source_count: 2
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# MATLAB for Row Operations and Geometric Interpretation

This page explores the use of MATLAB to visualise and understand the geometric effects of elementary row operations on linear systems in both two-dimensional ($xy$-plane) and three-dimensional ($xyz$-space) contexts [source:ma2001-lab-lab2-pdf#section-1]. These operations are fundamental to solving linear systems, and their geometric interpretations highlight why the solution set remains invariant under such transformations.

## Geometrical Interpretation in the $xy$-Plane

Elementary row operations performed on a system of linear equations in two variables correspond to transformations of lines in the $xy$-plane. MATLAB's `ezplot` command is used to plot the graphs of these lines [source:ma2001-lab-lab2-pdf#section-2].

Consider the following linear system:
$$
\begin{cases}
2x - y = 1 \\
x + y = 5
\end{cases}
$$ [source:ma2001-lab-lab2-pdf#section-2]

Each equation represents a line in the $xy$-plane. The solution to the system is the point where these two lines intersect.

### MATLAB for Plotting Lines

To plot these lines in MATLAB, use the `ezplot` command:
```matlab
>> ezplot('2*x - y = 1')
>> hold on % Keeps the previous plot
>> ezplot('x + y = 5')
``` [source:ma2001-lab-lab2-pdf#section-2]

The `hold on` command ensures that subsequent plots are added to the same figure, allowing both lines to be displayed simultaneously [source:ma2001-lab-lab2-pdf#section-2].

The augmented matrix for this system is:
$$
A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 1 & 5 \end{pmatrix}
$$ [source:ma2001-lab-lab2-pdf#section-2]

We use elementary matrices to represent row operations:
$$
E_1 = \begin{pmatrix} 0.5 & 0 \\ 0 & 1 \end{pmatrix}, \quad E_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad E_3 = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}
$$ [source:ma2001-lab-lab2-pdf#section-2]

### Effects of Elementary Row Operations in $xy$-Plane

1.  **Multiplying a row by a non-zero scalar ($kR_i$)**
    *   **Operation**: `0.5R1` (Multiply the first row by 0.5). This is achieved by `E1 * A`.
    *   **Resultant System**:
        $$
        \begin{cases}
        x - 0.5y = 0.5 \\
        x + y = 5
        \end{cases}
        $$ [source:ma2001-lab-lab2sol-pdf#section-2]
    *   **Geometric Interpretation**: The first equation `x - 0.5y = 0.5` represents the **same line** as `2x - y = 1`. Therefore, applying this operation results in no change to the graph of the system. The intersection point remains the same [source:ma2001-lab-lab2sol-pdf#section-2].

2.  **Swapping two rows ($R_i \leftrightarrow R_j$)**
    *   **Operation**: `R1 <-> R2` (Swap the first and second rows). This is achieved by `E2 * A`.
    *   **Resultant System**:
        $$
        \begin{cases}
        x + y = 5 \\
        2x - y = 1
        \end{cases}
        $$ [source:ma2001-lab-lab2sol-pdf#section-2]
    *   **Geometric Interpretation**: The equations are interchanged, but the set of lines remains the same. The graph of the new system is identical to the original, and the intersection point is unchanged [source:ma2001-lab-lab2sol-pdf#section-2].

3.  **Adding a multiple of one row to another ($R_i + kR_j$)**
    *   **Operation**: `R2 - R1` (Subtract the first row from the second row). This is achieved by `E3 * A`.
    *   **Resultant System**:
        $$
        \begin{cases}
        2x - y = 1 \\
        -x + 2y = 4
        \end{cases}
        $$ [source:ma2001-lab-lab2sol-pdf#section-2]
    *   **Geometric Interpretation**: The first line (`2x - y = 1`) remains unchanged. The second equation, `-x + 2y = 4`, represents a **new line** that is different from the original second line (`x + y = 5`). However, this new line still intersects the first line at the **same point** as the original system. This means the solution of the system remains invariant under this operation [source:ma2001-lab-lab2sol-pdf#section-3].

    *   **Remark**: In general, the row operation $R_i + kR_j$ creates a new line for row $i$ which, as $k$ increases, moves away from the original line $i$ but towards line $j$. Crucially, the intersection point (the system's solution) remains the same [source:ma2001-lab-lab2sol-pdf#section-3].
    
    To plot the new second line in MATLAB:
    ```matlab
    >> ezplot('-x + 2*y = 4')
    ``` [source:ma2001-lab-lab2sol-pdf#section-2]

## Geometrical Interpretation in the $xyz$-Space

Elementary row operations performed on a system of linear equations in three variables correspond to transformations of planes in the $xyz$-space. MATLAB's `ezsurf` command is used to plot the graphs of these surfaces (planes) [source:ma2001-lab-lab2-pdf#section-3].

Consider the following linear system:
$$
\begin{cases}
2x - y + z = 1 \\
x + y - z = 5
\end{cases}
$$ [source:ma2001-lab-lab2-pdf#section-3]

Each equation represents a plane in $xyz$-space. The solution to the system is the line where these two planes intersect.

### MATLAB for Plotting Planes

To plot these planes, it's often easier to rewrite the equations in terms of $z$:
$$
\begin{cases}
z = 1 - 2x + y \\
z = -5 + x + y
\end{cases}
$$ [source:ma2001-lab-lab2-pdf#section-4]

Use the `ezsurf` command to plot these surfaces. The `clf` command can be used to clear previous graphical figures [source:ma2001-lab-lab2-pdf#section-4].
```matlab
>> clf % Clears all graphical figures
>> ezsurf('1 - 2*x + y')
>> hold on
>> ezsurf('-5 + x + y')
``` [source:ma2001-lab-lab2-pdf#section-4]

The resulting 3D figure can be rotated interactively in the MATLAB plot window for better visualization [source:ma2001-lab-lab2-pdf#section-4].

The augmented matrix for this system is:
$$
B = \begin{pmatrix} 2 & -1 & 1 & 1 \\ 1 & 1 & -1 & 5 \end{pmatrix}
$$ [source:ma2001-lab-lab2-pdf#section-4]

We use the same elementary matrices ($E_1, E_2, E_3$) as before.

### Effects of Elementary Row Operations in $xyz$-Space

1.  **Multiplying a row by a non-zero scalar ($kR_i$)**
    *   **Operation**: `0.5R1` (Multiply the first row by 0.5). Achieved by `E1 * B`.
    *   **Resultant System**:
        $$
        \begin{cases}
        x - 0.5y + 0.5z = 0.5 \\
        x + y - z = 5
        \end{cases}
        $$ [source:ma2001-lab-lab2sol-pdf#section-4]
    *   **Geometric Interpretation**: The first equation `x - 0.5y + 0.5z = 0.5` represents the **same plane** as `2x - y + z = 1`. Thus, the graph of the system (two planes) remains unchanged, and their intersection line (the solution set) is preserved [source:ma2001-lab-lab2sol-pdf#section-4].

2.  **Swapping two rows ($R_i \leftrightarrow R_j$)**
    *   **Operation**: `R1 <-> R2` (Swap the first and second rows). Achieved by `E2 * B`.
    *   **Resultant System**:
        $$
        \begin{cases}
        x + y - z = 5 \\
        2x - y + z = 1
        \end{cases}
        $$ [source:ma2001-lab-lab2sol-pdf#section-4]
    *   **Geometric Interpretation**: Swapping the equations merely interchanges the order of the planes. The two planes themselves, and thus their intersection line, remain the same. The graph of the new system is identical to the original [source:ma2001-lab-lab2sol-pdf#section-4].

3.  **Adding a multiple of one row to another ($R_i + kR_j$)**
    *   **Operation**: `R2 - R1` (Subtract the first row from the second row). Achieved by `E3 * B`.
    *   **Resultant System**:
        $$
        \begin{cases}
        2x - y + z = 1 \\
        -x + 2y - 2z = 4
        \end{cases}
        $$ [source:ma2001-lab-lab2sol-pdf#section-4]
    *   **Geometric Interpretation**: The first plane (`2x - y + z = 1`) remains unchanged. The second equation, `-x + 2y - 2z = 4`, represents a **new plane** that is different from the original second plane (`x + y - z = 5`). However, this new plane still intersects the first plane along the **same line** as the original system. This ensures that the solution set (the intersection line) of the system remains invariant [source:ma2001-lab-lab2sol-pdf#section-5].

    *   **Remark**: Similar to the 2D case, the row operation $R_i + kR_j$ creates a new plane for row $i$ which, as $k$ increases, moves away from the original plane $i$ but towards plane $j$. The crucial outcome is that the intersection line (the solution of the system) remains invariant [source:ma2001-lab-lab2sol-pdf#section-5].
    
    To plot the new second plane in MATLAB:
    ```matlab
    >> ezsurf('(-4 - x + 2*y) / 2') % Solve -x + 2y - 2z = 4 for z
    ``` [source:ma2001-lab-lab2sol-pdf#section-5]

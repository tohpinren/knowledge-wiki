---
page_id: "y1s1-ma2001-matlab-basics"
title: "MATLAB Basics for Linear Algebra"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-ma2001"
parent_page_id: "y1s1-ma2001-hub"
batch_id: "y1s1-ma2001-20260412t144744z"
status: "canonical"
summary: "An introduction to MATLAB for linear algebra, covering basic interface, matrix input, and fundamental operations."
aliases:
tags:
  - "course"
  - "ma2001"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "ma2001-lab-lab1-pdf#section-1"
  - "ma2001-lab-assignment-a0251957u-lab-assignment-pdf#section-1"
topics:
  - "matlab"
  - "matrix"
  - "format"
  - "row"
  - "variable"
  - "digits"
  - "matrices"
  - "nus"
  - "question"
  - "assignment"
source_count: 2
lecture_number: null
last_compiled_at: "2026-04-12T15:06:40+00:00"
---
# MATLAB Basics for Linear Algebra

MATLAB (Matrix Laboratory) is a powerful computing software developed by MathWorks, widely used for tasks involving matrices, such as those encountered in linear algebra. As an NUS student, you can install MATLAB on your personal computer via the official student MATLAB portal (https://sm05.stf.nus.edu.sg/studentmatlab/) using your NUSNET ID. If you are not on the NUS network, an nVPN connection is required to access the installation link [source:ma2001-lab-lab1-pdf#section-1].

### MATLAB Statements

A fundamental component of interacting with MATLAB is through statements, which primarily come in two forms:
*   **Variable Assignment**: The most common form is `variable = expression`, where the result of the `expression` is assigned to the specified `variable` [source:ma2001-lab-lab1-pdf#section-2].
*   **Expression Evaluation**: A simpler form, `expression`, evaluates the expression and automatically assigns its result to a special default variable named `ans` (which stands for "answer") [source:ma2001-lab-lab1-pdf#section-2].

To obtain information or usage details about a specific function or topic, type `help topic` at the MATLAB command prompt (`>>`) [source:ma2001-lab-lab1-pdf#section-2].

### Working with Matrices

MATLAB is designed to work efficiently with matrices. Vectors are considered special cases of matrices: column vectors are $m \times 1$ matrices, and row vectors are $1 \times n$ matrices [source:ma2001-lab-lab1-pdf#section-3].

#### How to Enter Matrices
To set up an $m \times n$ matrix, say `A`, you execute a statement in the following format [source:ma2001-lab-lab1-pdf#section-3]:
```matlab
A = [ row1; row2; ...; rowm ]
```
where:
*   The entries for each row are separated by one or more blank spaces.
*   Rows are separated by semicolons (`;`).
*   The square brackets `[` and `]` are used for entering the matrix but are not considered part of the matrix data itself, nor are they stored as such by MATLAB [source:ma2001-lab-lab1-pdf#section-3].
*   MATLAB variable names are **case-sensitive**. For example, `B` and `b` would refer to two different variables [source:ma2001-lab-lab1-pdf#section-3].

**Example of Matrix Input**:
To create a matrix `A = [1 2 pi; 0.1 5 6; 7 8 1/2]`:
```matlab
>> A = [1,2, pi; 0.1, 5, 6; 7, 8, 1/2]
```
To create a column vector `b = [1; 2; 3]`:
```matlab
>> b = [1; 2; 3]
```
To create a row vector `x = [1, 2, 3]`:
```matlab
>> x = [1, 2, 3]
```

#### Basic Matrix Operations
MATLAB provides a comprehensive set of commands for performing various matrix operations. For matrices `A` and `B`, and a scalar `t`:

| Command        | Description                                       |
| :------------- | :------------------------------------------------ |
| `A(i,j)`       | The entry at row `i`, column `j` of matrix `A` [source:ma2001-lab-lab1-pdf#section-3]. |
| `A(i,:)`       | The entire `i`-th row of matrix `A` [source:ma2001-lab-lab1-pdf#section-3]. |
| `A(:,j)`       | The entire `j`-th column of matrix `A` [source:ma2001-lab-lab1-pdf#section-3]. |
| `A + B`        | Matrix addition [source:ma2001-lab-lab1-pdf#section-3].            |
| `A - B`        | Matrix subtraction [source:ma2001-lab-lab1-pdf#section-3].         |
| `t * A`        | Scalar multiplication (where `t` is a real number) [source:ma2001-lab-lab1-pdf#section-3]. |
| `A * B`        | Matrix multiplication [source:ma2001-lab-lab1-pdf#section-3].      |
| `A ^ n`        | Raising a square matrix `A` to a positive integral power `n` ($A^n$) [source:ma2001-lab-lab1-pdf#section-3]. |
| `A'`           | Transpose of matrix `A` ($A^T$) [source:ma2001-lab-lab1-pdf#section-3]. |
| `inv(A)`       | Inverse of an invertible square matrix `A` ($A^{-1}$) [source:ma2001-lab-lab1-pdf#section-3]. |
| `zeros(n)`     | An $n \times n$ zero matrix ($0_{n \times n}$) [source:ma2001-lab-lab1-pdf#section-3]. |
| `zeros(m,n)`   | An $m \times n$ zero matrix ($0_{m \times n}$) [source:ma2001-lab-lab1-pdf#section-3]. |
| `eye(n)`       | An $n \times n$ identity matrix ($I_n$) [source:ma2001-lab-lab1-pdf#section-3]. |
| `rref(A)`      | The reduced row echelon form of `A` [source:ma2001-lab-lab1-pdf#section-3]. |
| `det(A)`       | The determinant of `A` ($det(A)$) [source:ma2001-lab-lab1-pdf#section-3]. |

**Example of Matrix Operations**:
Given `A = [1,2, pi; 0.1, 5, 6; 7, 8, 1/2]`
*   To get the entry at row 2, column 3:
    ```matlab
    >> a = A(2,3)
    ```
*   To get the second row of `A`:
    ```matlab
    >> r = A(2, :)
    ```
*   To get the third column of `A`:
    ```matlab
    >> c = A(:,3)
    ```
*   To compute `0.3 * A`:
    ```matlab
    >> 0.3 * A
    ```
    The result will be assigned to `ans`.
*   To compute `A * x'` where `x = [1, 2, 3]`:
    ```matlab
    >> A * x'
    ```

#### Solving Linear Systems

MATLAB offers multiple ways to solve linear systems of the form $A\mathbf{x} = \mathbf{b}$.

1.  **Using the Inverse Matrix**: If $A$ is an invertible square matrix, the solution can be found by $\mathbf{x} = A^{-1}\mathbf{b}$. In MATLAB, this is computed as `inv(A)*b`.
    ```matlab
    >> A = [1 1 2; 3 6 -5; 2 4 3];
    >> b = [1; -1; 0];
    >> x = inv(A)*b
    ```

2.  **Using the Left Division Operator**: MATLAB's left division operator (`\`) is often a more numerically stable and efficient method for solving linear systems directly. It is typed as `A\b`.
    ```matlab
    >> A = [1 1 2; 3 6 -5; 2 4 3];
    >> b = [1; -1; 0];
    >> x = A\b
    ```
    (You are not required to understand the internal workings of the matrix left division for this module, but `help mldivide` can provide more information) [source:ma2001-lab-assignment-a0251957u-lab-assignment-pdf#section-7].

3.  **Using Reduced Row Echelon Form (RREF)**: For a system $A\mathbf{x} = \mathbf{b}$, the solution can be found by forming the augmented matrix $[A \mid \mathbf{b}]$ and then computing its reduced row echelon form using `rref([A, b])`. This method is particularly useful for analyzing systems with non-unique solutions or no solutions.
    ```matlab
    >> A = [1 1 2; 3 6 -5; 2 4 3];
    >> b = [1; -1; 0];
    >> rref([A, b])
    ```
    This command combines matrix `A` and vector `b` to form a single augmented matrix (e.g., a $3 \times 4$ matrix for a $3 \times 3$ matrix `A` and $3 \times 1$ vector `b`) and then applies the `rref` function [source:ma2001-lab-lab1-pdf#section-6].

### Precision and Display Format

MATLAB performs all numerical computations with approximately 16 decimal digits of precision. However, the format of the displayed output can be controlled using various `format` commands [source:ma2001-lab-lab1-pdf#section-4].

| Command       | Description                                                                 |
| :------------ | :-------------------------------------------------------------------------- |
| `format short`  | Scaled fixed-point format with 5 digits (this is the default setting) [source:ma2001-lab-lab1-pdf#section-4]. |
| `format long`   | Scaled fixed-point format with 15 digits [source:ma2001-lab-lab1-pdf#section-4]. |
| `format shorte` | Floating-point format with 5 digits [source:ma2001-lab-lab1-pdf#section-4]. |
| `format longe`  | Floating-point format with 15 digits [source:ma2001-lab-lab1-pdf#section-4]. |
| `format rat`    | Approximate fractions [source:ma2001-lab-lab1-pdf#section-4].               |

**Warning**: When using `format rat`, MATLAB approximates decimals with rational numbers, which can sometimes lead to unexpected results. Occasionally, an asterisk (`*`) may appear where a quantity of 0 is expected [source:ma2001-lab-lab1-pdf#section-4]. For MA2001 lab assignments, non-integer MATLAB answers should generally use `format short`, with specific exceptions like for Question 4(c) of the lab assignment where `format rat` is required for non-integer answers to be written in fraction form [source:ma2001-lab-assignment-a0251957u-lab-assignment-pdf#section-5].

**Example of Format Commands**:
```matlab
>> format rat
>> A % Displays matrix A with rational approximations
>> format short
>> A % Displays matrix A with 5-digit fixed-point format
>> format long
>> A % Displays matrix A with 15-digit fixed-point format
```

### Useful Tips

*   **Recall Commands**: Use the `[up arrow key]` (↑) to cycle through and recall previously typed commands in the command window [source:ma2001-lab-lab1-pdf#section-5].
*   **Clear Command Window**: Type `clc` to clear all text from the command window [source:ma2001-lab-lab1-pdf#section-5].
*   **Clear Variables**:
    *   `clear`: Clears all previously assigned variables from the workspace [source:ma2001-lab-lab1-pdf#section-5].
    *   `clear variablename`: Clears a specific variable named `variablename` [source:ma2001-lab-lab1-pdf#section-5].
*   **Edit Variables**: Double-clicking a variable name in the workspace window allows you to open and edit its contents [source:ma2001-lab-lab1-pdf#section-5].

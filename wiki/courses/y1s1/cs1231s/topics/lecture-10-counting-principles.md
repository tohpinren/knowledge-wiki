---
page_id: "y1s1-cs1231s-lecture-10-counting-principles"
title: "Lecture 10: Sum, Product, and Pigeonhole Principles"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Introduces fundamental counting techniques such as the Sum Rule, Product Rule, and the Pigeonhole Principle for solving combinatorial problems."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2"
  - "cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-2"
  - "cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1"
  - "cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09qns-pdf#section-1"
  - "cs1231s-tutorial-tut09ans-post-pdf#section-1"
topics:
  - "rule"
  - "elements"
  - "theorem"
  - "states"
  - "probability"
  - "principle"
  - "pigeonhole"
  - "sets"
  - "finite"
  - "set"
source_count: 5
lecture_number: 10
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 10: Sum, Product, and Pigeonhole Principles

This page introduces fundamental counting principles, including the Sum Rule, Product Rule, and the Pigeonhole Principle, crucial for solving combinatorial problems and understanding concepts in computer science like algorithm complexity and discrete probability [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1].

## 9.1 Introduction to Counting and Probability

This lecture, based on Chapter 9 of Epp's book, lays the groundwork for understanding random processes, sample spaces, events, and probability [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-1].

### Key Definitions

*   A **random process** is an experiment or process where one outcome from a set of outcomes is certain to occur, but which specific outcome cannot be predicted with certainty [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1].
*   A **sample space** ($S$) is the set of all possible outcomes of a random process or experiment [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-1].
*   An **event** ($E$) is any subset of a sample space [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-1].
*   For a finite set $A$, $|A|$ denotes the number of elements in $A$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-1].

### Equally Likely Probability Formula

For an event $E$ in a finite sample space $S$ where all outcomes are equally likely, the probability of $E$, denoted $P(E)$, is given by [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-1]:

$P(E) = \frac{\text{The number of outcomes in } E}{\text{The total number of outcomes in } S} = \frac{|E|}{|S|}$

**Example: Tossing Two Coins**
When tossing two coins, the sample space $S = \{HH, HT, TH, TT\}$, so $|S|=4$.
*   Event "0 heads": $E_0 = \{TT\}$, so $|E_0|=1$. $P(E_0) = 1/4$.
*   Event "1 head": $E_1 = \{HT, TH\}$, so $|E_1|=2$. $P(E_1) = 2/4 = 1/2$.
*   Event "2 heads": $E_2 = \{HH\}$, so $|E_2|=1$. $P(E_2) = 1/4$.

It is incorrect to assume each outcome (0, 1, or 2 heads) has a 1/3 probability, as these outcomes are not equally likely [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1].

### Counting Elements of a List

**Theorem 9.1.1: The Number of Elements in a List**
If $m$ and $n$ are integers and $m \leq n$, then there are $n - m + 1$ integers from $m$ to $n$ inclusive [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-1].

**Example: 3-Digit Integers Divisible by 5**
To find how many 3-digit integers (from 100 to 999 inclusive) are divisible by 5:
The integers are $5 \times 20, 5 \times 21, \dots, 5 \times 199$.
Using Theorem 9.1.1, the number of such integers is $199 - 20 + 1 = 180$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-1].

## 9.2 Possibility Trees and the Multiplication Rule

### Possibility Trees

A **possibility tree** is a useful visual tool for systematically tracking all possibilities when events happen in order [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

**Example: Tournament Completion**
In a tournament where the first team to win four games wins, and Team A has already won the first two games against Team B. To find the number of ways the tournament can be completed, a possibility tree can be drawn. Each path from the root (start) to a leaf (tournament ends) represents a unique way the tournament can be completed [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2, cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1]. There are 15 such ways [source:cs1231s-tutorial-tut09ans-post-pdf#section-1].

### The Multiplication/Product Rule

**Theorem 9.2.1: The Multiplication/Product Rule**
If an operation consists of $k$ steps, and the first step can be performed in $n_1$ ways, the second step in $n_2$ ways (regardless of the first), ..., and the $k$-th step in $n_k$ ways (regardless of preceding steps), then the entire operation can be performed in $n_1 \times n_2 \times n_3 \times \dots \times n_k$ ways [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-2].

**Example: Pairing Computer Units**
A computer installation has four input/output units (A, B, C, D) and three central processing units (X, Y, Z). If any I/O unit can be paired with any CPU, the total number of ways to pair them is $4 \times 3 = 12$ ways [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2]. This can also be visualized with a possibility tree.

**Example: Number of Personal Identification Numbers (PINs)**
A PIN is a sequence of four symbols chosen from 26 letters and 10 digits (36 total symbols), with repetition allowed.
To form a PIN is a four-step operation:
1.  Choose the 1st symbol: 36 choices.
2.  Choose the 2nd symbol: 36 choices.
3.  Choose the 3rd symbol: 36 choices.
4.  Choose the 4th symbol: 36 choices.
By the multiplication rule, there are $36 \times 36 \times 36 \times 36 = 36^4 = 1,679,616$ possible PINs [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

**Example: PINs without Repetition**
If repetition is not allowed for the PINs:
1.  Choose the 1st symbol: 36 choices.
2.  Choose the 2nd symbol: 35 choices (one less).
3.  Choose the 3rd symbol: 34 choices.
4.  Choose the 4th symbol: 33 choices.
The number of PINs without repetition is $36 \times 35 \times 34 \times 33 = 1,413,720$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

**Application: Power Set Size**
For a finite set $A$ with $|A|=n$ elements, the number of subsets (the size of its power set, $P(A)$) is $2^n$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2]. This is because for each of the $n$ elements, there are two choices: either to pick it or drop it when forming a subset. By the multiplication rule, this results in $2 \times 2 \times \dots \times 2$ ($n$ times) = $2^n$ ways [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

**When the Multiplication Rule is Difficult to Apply**
The multiplication rule requires that the number of ways to perform each step is independent of the choices made in previous steps. If this condition is not met, the rule can lead to incorrect results [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

**Example: Officer Selection Problem**
Three officers (president, treasurer, secretary) are to be chosen from Ann, Bob, Cyd, and Dan. Constraints: Ann cannot be president, and either Cyd or Dan must be secretary.
An incorrect application of the multiplication rule might suggest $3 \times 3 \times 2 = 18$ ways [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2]. This is wrong because the number of choices for secretary depends on who is chosen for president and treasurer. For example:
*   If Bob is president and Ann is treasurer, two choices for secretary (Cyd or Dan).
*   If Bob is president and Cyd is treasurer, only one choice for secretary (Dan, since Cyd is already treasurer and must be secretary).
The clearer way to solve this is by constructing a possibility tree, which reveals 8 ways [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

Alternatively, the steps can be reordered to allow for the multiplication rule:
1.  Choose the secretary (Cyd or Dan): 2 ways.
2.  Choose the president (neither Ann nor the person chosen as secretary): 2 ways.
3.  Choose the treasurer (either of the 2 persons not chosen in steps 1 and 2): 2 ways.
Total ways = $2 \times 2 \times 2 = 8$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

### Permutations

A **permutation** of a set of objects is an ordering of these objects in a row [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-2].

**Theorem 9.2.2: Permutations**
The number of permutations of a set with $n$ ($n \geq 1$) elements is $n!$ (n factorial) [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-2].
This is derived from the multiplication rule:
1.  Choose the 1st element: $n$ ways.
2.  Choose the 2nd element: $n-1$ ways.
...
$n$. Choose the $n$-th element: 1 way.
Total ways: $n \times (n-1) \times \dots \times 1 = n!$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].
Note: $0!$ is defined as 1 [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

**Example: Permutations of Letters in "COMPUTER"**
a. How many ways can the 8 distinct letters in "COMPUTER" be arranged in a row?
   $8! = 40,320$ ways [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].
b. How many ways if "CO" must remain next to each other (in order) as a unit?
   Treat "CO" as a single block. Now we are arranging 7 "units" (the "CO" block and the remaining 6 letters). So, $7!$ ways.

### Permutations of Selected Elements ($r$-permutations)

An **$r$-permutation** of a set of $n$ elements is an ordered selection of $r$ elements taken from the set [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-2].
It is denoted as $P(n, r)$, $_n P_r$, or $P^n_r$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

**Theorem 9.2.3: $r$-permutations from a set of $n$ elements**
If $n$ and $r$ are integers and $1 \leq r \leq n$, the number of $r$-permutations of a set of $n$ elements is given by [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-2]:
$P(n, r) = n(n-1)(n-2)\dots(n-r+1)$
or, equivalently:
$P(n, r) = \frac{n!}{(n-r)!}$

**Example: Evaluate P(5, 2)**
$P(5, 2) = \frac{5!}{(5-2)!} = \frac{5!}{3!} = 5 \times 4 = 20$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-2].

**Example: Combination Lock**
A lock with 40 positions requires a 3-number code (clockwise, counterclockwise, clockwise). Consecutive numbers cannot be the same [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1, cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09qns-pdf#section-1].
1.  First number: 40 choices.
2.  Second number: 39 choices (cannot be the same as the first).
3.  Third number: 39 choices (cannot be the same as the second).
Total combinations: $40 \times 39 \times 39 = 60,840$ [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1].

**Circular Permutations**
The number of circular permutations of $n$ distinct objects is $(n-1)!$ [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09qns-pdf#section-2]. This is because fixing one object's position eliminates rotational symmetry.

**Example: Boys and Girls at a Circular Table**
In how many ways can 8 boys and 4 girls sit around a circular table so that no two girls sit together?
1.  Seat the 8 boys first in a circle: $(8-1)! = 7!$ ways [source:cs1231s-tutorial-tut09ans-post-pdf#section-4].
2.  This creates 8 spaces between the boys where the girls can sit.
3.  Select 4 of these 8 spaces for the 4 girls and arrange them: $P(8,4)$ ways.
Total ways = $7! \times P(8,4) = 5040 \times 1680 = 8,467,200$ [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1, cs1231s-tutorial-tut09ans-post-pdf#section-4].

## 9.3 Counting Elements of Disjoint Sets

### The Addition/Sum Rule

**Theorem 9.3.1: The Addition/Sum Rule**
If a finite set $A$ is the union of $k$ distinct, mutually disjoint subsets $A_1, A_2, \dots, A_k$, then the number of elements in $A$ is the sum of the number of elements in each subset [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-3]:
$|A| = |A_1| + |A_2| + \dots + |A_k|$

**Example: Counting Passwords with 3 or Fewer Letters**
A computer password consists of 1, 2, or 3 letters chosen from 26 letters with repetition allowed.
*   Passwords of length 1: 26 ways.
*   Passwords of length 2: $26^2$ ways.
*   Passwords of length 3: $26^3$ ways.
Since these are disjoint sets of passwords, the total number is $26 + 26^2 + 26^3 = 18,278$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3].

**Example: White/Blue Balls in Boxes**
Given $n$ boxes, each with a white or blue ball. At least one box has a white ball, and boxes with white balls must be consecutively numbered.
The number of ways this can be done can be found using the addition rule [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1].
*   Case 1: 1 white ball (e.g., in box 1, or box 2, ..., or box $n$): $n$ ways.
*   Case 2: 2 consecutive white balls: $n-1$ ways.
*   Case 3: 3 consecutive white balls: $n-2$ ways.
...
*   Case $n$: $n$ consecutive white balls: 1 way.
Total ways = $n + (n-1) + \dots + 1 = \sum_{k=1}^n k = \frac{n(n+1)}{2}$ [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1, cs1231s-tutorial-tut09ans-post-pdf#section-3].

### The Difference Rule

**Theorem 9.3.2: The Difference Rule**
If $A$ is a finite set and $B \subseteq A$, then the number of elements in $A$ but not in $B$ is $|A \setminus B| = |A| - |B|$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-3]. This follows because $B$ and $A \setminus B$ are disjoint sets whose union is $A$.

**Example: Counting PINs with Repeated Symbols**
A typical PIN (4 symbols from 36, repetition allowed) has $36^4 = 1,679,616$ total PINs.
The number of PINs with no repeated symbols (calculated earlier as an $r$-permutation) is $P(36,4) = 1,413,720$.
Using the difference rule, the number of PINs that contain at least one repeated symbol is $1,679,616 - 1,413,720 = 265,896$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3].

### Probability of the Complement of an Event

A general property of probabilities states that the probability of the complement of an event is obtained by subtracting the probability of the event from 1 [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-3].
If $S$ is a finite sample space and $A$ is an event in $S$, then $P(\bar{A}) = 1 - P(A)$.
For the PIN example, the probability that a randomly chosen PIN contains a repeated symbol is $1 - P(\text{no repeated symbols}) = 1 - \frac{1,413,720}{1,679,616} \approx 1 - 0.842 = 0.158$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3].

### The Inclusion/Exclusion Rule

The addition rule applies to mutually disjoint sets. When sets overlap, the **Inclusion/Exclusion Rule** is used to count elements in their union [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3].

**Theorem 9.3.3: The Inclusion/Exclusion Rule for 2 or 3 Sets**
*   For two finite sets $A$ and $B$:
    $|A \cup B| = |A| + |B| - |A \cap B|$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-3].
*   For three finite sets $A$, $B$, and $C$:
    $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-3].

**Example: Counting Multiples of 3 or 5**
How many integers from 1 to 1,000 are multiples of 3 or multiples of 5?
*   Let $A$ be the set of multiples of 3: $|A| = \lfloor 1000/3 \rfloor = 333$.
*   Let $B$ be the set of multiples of 5: $|B| = \lfloor 1000/5 \rfloor = 200$.
*   $A \cap B$ is the set of multiples of 15: $|A \cap B| = \lfloor 1000/15 \rfloor = 66$.
Using the Inclusion/Exclusion Rule:
$|A \cup B| = |A| + |B| - |A \cap B| = 333 + 200 - 66 = 467$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3].

To find how many integers are *neither* multiples of 3 nor 5, use the difference rule and De Morgan's law:
$|\overline{A} \cap \overline{B}| = |\overline{A \cup B}| = |U| - |A \cup B|$
Where $U$ is the universe of integers from 1 to 1,000, so $|U|=1000$.
Number of integers neither multiples of 3 nor 5 = $1000 - 467 = 533$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-3].

**Example: CS Students Taking Modules**
There are 789 CS students. Given counts for students taking CS1231S ($A$), CS1101S ($B$), MA1101R ($C$), and various overlaps (e.g., $|A \cap B|$, $|A \cap C|$, $|B \cap C|$, $|A \cap B \cap C|$).
To find how many students are not taking any of these three modules, first apply the Inclusion/Exclusion Rule for three sets to find $|A \cup B \cup C|$ [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1, cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09qns-pdf#section-2, cs1231s-tutorial-tut09ans-post-pdf#section-2]:
$|A \cup B \cup C| = 672 + 629 + 153 - 608 - 87 - 53 + 46 = 752$.
Then, use the difference rule with the total number of CS students ($|U|=789$):
$|\overline{A} \cap \overline{B} \cap \overline{C}| = |U| - |A \cup B \cup C| = 789 - 752 = 37$ [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1, cs1231s-tutorial-tut09ans-post-pdf#section-2].

## 9.4 The Pigeonhole Principle (PHP)

### Introduction to PHP

The **Pigeonhole Principle (PHP)** states that if $n$ pigeons fly into $m$ pigeonholes and $n > m$, then at least one pigeonhole must contain two or more pigeons [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-4]. It is also known as the Dirichlet box principle [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

**Mathematical Formulation:** A function from one finite set (pigeons) to a smaller finite set (pigeonholes) cannot be one-to-one. There must be at least two elements in the domain that have the same image in the co-domain [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-4].

**Example: Birthdays**
In a group of 13 people, must at least two have been born in the same month?
*   Pigeons: 13 people ($n=13$).
*   Pigeonholes: 12 months ($m=12$).
Since $n > m$ ($13 > 12$), by PHP, at least two people must share a birth month [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

**Example: Hairs on Heads**
Among the population of Singapore (approx. 5.47 million in June 2014), are there at least two people with the same number of hairs on their heads?
*   Pigeons: Population of Singapore ($n \approx 5.47 \text{ million}$).
*   Pigeonholes: Possible number of hairs on a head (0 to 300,000, so $m = 300,001$).
Since $n > m$, at least two people must have the same number of hairs on their heads [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

**Application: Decimal Expansions of Fractions**
The PHP guarantees that the decimal expansion of any rational number either terminates or repeats [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4]. When performing long division for $a/b$, the remainders must be integers from $0$ to $b-1$. Since there are $b$ possible remainder values, if the division continues for more than $b$ steps, a remainder value must repeat. Once a remainder repeats, the sequence of subsequent decimal digits will also repeat [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

### Generalized Pigeonhole Principle

The **Generalized Pigeonhole Principle** states that if $n$ pigeons fly into $m$ pigeonholes and, for some positive integer $k$, $k < n/m$, then at least one pigeonhole contains $k+1$ or more pigeons [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-4].
Alternatively, for a function $f$ from a finite set $X$ with $n$ elements to a finite set $Y$ with $m$ elements, if for any positive integer $k$, $k < n/m$, then there is some $y \in Y$ such that $y$ is the image of at least $k+1$ distinct elements of $X$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-4].

**Example: Last Initials**
In a group of 85 people, show that at least 4 must have the same last initial ('A', 'B', ..., 'Z').
*   Pigeons: 85 people ($n=85$).
*   Pigeonholes: 26 possible last initials ($m=26$).
Calculate $n/m = 85/26 \approx 3.27$.
Since $3 < 85/26$, according to the Generalized PHP, at least $3+1=4$ people must share the same last initial [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

### Generalized Pigeonhole Principle (Contrapositive Form)

The contrapositive form states that for any function $f$ from a finite set $X$ with $n$ elements to a finite set $Y$ with $m$ elements, and for any positive integer $k$, if for each $y \in Y$, $f^{-1}(\{y\})$ has at most $k$ elements, then $X$ has at most $km$ elements; in other words, $n \leq km$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-summary-pdf#section-4].

**Example: Last Initials (using Contrapositive)**
Suppose, for contradiction, that no 4 people out of 85 had the same last initial. This means at most 3 people share any particular initial ($k=3$). With 26 initials ($m=26$), the total number of people ($n$) would be at most $3 \times 26 = 78$. This contradicts the fact that there are 85 people. Therefore, the supposition is false, and at least 4 people must share a last initial [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

**Example: Students and Computers**
There are 42 students sharing 12 computers. Each student uses exactly 1 computer, and no computer is used by more than 6 students. Show that at least 5 computers are used by 3 or more students.

**Argument by Contradiction:**
Suppose fewer than 5 computers (i.e., 4 or fewer) are used by 3 or more students. This implies that 8 or more computers (out of 12) are used by 2 or fewer students.
Divide computers into two sets:
*   $C_1$: 8 computers used by at most 2 students each. Max students served by $C_1 = 2 \times 8 = 16$.
*   $C_2$: 4 computers used by 3 to 6 students each. Max students served by $C_2 = 6 \times 4 = 24$.
Total maximum students served = $16 + 24 = 40$.
This contradicts the fact that 42 students are served. Therefore, the initial supposition is false, and at least 5 computers must be used by 3 or more students [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

**Direct Argument:**
Let $k$ be the number of computers used by 3 or more students. We want to show $k \geq 5$.
*   These $k$ computers serve at most $6k$ students (each serves at most 6).
*   The remaining $12-k$ computers serve at most 2 students each (by the problem statement, or if used by fewer than 3, then at most 2). So, they serve at most $2(12-k) = 24-2k$ students.
Total students served: $6k + (24-2k) = 4k + 24$.
Since 42 students are served, $4k + 24 \geq 42$.
Solving for $k$: $4k \geq 18 \implies k \geq 4.5$.
Since $k$ must be an integer, $k \geq 5$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

**Example: Points in a Unit Square**
Prove that if you randomly put 51 points inside a unit square, there are always 3 points that can be covered by a circle of radius $1/7$.
1.  Divide the unit square into 25 smaller squares of side $1/5$ each.
2.  Consider the 51 points as "pigeons" and the 25 smaller squares as "pigeonholes". By the Generalized PHP, since $51 > 2 \times 25 = 50$, at least one square must contain $2+1=3$ or more points [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1, cs1231s-tutorial-tut09ans-post-pdf#section-5].
3.  The smallest circle that covers a square of side $1/5$ has a radius equal to half its diagonal. Diagonal length is $\sqrt{(1/5)^2 + (1/5)^2} = \sqrt{2/25} = \sqrt{2}/5$. Radius is $\sqrt{2}/10$.
4.  $\sqrt{2}/10 \approx 0.1414$. Given radius is $1/7 \approx 0.1428$. Since $\sqrt{2}/10 < 1/7$ (or $\sqrt{1/50} < \sqrt{1/49}$), a circle of radius $1/7$ can cover any square of side $1/5$. Thus, the 3 points in that square are covered [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1, cs1231s-tutorial-tut09ans-post-pdf#section-5].

**Example: Sum to 15**
Given $S = \{3,4,5,6,7,8,9,10,11,12\}$. What is the smallest number of integers you must choose from $S$ such that two of them sum to 15?
1.  Partition $S$ into subsets where elements in each subset sum to 15:
    $\{\{3,12\}, \{4,11\}, \{5,10\}, \{6,9\}, \{7,8\}\}$.
2.  These subsets are the "pigeonholes" (5 pigeonholes). The integers chosen are the "pigeons".
3.  If you choose more than 5 integers (pigeons), then by PHP, at least two must come from the same subset (pigeonhole), meaning they sum to 15.
4.  Thus, the smallest number of integers you must choose is $5+1=6$ [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1].

**Example: Consecutive Numbered Houses**
In a city, houses are randomly assigned distinct numbers between 1 and 50 inclusive. What is the minimum number of houses to ensure there are 5 consecutively numbered houses?
1.  Define "pigeonholes" as groups of 4 non-consecutive house numbers. For example, houses $1-4$, $6-9$, $11-14$, etc. This creates 10 such groups within 1 to 50: $(1-4), (6-9), \dots, (46-50)$.
2.  If we select 4 houses from each group, we can select $10 \times 4 = 40$ houses without any 5 being consecutive. For instance, $1,2,3,4, 6,7,8,9, \dots, 46,47,48,49$.
3.  If we add one more house (pigeon), making it 41 houses, then by the generalized PHP, this 41st house must complete a set of 5 consecutive houses within one of the groups [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1].
4.  Thus, the minimum number of houses is $10 \times 4 + 1 = 41$ [source:cs1231s-cs1231s-extra-tutorials-tutorial-9-tut09-enzio-pdf#section-1].

---
_Next week's lectures will cover more counting topics, including Combinations, Pascal's Formula, the Binomial Theorem, and Probability topics like Expected Value and Conditional Probability_ [source:cs1231s-cs1231s-extra-lecture-slides-lecture10-counting1-pdf#section-4].

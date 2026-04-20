---
page_id: "y1s1-cs1231s-lecture-11-expected-conditional-probability"
title: "Lecture 11: Expected Value and Conditional Probability"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Covers calculating expected value, permutations with indistinguishable objects, combinations with repetition, and advanced probability concepts including conditional probability and Bayes' Theorem."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-2"
  - "cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-1"
  - "cs1231s-cs1231s-extra-tutorials-tutorial-10-tut10-enzio-pdf#section-1"
  - "cs1231s-tutorial-tut10ans-post-pdf#section-4"
  - "cs1231s-tutorial-tut10qns-pdf#section-1"
topics:
  - "choose"
  - "repetition"
  - "probability"
  - "formula"
  - "elements"
  - "counting"
  - "binomial"
  - "events"
  - "set"
  - "theorem"
source_count: 5
lecture_number: 11
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 11: Expected Value and Conditional Probability

This lecture covers advanced counting techniques, including combinations with repetition and permutations of indistinguishable objects, and introduces fundamental concepts in probability, such as expected value, conditional probability, Bayes' Theorem, and independent events [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-1]. The content is primarily based on Chapter 9 of Epp's textbook [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-2].

## 9.5 Counting Subsets of a Set: Combinations

An *r-combination* is an unordered subset of *r* elements chosen from a set of *n* elements [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-3]. Unlike *r-permutations*, the order of selection does not matter for *r-combinations* [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-6].

The number of *r-combinations* of a set of *n* elements is denoted as $\binom{n}{r}$, read as "n choose r" [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-3]. Other common notations include $C(n,r)$, $nCr$, $C_{n,r}$, or $^{n}C_r$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-3].

The formula for calculating the number of *r-combinations* is given by:
$$ \binom{n}{r} = \frac{P(n,r)}{r!} = \frac{n!}{r!(n-r)!} $$
where $n$ and $r$ are non-negative integers with $r \le n$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-10, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-3].

**Example: Teams with Members of Two Types**
Consider a group of 12 people consisting of 5 men and 7 women.
1.  **How many 5-person teams can be chosen that consist of 3 men and 2 women?**
    This can be solved as a two-step process:
    *   Choose 3 men from 5: $\binom{5}{3}$
    *   Choose 2 women from 7: $\binom{7}{2}$
    Using the product rule, the total number of teams is $\binom{5}{3} \times \binom{7}{2} = 10 \times 21 = 210$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-11].

2.  **How many 5-person teams contain at least one man?**
    This can be found using the difference rule.
    *   Total number of 5-person teams from 12 people: $\binom{12}{5} = 792$
    *   Number of 5-person teams with no men (i.e., all women): $\binom{7}{5} = 21$
    *   Number of teams with at least one man = Total teams - Teams with no men = $792 - 21 = 771$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-12].

3.  **How many 5-person teams contain at most one man?**
    This means teams with 0 men or 1 man.
    *   Teams with 0 men: $\binom{5}{0} \times \binom{7}{5} = 1 \times 21 = 21$
    *   Teams with 1 man: $\binom{5}{1} \times \binom{7}{4} = 5 \times 35 = 175$
    *   Total teams with at most one man = $21 + 175 = 196$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-13].

### Permutations with Indistinguishable Objects

When dealing with a collection of *n* objects where some are indistinguishable, the number of distinct permutations can be calculated. Suppose there are $n_1$ objects of type 1, $n_2$ objects of type 2, ..., $n_k$ objects of type *k*, where $n_1 + n_2 + \dots + n_k = n$.
The number of distinguishable permutations is given by:
$$ \frac{n!}{n_1! n_2! n_3! \dots n_k!} $$
[source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-15, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-4].

**Example: "MISSISSIPPI"**
To order the letters in the word "MISSISSIPPI":
*   Total letters (n) = 11
*   M: 1 ($n_M = 1$)
*   I: 4 ($n_I = 4$)
*   S: 4 ($n_S = 4$)
*   P: 2 ($n_P = 2$)
The number of distinguishable orderings is $\frac{11!}{1!4!4!2!} = 34650$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-14].

## 9.6 r-Combinations with Repetition Allowed

An *r-combination with repetition allowed*, also known as a *multiset* of size *r*, is an unordered selection of *r* elements from a set of *n* elements where repetition is permitted [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-18, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-5].

The number of *r-combinations* with repetition allowed from a set of *n* elements is given by:
$$ \binom{r+n-1}{r} $$
This is equivalent to the number of ways to select *r* objects from *n* categories with repetitions allowed [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-21, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-5]. This formula is useful for problems like distributing indistinguishable items into distinguishable bins.

**Example: Solutions to Equations**
Find the number of solutions to the equation $x_1 + x_2 + x_3 = 20$.
*   **Each $x_i$ is a non-negative integer:**
    Here, $n=3$ (number of variables/categories) and $r=20$ (the sum).
    The number of solutions is $\binom{20+3-1}{20} = \binom{22}{20} = \frac{22 \times 21}{2} = 231$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-22].

### Summary of Counting Formulas

The choice of formula depends on whether order matters and whether repetition is allowed [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-23, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-6].
|                       | Order Matters | Order Does Not Matter |
| :-------------------- | :------------ | :-------------------- |
| **Repetition Allowed**    | $n^k$         | $\binom{k+n-1}{k}$   |
| **Repetition Not Allowed** | $P(n,k)$      | $\binom{n}{k}$       |

## 9.7 Pascal's Formula and the Binomial Theorem

### Pascal's Formula

Pascal's Formula states a relationship between binomial coefficients:
$$ \binom{n+1}{r} = \binom{n}{r-1} + \binom{n}{r} $$
for positive integers $n$ and $r$ with $r \le n$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-25, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-7]. This formula can be proven algebraically (using the definition of combinations) or combinatorially (by partitioning a set into those that contain a specific element and those that do not) [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-26].
This formula is the basis for constructing Pascal's Triangle, where each number is the sum of the two numbers directly above it [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-25].

### The Binomial Theorem

A *binomial* is a sum of two terms, like $a+b$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-28, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-7]. The Binomial Theorem provides a formula for expanding powers of a binomial $(a+b)^n$:
$$ (a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k $$
$$ = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b^1 + \binom{n}{2}a^{n-2}b^2 + \dots + \binom{n}{n-1}a^1b^{n-1} + \binom{n}{n}b^n $$
The coefficients $\binom{n}{k}$ are known as *binomial coefficients* [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-28, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-7].

**Example: Finding a term independent of x**
To find the term independent of $x$ in the expansion of $(2x^2 + \frac{1}{x})^9$:
The general term is $\binom{9}{r} (2x^2)^{9-r} (\frac{1}{x})^r = \binom{9}{r} 2^{9-r} x^{18-2r} x^{-r} = \binom{9}{r} 2^{9-r} x^{18-3r}$.
For the term to be independent of $x$, the exponent of $x$ must be 0:
$18 - 3r = 0 \Rightarrow r = 6$.
The term is $\binom{9}{6} 2^{9-6} = 84 \times 2^3 = 84 \times 8 = 672$ [source:cs1231s-tutorial-tut10ans-post-pdf#section-1, cs1231s-tutorial-tut10qns-pdf#section-2].

### Combinatorial Proofs

A *combinatorial proof* (or *combinatorial argument*) uses counting principles to prove identities [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-34]. Two common types are:
*   **Bijective proof:** Demonstrating a one-to-one correspondence (bijection) between elements of two sets to show they have the same cardinality.
*   **Proof by double counting:** Counting the elements of a set in two different ways to arrive at two expressions that must be equal.

**Example: $\binom{n}{k} = \binom{n}{n-k}$**
This identity can be proven combinatorially by considering a set of $n$ pupils from which $k$ are to be selected for an audition.
1.  **Approach 1:** Choose $k$ pupils to go to the audition. The number of ways is $\binom{n}{k}$.
2.  **Approach 2:** Choose $n-k$ pupils *not* to go to the audition. The remaining $k$ pupils will go. The number of ways is $\binom{n}{n-k}$.
Since both approaches count the same set of outcomes, the two quantities must be equal [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-35].

## 9.8 Probability Axioms and Expected Value

### Probability Axioms

A *sample space* is the set of all possible outcomes of a random process or experiment, and an *event* is a subset of the sample space [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-38, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-8]. A *probability function* $P$ assigns real numbers to events, satisfying the following axioms for any events $A$ and $B$:
1.  $0 \le P(A) \le 1$ (Probabilities are between 0 and 1) [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-38, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-8].
2.  $P(\emptyset) = 0$ (The probability of an impossible event is 0) and $P(S) = 1$ (The probability of the sample space is 1) [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-38, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-8].
3.  If $A$ and $B$ are *disjoint events* ($A \cap B = \emptyset$), then $P(A \cup B) = P(A) + P(B)$ (The probability of their union is the sum of their individual probabilities) [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-38, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-8].

### Probability of the Complement of an Event

For any event $A$ in a sample space $S$, the probability of its complement, $P(\bar{A})$, is given by:
$$ P(\bar{A}) = 1 - P(A) $$
[source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-39, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-8]. For example, if the probability of rolling a 3 on a fair die is $1/6$, the probability of *not* rolling a 3 is $1 - 1/6 = 5/6$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-39].

### Probability of a General Union of Two Events

For any two events $A$ and $B$ in a sample space $S$, the probability of their union is:
$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$
[source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-40, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-8]. This is also known as the Inclusion-Exclusion Principle for two events.

### Expected Value

The *expected value* of an experiment or random process, with possible outcomes $a_1, a_2, \dots, a_n$ occurring with probabilities $p_1, p_2, \dots, p_n$ respectively, is defined as:
$$ E = \sum_{k=1}^{n} a_k p_k = a_1 p_1 + a_2 p_2 + a_3 p_3 + \dots + a_n p_n $$
[source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-42, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-9]. The expected value represents the average outcome if the experiment were repeated many times.

**Example: Expected Value of a Die**
For a fair die, each outcome (1, 2, 3, 4, 5, 6) has a probability of $1/6$.
The expected value is $E = \frac{1}{6}(1) + \frac{1}{6}(2) + \frac{1}{6}(3) + \frac{1}{6}(4) + \frac{1}{6}(5) + \frac{1}{6}(6) = 3.5$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-43].

**Example: Expected Value of a Lottery Ticket**
Suppose 500,000 lottery tickets are sold for $5 each.
*   Grand prize: $1,000,000 (net gain: $999,995)
*   10 second prizes: $1,000 each (net gain: $995)
*   1,000 third prizes: $500 each (net gain: $495)
*   10,000 fourth prizes: $10 each (net gain: $5)
*   Remaining 488,989 tickets: $0 prize (net gain: $-5)
Each ticket has a probability of $1/500000$ of being selected for any specific prize or loss [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-44, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-45].
The expected value is calculated by summing the products of net gain and probability for all outcomes.
$E = \frac{1}{500000} \sum_{k=1}^{500000} a_k = \frac{1}{500000} (999995 + 10 \times 995 + 1000 \times 495 + 10000 \times 5 + 488989 \times (-5)) = \frac{1}{500000} (999995 + 9950 + 495000 + 50000 - 2444945) = \frac{1}{500000} (-880000) = -1.76$
The expected value of a ticket is -$1.76$, meaning on average, a player loses $1.76 per ticket [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-46].

### Linearity of Expectation

The expected value of the sum of random variables is equal to the sum of their individual expected values, regardless of whether the variables are independent or dependent [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-47, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-9].
*   For random variables $X$ and $Y$: $E[X+Y] = E[X] + E[Y]$
*   More generally, for random variables $X_1, \dots, X_n$ and constants $c_1, \dots, c_n$: $E[\sum_{i=1}^{n} c_i X_i] = \sum_{i=1}^{n} (c_i E[X_i])$
[source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-47, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-9].

**Example: Expected Value of Sum of Two Dice**
The expected value of rolling a single fair die is $3.5$.
Using linearity of expectation, the expected value of the sum of two fair dice is $E[\text{Die1} + \text{Die2}] = E[\text{Die1}] + E[\text{Die2}] = 3.5 + 3.5 = 7$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-48].

## 9.9 Conditional Probability, Bayes' Formula, and Independent Events

### Conditional Probability

The *conditional probability* of an event $B$ occurring given that event $A$ has already occurred, denoted $P(B|A)$, is defined as:
$$ P(B|A) = \frac{P(A \cap B)}{P(A)} $$
provided that $P(A) \ne 0$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-52, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-10].
This formula can be rearranged to find the probability of the intersection of two events:
$$ P(A \cap B) = P(B|A) \cdot P(A) $$
[source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-52, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-10].

**Example: Urn Problem**
An urn contains 5 blue and 7 gray balls. Two balls are chosen at random, one after the other, without replacement.
Let $B_1$ be the event that the first ball is blue, and $B_2$ be the event that the second ball is blue.
*   $P(B_1) = \frac{5}{12}$
*   $P(\bar{B_1}) = \frac{7}{12}$
*   $P(B_2|B_1) = \frac{4}{11}$ (If the first was blue, 4 blue balls left out of 11)
*   $P(\bar{B_2}|B_1) = \frac{7}{11}$
*   $P(B_2|\bar{B_1}) = \frac{5}{11}$ (If the first was gray, 5 blue balls left out of 11)
*   $P(\bar{B_2}|\bar{B_1}) = \frac{6}{11}$

Using $P(A \cap B) = P(B|A) \cdot P(A)$:
*   $P(B_1 \cap B_2)$ (both blue) = $P(B_2|B_1) \cdot P(B_1) = \frac{4}{11} \cdot \frac{5}{12} = \frac{20}{132}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-56].
*   $P(B_1 \cap \bar{B_2})$ (first blue, second not) = $P(\bar{B_2}|B_1) \cdot P(B_1) = \frac{7}{11} \cdot \frac{5}{12} = \frac{35}{132}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-56].
*   $P(\bar{B_1} \cap B_2)$ (first not blue, second blue) = $P(B_2|\bar{B_1}) \cdot P(\bar{B_1}) = \frac{5}{11} \cdot \frac{7}{12} = \frac{35}{132}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-56].
*   $P(\bar{B_1} \cap \bar{B_2})$ (neither blue) = $P(\bar{B_2}|\bar{B_1}) \cdot P(\bar{B_1}) = \frac{6}{11} \cdot \frac{7}{12} = \frac{42}{132}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-56].

**What is the probability that the 2nd ball is blue?**
$P(B_2) = P((B_2 \cap B_1) \cup (B_2 \cap \bar{B_1})) = P(B_2 \cap B_1) + P(B_2 \cap \bar{B_1})$ (since $B_2 \cap B_1$ and $B_2 \cap \bar{B_1}$ are disjoint events).
$P(B_2) = \frac{20}{132} + \frac{35}{132} = \frac{55}{132} = \frac{5}{12}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-58].

**Expected value of the number of blue balls:**
Let $X$ be the number of blue balls.
*   $P(X=0) = P(\text{no blue balls}) = P(\bar{B_1} \cap \bar{B_2}) = \frac{42}{132} = \frac{7}{22}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-60, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-61].
*   $P(X=1) = P(\text{one blue ball}) = P(B_1 \cap \bar{B_2}) + P(\bar{B_1} \cap B_2) = \frac{35}{132} + \frac{35}{132} = \frac{70}{132}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-60, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-61].
*   $P(X=2) = P(\text{two blue balls}) = P(B_1 \cap B_2) = \frac{20}{132}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-60, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-61].
Expected value $E[X] = 0 \cdot P(X=0) + 1 \cdot P(X=1) + 2 \cdot P(X=2) = 0 \cdot \frac{42}{132} + 1 \cdot \frac{70}{132} + 2 \cdot \frac{20}{132} = \frac{70+40}{132} = \frac{110}{132} = \frac{55}{66} \approx 0.833$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-61].

### Bayes' Theorem

Bayes' Theorem provides a way to update the probability of an event based on new evidence. Suppose a sample space $S$ is partitioned into $n$ mutually disjoint events $B_1, B_2, \dots, B_n$. If $A$ is an event in $S$ with non-zero probability, then for any $B_k$ (where $1 \le k \le n$):
$$ P(B_k|A) = \frac{P(A|B_k) \cdot P(B_k)}{P(A|B_1) \cdot P(B_1) + P(A|B_2) \cdot P(B_2) + \dots + P(A|B_n) \cdot P(B_n)} $$
[source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-65, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-10].

**Example: Medical Test**
Consider a medical test for a disease found in 5 out of 1,000 people ($P(B_1) = 0.005$, where $B_1$ is having the disease). The false positive rate is 3% and the false negative rate is 1%.
*   $B_1$: person has the disease. $P(B_1) = 0.005$.
*   $B_2$: person does not have the disease. $P(B_2) = 1 - P(B_1) = 0.995$.
*   $A$: person tests positive.
*   $\bar{A}$: person tests negative.

Given:
*   Sensitivity (true positive rate): $P(A|B_1) = 1 - \text{false negative rate} = 1 - 0.01 = 0.99$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-68].
*   False positive rate: $P(A|B_2) = 0.03$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-68].
*   True negative rate: $P(\bar{A}|B_2) = 1 - \text{false positive rate} = 1 - 0.03 = 0.97$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-67].
*   False negative rate: $P(\bar{A}|B_1) = 0.01$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-67].

1.  **Probability that a randomly chosen person who tests positive actually has the disease, $P(B_1|A)$:**
    $$ P(B_1|A) = \frac{P(A|B_1) \cdot P(B_1)}{P(A|B_1) \cdot P(B_1) + P(A|B_2) \cdot P(B_2)} $$
    $$ P(B_1|A) = \frac{(0.99)(0.005)}{(0.99)(0.005) + (0.03)(0.995)} = \frac{0.00495}{0.00495 + 0.02985} = \frac{0.00495}{0.0348} \approx 0.1422 \approx 14.2\% $$
    Thus, a person with a positive test result has the disease with approximately 14.2% probability [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-69].

2.  **Probability that a randomly chosen person who tests negative does not indeed have the disease, $P(B_2|\bar{A})$:**
    $$ P(B_2|\bar{A}) = \frac{P(\bar{A}|B_2) \cdot P(B_2)}{P(\bar{A}|B_1) \cdot P(B_1) + P(\bar{A}|B_2) \cdot P(B_2)} $$
    $$ P(B_2|\bar{A}) = \frac{(0.97)(0.995)}{(0.01)(0.005) + (0.97)(0.995)} = \frac{0.96515}{0.00005 + 0.96515} = \frac{0.96515}{0.9652} \approx 0.999948 \approx 99.995\% $$
    Thus, a person with a negative test result does not have the disease with approximately 99.995% probability [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-70].

### Independent Events

Two events $A$ and $B$ in a sample space $S$ are *independent* if and only if:
$$ P(A \cap B) = P(A) \cdot P(B) $$
[source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-72, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-11].
If $P(A) \ne 0$, then independence also implies $P(B|A) = P(B)$. Similarly, if $P(B) \ne 0$, then $P(A|B) = P(A)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-71].

**Pairwise Independent vs. Mutually Independent**
For three or more events, there's a distinction:
*   **Pairwise independent:** Events $A, B, C$ are pairwise independent if $P(A \cap B) = P(A)P(B)$, $P(A \cap C) = P(A)P(C)$, and $P(B \cap C) = P(B)P(C)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-77, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-11].
*   **Mutually independent:** Events $A, B, C$ are mutually independent if they are pairwise independent AND $P(A \cap B \cap C) = P(A)P(B)P(C)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-78, cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-summary-pdf#section-11].
In general, for $n \ge 2$ events $A_1, \dots, A_n$ to be mutually independent, the probability of the intersection of *any* subset of these events must equal the product of the probabilities of the events in that subset [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-79].

**Example: Tossing a Loaded Coin Ten Times**
A loaded coin has $P(H) = 0.6$ and $P(T) = 0.4$. The tosses are mutually independent.
1.  **Probability of obtaining eight heads:**
    The probability of any specific sequence of 8 heads and 2 tails (e.g., HHHHHHHHTT) is $(0.6)^8 (0.4)^2$ due to mutual independence [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-81].
    The number of such sequences is $\binom{10}{8}$ (choosing 8 positions for heads out of 10 tosses).
    So, $P(\text{eight heads}) = \binom{10}{8} (0.6)^8 (0.4)^2$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-82].

2.  **Probability of obtaining at least eight heads:**
    This means 8 heads, 9 heads, or 10 heads.
    *   $P(\text{eight heads}) = \binom{10}{8} (0.6)^8 (0.4)^2$
    *   $P(\text{nine heads}) = \binom{10}{9} (0.6)^9 (0.4)^1$
    *   $P(\text{ten heads}) = \binom{10}{10} (0.6)^{10} (0.4)^0$
    $P(\text{at least 8 heads}) = \binom{10}{8} (0.6)^8 (0.4)^2 + \binom{10}{9} (0.6)^9 (0.4)^1 + \binom{10}{10} (0.6)^{10} \approx 0.167 = 16.7\%$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-83].
    Probabilities of the form $\binom{n}{k} p^k (1-p)^{n-k}$ are called *binomial probabilities* [source:cs1231s-cs1231s-extra-lecture-slides-lecture11-counting2-pdf#section-83].

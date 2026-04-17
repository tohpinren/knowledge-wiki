---
page_id: "y1s1-cs1231s-lecture-07-strong-induction-recursion"
title: "Lecture 07: Strong Induction and Recursive Definitions"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Introduces the principle of Strong Mathematical Induction and methods for defining sequences, sets, and structures recursively."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-2"
  - "cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-1"
  - "cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-2"
  - "cs1231s-tutorial-tut07ans-post-pdf#section-1"
  - "cs1231s-cs1231s-extra-tutorials-tutorial-5-tut05-enzio-pdf#section-3"
topics:
  - "induction"
  - "mathematical"
  - "principle"
  - "strong"
  - "true"
  - "can"
  - "step"
  - "all"
  - "wff"
  - "clause"
source_count: 5
lecture_number: 7
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 07: Strong Induction and Recursive Definitions

This page introduces the principles of Strong Mathematical Induction and various methods for defining mathematical objects recursively, including sequences, sets, and well-formed formulas, along with the proof technique of structural induction.

---

## Introduction to Induction

Mathematical Induction (MI) is a powerful deductive proof method primarily used for propositions involving natural numbers (n ≥ 0 or n ≥ m for some integer m) [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-1]. It differs from non-deductive forms of induction and is fundamental to characterizing natural numbers and recursively defined objects [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-2].

The **Sorites Paradox** highlights a logical challenge that MI addresses: if one grain of sand doesn't make a heap, and if `n` grains don't make a heap, then `n+1` grains also don't. By the Principle of Mathematical Induction, this would imply that no number of grains can make a heap, illustrating a flawed premise or definition [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-1].

## Principle of Mathematical Induction (MI)

To prove that a proposition $P(n)$ is true for all integers $n \geq m$ (where $m$ is some integer), it is sufficient to demonstrate two steps [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-1, cs1231s-cs1231s-extra-tutorials-tutorial-5-tut05-enzio-pdf#section-1]:

1.  **Base Step:** Show that $P(m)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-1].
2.  **Induction Step:** Show that for all integers $k \geq m$, the implication $P(k) \Rightarrow P(k+1)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-1].

This principle is justified by a series of Modus Ponens applications: if $P(m)$ is true (base step) and $P(k) \Rightarrow P(k+1)$ is true for all $k \geq m$, then $P(m) \Rightarrow P(m+1)$, which means $P(m+1)$ is true. This continues indefinitely, establishing the truth of $P(n)$ for all $n \geq m$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-1].

### Terminology
*   **Induction Hypothesis:** The assumption that $P(k)$ is true in the induction step [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-1].
*   **Induction on `n`:** Refers to `n` as the active variable in the induction proof [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-1].

### Examples of Proofs by Mathematical Induction

1.  **Sum of First `n` Natural Numbers** [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-1]
    Prove: $1 + 2 + \dots + n = \frac{1}{2}n(n+1)$ for all $n \in \mathbb{Z}_{\geq 1}$.
    *   **Base Step (P(1)):** $1 = \frac{1}{2}(1)(1+1) = 1$. True [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-5].
    *   **Induction Hypothesis:** Assume $P(k)$ is true for some $k \in \mathbb{Z}_{\geq 1}$, i.e., $1 + 2 + \dots + k = \frac{1}{2}k(k+1)$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-5].
    *   **Induction Step (P(k+1)):** Show $1 + 2 + \dots + (k+1) = \frac{1}{2}(k+1)((k+1)+1)$.
        $1 + 2 + \dots + k + (k+1) = \frac{1}{2}k(k+1) + (k+1)$ (by induction hypothesis)
        $= (k+1)(\frac{1}{2}k + 1) = (k+1)(\frac{k+2}{2}) = \frac{1}{2}(k+1)(k+2) = \frac{1}{2}(k+1)((k+1)+1)$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-5].
    Thus, $P(n)$ is true for all $n \in \mathbb{Z}_{\geq 1}$ by MI.

2.  **Sum of Squares Formula** [source:cs1231s-tutorial-tut07ans-post-pdf#section-1]
    Prove: $1^2 + 2^2 + \dots + n^2 = \frac{1}{6}n(n+1)(2n+1)$ for all $n \in \mathbb{Z}^+$.
    *   **Base Step (P(1)):** $1^2 = 1$. $\frac{1}{6}(1)(1+1)(2(1)+1) = \frac{1}{6}(1)(2)(3) = 1$. True [source:cs1231s-tutorial-tut07ans-post-pdf#section-1].
    *   **Induction Hypothesis:** Assume $P(k)$ is true for some $k \in \mathbb{Z}^+$, i.e., $1^2 + \dots + k^2 = \frac{1}{6}k(k+1)(2k+1)$ [source:cs1231s-tutorial-tut07ans-post-pdf#section-1].
    *   **Induction Step (P(k+1)):** Show $1^2 + \dots + (k+1)^2 = \frac{1}{6}(k+1)(k+2)(2k+3)$.
        $1^2 + \dots + k^2 + (k+1)^2 = \frac{1}{6}k(k+1)(2k+1) + (k+1)^2$ (by induction hypothesis)
        $= (k+1)[\frac{1}{6}k(2k+1) + (k+1)]$
        $= (k+1)[\frac{2k^2+k+6k+6}{6}] = (k+1)[\frac{2k^2+7k+6}{6}]$
        $= (k+1)\frac{(k+2)(2k+3)}{6} = \frac{1}{6}(k+1)(k+2)(2k+3)$ [source:cs1231s-tutorial-tut07ans-post-pdf#section-1].
    Thus, $P(n)$ is true for all $n \in \mathbb{Z}^+$ by MI.

3.  **Inequality: $n! > 2^n$** [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-2]
    Prove: $n! > 2^n$ for all $n \in \mathbb{Z}_{\geq 4}$.
    *   **Base Step (P(4)):** $4! = 24$. $2^4 = 16$. Since $24 > 16$, $P(4)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-6].
    *   **Induction Hypothesis:** Assume $P(k)$ is true for some $k \in \mathbb{Z}_{\geq 4}$, i.e., $k! > 2^k$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-6].
    *   **Induction Step (P(k+1)):** Show $(k+1)! > 2^{k+1}$.
        $(k+1)! = (k+1) \times k!$ (by definition of factorial)
        $> (k+1) \times 2^k$ (by induction hypothesis)
        Since $k \geq 4$, then $k+1 \geq 5 > 2$.
        So, $(k+1) \times 2^k > 2 \times 2^k = 2^{k+1}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-6].
    Thus, $P(k+1)$ is true. Hence $P(n)$ is true for all $n \in \mathbb{Z}_{\geq 4}$ by MI.

4.  **Covering a Checkerboard with L-trominos** [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-2]
    Prove: For all $n \in \mathbb{Z}_{\geq 1}$, if one square is removed from a $2^n \times 2^n$ checkerboard, the remaining squares can be covered by L-trominos.
    *   **Base Step (P(1)):** A $2^1 \times 2^1$ checkerboard (a $2 \times 2$ board) with one square removed is itself an L-tromino. True [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
    *   **Induction Hypothesis:** Assume $P(k)$ is true for some $k \in \mathbb{Z}_{\geq 1}$, i.e., a $2^k \times 2^k$ checkerboard with one square removed can be covered by L-trominos [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
    *   **Induction Step (P(k+1)):** Consider a $2^{k+1} \times 2^{k+1}$ checkerboard $B$ with one square removed. Divide $B$ into four $2^k \times 2^k$ quadrants. Let $Q$ be the quadrant containing the removed square. Place one L-tromino at the center of $B$ such that it covers one square from each quadrant *other than* $Q$. This leaves four $2^k \times 2^k$ checkerboards, each with one square removed. By the induction hypothesis, each of these four smaller checkerboards can be covered by L-trominos. Therefore, the entire $2^{k+1} \times 2^{k+1}$ board with one square removed can be covered by L-trominos [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
    Thus, $P(n)$ is true for all $n \in \mathbb{Z}_{\geq 1}$ by MI.

5.  **The "All Participants Have the Same Birthday" Paradox** [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-2]
    This example illustrates a common fallacy in inductive proofs. The proposition $P(n)$ states: "If a Zoom meeting has exactly $n$ participants, then all its participants have the same birthday."
    *   **Base Step (P(1)):** If there is 1 participant, they trivially have the same birthday as themselves. True [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8].
    *   **Flawed Induction Step:** Assume $P(k)$ is true. Consider a meeting with $k+1$ participants. Pick two participants, `a` and `b`.
        1.  Ask `a` to leave. There are $k$ participants left. By $P(k)$, the remaining $k$ participants (including `b`) all have the same birthday.
        2.  Ask `a` to rejoin, and `b` to leave. There are again $k$ participants left. By $P(k)$, these $k$ participants (including `a`) all have the same birthday.
        3.  The participants who stayed throughout have the same birthday as `a` and `b`. Therefore, `a` and `b` must have the same birthday.
    The flaw lies when $k=1$. In this case, `a` and `b` are the only participants. When `a` leaves, `b` is the only one left (trivially shares a birthday). When `b` leaves, `a` is the only one left. But the argument that "participants who stayed throughout" share a birthday with both `a` and `b` breaks down. There are no "participants who stayed throughout" other than `a` and `b` themselves. The induction step $P(k) \Rightarrow P(k+1)$ fails for $k=1$ because the two groups of $k$ participants (excluding `a`, and excluding `b`) do not necessarily overlap for the argument to hold. If $k=1$, the intersection of these two groups is empty, so there are no "remaining participants" to link `a` and `b`'s birthdays [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8].

## Principle of Strong Mathematical Induction (Strong MI)

Sometimes, the assumption $P(k)$ alone is insufficient to prove $P(k+1)$. For instance, in an attempt to prove an upper bound for the Fibonacci sequence $F_{n+1} \le (7/4)^n$, the proof using standard MI stalls because $F_{k+2} = F_{k+1} + F_k$ requires knowledge of $F_k$ in addition to $F_{k+1}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-6]. This is where Strong MI is useful.

To prove that a proposition $P(n)$ is true for all integers $n \geq m$ (where $m$ is some integer), it is sufficient to demonstrate two steps [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-3, cs1231s-cs1231s-extra-tutorials-tutorial-5-tut05-enzio-pdf#section-1]:

1.  **Base Step:** Show that $P(m), P(m+1), \dots, P(m')$ are true for a sufficient number of initial values [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7]. Often this means proving for $P(0)$ and $P(1)$ when $m=0$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
2.  **Induction Step:** Show that for all integers $k \geq m'$, if $P(m) \land P(m+1) \land \dots \land P(k)$ are all true (the strong induction hypothesis), then $P(k+1)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-3].

**Justification:** This principle is also justified by a series of Modus Ponens applications. If the base cases $P(m), \dots, P(m')$ are true, then for $k=m'$, the strong induction hypothesis $P(m) \land \dots \land P(m')$ allows us to deduce $P(m'+1)$. This process propagates the truth for all subsequent integers [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-3].

**Remark:** Given the same proposition $P(n)$, Strong MI is generally more likely to succeed than standard MI because it leverages more information in the induction hypothesis [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].

### Example: Upper Bound for Fibonacci Sequence (Revisited)

The Fibonacci sequence is defined as $F_0 = 0, F_1 = 1$, and $F_{n+2} = F_{n+1} + F_n$ for $n \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-3].
Prove: $F_{n+1} \leq (7/4)^n$ for every $n \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-4].

*   **Base Steps (P(0) and P(1)):**
    *   $P(0)$: $F_{0+1} = F_1 = 1$. $(7/4)^0 = 1$. So $1 \leq 1$. True [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
    *   $P(1)$: $F_{1+1} = F_2 = F_1 + F_0 = 1+0=1$. $(7/4)^1 = 7/4$. So $1 \leq 7/4$. True [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
*   **Strong Induction Hypothesis:** Assume $P(i)$ is true for all $i \in \{0, 1, \dots, k+1\}$, i.e., $F_{i+1} \leq (7/4)^i$ for some $k \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
*   **Induction Step (P(k+2)):** Show $F_{(k+2)+1} \leq (7/4)^{k+2}$.
    $F_{(k+2)+1} = F_{k+3} = F_{k+2} + F_{k+1}$ (by definition of Fibonacci) [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
    Using the induction hypothesis:
    $F_{k+2} \leq (7/4)^{k+1}$ (from $P(k+1)$ being true)
    $F_{k+1} \leq (7/4)^k$ (from $P(k)$ being true)
    So, $F_{k+3} \leq (7/4)^{k+1} + (7/4)^k$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
    Factor out $(7/4)^k$:
    $F_{k+3} \leq (7/4)^k((7/4) + 1) = (7/4)^k(11/4)$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
    Since $11/4 < (7/4)^2 = 49/16$ (because $44/16 < 49/16$), we have:
    $F_{k+3} \leq (7/4)^k(11/4) < (7/4)^k(49/16) = (7/4)^k(7/4)^2 = (7/4)^{k+2}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-7].
    Thus, $P(k+2)$ is true. Hence $P(n)$ is true for all $n \in \mathbb{Z}_{\geq 0}$ by Strong MI.

### Alternative Formulation of Strong MI
An alternative formulation states that to prove $\forall n \in \mathbb{Z}_{\geq 0} P(n)$ is true, it suffices to show that $\forall l \in \mathbb{Z}_{\geq 0} ((\forall i \in \mathbb{Z}_{\geq 0} (i < l \Rightarrow P(i))) \Rightarrow P(l))$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-4]. This formulation implicitly covers the base cases and the induction step.

## Well-Ordering Principle

The **Well-Ordering Principle** states that every nonempty subset of the set of non-negative integers ($\mathbb{Z}_{\geq 0}$) has a smallest element [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-4, cs1231s-cs1231s-extra-tutorials-tutorial-5-tut05-enzio-pdf#section-1].

### Examples
*   The set $S = \{x \in \mathbb{Z}_{\geq 0} : 0 < x < 5\}$ has a smallest element, which is 1 [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8].
*   The set $S' = \{x \in \mathbb{Q}_{\geq 0} : 0 < x < 5\}$ (non-negative rational numbers) does *not* have a smallest element, because for any $x \in S'$, $x/2$ is also in $S'$ and $x/2 < x$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-5]. This highlights that the Well-Ordering Principle applies specifically to subsets of integers.

### Proof of the Well-Ordering Principle
The Well-Ordering Principle can be proven using Strong Mathematical Induction.
Let $S$ be a nonempty subset of $\mathbb{Z}_{\geq 0}$ that has no smallest element. We want to show that this leads to a contradiction, implying that such a set $S$ cannot exist.
Let $P(n)$ be the proposition "$n \notin S$".
*   **Base Step (P(0)):** Assume $0 \in S$. Since $S \subseteq \mathbb{Z}_{\geq 0}$, $0$ would be the smallest element of $S$. This contradicts our initial assumption that $S$ has no smallest element. Therefore, $0 \notin S$, and $P(0)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8].
*   **Strong Induction Hypothesis:** Assume $P(i)$ is true for all $i \in \{0, 1, \dots, k\}$, meaning $0, 1, \dots, k \notin S$ for some $k \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8].
*   **Induction Step (P(k+1)):** Assume $k+1 \in S$. By the strong induction hypothesis, since $0, 1, \dots, k \notin S$, $k+1$ would be the smallest element of $S$. This again contradicts our initial assumption that $S$ has no smallest element. Therefore, $k+1 \notin S$, and $P(k+1)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8].
Since $P(n)$ is true for all $n \in \mathbb{Z}_{\geq 0}$, it means no element of $\mathbb{Z}_{\geq 0}$ is in $S$, so $S$ must be empty. This contradicts the initial assumption that $S$ is nonempty. Hence, every nonempty subset of $\mathbb{Z}_{\geq 0}$ must have a smallest element [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8].

### The "Every Element of $\mathbb{Z}_{\geq 0}$ is Interesting" Paradox
This is a humorous illustration of the Well-Ordering Principle. Suppose there is an "uninteresting" non-negative integer. By the Well-Ordering Principle, there must be a *smallest* uninteresting non-negative integer. However, being the *smallest* uninteresting integer makes it highly interesting, creating a contradiction. This implies that no uninteresting non-negative integers can exist, and therefore, every non-negative integer is interesting [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-8].

## Recursion

Induction and recursion are fundamentally linked [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-2]. Recursive processes are natural and ubiquitous, forming a central concept in computations [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-2].

### Recursively Defined Sequences
A sequence $a_0, a_1, a_2, \dots$ is **recursively defined** if the definition of $a_n$ involves one or more preceding terms ($a_0, a_1, \dots, a_{n-1}$) for all but finitely many $n \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-5].

#### Examples of Recursively Defined Sequences
1.  **Factorial Sequence ($n!$)** [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-3]
    *   Base case: $0! = 1$
    *   Recursive step: $(n+1)! = (n+1) \times n!$ for $n \in \mathbb{Z}_{\geq 0}$
    This defines $1! = 1 \times 0! = 1$, $2! = 2 \times 1! = 2$, $3! = 3 \times 2! = 6$, and so on.

2.  **Fibonacci Sequence ($F_n$)** [source:cs1231s-cs1231s-extra-lecture-slides-7-1-indn-0-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-3]
    *   Base cases: $F_0 = 0$, $F_1 = 1$
    *   Recursive step: $F_{n+2} = F_{n+1} + F_n$ for $n \in \mathbb{Z}_{\geq 0}$
    This generates the sequence: $F_2 = 1+0=1$, $F_3 = 1+1=2$, $F_4 = 2+1=3$, etc.

3.  **Logistic Map** [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-4]
    *   Given $r \in [0,4]$ and $p_0 \in [0,1]$
    *   Recursive step: $p_{n+1} = r(p_n - p_n^2)$ for $n \in \mathbb{Z}_{\geq 0}$
    For example, if $r=3$ and $p_0=1/2$, then $p_1 = 3(1/2 - (1/2)^2) = 3(1/4) = 3/4$.

4.  **Collatz Conjecture** [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-4]
    *   Given $a_0 \in \mathbb{Z}^+$
    *   Recursive step: $a_{n+1} = \begin{cases} a_n/2 & \text{if } a_n \text{ is even} \\ 3a_n + 1 & \text{if } a_n \text{ is odd} \end{cases}$ for $n \in \mathbb{Z}_{\geq 0}$
    The conjecture states that this sequence eventually reaches 1 for any positive integer $a_0$. For $a_0=1$, the sequence is $1, 4, 2, 1, \dots$.

#### Well-definition of the Fibonacci Sequence (Proof Sketch)
To prove that there is a unique sequence satisfying the Fibonacci definition ($a_0=0, a_1=1, a_{n+2}=a_{n+1}+a_n$):
*   **Existence:** Use induction on $n$ to show that $a_n$ exists for every $n \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-5].
*   **Uniqueness:** Assume there are two such sequences, $b_n$ and $c_n$. Use induction on $n$ to show that $b_n = c_n$ for every $n \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-5].

### Recursively Defined Sets
A set can be defined recursively by providing:
1.  **Base Clauses:** Specifies initial elements of the set.
2.  **Recursion Clauses:** Provides rules to generate new elements from existing ones.
3.  **Minimality Clause:** States that the set contains only elements formed by applying the base and recursion clauses a finite number of times [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-7].

#### Examples of Recursively Defined Sets
1.  **The Set of Natural Numbers ($\mathbb{Z}_{\geq 0}$)** [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-5]
    *   **Base Clause:** $0 \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-7].
    *   **Recursion Clause:** If $x \in \mathbb{Z}_{\geq 0}$, then $x+1 \in \mathbb{Z}_{\geq 0}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-7].
    *   **Minimality Clause:** Membership for $\mathbb{Z}_{\geq 0}$ can only be demonstrated by finitely many successive applications of the above clauses [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-7].
    Note that clauses (1) and (2) are also true for rational numbers ($\mathbb{Q}_{\geq 0}$), but (3) is not, as there's no finite way to generate all rationals from 0 using only +1 [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-7].

2.  **The Set of Positive Even Integers ($2\mathbb{Z}_{\geq 1}$)** [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-8, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-5]
    *   **Base Clause:** $2 \in 2\mathbb{Z}_{\geq 1}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-8].
    *   **Recursion Clause:** If $x \in 2\mathbb{Z}_{\geq 1}$, then $x+2 \in 2\mathbb{Z}_{\geq 1}$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-8].
    *   **Minimality Clause:** Membership for $2\mathbb{Z}_{\geq 1}$ can only be demonstrated by finitely many successive applications of the above clauses [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-8].

3.  **General Set Definition Example** [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-9]
    Define a set $S$ recursively:
    *   **Base Clause:** $1 \in S$
    *   **Recursion Clause:** If $x \in S$, then $2x \in S$ and $3x \in S$
    *   **Minimality Clause:** Membership for $S$ can always be demonstrated by finitely many successive applications of clauses.
    To determine if numbers like 9, 10, 11, 12, 13 are in $S$:
    *   Start with $1 \in S$.
    *   $2 \times 1 = 2 \in S$, $3 \times 1 = 3 \in S$.
    *   From $2$: $2 \times 2 = 4 \in S$, $3 \times 2 = 6 \in S$.
    *   From $3$: $2 \times 3 = 6 \in S$ (already found), $3 \times 3 = 9 \in S$.
    *   From $4$: $2 \times 4 = 8 \in S$, $3 \times 4 = 12 \in S$.
    *   From $6$: $2 \times 6 = 12 \in S$ (already found), $3 \times 6 = 18 \in S$.
    Thus, 9 and 12 are in $S$. Numbers like 10, 11, 13 are not in $S$ as they cannot be formed by these rules. Note that all elements in this set $S$ must be of the form $2^a 3^b$ for non-negative integers $a, b$.

### Structural Induction
**Structural induction** is a proof technique used to prove propositions about elements of recursively defined sets. It mirrors mathematical induction but adapts to the structure of the set [source:cs1231s-cs1231s-extra-tutorials-tutorial-5-tut05-enzio-pdf#section-1].

To prove that $\forall x \in \text{Set} P(x)$ is true, where $P(x)$ is a proposition and 'Set' is a recursively defined set, it suffices to:
1.  **Base Step:** Show that $P(x)$ is true for all elements $x$ introduced by the **base clauses**.
2.  **Induction Step:** Show that for every **recursion clause**, if the proposition $P$ holds for the input elements of the clause, it also holds for the output element [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-13].

#### Example: Structural Induction over $2\mathbb{Z}_{\geq 1}$
To prove $\forall n \in 2\mathbb{Z}_{\geq 1} P(n)$ is true, it suffices to:
*   **Base Step:** Show $P(2)$ is true (since 2 is the base element).
*   **Induction Step:** Show that $\forall x \in 2\mathbb{Z}_{\geq 1} (P(x) \Rightarrow P(x+2))$ is true (since $x+2$ is how new elements are generated from existing $x$).

#### Recursively Defined Well-Formed Formulas (WFFs) in Propositional Logic
Let $\Sigma$ be a nonempty set of propositional variables (e.g., $\{p, q\}$). The set WFF($\Sigma$) is recursively defined as follows [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-10, cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-5]:
1.  **Base Clause:** Every element $p \in \Sigma$ is in WFF($\Sigma$) [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-10].
2.  **Recursion Clauses:** If $x, y \in \text{WFF}(\Sigma)$, then $\neg x$, $(x \land y)$, and $(x \lor y)$ are in WFF($\Sigma$) [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-10].
3.  **Minimality Clause:** Membership for WFF($\Sigma$) can only be demonstrated by finitely many successive applications of the above clauses [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-10].

#### Positive Well-Formed Formulas ($WFF^+(\Sigma)$)
A subset called WFF$^+(\Sigma)$ (Positive Well-Formed Formulas) can be defined recursively by excluding the negation operator [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-12]:
1.  **Base Clause:** Every element $p \in \Sigma$ is in WFF$^+(\Sigma)$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-12].
2.  **Recursion Clauses:** If $x, y \in \text{WFF}^+(\Sigma)$, then $(x \land y)$ and $(x \lor y)$ are in WFF$^+(\Sigma)$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-12].
3.  **Minimality Clause:** Membership for WFF$^+(\Sigma)$ can only be demonstrated by finitely many successive applications of the above clauses [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-12].

#### Structural Induction over $WFF^+(\Sigma)$
To prove $\forall x \in \text{WFF}^+(\Sigma) P(x)$ is true, it suffices to [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-13]:
*   **Base Step:** Show $P(p)$ is true for every propositional variable $p \in \Sigma$ [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-13].
*   **Induction Step:** Show that $\forall x, y \in \text{WFF}^+(\Sigma) ((P(x) \land P(y)) \Rightarrow (P((x \land y)) \land P((x \lor y))))$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-13].

#### All-False Assignments Lemma
**Lemma 7.3.19:** Let $\Sigma$ be a nonempty set. If $x \in \text{WFF}^+(\Sigma)$, then assigning `false` to all elements of $\Sigma$ makes $x$ evaluate to `false` [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-14, cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-15].
*   **Proof using Structural Induction over WFF$^+(\Sigma)$**:
    Let $P(x)$ be the proposition "assigning `false` to all elements of $\Sigma$ makes $x$ evaluate to `false`."
    *   **Base Step:** For any $p \in \Sigma$, if `false` is assigned to $p$, then $p$ evaluates to `false`. So $P(p)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-15].
    *   **Induction Step:** Assume $P(x)$ and $P(y)$ are true for $x, y \in \text{WFF}^+(\Sigma)$, meaning $x$ evaluates to `false` and $y$ evaluates to `false` when all propositional variables are `false`.
        Then, for $(x \land y)$, it evaluates to `false \land false = false`.
        For $(x \lor y)$, it evaluates to `false \lor false = false` [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-15].
    Thus, $P((x \land y))$ and $P((x \lor y))$ are true. By structural induction, the lemma holds.

**Theorem 7.3.20:** The set $\{\land, \lor\}$ is not a complete set of propositional connectives. In other words, for every nonempty set $\Sigma$, there exists an $x \in \text{WFF}(\Sigma)$ such that for all $y \in \text{WFF}^+(\Sigma)$, $y \not\equiv x$ (where $\equiv$ denotes logical equivalence) [source:cs1231s-cs1231s-extra-lecture-slides-7-2-recn-0-pdf#section-14].
*   **Proof:**
    1.  Pick any $p \in \Sigma$ (possible since $\Sigma$ is nonempty).
    2.  Consider the formula $\neg p \in \text{WFF}(\Sigma)$.
    3.  Assign `false` to all elements of $\Sigma$. By Lemma 7.3.19, any $y \in \text{WFF}^+(\Sigma)$ will evaluate to `false`.
    4.  However, $\neg p$ will evaluate to $\neg \text{false} = \text{true}$.
    5.  Since $y$ evaluates to `false` and $\neg p$ evaluates to `true` under the same assignment, $y \not\equiv \neg p$.
    Thus, there is at least one WFF (like $\neg p$) that cannot be expressed using only positive WFFs.

### Connection between Mathematical Induction and Structural Induction
Mathematical Induction is a specific instance of structural induction. When we define $\mathbb{Z}_{\geq 0}$ recursively with $0$ as the base clause and $x+1$ as the recursion clause, performing structural induction over $\mathbb{Z}_{\geq 0}$ is precisely what Mathematical Induction (with $m=0$) entails [source:cs1231s-cs1231s-extra-lecture-slides-notes7-indn-pdf#section-5].

---
page_id: "y1s1-cs1231s-lecture-01-mathematical-language"
title: "Lecture 01: Mathematical Language and Statements"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Introduction to the language of mathematics, variables, and different types of mathematical statements, laying the groundwork for formal proofs."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-1"
  - "cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-2"
  - "cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3"
  - "cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-1"
topics:
  - "proof"
  - "mathematical"
  - "statements"
  - "integers"
  - "true"
  - "statement"
  - "proofs"
  - "can"
  - "set"
  - "chapter"
source_count: 2
lecture_number: 1
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 01: Mathematical Language and Statements

## The Language of Mathematics

Mathematics relies on a precise and unambiguous language to communicate complex ideas. This language consists of a system including symbols, specific vocabulary, grammatical structures, conventions, abbreviations, and even pronunciation [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-1]. Understanding this language is fundamental to reading, understanding, and constructing mathematical proofs [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-1].

Examples of how mathematical expressions are pronounced and common symbolic differences in this course (CS1231S) include:
*   $p \to q$ is read as "p implies q" or "if p, then q".
*   $A \subseteq B$ is read as "A is a subset of B" or "A is contained in B".
*   $A - B$ (or $A \setminus B$) is read as "A minus B" or "the difference between set A and set B" [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-1].

### Variables

Variables are crucial in mathematics for two main reasons:
1.  **To give names to what is being sought.** This allows for the precise formulation of problems.
2.  **To maintain generality in mathematical statements.** Using variables allows expressions of properties that hold for entire classes of numbers or objects, rather than just specific instances [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-2].

For example, the sentence "Is there a number with the following property: doubling it and adding 3 gives the same result as squaring it?" can be rewritten using a variable $x$ as: "Is there a number $x$ such that $2x + 3 = x^2$?" [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-2].

Similarly, "Given any real number, its square is non-negative" can be expressed using a variable $r$ as: "Given any real number $r$, $r^2$ is non-negative" [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-2].

### Important Sets and Their Notations

Several fundamental sets of numbers are frequently encountered in mathematics and have standard notations:

*   **Natural Numbers ($\mathbb{N}$):** The set of non-negative integers used for counting. In CS1231S, we include 0 in the set of natural numbers: $\{0, 1, 2, 3, \dots\}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3]. It's important to note that the inclusion of 0 can vary across mathematical texts [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2].
*   **Integers ($\mathbb{Z}$):** The set of all whole numbers, including positive, negative, and zero. For example, $315, -9047, 3^5, \sqrt{49}$ are integers [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3]. The notation $\mathbb{Z}$ comes from the German word "zahlen" meaning "to count" [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2].
*   **Rational Numbers ($\mathbb{Q}$):** The set of numbers that can be expressed as a fraction $a/b$, where $a$ and $b$ are integers and $b \neq 0$. Examples include $1/2, -23, 8.6, -37/5$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3]. The notation $\mathbb{Q}$ comes from the word "quotient" [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2]. It is well-known that all integers are rational numbers [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3].
*   **Real Numbers ($\mathbb{R}$):** The set of all numbers that can be marked on a one-dimensional number line. Examples include $-1, \pi, \sqrt{2}, 4.5$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3]. All rational numbers are real numbers [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3].
*   **Irrational Numbers:** Real numbers that cannot be expressed as a fraction of two integers [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2].
*   **Positive, Negative, and Non-Negative Numbers:**
    *   $\mathbb{Z}^+$: The set of all positive integers (integers greater than 0) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2].
    *   $\mathbb{R}^-$: The set of all negative real numbers (real numbers less than 0) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2].
    *   $\mathbb{Z}_{\ge 12}$: The set of all integers greater than or equal to 12 [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3].
    *   Note that 0 is neither negative nor positive [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3]. Non-negative numbers include all real numbers greater than or equal to zero [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2].
*   **Element of a Set:** The symbol $\in$ means "is an element/member of" [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3]. For example, $x \in \mathbb{Z}$ means $x$ is a member of the set of integers, or $x$ is an integer. The symbol $\notin$ indicates "is not an element of" [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-2].

## Mathematical Statements

A **statement** is a sentence, or group of sentences, that is definitively either true or false, but not both [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-3, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3]. For a sentence involving variables to be considered a statement, its variables must be clearly defined [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3]. Opinions (e.g., "Chocolate ice cream is the best") or ambiguous sentences (e.g., "$x - 1 = (x+2)(x+3)$" without defining $x$) are not statements because their truth value cannot be determined. A paradox, such as "This sentence is false," is also not a statement because it cannot be assigned a truth value [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3].

In this course, we focus exclusively on mathematical statements, meaning if a statement is not true, it must be false [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3].

### Types of Mathematical Statements

Three fundamental types of statements are used in mathematics [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4]:

1.  **Universal Statement:** Asserts that a certain property holds for *all* elements in a given set.
    *   **Keywords:** 'all', 'every', 'any' [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4].
    *   **Symbol:** $\forall$ (for all, for every, for each) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].
    *   **Example:** "All positive integers are greater than zero." [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4]

2.  **Conditional Statement:** States that if one thing is true (the hypothesis), then another thing must also be true (the conclusion).
    *   **Keywords:** 'if ... then' [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4].
    *   **Symbol:** $\to$ (implies) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3].
    *   **Example:** "If 378 is divisible by 18, then 378 is divisible by 6." [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4]
    *   **Truth Value:** A conditional statement "If p, then q" is false only when the hypothesis ($p$) is true and the conclusion ($q$) is false. In all other cases, it is true [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3].
    *   **Other forms of "p implies q"**:
        *   $q$ if $p$
        *   For $q$ to occur, it is enough that $p$ occurs.
        *   $p$ is sufficient for $q$.
        *   For $q$, $p$ is sufficient.
        *   For $p$ to occur, $q$ must occur.
        *   $p$ does not occur without $q$.
        *   $p$ only if $q$.
        *   $q$ is necessary for $p$.
        *   For $p$, $q$ is necessary.
        *   $q$ unless not $p$.
        *   $p$ cannot occur without $q$ occurring.
        *   $q$ whenever $p$.
        *   $q$ provided that $p$. [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-3]

3.  **Existential Statement:** Asserts that there is *at least one* thing for which a certain property is true.
    *   **Keywords:** 'there exists', 'there is', 'some' [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4].
    *   **Symbol:** $\exists$ (there exists, for some) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].
    *   **Example:** "There is a prime number that is even." [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4]
    *   **Existential Unique Quantifier:** $\exists!$ means "there is one and only one" or "there is exactly one" or "there is a unique" [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].

The phrase "such that" is often abbreviated as "s.t." or represented by the symbol $\ni$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-7, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].

### Combinations of Statements

Mathematical concepts often require combining these basic statement types:

*   **Universal Conditional Statement:** A statement that is both universal and conditional.
    *   **Example:** "For all animals $a$, if $a$ is a dog, then $a$ is a mammal." This can be rewritten as purely universal ("All dogs are mammals") or purely conditional ("If an animal is a dog, it is a mammal") [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4].
*   **Universal Existential Statement:** The first part is universal, stating a property is true for all objects of a given type, and the second part is existential, asserting the existence of something.
    *   **Example:** "Every real number has an additive inverse." (For every real number $n$, there exists an additive inverse such that when added to $n$, it yields zero) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4].
*   **Existential Universal Statement:** The first part is existential, asserting that a certain object exists, and the second part is universal, stating that the object satisfies a certain property for all things of a certain kind.
    *   **Example:** "There is a positive integer that is less than or equal to every positive integer." [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4]
*   **Complex Combinations:** Some important mathematical concepts, like the definition of a limit, combine universal, existential, and conditional statements [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-4].

The order of quantifiers in a statement with multiple quantifiers can significantly change its meaning and truth value [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4].

## Introduction to Proofs

A **mathematical proof** is a written argument that uses logic and established facts to demonstrate the truth of a mathematical statement [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-1]. It is an inferential argument, where previously established statements (such as theorems) can be used [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5]. In principle, a proof can be traced back to self-evident or assumed statements, known as **axioms**, along with accepted **rules of inference** [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5].

The primary goal of studying proofs is to develop the ability to read, understand, and construct them, transitioning from algorithmic to abstract thinking [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-1].

Pierre de Fermat emphasized that "The essential quality of a proof is to compel belief" [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5]. A good proof is a **concise, polished argument** that logically explains the validity of a statement to a skeptic [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5].
*   **Concise:** No irrelevant details, uses few words [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5].
*   **Polished:** It should be the final draft, revised multiple times for clarity and understandability [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5].
*   **Argument:** Every step must follow logically from previous steps [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5].

### Terminology of Proofs

Understanding specific terminology is essential for formal mathematical reasoning:

*   **Definition:** A precise and unambiguous description of a mathematical term, characterizing all and only the properties that must be true [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5]. Definitions are inherently "if and only if" (iff) statements [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
    *   **Example:** For any $x \in \mathbb{R}$, the absolute value of $x$, denoted $|x|$, is defined as: $|x| = x$ if $x \ge 0$, and $|x| = -x$ if $x < 0$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5].
*   **Axiom/Postulate:** A statement assumed to be true without proof. Axioms are the basic building blocks from which all theorems are proven, considered fundamental truths by the mathematical community [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
    *   **Examples:** Euclid's five postulates, Peano axioms, or the commutative property of addition ($a+b = b+a$ for real numbers $a,b$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Theorem:** A mathematical statement that is proven using rigorous mathematical reasoning. Theorems usually represent major or important results [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Lemma:** A "small theorem"; a minor result proven to aid in proving a larger theorem. Lemmas sometimes become notable in their own right [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Corollary:** A result that is a simple or immediate deduction from a theorem [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Conjecture:** A statement believed to be true, but for which there is no proof yet [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
    *   **Example:** Goldbach's conjecture: "Every even integer greater than 2 can be expressed as the sum of two primes." [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5]
*   **Proof:** A complete and concisely written argument establishing the truth of a mathematical statement [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Disproof:** A complete and concisely written argument establishing that a statement is not true [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].

### Basic Properties of Integers

In proofs involving integers, certain properties are often assumed as axioms:
*   **Closure:** Integers are closed under addition ($x+y \in \mathbb{Z}$) and multiplication ($xy \in \mathbb{Z}$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-6].
*   **Commutativity:** Addition and multiplication are commutative ($x+y = y+x$ and $xy = yx$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-6].
*   **Associativity:** Addition and multiplication are associative ($(x+y)+z = x+(y+z)$ and $(xy)z = x(yz)$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-6].
*   **Distributivity:** Multiplication is distributive over addition ($x(y+z) = xy+xz$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-6].
*   **Trichotomy:** For any two integers $x, y$, exactly one of the following is true: $x=y$, $x<y$, or $x>y$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-6].

These properties are foundational and can be quoted in proofs without needing to re-prove them [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-6].

#### Definitions: Even and Odd Integers
An integer $n$ is **even** if, and only if (iff), $n$ equals twice some integer. Symbolically, $n \text{ is even } \iff \exists \text{ an integer } k \text{ such that } n = 2k$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-7, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].

An integer $n$ is **odd** if, and only if (iff), $n$ equals twice some integer plus 1. Symbolically, $n \text{ is odd } \iff \exists \text{ an integer } k \text{ such that } n = 2k + 1$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-7, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].

#### Definition: Divisibility
If $n$ and $d$ are integers and $d \neq 0$, then $n$ is **divisible** by $d$ iff $n$ equals $d$ times some integer. We may also say that "$n$ is a multiple of $d$", or "$d$ is a factor of $n$", or "$d$ is a divisor of $n$", or "$d$ divides $n$". The notation $d | n$ means "$d$ divides $n$". Symbolically, if $n, d \in \mathbb{Z}$ and $d \neq 0$: $d | n \iff \exists k \in \mathbb{Z} \text{ such that } n = dk$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-7, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].

It is important to note that $d | n$ is a statement (which can be true or false), not a numerical value or an operation of division [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-7].

### Common Proof Methods

Several methods are used to construct mathematical proofs. Here are some key techniques:

1.  **Direct Proof:** To prove an "if $P$, then $Q$" statement, a direct proof begins by assuming the hypothesis $P$ is true and then uses logical steps and established facts to show that the conclusion $Q$ must follow [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
    *   **Example:** Prove that the product of two consecutive odd numbers is always odd.
        1.  Let $a$ and $b$ be two consecutive odd numbers.
        2.  Without loss of generality (WLOG), assume $a < b$, so $b = a+2$.
        3.  By definition of odd numbers, $a = 2k+1$ for some integer $k$.
        4.  Then $b = (2k+1)+2 = 2k+3$.
        5.  The product $ab = (2k+1)(2k+3) = 4k^2 + 6k + 2k + 3 = 4k^2 + 8k + 3$ (by basic algebra).
        6.  Rewrite as $2(2k^2+4k+1)+1$.
        7.  Let $m = 2k^2+4k+1$. Since integers are closed under multiplication and addition, $m$ is an integer.
        8.  Therefore, $ab = 2m+1$, which is odd by definition of odd numbers. [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8]
    *   WLOG (Without Loss Of Generality) is used when an assumption narrows the premise to a special case, implying the proof applies to all other cases easily [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].

2.  **Proof by Construction (Existence Proof):** Used to prove existential statements (i.e., that something exists). This involves explicitly finding or constructing an example that satisfies the given property [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
    *   **Example:** Prove $\exists x \in \mathbb{Z}$ s.t. $x > 2$ and $x^2 - 5x + 6 > 0$.
        1.  Let $x = 17$.
        2.  Note that $17 \in \mathbb{Z}$ and $17 > 2$.
        3.  Also, $17^2 - 5(17) + 6 = 289 - 85 + 6 = 210$, which is indeed $> 0$.
        4.  Since we found such an $x$, the statement is proven [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].
    *   The process of finding the value is preliminary scratch work and is not part of the formal proof itself [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].

3.  **Disproof by Counterexample:** Used to prove that a universal statement is false. This requires finding just one specific example (a counterexample) for which the statement does not hold [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
    *   **Example:** Disprove: "The product of two irrational numbers is always irrational."
        1.  Let the two irrational numbers be $\sqrt{2}$ and $\sqrt{8}$.
        2.  Their product is $\sqrt{2} \times \sqrt{8} = \sqrt{16} = 4$.
        3.  Since $4$ is a rational number, this single counterexample disproves the statement [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].

4.  **Proof by Exhaustion (Proof by Cases / Brute Force):** Suitable when the number of possible cases is finite. The proof proceeds by examining each case individually to show the statement holds true [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-5, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
    *   **Example:** Prove that $6a$ is not divisible by 5 for an integer $a$ between 1 and 4 inclusive.
        1.  **Case 1:** If $a=1$, then $6a = 6$. $5 \nmid 6$.
        2.  **Case 2:** If $a=2$, then $6a = 12$. $5 \nmid 12$.
        3.  **Case 3:** If $a=3$, then $6a = 18$. $5 \nmid 18$.
        4.  **Case 4:** If $a=4$, then $6a = 24$. $5 \nmid 24$.
        5.  Since the statement holds for all possible integer values of $a$ between 1 and 4, the proof is complete [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].

5.  **Proof by Deduction:** A type of direct proof used for general problems with an infinite number of cases. It uses algebraic manipulation and definitions to prove a statement universally [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].
    *   **Example:** Prove that the difference of two consecutive squares is always odd.
        1.  Let the numbers be $n$ and $n+1$.
        2.  The difference of their squares is $(n+1)^2 - n^2$.
        3.  Using basic algebra: $(n+1)^2 - n^2 = (n^2 + 2n + 1) - n^2 = 2n + 1$.
        4.  By the definition of an odd number, $2n+1$ is odd.
        5.  Therefore, the difference of two consecutive squares is always odd [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].

6.  **Proof by Contradiction (Indirect Proof):** To prove a statement $S$, one assumes its negation ($\neg S$) is true. Based on this assumption, one uses known facts and theorems to arrive at a logical contradiction. Since every step in the argument from $\neg S$ to the contradiction is logically correct, the problem must lie in the initial assumption that $\neg S$ is true. Thus, $\neg S$ is false, which means $S$ is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5]. A contradiction is a statement that can never be true [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
    *   **Example:** Prove that $\sqrt{2}$ is irrational.
        1.  Suppose, for contradiction, that $\sqrt{2}$ is rational.
        2.  By definition of rational numbers, $\exists m, n \in \mathbb{Z}$ such that $\sqrt{2} = \frac{m}{n}$ where $\frac{m}{n}$ is in its lowest terms (i.e., the only common factor of $m$ and $n$ is 1).
        3.  Squaring both sides gives $2 = \frac{m^2}{n^2}$, so $m^2 = 2n^2$.
        4.  This means $m^2$ is even. By [[lecture-02-logical-equivalence#Proposition 4.6.4|Proposition 4.6.4]], if $m^2$ is even, then $m$ is even.
        5.  Since $m$ is even, we can write $m = 2k$ for some integer $k$.
        6.  Substituting $m=2k$ into $m^2 = 2n^2$: $(2k)^2 = 2n^2 \implies 4k^2 = 2n^2 \implies n^2 = 2k^2$.
        7.  This means $n^2$ is even. By [[lecture-02-logical-equivalence#Proposition 4.6.4|Proposition 4.6.4]], if $n^2$ is even, then $n$ is even.
        8.  So, both $m$ and $n$ are even, which means they have a common factor of 2.
        9.  This contradicts our initial assumption that $\frac{m}{n}$ is in its lowest terms.
        10. Therefore, the assumption that $\sqrt{2}$ is rational must be false. Hence, $\sqrt{2}$ is irrational [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].

7.  **Proof by Contraposition:** To prove a conditional statement "$P \to Q$", one proves its contrapositive, "$\neg Q \to \neg P$". These two statements are logically equivalent, meaning if one is true, the other must also be true [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-4]. This method is often helpful when directly proving "$P \to Q$" is difficult [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].

### How to Write Proofs

Writing proofs is a specialized skill that requires practice and refinement. It's like solving a jigsaw puzzle; each proof is unique, and you don't always solve it from top to bottom [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].
*   **Structure and Clarity:** Organize your proof with numbering and indentation. Read your proof aloud to ensure logical flow and grammatical correctness [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8, cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Variable Definition:** Always clearly define all variables when they are introduced [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Conciseness:** Avoid irrelevant details or unnecessary information that detracts from the main argument [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Polished Draft:** Proofs should be a final, polished piece of writing. It's recommended to write multiple drafts, detailing your thought process initially, then refining it for clarity and conciseness [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Use of Symbols:** While mathematical symbols are appropriate, they should be used in grammatically correct sentences. For instance, prefer "therefore" over $\therefore$ in formal writing, and italicize variables to distinguish them from words [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Assumptions:** Begin your proof by clearly stating all assumptions and the given hypothesis [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].
*   **Conclusion:** The end of a proof is typically indicated by "Q.E.D." (quod erat demonstrandum) or a shaded box ($\blacksquare$) [source:cs1231s-cs1231s-extra-cs1231s-introductiontoadvancedmathematics-aguidetounderstandingproof-pdf#section-5].

#### Example: Proving "Colorful" Integers
A special definition used for CS1231S is: an integer $n$ is **colorful** iff there exists some integer $k$ such that $n = 3k$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8].

**Statement:** Prove that if $x, y$ are colorful integers, then $x + 2y$ is colorful.
**Proof:**
1.  Let $x, y$ be colorful integers.
    1.1. By the definition of colorful integers, $\exists a, b \in \mathbb{Z}$ such that $x = 3a$ and $y = 3b$.
    1.2. Now, consider the expression $x + 2y$. Substituting the definitions from step 1.1: $x + 2y = 3a + 2(3b) = 3a + 6b = 3(a + 2b)$ (by basic algebra).
2.  Let $c = a + 2b$. Since $a$ and $b$ are integers, and integers are closed under multiplication and addition, $c$ is an integer ($c \in \mathbb{Z}$).
3.  Therefore, $\exists c \in \mathbb{Z}$ such that $x + 2y = 3c$.
4.  By the definition of colorful integers, $x + 2y$ is colorful. $\blacksquare$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture01-speaking-mathematically-full-pdf#section-8]

---
page_id: "y1s1-cs1231s-lecture-03-predicates-quantifiers"
title: "Lecture 03: Predicates, Quantifiers and Truth Sets"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Explores predicates, universal and existential quantifiers, and how to determine the truth sets for quantified statements, forming the basis of predicate logic."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1"
  - "cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1"
  - "cs1231s-tutorial-tut02ans-post-pdf#section-1"
  - "cs1231s-tutorial-tut02qns-pdf#section-1"
topics:
  - "universal"
  - "statements"
  - "statement"
  - "quantified"
  - "true"
  - "equivalent"
  - "section"
  - "predicate"
  - "means"
  - "its"
source_count: 4
lecture_number: 3
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 03: Predicates, Quantifiers and Truth Sets

This page explores the foundational concepts of predicate logic, including predicates, quantifiers (universal and existential), and truth sets. It details how to construct and evaluate quantified statements, their negations, and introduces formal argument structures like Universal Modus Ponens and Modus Tollens.

---

### 3.1 Predicates and Quantified Statements I

Predicate logic extends propositional logic by allowing statements to contain variables, which can then be quantified [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].

#### Predicates
A **predicate** is a sentence that contains one or more variables and becomes a [statement](/y1s1-cs1231s-lecture-01-mathematical-language#statements) when specific values are substituted for these variables [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1]. Predicates can also be referred to as "propositional functions" or "open sentences" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

For example:
*   $P(x) = \text{"x is a student at Bedford College"}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1]
*   $Q(x, y) = \text{"x is a student at y"}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1]

The **domain** of a predicate variable is the set of all possible values that can be substituted for that variable [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1]. This is also known as the "domain of discourse," "universe of discourse," or "universal set" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

#### Truth Sets
When an element from the domain is substituted into a one-variable predicate, the resulting statement is either true or false [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
The **truth set** of a predicate $P(x)$ with domain $D$ is the set of all elements in $D$ that make $P(x)$ true upon substitution [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].
It is denoted as $\{x \in D \mid P(x)\}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].

**Example:**
Let $Q(n)$ be the predicate "$n$ is a factor of 8."
*   If the domain of $n$ is $\mathbb{Z}^+$, the truth set is $\{1, 2, 4, 8\}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
*   If the domain of $n$ is $\mathbb{Z}$, the truth set is $\{-8, -4, -2, -1, 1, 2, 4, 8\}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

#### Quantifiers
Quantifiers are used to transform predicates into statements by specifying the quantity of elements in the domain for which the predicate is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

##### Universal Quantifier ($\forall$)
The symbol $\forall$ (read as "for all," "for any," "for every," or "for each") is the **universal quantifier** [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
A **universal statement** takes the form "$\forall x \in D, Q(x)$" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].
*   It is true if $Q(x)$ is true for **every** $x$ in $D$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].
*   It is false if $Q(x)$ is false for **at least one** $x$ in $D$. Such a value for $x$ is called a **counterexample** [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].

**Example:**
*   Let $D = \{1, 2, 3, 4, 5\}$. The statement "$\forall x \in D, x^2 \ge x$" is true, verifiable by checking each element (method of exhaustion) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
*   The statement "$\forall x \in \mathbb{R}, x^2 \ge x$" is false. A counterexample is $x = \frac{1}{2}$, because $(\frac{1}{2})^2 = \frac{1}{4}$ which is not $\ge \frac{1}{2}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

##### Existential Quantifier ($\exists$)
The symbol $\exists$ (read as "there exists," "there is a," "we can find a," "there is at least one," or "for some") is the **existential quantifier** [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
An **existential statement** takes the form "$\exists x \in D \text{ such that } Q(x)$" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].
*   It is true if $Q(x)$ is true for **at least one** $x$ in $D$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].
*   It is false if $Q(x)$ is false for **all** $x$ in $D$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-1].

**Example:**
*   The statement "$\exists m \in \mathbb{Z}^+ \text{ such that } m^2 = m$" is true because $1^2 = 1$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
*   Let $E = \{5, 6, 7, 8\}$. The statement "$\exists m \in E \text{ such that } m^2 = m$" is false, as $m^2=m$ is not true for any $m$ in $E$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

##### Unique Existential Quantifier ($\exists!$)
The symbol $\exists!$ means "there exists a unique" or "there is one and only one" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
**Example:** $\exists! x \in \mathbb{Z}^+ \text{ such that } x \text{ is even and prime}$. (The answer is 2.) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1]

#### Formal Versus Informal Language
Quantified statements can be expressed in formal notation or informal natural language. It's crucial to be able to translate between the two.

**Examples of Informal Translations:**
*   **Formal:** $\forall x \in \mathbb{R}, x^2 \ge 0$.
    *   **Informal:** All real numbers have non-negative squares. Every real number has a non-negative square. The square of each real number is non-negative [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
*   **Formal:** $\exists m \in \mathbb{Z}^+ \text{ such that } m^2 = m$.
    *   **Informal:** There is a positive integer whose square is itself. We can find at least one positive integer equal to its own square. Some positive integer equals its own square [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

#### Universal Conditional Statements
A particularly important form of statement in mathematics is the **universal conditional statement**, expressed as:
$\forall x (\text{if } P(x) \text{ then } Q(x))$ or $\forall x (P(x) \rightarrow Q(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

#### Equivalent Forms of Universal and Existential Statements
A universal conditional statement $\forall x \in U (P(x) \rightarrow Q(x))$ can be rephrased as $\forall x \in D, Q(x)$ by narrowing the domain $U$ to $D$, where $D$ consists of all values of $x$ for which $P(x)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
**Example:** "$\forall \text{ real numbers } x, \text{ if } x \text{ is an integer then } x \text{ is rational}$" is equivalent to "$\forall \text{ integers } x, x \text{ is rational}$" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

Similarly, an existential statement "$\exists x \text{ such that } (P(x) \text{ and } Q(x))$" is equivalent to "$\exists x \in D \text{ such that } Q(x)$", where $D$ is the set of all $x$ for which $P(x)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

#### Implicit Quantification
Mathematical writing often uses **implicitly quantified statements**, where quantifiers are not explicitly stated but understood from context. This can happen with words like "a" or "an", or from the general context of a sentence [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

*   **Notation $P(x) \Rightarrow Q(x)$**: Means that every element in the truth set of $P(x)$ is in the truth set of $Q(x)$, or equivalently, $\forall x (P(x) \rightarrow Q(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
*   **Notation $P(x) \Leftrightarrow Q(x)$**: Means that $P(x)$ and $Q(x)$ have identical truth sets, or equivalently, $\forall x (P(x) \leftrightarrow Q(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

**Example:**
Given predicates $Q(n): \text{"n is a factor of 8"}$, $R(n): \text{"n is a factor of 4"}$, $S(n): \text{"n < 5 and n } \ne 3"$, with domain $\mathbb{Z}^+$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
*   Truth set of $Q(n)$ is $\{1, 2, 4, 8\}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
*   Truth set of $R(n)$ is $\{1, 2, 4\}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
*   Truth set of $S(n)$ is $\{1, 2, 4\}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].
Thus, $R(n) \Rightarrow Q(n)$ (since $\{1,2,4\} \subseteq \{1,2,4,8\}$) and $R(n) \Leftrightarrow S(n)$ (since $\{1,2,4\} = \{1,2,4\}$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

#### Tarski's World
Tarski's World is a computer program used to teach logic principles, providing a visual grid of objects with various sizes, shapes, and colors. Logical statements about these objects can be evaluated for truth or falsity within this defined world [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1]. Predicates like Triangle(x), Blue(y), RightOf(x,y) describe properties and relations of objects [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-1].

### 3.2 Predicates and Quantified Statements II

#### Negations of Quantified Statements
Negating quantified statements follows specific rules:
*   **Negation of a Universal Statement:** The negation of "$\forall x \in D, P(x)$" is logically equivalent to "$\exists x \in D \text{ such that } \sim P(x)$" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
    *   Symbolically: $\sim(\forall x \in D, P(x)) \equiv \exists x \in D \text{ such that } \sim P(x)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
    *   Informally: "Not all are" is equivalent to "some are not" or "there is at least one that is not" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
*   **Negation of an Existential Statement:** The negation of "$\exists x \in D \text{ such that } P(x)$" is logically equivalent to "$\forall x \in D, \sim P(x)$" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
    *   Symbolically: $\sim(\exists x \in D \text{ such that } P(x)) \equiv \forall x \in D, \sim P(x)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
    *   Informally: "Not some are" (i.e., "none are") is equivalent to "all are not" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].

**Quick Quiz Example:**
*   **Statement:** $\forall \text{ primes } p, p \text{ is odd}$.
*   **Negation:** $\exists \text{ a prime } p \text{ such that } p \text{ is not odd}$. (This is true, as $2$ is prime but not odd) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].

#### Negations of Universal Conditional Statements
The negation of a universal conditional statement $\forall x (P(x) \rightarrow Q(x))$ is particularly important:
$\sim(\forall x (P(x) \rightarrow Q(x))) \equiv \exists x \text{ such that } \sim(P(x) \rightarrow Q(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
Since $\sim(P(x) \rightarrow Q(x)) \equiv P(x) \land \sim Q(x)$, the negation becomes:
$\sim(\forall x (P(x) \rightarrow Q(x))) \equiv \exists x \text{ such that } (P(x) \land \sim Q(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].

**Quick Quiz Example:**
*   **Statement:** $\forall \text{ people } p, \text{ if } p \text{ is blond then } p \text{ has blue eyes}$.
*   **Formal Negation:** $\exists \text{ a person } p \text{ such that } p \text{ is blond and } p \text{ does not have blue eyes}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].

#### Relation among $\forall, \exists, \land$, and $\lor$
The negation rules for quantifiers are analogous to [De Morgan's Laws](/y1s1-cs1231s-lecture-02-logical-equivalence#de-morgan's-laws) in propositional logic. Universal statements are generalizations of conjunctions (AND statements), and existential statements are generalizations of disjunctions (OR statements) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
For a finite domain $D = \{x_1, x_2, \ldots, x_n\}$:
*   $\forall x \in D, Q(x) \equiv Q(x_1) \land Q(x_2) \land \ldots \land Q(x_n)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
*   $\exists x \in D, Q(x) \equiv Q(x_1) \lor Q(x_2) \lor \ldots \lor Q(x_n)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].

#### Vacuous Truth of Universal Statements
A universal conditional statement of the form $\forall x \in D (P(x) \rightarrow Q(x))$ is called **vacuously true** (or true by default) if $P(x)$ is false for every $x$ in $D$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2]. This occurs because the hypothesis (antecedent) cannot be satisfied [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
**Example:** The statement "All mooloomeelees are mammals" is vacuously true if there are no mooloomeelees [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
Similarly, the empty set $\emptyset$ is a subset of every set $A$ ($\emptyset \subseteq A$), because the condition for falsity (an element in $\emptyset$ not being in $A$) cannot be met [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].

#### Variants of Universal Conditional Statements
Just like simple conditional statements, universal conditional statements also have contrapositives, converses, and inverses [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2]. For a statement of the form $\forall x \in D (P(x) \rightarrow Q(x))$:
1.  Its **contrapositive** is $\forall x \in D (\sim Q(x) \rightarrow \sim P(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
2.  Its **converse** is $\forall x \in D (Q(x) \rightarrow P(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
3.  Its **inverse** is $\forall x \in D (\sim P(x) \rightarrow \sim Q(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].

A universal conditional statement is logically equivalent to its contrapositive [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2]. However, it is **not** logically equivalent to its converse or inverse [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].

**Example:**
*   **Statement:** "If a real number is greater than 2, then its square is greater than 4." ($\forall x \in \mathbb{R} (x > 2 \rightarrow x^2 > 4)$) - True [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
*   **Contrapositive:** "If the square of a real number is less than or equal to 4, then the number is less than or equal to 2." ($\forall x \in \mathbb{R} (x^2 \le 4 \rightarrow x \le 2)$) - True [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2].
*   **Converse:** "If the square of a real number is greater than 4, then the number is greater than 2." ($\forall x \in \mathbb{R} (x^2 > 4 \rightarrow x > 2)$) - False (e.g., $x=-3$, $(-3)^2 = 9 > 4$, but $-3 \not > 2$) [source:cs1231s-tutorial-tut02ans-post-pdf#section-1].
*   **Inverse:** "If a real number is less than or equal to 2, then the square of the number is less than or equal to 4." ($\forall x \in \mathbb{R} (x \le 2 \rightarrow x^2 \le 4)$) - False (e.g., $x=-3$, $-3 \le 2$, but $(-3)^2 = 9 \not \le 4$) [source:cs1231s-tutorial-tut02ans-post-pdf#section-1].

#### Necessary and Sufficient Conditions, Only If
These logical concepts can also be extended to universal conditional statements [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
*   "$\forall x, r(x)$ is a **sufficient condition** for $s(x)$" means $\forall x (r(x) \rightarrow s(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
*   "$\forall x, r(x)$ is a **necessary condition** for $s(x)$" means $\forall x (\sim r(x) \rightarrow \sim s(x))$, or equivalently, $\forall x (s(x) \rightarrow r(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
*   "$\forall x, r(x)$ **only if** $s(x)$" means $\forall x (\sim s(x) \rightarrow \sim r(x))$, or equivalently, $\forall x (r(x) \rightarrow s(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].

### 3.3 Statements with Multiple Quantifiers

Statements can involve more than one quantifier. Interpreting these statements requires careful attention to the order of quantifiers.

#### Interpreting Multiply-Quantified Statements
The order of quantifiers is crucial for determining the truth value of a statement.
*   **$\forall x \in D, \exists y \in E \text{ such that } P(x, y)$**: To establish truth, for *any* $x$ chosen, you must be able to find a $y$ that makes $P(x, y)$ true. The $y$ found can depend on $x$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
*   **$\exists x \in D \text{ such that } \forall y \in E, P(x, y)$**: To establish truth, you must find *one particular* $x$ that makes $P(x, y)$ true for *all* $y$. This $x$ must work independently of $y$'s choice [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].

**Example (Cafeteria line):**
Consider items chosen by students (Uta, Tim, Yuen) from categories (Salads, Main courses, Desserts, Beverages) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
*   **$\exists$ an item $I$ such that $\forall$ students $S, S \text{ chose } I$**. (Informal: "There is an item that was chosen by every student." **True** - pie) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
*   **$\exists$ a student $S$ such that $\forall$ items $I, S \text{ chose } I$**. (Informal: "There is a student who chose every available item." **False**) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].

#### Translating from Informal to Formal Language
Many problems are stated informally and require translation into formal logic to solve.
**Example:**
*   **Informal:** "Every nonzero real number has a reciprocal."
*   **Formal:** $\forall \text{ nonzero real numbers } u, \exists \text{ a real number } v \text{ such that } uv = 1$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].

#### Ambiguous Language
Informal language can be ambiguous, especially with mixed quantifiers. The meaning often depends on context [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
**Example:** "There is a person supervising every detail of the production process."
This could mean:
1.  There is one single person who supervises *all* the details ( $\exists p \forall d, \text{Supervises}(p, d)$).
2.  For any particular production detail, there is *a* person who supervises it ( $\forall d \exists p, \text{Supervises}(p, d)$). (This allows for different supervisors for different details) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].

#### Negations of Multiply-Quantified Statements
Negating multiply-quantified statements involves applying the negation rules iteratively:
*   $\sim(\forall x \in D, \exists y \in E \text{ such that } P(x, y)) \equiv \exists x \in D \text{ such that } \forall y \in E, \sim P(x, y)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
*   $\sim(\exists x \in D \text{ such that } \forall y \in E, P(x, y)) \equiv \forall x \in D, \exists y \in E \text{ such that } \sim P(x, y)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].

#### Order of Quantifiers
In a statement containing both $\forall$ and $\exists$, changing the order of quantifiers usually changes the meaning of the statement [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
**Example:**
*   "$\forall \text{ people } x, \exists \text{ a person } y \text{ such that } x \text{ loves } y$" (Given any person, it's possible to find someone whom that person loves.) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
*   "$\exists \text{ a person } y \text{ such that } \forall \text{ people } x, x \text{ loves } y$" (There is one amazing individual who is loved by all people!) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
These two statements are not logically equivalent.

However, if one quantifier immediately follows another quantifier of the same type (e.g., $\forall x \forall y$ or $\exists x \exists y$), then the order does not affect the meaning [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
*   $\forall x \forall y \equiv \forall y \forall x$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
*   $\exists x \exists y \equiv \exists y \exists x$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
These can be abbreviated as $\forall x, y$ and $\exists x, y$ respectively [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].

#### Formal Logical Notation
In computer science, logical statements are often expressed in purely symbolic notation, omitting words like "such that".
*   "$\forall x \in D, P(x)$" is written as $\forall x (x \in D \rightarrow P(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
*   "$\exists x \in D \text{ such that } P(x)$" is written as $\exists x (x \in D \land P(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].
The combination of quantifiers, variables, predicates, and logical connectives forms the **language of first-order logic** [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].

#### Prolog (For Reading)
Prolog (Programming in Logic) is a logic programming language developed in the 1970s, used in fields like artificial intelligence. Prolog programs consist of statements describing a situation, and built-in search/inference techniques answer questions by deriving answers from these statements [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-3].

### 3.4 Arguments with Quantified Statements

#### Universal Instantiation
**Universal instantiation** is a fundamental tool of [deductive reasoning](/y1s1-lecture-02-logical-equivalence#deductive-reasoning). It states that if a property is true of *everything* in a set, then it is true of *any particular thing* in that set [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4].

#### Universal Modus Ponens
Universal instantiation combined with [Modus Ponens](/y1s1-lecture-02-logical-equivalence#rules-of-inference) forms the **Universal Modus Ponens** valid argument form [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
*   **Formal Version:**
    1.  $\forall x (P(x) \rightarrow Q(x))$
    2.  $P(a)$ for a particular $a$.
    3.  $\therefore Q(a)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
*   **Informal Version:**
    1.  If $x$ makes $P(x)$ true, then $x$ makes $Q(x)$ true.
    2.  $a$ makes $P(x)$ true.
    3.  $\therefore a$ makes $Q(x)$ true [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].

**Example:**
*   **Premise 1:** If an integer is even, then its square is even. ($\forall x (E(x) \rightarrow S(x))$)
*   **Premise 2:** $k$ is a particular integer that is even. ($E(k)$)
*   **Conclusion:** $k^2$ is even. ($\therefore S(k)$)
This argument is valid [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4].

#### Universal Modus Tollens
Universal instantiation combined with [Modus Tollens](/y1s1-lecture-02-logical-equivalence#rules-of-inference) forms the **Universal Modus Tollens** valid argument form [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2]. This rule is central to [proof by contradiction](/y1s1-lecture-04-direct-proof-disproof#methods-of-disproof) [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4].
*   **Formal Version:**
    1.  $\forall x (P(x) \rightarrow Q(x))$
    2.  $\sim Q(a)$ for a particular $a$.
    3.  $\therefore \sim P(a)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
*   **Informal Version:**
    1.  If $x$ makes $P(x)$ true, then $x$ makes $Q(x)$ true.
    2.  $a$ does not make $Q(x)$ true.
    3.  $\therefore a$ does not make $P(x)$ true [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].

**Example:**
*   **Premise 1:** All human beings are mortal. ($\forall x (H(x) \rightarrow M(x))$)
*   **Premise 2:** Zeus is not mortal. ($\sim M(\text{Zeus})$)
*   **Conclusion:** Zeus is not human. ($\therefore \sim H(\text{Zeus})$)
This argument is valid [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4].

#### Proving Validity of Arguments with Quantified Statements
An argument form is **valid** if, no matter what particular predicates are substituted for the predicate symbols in its premises, if the resulting premise statements are all true, then the conclusion is also true. An argument is called valid if, and only if, its form is valid [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].

##### Using Diagrams to Test for Validity
Venn diagrams can illustrate universal statements. For example, "All integers are rational numbers" can be shown by drawing a circle for "integers" entirely contained within a circle for "rational numbers" [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4].

Diagrams can also show invalidity. Consider the argument:
*   All human beings are mortal.
*   Felix is mortal.
*   $\therefore$ Felix is a human being.
This argument is **invalid**. A diagram shows that Felix could be mortal and outside the "human beings" circle but still inside the "mortals" circle [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4]. This exemplifies the **converse error**.

#### Converse Error (Quantified Form)
The **converse error** in quantified form occurs when one assumes a universal conditional statement is equivalent to its converse.
*   **Formal Version:**
    1.  $\forall x (P(x) \rightarrow Q(x))$
    2.  $Q(a)$ for a particular $a$.
    3.  $\therefore P(a)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
This argument form is **invalid** [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4].

#### Inverse Error (Quantified Form)
The **inverse error** in quantified form occurs when one assumes a universal conditional statement is equivalent to its inverse.
*   **Formal Version:**
    1.  $\forall x (P(x) \rightarrow Q(x))$
    2.  $\sim P(a)$ for a particular $a$.
    3.  $\therefore \sim Q(a)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].
This argument form is **invalid** [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4].

#### Creating Additional Forms of Argument
Universal instantiation can be combined with other valid argument forms to create new ones. For example, combining it with [transitivity](/y1s1-lecture-02-logical-equivalence#law-of-transitivity) yields **Universal Transitivity** [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2]:
*   **Formal Version:**
    1.  $\forall x (P(x) \rightarrow Q(x))$
    2.  $\forall x (Q(x) \rightarrow R(x))$
    3.  $\therefore \forall x (P(x) \rightarrow R(x))$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-summary-pdf#section-2].

#### Remark on the Converse and Inverse Errors (For Reading)
While logically invalid, a variation of the converse error is a useful reasoning tool in practice, known as **abduction**. This involves inferring a possible cause from observed effects, which is common in fields like medical diagnosis or artificial intelligence [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4]. For example, if pneumonia (P) causes fever (Q), and John has a fever (Q(John)), one might tentatively conclude John has pneumonia (P(John)) as a strong possibility, though not a certainty [source:cs1231s-cs1231s-extra-lecture-slides-lecture03-logicofquantifiedstatements-full-pdf#section-4].

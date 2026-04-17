---
page_id: "y1s1-cs1231s-lecture-02-logical-equivalence"
title: "Lecture 02: Logical Equivalence and Laws"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Covers logical connectives, truth tables, and fundamental laws of logical equivalence for compound statements, essential for propositional logic."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1"
  - "cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-1"
  - "cs1231s-assignment-assignment-1-a0251957u-copy-pdf#section-1"
  - "cs1231s-cscheatsheet-pdf#section-1"
  - "cs1231s-tutorial-tut01ans-post-pdf#section-1"
topics:
  - "true"
  - "then"
  - "logical"
  - "statement"
  - "statements"
  - "form"
  - "truth"
  - "all"
  - "false"
  - "not"
source_count: 5
lecture_number: 2
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 02: Logical Equivalence and Laws

This page introduces propositional logic, covering how to form and evaluate compound statements using logical connectives, and the fundamental laws of logical equivalence. It also delves into conditional statements and their variations, along with the principles of valid and invalid arguments and rules of inference.

---

## 2.1 Logical Form and Logical Equivalence

### Statements (Propositions)

A **statement** (or **proposition**) is a sentence that can be definitively classified as either true or false, but not both [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-1].

### Compound Statements and Logical Connectives

Individual statements can be combined using **logical connectives** to form compound statements. The primary connectives are [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-1]:

*   **Negation ($\sim p$ or 'not p'):** "It is not the case that p". If $p$ is true, $\sim p$ is false, and vice versa [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-1].
*   **Conjunction ($p \land q$ or 'p and q'):** "p and q". True only if both $p$ and $q$ are true [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-1].
*   **Disjunction ($p \lor q$ or 'p or q'):** "p or q". True if at least one of $p$ or $q$ is true (inclusive OR) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-1].

#### Truth Tables for Basic Connectives

Truth tables systematically list the truth values of a compound statement for every possible combination of truth values of its component statements [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1].

| $p$ | $\sim p$ |
| :-- | :------- |
| T   | F        |
| F   | T        |
[source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]

| $p$ | $q$ | $p \land q$ |
| :-- | :-- | :---------- |
| T   | T   | T           |
| T   | F   | F           |
| F   | T   | F           |
| F   | F   | F           |
[source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]

| $p$ | $q$ | $p \lor q$ |
| :-- | :-- | :--------- |
| T   | T   | T          |
| T   | F   | T          |
| F   | T   | T          |
| F   | F   | F          |
[source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]

#### Order of Operations

To avoid ambiguity in complex statements, a specific order of operations is followed [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]:

1.  **Negation** ($\sim$) is performed first.
2.  **Conjunction** ($\land$) and **Disjunction** ($\lor$) are coequal in precedence.
3.  **Parentheses** must be used to override or disambiguate the order of operations [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]. For example, $\sim p \land q$ is interpreted as $(\sim p) \land q$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1].

### Statement Form (Propositional Form)

A **statement form** (or **propositional form**) is an expression constructed from statement variables (like $p, q, r$) and logical connectives. It becomes a concrete statement when actual statements are substituted for its variables [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-2].
Examples include $\sim p \lor q$ or $(p \land q) \land \sim (p \land q)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1].

### Logical Equivalence

Two statement forms are **logically equivalent** if, and only if, they have identical truth values for every possible substitution of statements for their statement variables [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-2]. Logical equivalence between statement forms $P$ and $Q$ is denoted by $P \equiv Q$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1].

To demonstrate that two statement forms are *not* logically equivalent, one can [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]:
1.  Construct a truth table and find at least one row where their truth values differ.
2.  Find a **counterexample**: specific statements for the variables where one form is true and the other is false.

For example, $p \land q \equiv q \land p$ because they always have the same truth values [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]. However, $\sim(p \land q)$ and $\sim p \land \sim q$ are not logically equivalent, as shown by their truth tables and counterexamples [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1].

### Tautologies and Contradictions

*   A **tautology** is a statement form that is *always true*, regardless of the truth values of its individual statement variables. A statement whose form is a tautology is called a tautological statement [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-2].
*   A **contradiction** is a statement form that is *always false*, regardless of the truth values of its individual statement variables. A statement whose form is a contradiction is called a contradictory statement [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-2].

Constants like "true" (a tautology) and "false" (a contradiction) are often used in logical equivalence examples [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]. For instance, $p \land \text{true} \equiv p$ and $p \land \text{false} \equiv \text{false}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1].

### Summary of Logical Equivalences (Laws)

These laws allow for the simplification and transformation of logical expressions. Given any statement variables $p, q, r$, a tautology 'true', and a contradiction 'false':

| Law                  | Conjunction ($\land$)                      | Disjunction ($\lor$)                     | Other                               |
| :------------------- | :----------------------------------------- | :--------------------------------------- | :---------------------------------- |
| **Commutative**      | $p \land q \equiv q \land p$ [source:cs1231s-cscheatsheet-pdf#section-1] | $p \lor q \equiv q \lor p$ [source:cs1231s-cscheatsheet-pdf#section-1] |                                     |
| **Associative**      | $(p \land q) \land r \equiv p \land (q \land r)$ [source:cs1231s-cscheatsheet-pdf#section-1] | $(p \lor q) \lor r \equiv p \lor (q \lor r)$ [source:cs1231s-cscheatsheet-pdf#section-1] |                                     |
| **Distributive**     | $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ [source:cs1231s-cscheatsheet-pdf#section-1] | $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ [source:cs1231s-cscheatsheet-pdf#section-1] |                                     |
| **Identity**         | $p \land \text{true} \equiv p$ [source:cs1231s-cscheatsheet-pdf#section-1] | $p \lor \text{false} \equiv p$ [source:cs1231s-cscheatsheet-pdf#section-1] |                                     |
| **Negation**         | $p \land \sim p \equiv \text{false}$ [source:cs1231s-cscheatsheet-pdf#section-1] | $p \lor \sim p \equiv \text{true}$ [source:cs1231s-cscheatsheet-pdf#section-1] |                                     |
| **Double Negative**  |                                            |                                          | $\sim (\sim p) \equiv p$ [source:cs1231s-cscheatsheet-pdf#section-1] |
| **Idempotent**       | $p \land p \equiv p$ [source:cs1231s-cscheatsheet-pdf#section-1] | $p \lor p \equiv p$ [source:cs1231s-cscheatsheet-pdf#section-1] |                                     |
| **Universal Bound**  | $p \land \text{false} \equiv \text{false}$ [source:cs1231s-cscheatsheet-pdf#section-1] | $p \lor \text{true} \equiv \text{true}$ [source:cs1231s-cscheatsheet-pdf#section-1] |                                     |
| **De Morgan's Laws** | $\sim (p \land q) \equiv \sim p \lor \sim q$ [source:cs1231s-cscheatsheet-pdf#section-1] | $\sim (p \lor q) \equiv \sim p \land \sim q$ [source:cs1231s-cscheatsheet-pdf#section-1] |                                     |
| **Absorption**       | $p \land (p \lor q) \equiv p$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1] | $p \lor (p \land q) \equiv p$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1] |                                     |
| **Negation of True/False** | $\sim \text{true} \equiv \text{false}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1] | $\sim \text{false} \equiv \text{true}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1] |                                     |

These laws can be extended to more than two variables, particularly De Morgan's Laws [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1].

**Example:** Simplifying $\sim (\sim p \land q) \land (p \lor q)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]:
$\sim (\sim p \land q) \land (p \lor q)$
$\equiv (\sim(\sim p) \lor \sim q) \land (p \lor q)$ (De Morgan's Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]
$\equiv (p \lor \sim q) \land (p \lor q)$ (Double Negative Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]
$\equiv p \lor (\sim q \land q)$ (Distributive Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]
$\equiv p \lor (q \land \sim q)$ (Commutative Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]
$\equiv p \lor \text{false}$ (Negation Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]
$\equiv p$ (Identity Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-1]

## 2.2 Conditional Statements

### Definition and Truth Table

A **conditional statement** expresses an "if-then" relationship, denoted as $p \rightarrow q$ (read "if $p$ then $q$" or "$p$ implies $q$") [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-6].
*   $p$ is the **hypothesis** (or antecedent) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].
*   $q$ is the **conclusion** (or consequent) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].

The truth value of $p \rightarrow q$ is defined as follows: it is false only when the hypothesis $p$ is true and the conclusion $q$ is false; otherwise, it is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-6].

| $p$ | $q$ | $p \rightarrow q$ |
| :-- | :-- | :---------------- |
| T   | T   | T                 |
| T   | F   | F                 |
| F   | T   | T                 |
| F   | F   | T                 |
[source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2]

A conditional statement is considered **vacuously true** (or true by default) if its hypothesis is false, regardless of the truth value of its conclusion [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2]. For example, "If 0 = 1, then 1 = 2" is true because "0 = 1" is false [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].

### Order of Operations (with Conditional)

With the addition of the conditional connective, the order of operations is [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2]:
1.  **Negation** ($\sim$)
2.  **Conjunction** ($\land$) and **Disjunction** ($\lor$) (coequal)
3.  **Conditional** ($\rightarrow$) (performed last)

### Implication Law

The **Implication Law** states that a conditional statement $p \rightarrow q$ is logically equivalent to $\sim p \lor q$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, csheatsheet-pdf#section-1]. This can be verified using a truth table [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].

### Negation of a Conditional Statement

The negation of a conditional statement $\sim (p \rightarrow q)$ is logically equivalent to $p \land \sim q$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2]. This is derived using the Implication Law and De Morgan's Law:
$\sim (p \rightarrow q) \equiv \sim (\sim p \lor q)$ (Implication Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2]
$\equiv \sim (\sim p) \land \sim q$ (De Morgan's Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2]
$\equiv p \land \sim q$ (Double Negative Law) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2]

### Related Conditional Statements: Contrapositive, Converse, and Inverse

For a conditional statement "$p \rightarrow q$":

*   The **contrapositive** is "if $\sim q$ then $\sim p$", denoted $\sim q \rightarrow \sim p$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-6]. A conditional statement is **logically equivalent** to its contrapositive [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-7].
*   The **converse** is "if $q$ then $p$", denoted $q \rightarrow p$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-6]. The original conditional and its converse are **not logically equivalent** [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-7].
*   The **inverse** is "if $\sim p$ then $\sim q$", denoted $\sim p \rightarrow \sim q$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-6]. The inverse is **logically equivalent** to the converse [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-7].

### "Only If" and the Biconditional

*   **"p only if q"**: This means that $p$ can occur only if $q$ also occurs. It is equivalent to "if not $q$ then not $p$" or, contrapositively, "if $p$ then $q$" [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-8].

*   **Biconditional ($p \leftrightarrow q$ or "p if, and only if, q")**: Denoted as $p \leftrightarrow q$ (sometimes abbreviated "iff") [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, csheatsheet-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-8].
    *   It is true if $p$ and $q$ have the same truth values (both true or both false) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].
    *   It is false if $p$ and $q$ have opposite truth values [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].
    *   The biconditional $p \leftrightarrow q$ is logically equivalent to the conjunction of a conditional statement and its converse: $(p \rightarrow q) \land (q \rightarrow p)$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].

| $p$ | $q$ | $p \leftrightarrow q$ |
| :-- | :-- | :-------------------- |
| T   | T   | T                     |
| T   | F   | F                     |
| F   | T   | F                     |
| F   | F   | T                     |
[source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2]

**Order of Operations (with Biconditional):**
1.  Negation ($\sim$)
2.  Conjunction ($\land$) and Disjunction ($\lor$) (coequal)
3.  Conditional ($\rightarrow$) and Biconditional ($\leftrightarrow$) (coequal, performed last) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].

### Necessary and Sufficient Conditions

For statements $r$ and $s$:

*   **"r is a sufficient condition for s"**: Means that the occurrence of $r$ is enough to guarantee the occurrence of $s$. This is equivalent to "if $r$ then $s$" ($r \rightarrow s$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-8].
*   **"r is a necessary condition for s"**: Means that $r$ must occur for $s$ to occur. If $r$ does not occur, then $s$ cannot occur. This is equivalent to "if not $r$ then not $s$" ($\sim r \rightarrow \sim s$) or, contrapositively, "if $s$ then $r$" ($s \rightarrow r$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-8].
*   **"r is a necessary and sufficient condition for s"**: This means "$r$, if and only if, $s$" ($r \leftrightarrow s$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-2].

## 2.3 Valid and Invalid Arguments

### Arguments and Validity

An **argument** (or **argument form**) is a sequence of statements, where all statements except the final one are called **premises** (or assumptions or hypotheses), and the final statement is the **conclusion** [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-10]. The symbol '$\therefore$' (read "therefore") is typically placed before the conclusion [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3].

An argument form is **valid** if, and only if, whenever all premises are true, the conclusion is also true. The truth of the conclusion is said to be **inferred** or **deduced** from the truth of the premises [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-10]. If the conclusion does not necessarily follow from true premises, the argument is invalid [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3].

### Determining Validity

To test an argument form for validity [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3]:
1.  Identify the premises and conclusion.
2.  Construct a truth table showing the truth values for all premises and the conclusion.
3.  Identify **critical rows**: rows in the truth table where all premises are true.
    *   If there is a critical row where the conclusion is false, the argument form is **invalid**.
    *   If the conclusion is true in every critical row, the argument form is **valid**.

Alternatively, an argument with premises $P_1, P_2, \dots, P_k$ and conclusion $Q$ is valid if and only if the statement form $(P_1 \land P_2 \land \dots \land P_k) \rightarrow Q$ is a tautology [source:cs1231s-tutorial-tut01ans-post-pdf#section-1].

### Syllogism and Basic Rules of Inference

A **syllogism** is an argument form consisting of two premises and a conclusion [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3].

Common valid argument forms are known as **rules of inference** [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3].

*   **Modus Ponens** (Method of Affirming) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3, csheatsheet-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-11]:
    If $p$ then $q$
    $p$
    $\therefore q$

*   **Modus Tollens** (Method of Denying) [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3, csheatsheet-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-11]:
    If $p$ then $q$
    $\sim q$
    $\therefore \sim p$

### Additional Rules of Inference

| Rule of Inference                   | Form (Premises above line, Conclusion below)                                                                         |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **Generalization** [source:cs1231s-cscheatsheet-pdf#section-1] | $p$ <br/> $\therefore p \lor q$ (and $q$ <br/> $\therefore p \lor q$)                                                |
| **Specialization** [source:cs1231s-cscheatsheet-pdf#section-1] | $p \land q$ <br/> $\therefore p$ (and $p \land q$ <br/> $\therefore q$)                                                |
| **Conjunction** [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3] | $p$ <br/> $q$ <br/> $\therefore p \land q$                                                                    |
| **Elimination** [source:cs1231s-cscheatsheet-pdf#section-1]     | $p \lor q$ <br/> $\sim q$ <br/> $\therefore p$ (and $p \lor q$ <br/> $\sim p$ <br/> $\therefore q$)               |
| **Transitivity** [source:cs1231s-cscheatsheet-pdf#section-1]    | $p \rightarrow q$ <br/> $q \rightarrow r$ <br/> $\therefore p \rightarrow r$                                      |
| **Proof by Division into Cases** [source:cs1231s-cscheatsheet-pdf#section-1] | $p \lor q$ <br/> $p \rightarrow r$ <br/> $q \rightarrow r$ <br/> $\therefore r$                                     |
| **Contradiction Rule** [source:cs1231s-cscheatsheet-pdf#section-1] | $\sim p \rightarrow \text{false}$ (or a contradiction) <br/> $\therefore p$                                          |

### Fallacies

A **fallacy** is an error in reasoning that leads to an invalid argument [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3]. Common fallacies include:
1.  **Using ambiguous premises**: Treating premises as unambiguous when they are not.
2.  **Circular reasoning**: Assuming what is to be proved without deriving it from premises.
3.  **Jumping to a conclusion**: Drawing a conclusion without adequate grounds [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3].

Specific types of fallacies related to conditional statements are:

*   **Converse Error (Fallacy of Affirming the Consequence)**: This invalid argument form is structured as:
    If $p$ then $q$
    $q$
    $\therefore p$
    [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3]

*   **Inverse Error**: This invalid argument form is structured as:
    If $p$ then $q$
    $\sim p$
    $\therefore \sim q$
    [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3]

It is crucial to distinguish between a **valid argument** and an argument with a **true conclusion**. An argument can be valid even if its premises (and thus conclusion) are false, and an argument can be invalid even if its premises and conclusion are true [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3].

### Sound and Unsound Arguments

An argument is called **sound** if, and only if, it is both valid and all its premises are true. An argument that is not sound is called **unsound** [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-summary-pdf#section-10].

### Contradiction Rule and Proof by Contradiction

The **contradiction rule** states that if you can show that the supposition that a statement $p$ is false leads logically to a contradiction, then you can conclude that $p$ is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3]. This rule is the logical foundation of **proof by contradiction** [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3]. A common variation used in solving puzzles is: if an assumption leads to a contradiction, then that assumption must be false [source:cs1231s-cs1231s-extra-lecture-slides-lecture02-logicofcompoundstatements-full-pdf#section-3].

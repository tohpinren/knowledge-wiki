---
page_id: "y1s1-cs1231s-lecture-13-rooted-trees-traversals"
title: "Lecture 13: Rooted Trees and Traversals"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Delves into specialized tree structures such as rooted trees, defining terms like parent, child, sibling, and exploring traversal methods (e.g., pre-order, in-order, post-order)."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2"
  - "cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2"
  - "cs1231s-tutorial-tut11ans-post-pdf#section-3"
  - "cs1231s-tutorial-tut11qns-pdf#section-2"
topics:
  - "tree"
  - "trees"
  - "vertex"
  - "vertices"
  - "binary"
  - "graph"
  - "spanning"
  - "has"
  - "root"
  - "edges"
source_count: 4
lecture_number: 13
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 13: Rooted Trees and Traversals

This page delves into specialized tree structures, defining terms like parent, child, sibling, and exploring traversal methods such as pre-order, in-order, and post-order. It also introduces spanning trees and minimum spanning tree algorithms.

## 10.5 Trees: Definitions and Characterization

A **graph** is said to be **circuit-free** if it contains no circuits [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-1].
A **tree** is a graph that is circuit-free and connected [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-1].
A **trivial tree** consists of a single vertex [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-1].
A **forest** is a graph that is circuit-free and not connected [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-1].

Trees are widely used in computer science to store hierarchically ordered data, such as in computer file systems, abstract syntax trees (for representing algebraic expressions), and binary search trees [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1].

### Characterizing Trees

**Lemma 10.5.1:** Any non-trivial tree has at least one vertex of degree 1 [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   **Proof Idea:** Start at an arbitrary vertex $v$ and an edge $e$ incident on it. If $deg(v) > 1$, move along another edge $e'$ to a new vertex $v'$. Repeat this process. Since the tree is finite and circuit-free, this process must eventually terminate at a vertex with degree 1 [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1]. (A non-trivial tree actually has at least two vertices of degree 1).

**Definitions: Terminal (Leaf) and Internal Vertices**
Let $T$ be a tree.
*   If $T$ has only one or two vertices, each is called a **terminal vertex** (or **leaf**) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-1].
*   If $T$ has at least three vertices, a vertex of degree 1 in $T$ is called a **terminal vertex** (or **leaf**) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-1].
*   A vertex of degree greater than 1 in $T$ is called an **internal vertex** [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-1].

**Theorem 10.5.2:** Any tree with $n$ vertices ($n > 0$) has $n-1$ edges [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   **Proof Idea (by Mathematical Induction):**
    *   **Base Case P(1):** A tree with one vertex has zero edges ($1-1=0$). True.
    *   **Inductive Hypothesis P(k):** Assume a tree with $k$ vertices has $k-1$ edges.
    *   **Inductive Step P(k+1):** Consider a tree $T$ with $k+1$ vertices. By Lemma 10.5.1, $T$ has a vertex $v$ of degree 1. Removing $v$ and its incident edge $e$ results in a subgraph $T'$ with $k$ vertices. $T'$ is also connected and circuit-free, so it's a tree. By the inductive hypothesis, $T'$ has $k-1$ edges. Since $T$ was formed by adding one edge to $T'$, $T$ has $(k-1) + 1 = k$ edges. Thus, $P(k+1)$ is true [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1].

**Lemma 10.5.3:** If $G$ is any connected graph, $C$ is any circuit in $G$, and one of the edges of $C$ is removed from $G$, then the graph that remains is still connected [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2, cs1231s-tutorial-tut11ans-post-pdf#section-1].
*   **Reasoning:** Any two vertices in a circuit are connected by at least two distinct paths. Removing one edge along one path still leaves another path, ensuring connectivity [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1].

**Theorem 10.5.4:** If $G$ is a connected graph with $n$ vertices and $n-1$ edges, then $G$ is a tree [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   **Proof Idea (by Contradiction):**
    *   Assume $G$ is connected with $n$ vertices and $n-1$ edges, but it is *not* circuit-free.
    *   If $G$ contains a circuit, by Lemma 10.5.3, we can remove an edge from the circuit, and the graph remains connected. Repeat this process until all circuits are removed, resulting in a new graph $G''$ that is connected and circuit-free (i.e., a tree).
    *   Since no vertices were removed, $G''$ still has $n$ vertices. By Theorem 10.5.2, $G''$ must have $n-1$ edges.
    *   However, because we removed at least one edge from $G$ to form $G''$ (as we supposed $G$ had circuits), $G''$ would have fewer than $n-1$ edges. This contradicts the conclusion that $G''$ must have $n-1$ edges.
    *   Therefore, the initial supposition that $G$ is not circuit-free must be false, meaning $G$ is circuit-free and thus a tree [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-1].

## 10.6 Rooted Trees

A **rooted tree** is a tree in which one vertex is distinguished from the others and is called the **root** [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].

For any vertex in a rooted tree:
*   The **level** of a vertex is the number of edges along the unique path between it and the root [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2]. The root is at level 0.
*   The **height** of a rooted tree is the maximum level of any vertex in the tree [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].

**Terminology for Relationships in Rooted Trees:**
Given the root or any internal vertex $v$ of a rooted tree:
*   The **children** of $v$ are all those vertices that are adjacent to $v$ and are one level farther away from the root than $v$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   If $w$ is a child of $v$, then $v$ is called the **parent** of $w$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   Two distinct vertices that are both children of the same parent are called **siblings** [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   Given two distinct vertices $v$ and $w$, if $v$ lies on the unique path between $w$ and the root, then $v$ is an **ancestor** of $w$, and $w$ is a **descendant** of $v$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].

### Binary Trees

A **binary tree** is a rooted tree in which every parent has at most two children. Each child is designated as either a left child or a right child (but not both), and every parent has at most one left child and one right child [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].

A **full binary tree** is a binary tree in which each parent has exactly two children [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].

**Definitions: Left Subtree, Right Subtree**
Given any parent $v$ in a binary tree $T$:
*   If $v$ has a left child, the **left subtree** of $v$ is the binary tree whose root is the left child of $v$, whose vertices consist of the left child of $v$ and all its descendants, and whose edges connect these vertices [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   The **right subtree** of $v$ is defined analogously [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].

Binary trees can represent algebraic expressions, where internal vertices are operators and terminal vertices are variables. Operators act on their left and right subtrees in left-right order (e.g., `a / (c + d)`) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2].

**Theorem 10.6.1: Full Binary Tree Theorem**
If $T$ is a full binary tree with $k$ internal vertices, then $T$ has a total of $2k+1$ vertices and $k+1$ terminal vertices (leaves) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   **Proof Idea:**
    1.  Every vertex except the root has a parent.
    2.  Each internal vertex has exactly two children. So, the number of vertices with a parent is $2k$.
    3.  The total number of vertices in $T$ is (number of vertices with a parent) + (number of vertices without a parent, i.e., the root) $= 2k + 1$.
    4.  The number of terminal vertices is (total vertices) - (internal vertices) $= (2k+1) - k = k+1$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2].

**Theorem 10.6.2: Height and Terminal Vertices of a Binary Tree**
For non-negative integers $h$, if $T$ is any binary tree with height $h$ and $t$ terminal vertices (leaves), then $t \le 2^h$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
Equivalently, $\log_2 t \le h$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2].
*   This means the maximum number of terminal vertices for a binary tree of height $h$ is $2^h$.
*   **Proof Idea (by Strong Mathematical Induction on height h):**
    *   **P(h):** "If $T$ is any binary tree of height $h$, then the number of leaves of $T$ is at most $2^h$."
    *   **Base Case P(0):** A tree of height 0 consists of one vertex (the root), which is also a terminal vertex. $t=1=2^0$. True.
    *   **Inductive Hypothesis:** Assume $P(i)$ is true for all integers $i$ from $0$ through $k$.
    *   **Inductive Step P(k+1):** Consider a binary tree $T$ of height $k+1$ with root $v$ and $t$ leaves. Since $k+1 \ge 1$, $v$ has at least one child.
        *   **Case 1: $v$ has only one child ($v_L$ or $v_R$).** Let $T_L$ be the subtree rooted at $v_L$. $T_L$ has height $k$ (one less than $T$). $v$ itself is a leaf (degree 1). The total number of leaves in $T$ is $t = t_L + 1$. By inductive hypothesis, $t_L \le 2^k$. Therefore, $t = t_L + 1 \le 2^k + 1 \le 2^k + 2^k = 2^{k+1}$ (since $k+1 \ge 1$, $2^k \ge 1$).
        *   **Case 2: $v$ has two children ($v_L$ and $v_R$).** Let $T_L$ and $T_R$ be the left and right subtrees rooted at $v_L$ and $v_R$, respectively. Let their heights be $h_L$ and $h_R$, and their number of leaves be $t_L$ and $t_R$. Since $T_L$ and $T_R$ are subtrees of $T$ obtained by joining $T_L$ and $T_R$ and adding a level, $h_L \le k$ and $h_R \le k$. The total number of leaves in $T$ is $t = t_L + t_R$. By inductive hypothesis, $t_L \le 2^{h_L}$ and $t_R \le 2^{h_R}$. Therefore, $t = t_L + t_R \le 2^{h_L} + 2^{h_R} \le 2^k + 2^k = 2 \cdot 2^k = 2^{k+1}$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2].
    *   In both cases, $P(k+1)$ is true. Hence, the theorem holds by strong induction.

### Binary Tree Traversal

**Tree traversal** (also known as tree search) is the process of visiting each node in a tree data structure exactly once in a systematic manner [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2].
There are two main types of traversal: Breadth-First Search (BFS) and Depth-First Search (DFS) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2]. While described for binary trees, these methods can be applied to any type of tree or graph.

**1. Breadth-First Search (BFS)**
In BFS (introduced by E.F. Moore), traversal starts at the root, visits its adjacent vertices, and then proceeds to the next level of vertices [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2]. It explores all nodes at the current depth level before moving on to nodes at the next depth level.

**2. Depth-First Search (DFS)**
There are three types of depth-first traversal for binary trees, each defining the order in which the root and its left/right subtrees are visited [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2, cs1231s-tutorial-tut11qns-pdf#section-1].
*   **Pre-order Traversal (Root-Left-Right):**
    1.  Print the data of the root (or current vertex).
    2.  Traverse the left subtree by recursively calling the pre-order function.
    3.  Traverse the right subtree by recursively calling the pre-order function [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   **In-order Traversal (Left-Root-Right):**
    1.  Traverse the left subtree by recursively calling the in-order function.
    2.  Print the data of the root (or current vertex).
    3.  Traverse the right subtree by recursively calling the in-order function [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].
*   **Post-order Traversal (Left-Right-Root):**
    1.  Traverse the left subtree by recursively calling the post-order function.
    2.  Traverse the right subtree by recursively calling the post-order function.
    3.  Print the data of the root (or current vertex) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-2].

## 10.7 Spanning Trees and Shortest Paths

A **spanning tree** for a graph $G$ is a subgraph of $G$ that contains every vertex of $G$ and is a tree [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3]. A spanning tree connects all vertices using the minimum possible number of edges. If a graph were to contain a circuit, one edge from that circuit could be removed without disconnecting the graph (by Lemma 10.5.3), resulting in a smaller number of routes [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-3].

**Proposition 10.7.1:**
1.  Every connected graph has a spanning tree.
2.  Any two spanning trees for a graph have the same number of edges [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3].

### Minimum Spanning Trees

A **weighted graph** is a graph for which each edge has an associated positive real number called a **weight**. The sum of the weights of all the edges is the **total weight** of the graph [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3].

A **minimum spanning tree (MST)** for a connected weighted graph is a spanning tree that has the least possible total weight compared to all other spanning trees for the graph [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3].

#### Kruskal's Algorithm (Joseph B. Kruskal, 1956)

Kruskal's algorithm finds an MST by examining the edges of a connected weighted graph one by one in order of increasing weight [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3].
At each stage, an edge is added to the developing MST, provided that its addition does not create a circuit. The process continues until $n-1$ edges have been added (where $n$ is the number of vertices), forming an MST [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-5].

**Algorithm 10.7.1 Kruskal:**
1.  Initialize $T$ to have all vertices of $G$ and no edges.
2.  Let $E$ be the set of all edges of $G$, and let $m = 0$.
3.  While $(m < n-1)$:
    a.  Find an edge $e$ in $E$ of least weight.
    b.  Delete $e$ from $E$.
    c.  If adding $e$ to the edge set of $T$ does not produce a circuit, then add $e$ to the edge set of $T$ and set $m = m+1$.
4.  Output: $T$ (which is a minimum spanning tree for $G$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3].

If multiple edges have the same weight, the order in which they are considered might affect the exact edges in the MST, but not its total weight. To ensure a unique output, edges with the same weight can be ordered based on their appearance in an array [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-5].

#### Prim's Algorithm (Robert C. Prim, 1957)

Prim's algorithm builds an MST by expanding outward from an initial vertex in connected links [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3].
At each stage, one edge and one vertex are added to the growing tree. The chosen edge is always the one of least weight that connects a vertex already in the current tree $T$ to a vertex not yet in $T$. The new vertex added is the endpoint of this edge that is not already in $T$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-6].

**Algorithm 10.7.2 Prim:**
1.  Pick a vertex $v$ of $G$ and let $T$ be the graph with only this vertex.
2.  Let $V'$ be the set of all vertices of $G$ except $v$.
3.  For $i = 1$ to $n-1$:
    a.  Find an edge $e$ of $G$ such that (1) $e$ connects $T$ to one of the vertices in $V'$, and (2) $e$ has the least weight of all edges connecting $T$ to a vertex in $V'$. Let $w$ be the endpoint of $e$ that is in $V'$.
    b.  Add $e$ and $w$ to the edge and vertex sets of $T$, and delete $w$ from $V'$.
4.  Output: $T$ (which is a minimum spanning tree for $G$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-6, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3].

Prim's algorithm will yield an MST with the same total weight as Kruskal's algorithm, though the sequence of edges added may differ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-6]. Similar to Kruskal's, consistent ordering for same-weight edges can ensure unique output.

### Dijkstra's Shortest Path Algorithm (Non-Examinable)

**Note:** Dijkstra's Shortest Path Algorithm is **non-examinable** for this semester [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7, cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-summary-pdf#section-3]. The information is retained for personal reading.

Developed by Edsger Dijkstra in 1959, this algorithm finds the shortest path between a starting vertex (source) and an ending vertex (destination) in a weighted graph where all edge weights are positive [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7].

**Intuition:**
*   It reports vertices in increasing order of their distance from the source vertex.
*   It constructs a shortest path tree edge by edge, adding a new edge at each step to build the shortest path to the current new vertex [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7].

The algorithm works outward from a source vertex $a$, adding vertices and edges to construct a shortest path tree $T$. It differs from Prim's algorithm in how it chooses the next vertex, ensuring that for each added vertex $v$, the length of the shortest path from $a$ to $v$ is identified [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7].

**Algorithm 10.7.3 Dijkstra:**
**Inputs:**
*   $G$: a connected simple graph with positive weight $w(u, v)$ for every edge $\{u, v\}$.
*   $\infty$: a number greater than the sum of all edge weights in $G$.
*   $a$: the source vertex.
*   $z$: the destination vertex [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7].

**Algorithm:**
1.  Initialize $T$ as a graph with vertex $a$ and no edges. Let $V(T)$ be $a$, and $E(T)$ be empty.
2.  Set $L(a) \leftarrow 0$. For all other vertices $u$ in $G$ except $a$, set $L(u) \leftarrow \infty$. ($L(u)$ is the current shortest path estimate from $a$ to $u$).
3.  Initialize $v \leftarrow a$ and $F \leftarrow \{a\}$ ($v$ is the most recently added vertex to $T$, $F$ is the set of "fringe" vertices) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7].
4.  While ($z \notin V(T)$):
    a.  Update the set of fringe vertices $F$: $F \leftarrow (F - \{v\}) \cup \{ \text{vertices } u \in \text{Adj}(v) \text{ and } u \notin V(T) \}$.
    b.  For each vertex $u \in \text{Adj}(v)$ and $u \notin V(T)$:
        If $L(v) + w(v, u) < L(u)$, then update $L(u) \leftarrow L(v) + w(v, u)$ and set $D(u) \leftarrow v$. ($D(u)$ tracks the predecessor that provided the shorter path).
    c.  Find a vertex $x$ in $F$ with the smallest label $L(x)$.
    d.  Add vertex $x$ to $V(T)$, and add edge $\{D(x), x\}$ to $E(T)$. Set $v \leftarrow x$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7].
5.  Output: $L(z)$ (this is the length of the shortest path from $a$ to $z$) [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7].

The graph $G$ is conceptually divided into three parts: the shortest path tree $T$ being built, the "fringe" vertices (candidates to join $T$), and the rest of the vertices in $G$. At each step, the fringe vertex with the minimum shortest path length from the source (through $T$) is chosen to be added to $T$ [source:cs1231s-cs1231s-extra-lecture-slides-lecture13-trees-pdf#section-7].

---
page_id: "y1s1-cs1231s-lecture-12-types-connectivity-graphs"
title: "Lecture 12: Types of Graphs and Connectivity"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1231s"
parent_page_id: "y1s1-cs1231s-hub"
batch_id: "y1s1-cs1231s-20260412t085135z"
status: "canonical"
summary: "Introduces various types of graphs (e.g., simple, complete, bipartite) and concepts related to graph connectivity, paths, and circuits."
aliases:
tags:
  - "course"
  - "cs1231s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2"
  - "cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1"
  - "cs1231s-cs1231s-extra-tutorials-tutorial-11-tut11qns-pdf#section-1"
topics:
  - "graph"
  - "vertices"
  - "edges"
  - "vertex"
  - "number"
  - "circuit"
  - "connected"
  - "every"
  - "has"
  - "graphs"
source_count: 3
lecture_number: 12
last_compiled_at: "2026-04-12T09:37:26+00:00"
---
# Lecture 12: Types of Graphs and Connectivity

## Lecture 12: Types of Graphs and Connectivity

Graph theory, a field of discrete mathematics, offers a powerful tool for modeling pairwise relationships between objects. Its origins trace back to Leonhard Euler's work on the Königsberg bridges problem in 1736 [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-1]. Graphs are widely applied in computer science for data structures, network design, image processing, GPS, search engines, and social network analysis, as well as in other areas like modeling disease spread [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-1].

### 10.1 Graphs: Definitions and Basic Properties

#### Types of Graphs (Informal Introduction)

Informally, graphs can be categorized by their characteristics [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-1]:
*   **Undirected Graphs**: Edges have no specific direction.
*   **Directed Graphs (Digraphs)**: Edges have a direction, often represented by arrows.
*   **Directed Acyclic Graphs (DAGs)**: Directed graphs that contain no directed cycles.
*   **Weighted Graphs**: Edges are assigned numerical values (weights), which can represent distances, costs, or capacities.

#### Formal Definitions of Graphs

A graph, denoted $G = (V, E)$, consists of two finite sets [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1]:
*   $V$: A nonempty set of **vertices** (or nodes).
*   $E$: A set of **edges**.

##### Undirected Graphs

An **undirected graph** $G$ consists of a nonempty set $V$ of vertices and a set $E$ of undirected edges. Each edge is associated with a set of either one or two vertices, called its **endpoints** [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
*   An edge $e$ connecting vertices $v$ and $w$ is denoted as $e = \{v, w\}$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
*   An edge is said to **connect** its endpoints.
*   Two vertices connected by an edge are called **adjacent vertices**. A vertex that is an endpoint of a loop is adjacent to itself [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].
*   An edge is said to be **incident on** each of its endpoints. Two edges incident on the same endpoint are called **adjacent edges** [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].
*   A **loop** is an edge that connects a vertex to itself (i.e., its endpoints are the same vertex) [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].
*   **Parallel edges** occur when two or more edges connect the same pair of vertices [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].
*   An **isolated vertex** is a vertex that has no incident edges [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].

##### Directed Graphs

A **directed graph**, or **digraph**, $G$ consists of a nonempty set $V$ of vertices and a set $E$ of directed edges. Each directed edge is associated with an **ordered pair** of vertices $(v, w)$ called its endpoints. The edge goes from vertex $v$ to vertex $w$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
*   We write $e = (v, w)$ for a directed edge $e$ from vertex $v$ to vertex $w$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].

#### Modelling Graph Problems: Vertex Colouring

Many real-world problems can be modeled using graphs, particularly with the concept of **vertex colouring** [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].
A **vertex colouring** of a graph is an assignment of colours to vertices such that no two adjacent vertices have the same colour [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].

Examples include:
*   **Map Colouring Problem**: Regions on a map are vertices, and an edge connects two regions if they share a common border. The goal is to colour adjacent regions differently using the minimum number of colours. The Four-Colour Conjecture states that four colours are sufficient for any map in a plane [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].
*   **Wedding Planner Problem**: Guests are vertices, and an edge connects two guests if they don't get along. The problem is to seat guests at the minimum number of tables such that no two conflicting guests share a table, equivalent to finding the minimum number of colours for the graph.
*   **Scheduling Classes**: Classes are vertices, and an edge connects two classes if they have students in common. Vertex colouring can be used to schedule non-overlapping classes.
*   **Radio Station Frequency Assignment**: Radio stations are vertices, and an edge connects two stations if they are close enough to interfere. Vertex colouring helps assign non-interfering frequencies.
*   **Traffic Signals**: Traffic signals at an intersection are vertices, and an edge connects two signals if they cannot be green at the same time. Vertex colouring can designate sets of signals that can be green concurrently.

#### Special Types of Graphs

*   **Simple Graph**: An undirected graph that has **no loops** and **no parallel edges**. There is at most one edge between each pair of distinct vertices [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
*   **Complete Graph ($K_n$)**: A simple graph on $n$ vertices ($n > 0$) where there is exactly one edge connecting each pair of distinct vertices [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
    *   The number of edges in $K_n$ is $n(n-1)/2$.
*   **Bipartite Graph (Bigraph)**: A simple graph whose vertices can be divided into two disjoint sets, $U$ and $V$, such that every edge connects a vertex in $U$ to one in $V$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
*   **Complete Bipartite Graph ($K_{m,n}$)**: A bipartite graph on two disjoint sets $U$ and $V$ (with $|U|=m$ and $|V|=n$) such that every vertex in $U$ connects to every vertex in $V$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
*   **Subgraph**: A graph $H$ is a subgraph of graph $G$ if and only if every vertex in $H$ is also a vertex in $G$, every edge in $H$ is also an edge in $G$, and every edge in $H$ has the same endpoints as it has in $G$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
*   **Complement of a Simple Graph ($\bar{G}$)**: If $G$ is a simple graph, its complement $\bar{G}$ has the same vertex set as $G$. However, two distinct vertices $v$ and $w$ are connected by an edge in $\bar{G}$ if and only if $v$ and $w$ are *not* connected by an edge in $G$ [source: cs1231s-cs1231s-extra-tutorials-tutorial-11-tut11qns-pdf#section-2].
*   **Self-complementary Graph**: A graph that is isomorphic with its complement [source: cs1231s-cs1231s-extra-tutorials-tutorial-11-tut11qns-pdf#section-2].
*   **Triangle**: A simple circuit (cycle) of length three [source: cs1231s-cs1231s-extra-tutorials-tutorial-11-tut11qns-pdf#section-2].

#### The Concept of Degree

For an undirected graph $G$ and a vertex $v \in V$:
*   **Degree of $v$ ($\text{deg}(v)$)**: The number of edges incident on $v$. An edge that is a loop is counted twice [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].
*   **Total Degree of $G$**: The sum of the degrees of all vertices in $G$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].

##### Handshake Theorem

**Theorem 10.1.1 (The Handshake Theorem)**: If $G$ is any graph with vertices $v_1, v_2, \ldots, v_n$ ($n \ge 0$), then the sum of the degrees of all vertices equals twice the number of edges in $G$.
Symbolically, $\text{Total degree of } G = \sum_{i=1}^{n} \text{deg}(v_i) = 2 \times (\text{number of edges in } G)$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].

**Corollary 10.1.2**: The total degree of any graph is an even number [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].

**Proposition 10.1.3**: In any graph, there is an even number of vertices that have an odd degree [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-1].

For directed graphs, each vertex has an **indegree** (number of incoming edges) and an **outdegree** (number of outgoing edges), but these are not covered in detail here [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-2].

### 10.2 Trails, Paths, and Circuits

#### The Königsberg Bridge Problem Revisited

Graph theory's origin is often attributed to Leonhard Euler's solution to the Königsberg bridges problem in 1736 [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3]. The problem asked if it was possible to take a walk around the town, starting and ending at the same location, and crossing each of its seven bridges exactly once. This translates to finding a route through a graph (where landmasses are vertices and bridges are edges) that starts and ends at the same vertex and traverses each edge exactly once [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3].

#### Definitions of Graph Traversal

Travel in a graph is accomplished by moving from one vertex to another along a sequence of adjacent edges [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3].

*   **Walk from $v$ to $w$**: A finite alternating sequence of adjacent vertices and edges of $G$, starting at $v$ and ending at $w$. The length of the walk is the number of edges in the sequence [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
    *   **Trivial walk**: A walk from $v$ to $v$ consisting only of the single vertex $v$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
*   **Trail from $v$ to $w$**: A walk from $v$ to $w$ that does not contain a repeated edge [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
*   **Path from $v$ to $w$**: A trail from $v$ to $w$ that does not contain a repeated vertex [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
*   **Closed walk**: A walk that starts and ends at the same vertex [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
*   **Circuit (or cycle)**: An undirected graph $G=(V, E)$ where $V = \{x_1, \ldots, x_n\}$ and $E = \{\{x_1, x_2\}, \ldots, \{x_{n-1}, x_n\}, \{x_n, x_1\}\}$ for $n \in \mathbb{Z}_{\ge 3}$. A cycle is a closed walk that does not contain a repeated edge [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
*   **Simple circuit (or simple cycle)**: A circuit that does not have any other repeated vertex except the first and last [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
*   **Cyclic graph**: An undirected graph is cyclic if it contains a loop or a cycle [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
*   **Acyclic graph**: An undirected graph that is not cyclic [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

For CS1231S, we follow the terminology used in Epp's textbook [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3].

#### Connectedness

*   **Connected vertices**: Two vertices $v$ and $w$ of a graph $G=(V,E)$ are connected if and only if there is a walk from $v$ to $w$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
*   **Connected graph**: A graph $G$ is connected if and only if for any two vertices $v$ and $w$ in $G$, there is a walk from $v$ to $w$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

**Lemma 10.2.1**:
a. If $G$ is connected, then any two distinct vertices of $G$ can be connected by a path.
b. If vertices $v$ and $w$ are part of a circuit in $G$ and one edge is removed from the circuit, then there still exists a trail from $v$ to $w$ in $G$.
c. If $G$ is connected and $G$ contains a circuit, then an edge of the circuit can be removed without disconnecting $G$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

*   **Connected Component**: A graph $H$ is a connected component of a graph $G$ if and only if:
    1.  $H$ is a subgraph of $G$.
    2.  $H$ is connected.
    3.  No connected subgraph of $G$ has $H$ as a subgraph and contains vertices or edges that are not in $H$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

#### Euler Circuits and Trails

An **Euler circuit** for a graph $G$ is a circuit that contains every vertex and traverses every edge of $G$ exactly once [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
An **Eulerian graph** is a graph that contains an Euler circuit [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

**Theorem 10.2.2**: If a graph has an Euler circuit, then every vertex of the graph has a positive even degree [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
**Contrapositive Version of Theorem 10.2.2**: If some vertex of a graph has an odd degree, then the graph does not have an Euler circuit [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

**Theorem 10.2.3**: If a graph $G$ is connected and the degree of every vertex of $G$ is a positive even integer, then $G$ has an Euler circuit [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

**Theorem 10.2.4**: A graph $G$ has an Euler circuit if and only if $G$ is connected and every vertex of $G$ has a positive even degree [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

An **Euler trail/path from $v$ to $w$** is a sequence of adjacent edges and vertices that starts at $v$, ends at $w$, passes through every vertex of $G$ at least once, and traverses every edge of $G$ exactly once [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

**Corollary 10.2.5**: Let $G$ be a graph, and let $v$ and $w$ be two distinct vertices of $G$. There is an Euler trail from $v$ to $w$ if and only if $G$ is connected, $v$ and $w$ have an odd degree, and all other vertices of $G$ have a positive even degree [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

#### Hamiltonian Circuits

A **Hamiltonian circuit** for a graph $G$ is a simple circuit that includes every vertex of $G$. This means every vertex appears exactly once, except for the first and the last, which are the same [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].
A **Hamiltonian graph** (or Hamilton graph) is a graph that contains a Hamiltonian circuit [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2].

The problem of finding a Hamiltonian circuit was introduced by Sir William Rowan Hamilton in 1859 with a puzzle involving a dodecahedron [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3]. The problem was to tour all cities (vertices) exactly once and return to the starting city.

**Distinction between Euler and Hamiltonian Circuits**:
*   An Euler circuit must include *every edge* of $G$ and may visit some vertices more than once.
*   A Hamiltonian circuit must include *every vertex* of $G$ exactly once (except start/end) but does not need to include all edges [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3].

Unlike Euler circuits, there is no simple analogous criterion for determining whether a graph has a Hamiltonian circuit, nor is there an efficient algorithm to find one [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3].

**Proposition 10.2.6**: If a graph $G$ has a Hamiltonian circuit, then $G$ has a subgraph $H$ with the following properties:
1.  $H$ contains every vertex of $G$.
2.  $H$ is connected.
3.  $H$ has the same number of edges as vertices.
4.  Every vertex of $H$ has degree 2.
The contrapositive states that if a graph $G$ does *not* have a subgraph $H$ with these properties, then $G$ does not have a Hamiltonian circuit [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-2]. This proposition provides a technique to show a graph *does not* have a Hamiltonian circuit.

**Travelling Salesman Problem (TSP)**: This problem involves finding a Hamiltonian circuit in a weighted graph that minimizes the total weight (e.g., distance) of the circuit. While one can list all possible Hamiltonian circuits and compute their total weights, this method is impractical for large graphs due to computational complexity (e.g., $N=30$ vertices results in approximately $4.42 \times 10^{30}$ circuits). Efficient algorithms exist that find "pretty good" solutions, though not necessarily optimal ones [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-3].

### 10.3 Matrix Representations of Graphs

Graphs can be represented using matrices, which are rectangular arrays of elements.
An $m \times n$ matrix $A$ over a set $S$ has $m$ rows and $n$ columns. A **square matrix** has an equal number of rows and columns ($n \times n$). The **main diagonal** of a square matrix consists of entries $a_{11}, a_{22}, \ldots, a_{nn}$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4].

#### Adjacency Matrix

*   **Adjacency Matrix of a Directed Graph**: For a directed graph $G$ with ordered vertices $v_1, v_2, \ldots, v_n$, the adjacency matrix $A = (a_{ij})$ is an $n \times n$ matrix where $a_{ij}$ is the number of arrows (directed edges) from vertex $v_i$ to vertex $v_j$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-3].
*   **Adjacency Matrix of an Undirected Graph**: For an undirected graph $G$ with ordered vertices $v_1, v_2, \ldots, v_n$, the adjacency matrix $A = (a_{ij})$ is an $n \times n$ matrix where $a_{ij}$ is the number of edges connecting $v_i$ and $v_j$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-3].
    *   An adjacency matrix for an undirected graph is always **symmetric**, meaning $a_{ij} = a_{ji}$ for all $i, j$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-3].

Another common representation of a graph is the adjacency list, covered in algorithms modules [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4].

#### Matrix Multiplication

*   **Scalar Product (Dot Product)**: The scalar product of the $i$-th row of matrix $A$ and the $j$-th column of matrix $B$ is the sum of the products of their corresponding entries [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4].
*   **Matrix Product ($AB$)**: If $A$ is an $m \times k$ matrix and $B$ is a $k \times n$ matrix, their product $AB$ is an $m \times n$ matrix $(c_{ij})$ where $c_{ij}$ is the scalar product of the $i$-th row of $A$ and the $j$-th column of $B$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4].
    *   Matrix multiplication is **not commutative** ($AB \ne BA$ in general) but is **associative** $((AB)C = A(BC))$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4].
*   **Identity Matrix ($I_n$)**: For a positive integer $n$, the $n \times n$ identity matrix $I_n = (\delta_{ij})$ is a square matrix where all entries on the main diagonal are $1$'s and all other entries are $0$'s. $\delta_{ij} = 1$ if $i=j$ and $0$ if $i \ne j$. This symbol is known as the Kronecker delta [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4].
*   **$n^{th}$ Power of a Matrix ($A^n$)**: For any $n \times n$ matrix $A$:
    *   $A^0 = I$ (the $n \times n$ identity matrix).
    *   $A^n = A A^{n-1}$ for all integers $n \ge 1$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-3].

#### Counting Walks of Length $N$

**Theorem 10.3.2**: If $G$ is a graph with vertices $v_1, v_2, \ldots, v_m$ and $A$ is its adjacency matrix, then for each positive integer $n$ and for all integers $i, j = 1, 2, \ldots, m$, the $ij$-th entry of $A^n$ equals the number of walks of length $n$ from $v_i$ to $v_j$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-4, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-3].

### 10.4 Isomorphisms of Graphs and Planar Graphs

#### Isomorphisms of Graphs

Two graphs $G$ and $G'$ are considered **isomorphic** if they are essentially the same graph, differing only in the labeling of their vertices and edges. This means there's a matching between their vertices such that two vertices are connected by an edge in $G$ if and only if their corresponding vertices are connected by an edge in $G'$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-4].

**Definition: Isomorphic Graph**: Let $G = (V_G, E_G)$ and $G' = (V_{G'}, E_{G'})$ be two graphs. $G$ is isomorphic to $G'$ (denoted $G \cong G'$) if and only if there exist bijections $g: V_G \to V_{G'}$ and $h: E_G \to E_{G'}$ that preserve the edge-endpoint functions of $G$ and $G'$ in the sense that for all $v \in V_G$ and $e \in E_G$, $v$ is an endpoint of $e \iff g(v)$ is an endpoint of $h(e)$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-4].

**Alternative Definition**: $G$ is isomorphic to $G'$ if and only if there exists a permutation $\pi: V_G \to V_{G'}$ such that $\{u, v\} \in E_G \iff \{\pi(u), \pi(v)\} \in E_{G'}$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-4].

**Theorem 10.4.1 (Graph Isomorphism is an Equivalence Relation)**: Let $S$ be a set of graphs. The relation of graph isomorphism ($\cong$) on $S$ is an equivalence relation (i.e., it is reflexive, symmetric, and transitive) [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-4].

#### Planar Graphs

A **planar graph** is a graph that can be drawn on a (two-dimensional) plane without any edges crossing [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-4].

**Examples of Non-Planar Graphs**: The complete graph $K_5$ and the complete bipartite graph $K_{3,3}$ are examples of non-planar graphs [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5].

**Kuratowski's Theorem**: A finite graph is planar if and only if it does not contain a subgraph that is a subdivision of the complete graph $K_5$ or the complete bipartite graph $K_{3,3}$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5].

#### Euler's Formula for Planar Graphs

When a planar graph is drawn in a plane, it divides the plane into distinct areas called **regions** or **faces** [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5].

**Euler's Formula**: For a connected planar simple graph $G = (V, E)$ with $e = |E|$ (number of edges) and $v = |V|$ (number of vertices), if $f$ is the number of faces, then:
$f = e - v + 2$ [source: cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-pdf#section-5, cs1231s-cs1231s-extra-lecture-slides-lecture12-graphs-summary-pdf#section-4].

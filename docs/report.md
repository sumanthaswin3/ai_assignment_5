# AI Programming Assignment Report

## Introduction

Artificial Intelligence (AI) techniques are widely used in solving complex problems involving decision-making, optimization, planning, reasoning, and prediction. This project implements several important AI algorithms and concepts including adversarial search algorithms, probabilistic reasoning, knowledge representation, and intelligent recommendation systems.

The assignment includes:

* Minimax Search
* Alpha-Beta Pruning
* Heuristic Alpha-Beta Search
* Monte-Carlo Tree Search
* AI-Based Travel Planner
* Knowledge Graphs
* Bayesian Networks

---

# Objectives

The objectives of this assignment are:

* To understand adversarial search algorithms
* To implement intelligent decision-making techniques
* To design an AI-based recommendation system
* To explore Knowledge Graph technologies
* To implement probabilistic reasoning using Bayesian Networks
* To gain practical experience with AI tools and libraries

---

# Algorithms Implemented

## 1. Minimax Algorithm

The Minimax algorithm is used in two-player games for optimal decision making. It recursively evaluates game states assuming both players play optimally.

### Features

* Recursive search
* Optimal move generation
* Adversarial game strategy

---

## 2. Alpha-Beta Pruning

Alpha-Beta pruning improves Minimax efficiency by eliminating unnecessary branches from the search tree.

### Advantages

* Faster execution
* Reduced computation
* Efficient game tree exploration

---

## 3. Heuristic Alpha-Beta Search

This algorithm combines alpha-beta pruning with heuristic evaluation functions to estimate state utility at limited depth.

### Features

* Depth-limited search
* Heuristic evaluation
* Faster approximate solutions

---

## 4. Monte-Carlo Tree Search (MCTS)

MCTS is a simulation-based search algorithm used in AI game playing systems.

### Phases

* Selection
* Expansion
* Simulation
* Backpropagation

---

# AI-Based Travel Planner

The Travel Planner is an intelligent recommendation system that suggests:

* Tourist places
* Restaurants
* Budget estimations
* Personalized travel plans

The system uses JSON-based knowledge sources to generate recommendations based on user preferences.

---

# Knowledge Graphs

Knowledge Graphs are structured representations of entities and relationships.

Example:

```text id="o6n5lu"
Hyderabad → hasPlace → Charminar
```

Tools explored:

* Neo4j
* RDFLib
* Protégé
* Apache Jena

The project implements a simple RDF-based graph using Python.

---

# Bayesian Networks

Bayesian Networks are probabilistic graphical models used for reasoning under uncertainty.

The project demonstrates:

* Conditional Probability Tables
* Bayesian Inference
* Disease prediction using symptoms

Tool used:

* pgmpy

---

# Results

All algorithms executed successfully.

Outputs generated:

* Optimal game moves
* Search evaluations
* Travel recommendations
* RDF triples
* Bayesian inference probabilities

Screenshots are included in the screenshots folder.

---

# Conclusion

This project provided practical understanding of important AI concepts including:

* Search algorithms
* Intelligent systems
* Knowledge representation
* Probabilistic reasoning

The implementation demonstrates how AI techniques can be applied to real-world problems such as game playing, travel planning, and prediction systems.

# Methodology

## Introduction

This project follows a modular implementation approach where each Artificial Intelligence concept is implemented independently using Python.

The methodology includes:

* Problem analysis
* Algorithm design
* Implementation
* Testing
* Result evaluation

---

# Development Environment

| Component            | Tool                 |
| -------------------- | -------------------- |
| Programming Language | Python               |
| IDE                  | VS Code              |
| Version Control      | Git & GitHub         |
| Libraries            | pgmpy, rdflib, numpy |

---

# Methodology for Search Algorithms

## Minimax Algorithm

### Steps

1. Generate possible game states
2. Evaluate terminal states
3. Apply recursive search
4. Choose optimal move

---

## Alpha-Beta Pruning

### Steps

1. Apply Minimax logic
2. Maintain alpha and beta values
3. Prune unnecessary branches
4. Return optimal result

---

## Heuristic Alpha-Beta Search

### Steps

1. Limit search depth
2. Apply heuristic evaluation
3. Estimate board utility
4. Return approximate best move

---

## Monte-Carlo Tree Search

### Phases

## 1. Selection

Select promising nodes using UCT.

## 2. Expansion

Expand unexplored nodes.

## 3. Simulation

Perform random rollout simulations.

## 4. Backpropagation

Update node statistics.

---

# Methodology for AI Travel Planner

## Steps

1. Collect user preferences
2. Load tourism knowledge base
3. Match places and restaurants
4. Estimate budget
5. Generate travel recommendations

The system uses JSON files as a lightweight knowledge base.

---

# Methodology for Knowledge Graph

## Steps

1. Define entities
2. Define relationships
3. Create RDF triples
4. Store graph using RDFLib

Example:

```text id="5wf7nd"
Hyderabad → hasPlace → Charminar
```

---

# Methodology for Bayesian Network

## Steps

1. Define random variables
2. Create network structure
3. Define Conditional Probability Tables
4. Apply inference algorithms
5. Predict probabilities

The pgmpy library is used for implementation.

---

# Testing Methodology

Testing was performed using:

* Sample game states
* Input validation
* Probabilistic queries
* Travel recommendation examples

Outputs were verified manually.

---

# Result Evaluation

The implemented algorithms successfully demonstrated:

* Optimal search behavior
* Efficient pruning
* Probabilistic reasoning
* Intelligent recommendations
* Knowledge representation

---

# Conclusion

The methodology used in this project helped in understanding the practical implementation of AI algorithms and systems. The modular structure improved maintainability and clarity of the project.

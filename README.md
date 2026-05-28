# AI Programming Assignment

## Overview

This repository contains implementations and demonstrations of important Artificial Intelligence concepts and algorithms including:

* Minimax Search Algorithm
* Alpha-Beta Pruning
* Heuristic Alpha-Beta Search
* Monte-Carlo Tree Search (MCTS)
* AI-Based Travel Planner
* Knowledge Graphs
* Bayesian Networks

The project demonstrates search techniques, intelligent planning systems, knowledge representation, and probabilistic reasoning using Python.

---

# Repository Structure

```text
ai_assignment_5/
│
├── README.md
├── requirements.txt
│
├── algorithms/
│   ├── game.py
│   ├── minimax.py
│   ├── alpha_beta.py
│   ├── heuristic_alpha_beta.py
│   ├── mcts.py
│   └── test_algorithms.py
│
├── travel_planner/
│   ├── travel_planner.py
│   ├── tourist_places.json
│   ├── restaurants.json
│   └── sample_output.txt
│
├── knowledge_graph/
│   ├── knowledge_graph.py
│   └── kg_description.md
│
├── bayesian_network/
│   ├── bayesian_network.py
│   └── bayesian_report.md
│
├── screenshots/
│
└── docs/
    ├── report.md
    └── methodology.md
```

---

# 1. Minimax Search Algorithm

## Description

Minimax is a decision-making algorithm used in adversarial games like Tic-Tac-Toe and Chess. It assumes that both players play optimally.

## Features

* Game tree exploration
* Optimal move selection
* Recursive implementation

## Execution

```bash
cd algorithms
python minimax.py
```

## Sample Output

```text
Best Move: (2, 1)
```

---

# 2. Alpha-Beta Pruning

## Description

Alpha-Beta pruning is an optimization technique for the Minimax algorithm that eliminates unnecessary branches in the search tree.

## Features

* Faster than basic minimax
* Reduces search space
* Improves efficiency

## Execution

```bash
cd algorithms
python alpha_beta.py
```

## Sample Output

```text
Optimal Value: 10
```

---

# 3. Heuristic Alpha-Beta Search

## Description

This algorithm combines alpha-beta pruning with heuristic evaluation functions to estimate board utility at limited depth.

## Features

* Depth-limited search
* Heuristic evaluation
* Faster approximate solutions

## Execution

```bash
cd algorithms
python heuristic_alpha_beta.py
```

## Sample Output

```text
Heuristic Alpha-Beta Value: 5
```

---

# 4. Monte-Carlo Tree Search (MCTS)

## Description

MCTS is a probabilistic search technique widely used in AI game playing systems.

## Features

* Random simulations
* UCT-based node selection
* Tree expansion and rollout

## Execution

```bash
cd algorithms
python mcts.py
```

## Sample Output

```text
Best State: 3
```

---

# 5. AI-Based Travel Planner

## Description

An intelligent travel recommendation system that suggests:

* Tourist places
* Restaurants
* Budget estimates
* Personalized travel plans

The system uses existing knowledge bases stored in JSON format.

## Features

* Budget-based recommendations
* Food preference suggestions
* Tourist attraction recommendations

## Execution

```bash
cd travel_planner
python travel_planner.py
```

## Example Input

```text
Enter city: Hyderabad
Budget level: medium
Preferred food: South Indian
```

## Example Output

```text
Recommended Places:
- Charminar
- Golconda Fort
- Ramoji Film City

Recommended Restaurants:
- Paradise
- Chutneys

Estimated Budget: 5000
```

---

# 6. Knowledge Graphs

## Description

A Knowledge Graph represents entities and relationships in a structured graph format.

## Technologies Used

* RDF
* RDFLib
* Semantic triples

## Example Triple

```text
Hyderabad --> hasPlace --> Charminar
```

## Tools Explored

| Tool        | Purpose                |
| ----------- | ---------------------- |
| Neo4j       | Graph Database         |
| Protégé     | Ontology Modeling      |
| RDFLib      | RDF Graph Processing   |
| Apache Jena | Semantic Web Framework |
| GraphDB     | Triple Store           |

## Execution

```bash
cd knowledge_graph
python knowledge_graph.py
```

---

# 7. Bayesian Networks

## Description

Bayesian Networks are probabilistic graphical models used for uncertainty handling and inference.

This project demonstrates disease prediction using symptoms.

## Example

Predicting Flu using:

* Fever
* Cough

## Tools Explored

| Tool       | Purpose                 |
| ---------- | ----------------------- |
| pgmpy      | Bayesian Modeling       |
| GeNIe      | Graphical Bayesian Tool |
| Netica     | Bayesian Analysis       |
| BayesiaLab | Probabilistic Modeling  |

## Execution

```bash
cd bayesian_network
python bayesian_network.py
```

## Sample Output

```text
True
+---------+----------+
| Flu     |   phi() |
+=========+==========+
| Flu(0)  |   0.704 |
| Flu(1)  |   0.296 |
+---------+----------+
```

---

# Test Cases

## Running Test Cases

```bash
cd algorithms
python test_algorithms.py
```

## Expected Output

```text
Test Passed
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

```text
rdflib
pgmpy
networkx
matplotlib
numpy
```

---

# Screenshots

All execution screenshots are stored inside:

```text
screenshots/
```

Suggested screenshots:

* minimax_output.png
* alpha_beta_output.png
* heuristic_output.png
* mcts_output.png
* travel_planner_output.png
* bayesian_network_output.png
* knowledge_graph_output.png

---

# Concepts Covered

* Adversarial Search
* Game Tree Search
* Heuristic Evaluation
* Monte-Carlo Simulations
* Intelligent Recommendation Systems
* Knowledge Representation
* Semantic Web
* Probabilistic Reasoning
* Bayesian Inference

---

# Technologies Used

* Python
* JSON
* RDFLib
* pgmpy
* NetworkX
* Git & GitHub

---

# Learning Outcomes

After completing this assignment, the following concepts were understood and implemented:

* Classical AI Search Algorithms
* Intelligent Planning Systems
* Knowledge Graph Construction
* Bayesian Inference Models
* AI-Based Decision Making

---

# Conclusion

This project demonstrates practical implementations of important Artificial Intelligence techniques including search algorithms, probabilistic reasoning, knowledge representation, and intelligent recommendation systems.

The assignment provides hands-on understanding of AI concepts and their real-world applications.

---

# Author

Name: Sumanth Aswin
Course: Artificial Intelligence 


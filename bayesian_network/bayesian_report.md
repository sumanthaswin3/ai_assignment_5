# Bayesian Networks

## Introduction

Bayesian Networks are probabilistic graphical models used to represent uncertainty and probabilistic relationships between variables.

They combine:

* Probability Theory
* Graph Theory
* Statistical Inference

Bayesian Networks are widely used in:

* Medical diagnosis
* Risk analysis
* Machine learning
* Decision support systems
* Artificial Intelligence

---

# What is a Bayesian Network?

A Bayesian Network is a Directed Acyclic Graph (DAG) where:

* Nodes represent random variables
* Edges represent probabilistic dependencies

Example:

```text id="0vml3n"
Flu → Fever
Flu → Cough
```

This indicates that Fever and Cough depend on whether a person has Flu.

---

# Components of Bayesian Networks

## 1. Nodes

Nodes represent variables.

Examples:

* Flu
* Fever
* Cough

---

## 2. Directed Edges

Edges show dependency relationships.

Example:

```text id="24bw7q"
Flu → Fever
```

---

## 3. Conditional Probability Tables (CPT)

Each node contains probabilities.

Example:

| Flu | Probability |
| --- | ----------- |
| Yes | 0.05        |
| No  | 0.95        |

---

# Bayes Theorem

Bayesian Networks are based on Bayes Theorem.

Where:

* P(A|B) = Posterior Probability
* P(B|A) = Likelihood
* P(A) = Prior Probability
* P(B) = Evidence Probability

---

# Applications of Bayesian Networks

| Application         | Description                       |
| ------------------- | --------------------------------- |
| Medical Diagnosis   | Disease prediction                |
| Weather Forecasting | Predict weather conditions        |
| Spam Detection      | Email classification              |
| Risk Analysis       | Financial prediction              |
| Robotics            | Decision making under uncertainty |

---

# Tools Explored

| Tool       | Purpose                         |
| ---------- | ------------------------------- |
| pgmpy      | Bayesian modeling in Python     |
| GeNIe      | GUI-based Bayesian modeling     |
| Netica     | Bayesian analysis software      |
| BayesiaLab | Advanced probabilistic modeling |

---

# pgmpy Library

pgmpy is a Python library used for:

* Bayesian Networks
* Markov Models
* Probabilistic Inference

Features:

* Easy model creation
* Variable elimination
* Probabilistic queries
* CPD support

---

# Problem Statement

In this project, a Bayesian Network is implemented to predict whether a person has Flu based on symptoms such as:

* Fever
* Cough

The network structure:

```text id="7k5v7o"
Flu → Fever
Flu → Cough
```

---

# Bayesian Network Implementation

## Model Structure

```python id="hlnpmo"
model = BayesianNetwork([
    ('Flu', 'Fever'),
    ('Flu', 'Cough')
])
```

---

# Conditional Probability Tables

## Flu Probability

| Flu | Probability |
| --- | ----------- |
| No  | 0.95        |
| Yes | 0.05        |

---

## Fever Given Flu

| Flu | Fever=No | Fever=Yes |
| --- | -------- | --------- |
| No  | 0.9      | 0.1       |
| Yes | 0.2      | 0.8       |

---

## Cough Given Flu

| Flu | Cough=No | Cough=Yes |
| --- | -------- | --------- |
| No  | 0.85     | 0.15      |
| Yes | 0.3      | 0.7       |

---

# Inference

The system performs probabilistic inference using Variable Elimination.

Example query:

```python id="l9ts1t"
result = inference.query(
    variables=['Flu'],
    evidence={'Fever': 1}
)
```

This predicts the probability of Flu given that Fever is present.

---

# Sample Output

```text id="d6ny3v"
True

+---------+----------+
| Flu     | phi()    |
+=========+==========+
| Flu(0)  | 0.704    |
| Flu(1)  | 0.296    |
+---------+----------+
```

Interpretation:

* Probability of NOT having Flu = 70.4%
* Probability of having Flu = 29.6%

---

# Advantages of Bayesian Networks

* Handles uncertainty effectively
* Supports probabilistic reasoning
* Easy visualization of dependencies
* Useful for prediction systems
* Efficient inferencing

---

# Limitations of Bayesian Networks

* Complex for large systems
* Requires probability estimation
* Computationally expensive for huge networks
* Difficult structure learning

---

# Real-World Applications

## Healthcare

Disease prediction using symptoms.

## Finance

Risk prediction and fraud detection.

## Artificial Intelligence

Decision making under uncertain conditions.

## Robotics

Autonomous navigation and sensor fusion.

---

# Conclusion

Bayesian Networks are powerful probabilistic models used for representing uncertain knowledge and making intelligent predictions.

This project demonstrated:

* Bayesian modeling
* Conditional probability tables
* Probabilistic inference
* Disease prediction using symptoms

The implementation used the pgmpy library in Python to build and evaluate the Bayesian Network.

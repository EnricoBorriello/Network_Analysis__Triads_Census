# 📊 Triad Census & Significance Profile in Directed Graphs

This Python module performs a **triad census** on a directed network represented as an adjacency matrix. It also computes the **Triad Significance Profile (TSP)** by comparing the real network to randomized versions preserving degree distributions.

---

### ✨ Features

- Count all 13 possible triad types in a directed graph
- Generate random directed graphs
- Convert between adjacency matrices and edge lists
- Degree-preserving network randomization using edge swaps
- Compute triad significance profiles (Z-scores)
- Clean, modular, and well-documented code

---

### 📦 Requirements

- Python 3.7+
- NumPy

Install dependencies with:

```bash
pip install numpy
```

---

### 🚀 Usage

```python
import numpy as np
from triads import *

# Generate a random graph with 10 nodes and 30% edge probability
A = random_adj_matrix(10, 0.3)

# Count the triads in the network
triads = triad_census(A)
print("Triad census:", triads)

# Get the triad significance profile (TSP)
tsp = triad_significance_profile(A, ensemble_size=100, edge_randomizations=500)
print("Triad Significance Profile:", tsp)
```

---

### Functions Overview

---

### Project Structure

triads/
├── triads.py        # Main module with all functions
└── README.md        # Documentation

---

### References

Milo et al., 2002 – Network Motifs: Simple Building Blocks of Complex Networks

---

### Author

Built by [Enrico Borriello](https://github.com/EnricoBorriello)









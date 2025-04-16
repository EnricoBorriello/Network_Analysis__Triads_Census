# Triad Census & Significance Profile in Directed Graphs

This Python module performs a **triad census** on a directed network represented as an adjacency matrix. It also computes the **Triad Significance Profile (TSP)** by comparing the real network to randomized versions preserving degree distributions.

---

## Features

- Count all 13 possible triad types in a directed graph
- Generate random directed graphs
- Convert between adjacency matrices and edge lists
- Degree-preserving network randomization using edge swaps
- Compute triad significance profiles (Z-scores)

---

## Requirements

- Python 3.7+
- NumPy

Install dependencies with:

```bash
pip install numpy
```

---

## Usage

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


## Functions Overview

| Function | Description |
|---------|-------------|
| `triad_census(matrix)` | Computes the counts of all 13 triad types in a directed graph. |
| `random_adj_matrix(n, p)` | Generates a random directed adjacency matrix with `n` nodes and edge probability `p`. |
| `edge_list(adj_matrix)` | Converts an adjacency matrix into a list of directed edges. |
| `adjacency_matrix(edge_list, size)` | Converts a list of directed edges into an adjacency matrix of given size. |
| `swap_edges(edge_list)` | Performs a double-edge swap that preserves the in/out-degree of nodes. |
| `randomize(matrix, iterations)` | Randomizes a network by performing valid edge swaps. |
| `triad_significance_profile (matrix, ensemble_size, edge_randomizations)` | Computes how unusual each triad type is in a graph vs. random graphs. |



## Project Structure

```
Network-Analysis-Triads-Census/
│
├── triad_utils.py   # Main module with all functions
├── README.md        # Documentation
└── Example.ipynb    # Example notebook
```


---

## License

MIT License. See `LICENSE` file for more details.

---

## Contributions

Pull requests are welcome! If you find a bug or want a feature, feel free to open an issue.

---

### References

- [Milo et al., 2002](https://www.science.org/doi/10.1126/science.298.5594.824) – Network Motifs: Simple Building Blocks of Complex Networks


---


### Author

Built by [Enrico Borriello](https://github.com/EnricoBorriello)









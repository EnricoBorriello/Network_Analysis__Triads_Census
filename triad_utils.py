import numpy as np
from numpy import linalg as lin
import random as rn

# --------------------------------------------------
def triad_census(matrix: np.ndarray) -> np.ndarray:
    """
    Computes the triad census of a directed graph represented by an adjacency matrix.
    Returns a 13-element vector representing counts of each triad type.
    """
    A = matrix
    n = A.shape[0]
    At = A.T
    Ones = np.ones((n, n), dtype=int)

    # Edge configuration helpers
    X = (Ones - A) * (Ones - At)  # No edges between node pairs
    Y = A * At                    # Mutual edges
    Z = A * (Ones - At)          # Asymmetric one-way edges

    Y2 = np.dot(Y, Y)
    Y3 = np.dot(Y2, Y)

    # Helper matrices for triad identification
    B = np.dot(At, A) - np.dot(Y, A) - np.dot(At, Y) + Y2
    Bp = np.dot(A, At) - np.dot(Y, At) - np.dot(A, Y) + Y2
    C = np.dot(A, A) - np.dot(Y, A) - np.dot(A, Y) + Y2
    D = np.dot(Y, At) - Y2
    E = np.dot(Y, A) - Y2

    t = np.zeros(13)

    # Count different triad types
    t[0]  = (np.sum(X * B) - np.trace(X * B)) / 2
    t[1]  = (np.sum(X * Bp) - np.trace(X * Bp)) / 2
    t[2]  = np.sum(X * C) - np.trace(X * C)
    t[3]  = np.sum(X * D) - np.trace(X * D)
    t[4]  = np.sum(X * E) - np.trace(X * E)
    t[5]  = (np.sum(X * Y2) - np.trace(X * Y2)) / 2
    t[6]  = np.sum(Z * C)
    t[7]  = np.trace(np.dot(Z, np.dot(Z, Z))) / 3
    t[8]  = np.sum(Y * B) / 2
    t[9]  = np.sum(Y * Bp) / 2
    t[10] = np.sum(Y * C)
    t[11] = np.sum(Z * Y2)
    t[12] = np.trace(Y3) / 6

    return t.astype(int)

# --------------------------------------------------
def random_adj_matrix(n: int, p: float) -> np.ndarray:
    """
    Generates a random directed adjacency matrix with edge probability p.
    No self-loops.
    """
    A = (np.random.rand(n, n) < p).astype(int)
    np.fill_diagonal(A, 0)
    return A

# --------------------------------------------------
def edge_list(adj_matrix: np.ndarray) -> list:
    """
    Converts an adjacency matrix to a list of directed edges.
    """
    return [[i, j] for i in range(len(adj_matrix)) for j in range(len(adj_matrix)) if adj_matrix[i, j] == 1]

# --------------------------------------------------
def adjacency_matrix(edge_list: list, size: int) -> np.ndarray:
    """
    Converts an edge list back to an adjacency matrix of specified size.
    """
    A = np.zeros((size, size), dtype=int)
    for src, tgt in edge_list:
        A[src, tgt] = 1
    return A

# --------------------------------------------------
def swap_edges(edge_list: list, max_attempts: int = 1000) -> list:
    """
    Attempts to perform a double-edge swap while avoiding self-loops and duplicate edges.
    """
    E = edge_list[:]
    for _ in range(max_attempts):
        x0, x1 = rn.sample(E, 2)
        y0, y1 = [x0[0], x1[1]], [x1[0], x0[1]]

        # Validity check
        if y0 not in E and y1 not in E and x0[0] != x1[1] and x1[0] != x0[1]:
            E.remove(x0)
            E.remove(x1)
            E.append(y0)
            E.append(y1)
            return E
    raise RuntimeError("Failed to swap edges after max attempts.")

# --------------------------------------------------
def randomize(matrix: np.ndarray, iterations: int) -> np.ndarray:
    """
    Randomizes a network via edge swaps while preserving in/out-degree distributions.
    """
    E = edge_list(matrix)
    for _ in range(iterations):
        E = swap_edges(E)
    return adjacency_matrix(E, len(matrix))

# --------------------------------------------------
def triad_significance_profile(matrix: np.ndarray, ensemble_size: int, edge_randomizations: int) -> list:
    """
    Computes the Triad Significance Profile (TSP) of a network by comparing the real triad distribution
    to those from randomized versions of the same network.
    """
    original = triad_census(matrix)
    ensemble = []

    for _ in range(ensemble_size):
        rand_mat = randomize(matrix, edge_randomizations)
        ensemble.append(triad_census(rand_mat))

    ensemble = np.array(ensemble)
    m = np.mean(ensemble, axis=0)
    s = np.std(ensemble, axis=0, ddof=1)

    tsp = [
        0 if s[i] == 0 else (original[i] - m[i]) / s[i]
        for i in range(13)
    ]
    return tsp

import numpy as np
from numpy import linalg as lin
import random as rn

# ------------------------------------

def triad_census(matrix):
    
    A   = matrix
    n   = len(A) 
    At  = np.transpose(A)
    Ones = np.ones((n,n))

    X  = np.multiply(Ones-A,Ones-At)
    Y = np.multiply(A,At)
    Z  = np.multiply(A,Ones-At)
    Y2 = lin.matrix_power(Y,2)
    Y3 = lin.matrix_power(Y,3)
    
    B = np.dot(At,A) -np.dot(Y,A) -np.dot(At,Y) +lin.matrix_power(Y ,2)
    Bp = np.dot(A,At) -np.dot(Y,At) -np.dot(A,Y) +lin.matrix_power(Y ,2)
    C = lin.matrix_power(A ,2) -np.dot(Y,A) -np.dot(A,Y) +lin.matrix_power(Y ,2)
    D = np.dot(Y,At) -lin.matrix_power(Y ,2)
    E = np.dot(Y,A) -lin.matrix_power(Y ,2)

    t = np.zeros(13) 
# Triad 1
    P1 = np.multiply(X,B)
    t[0]  = (np.sum(P1)-np.trace(P1))/2   # t[0] is the count for triad 1, etc. 
# Triad 2
    P2 = np.multiply(X,Bp)
    t[1]  = (np.sum(P2)-np.trace(P2))/2  
# Triad 3
    P3 = np.multiply(X,C)
    t[2] = np.sum(P3)-np.trace(P3)
# Triad 4
    P4 = np.multiply(X,D)
    t[3] = np.sum(P4)-np.trace(P4)
# Triad 5
    P5 = np.multiply(X,E)
    t[4] = np.sum(P5)-np.trace(P5)
# Triad 6
    P6 = np.multiply(X,Y2)
    t[5] = (np.sum(P6)-np.trace(P6))/2
# Triad 7
    P7 = np.multiply(Z,C)
    t[6] = np.sum(P7)   
# Triad 8    
    t[7] = np.trace(lin.matrix_power(Z,3))/3   
# Triad 9
    P9 = np.multiply(Y,B)
    t[8] = np.sum(P9)/2
# Triad 10
    P10 = np.multiply(Y,Bp)
    t[9] = np.sum(P10)/2
# Triad 11   
    P11 = np.multiply(Y,C)
    t[10] = np.sum(P11)   
# Triad 12   
    P12 = np.multiply(Z,Y2)
    t[11] = np.sum(P12)
# Triad 13
    t[12] = np.trace(Y3)/6

    return t.astype(int)

# ------------------------------------

def random_adj_matrix(N,p):
#random non symmetric with n, p
    A = np.zeros((N,N), dtype=int)
    for i in range(N):
        for j in range(N):
            if rn.random() < p and i!=j:
                A[i][j] = 1
    return A

# ------------------------------------

def edge_list(adjacency_matrix):
# only works for unweighted networks (weights = 1) 
    E = []
    A = np.array(adjacency_matrix)
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i,j] == 1:
                E.append([i,j])
    return E

# ------------------------------------

def adjacency_matrix(edge_list,size):
    n = size
    A = np.zeros((n,n)).astype(int)
    E = edge_list
    for e in E:
        A[e[0],e[1]] = 1
    return A

# ------------------------------------

def swap_edges(edge_list):
    E = edge_list
    
    marker = 0
    while marker == 0:

        [x0,x1] = rn.sample(E,2)
        y0 = [x0[0],x1[1]]
        y1 = [x1[0],x0[1]]

        if y0 in E or y1 in E or x0[0] == x1[1] or x1[0] == x0[1]:
        # 3rd and 4th conditions are there to prevent the formation of self-loops
            marker = 0
        else:
            marker = 1
            E.remove(x0)
            E.remove(x1)
            E.append(y0)
            E.append(y1)
    
    return E

# ------------------------------------

def randomize(matrix,iterations):
# suggested number of iterations = 10*len(edge_list(A))
    
    A = matrix
    E = edge_list(A)
    
    for i in range(iterations):
        E = swap_edges(E)
    
    return adjacency_matrix(E,len(A))

# ------------------------------------

def triad_significance_profile(matrix, ensemble_size, edge_randomizations):
# assumptions: no self-loops, all weights = 1

    ensemble = []
    
    p = triad_census(matrix)

    for _ in range(ensemble_size):
        profile = []
        random_matrix = randomize(matrix,edge_randomizations)
        t = list(triad_census(random_matrix))
        ensemble.append(t)

        m = np.mean(ensemble,axis = 0)
        s = np.std(ensemble,axis = 0)

    for i in range(13):
        if p[i] == m[i]:
            profile.append(0)
        else:
            profile.append(  (p[i]-m[i])/s[i]  )

    return profile
# ------------------------------------

def functions():
    return print(
    'triad_census(matrix)\n'
    'random_adj_matrix(N,p)\n'
    'edge_list(adjacency_matrix)\n'
    'adjacency_matrix(edge_list,size)\n'
    'swap_edges(edge_list)\n'
    'randomize(matrix,iterations)\n'
    'triad_significance_profile(matrix, ensemble_size, edge_randomizations):\n'


    'functions()\n'
    )

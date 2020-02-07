from __future__ import print_function,division

from graph import AdjListGraph
import sys

def grid_graph(M,N,diagonals=False):
    """Makes a grid graph of size (M,N).  Vertices are indices (i,j).
    
    If diagonals=True, then diagonal edges are added.
    """
    G = AdjListGraph([],[])
    for i in range(M):
        for j in range(N):
            n = (i,j)
            G.add_node(n)
    for i in range(M):
        for j in range(N):
            n = (i,j)
            if i > 0:
                G.add_edge(n,(i-1,j))
            if j > 0:
                G.add_edge(n,(i,j-1))
            if i+1 < M:
                G.add_edge(n,(i+1,j))
            if j+1 < N:
                G.add_edge(n,(i,j+1))
            if diagonals:
                if i > 0 and j > 0:
                    G.add_edge(n,(i-1,j-1))
                if i > 0 and j+1 < N:
                    G.add_edge(n,(i-1,j+1))
                if i+1 < M and j > 0:
                    G.add_edge(n,(i+1,j-1))
                if i+1 < M and j+1 < N:
                    G.add_edge(n,(i+1,j+1))
    return G


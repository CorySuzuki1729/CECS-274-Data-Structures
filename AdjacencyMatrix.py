"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack

class AdjacencyMatrix(object):
    def __init__(self, n):
        self.n = n
        self.a = np.zeros([n, n], np.bool_)
                
    def add_edge(self, i, j):
        self.a[i][j] = True
        #pass
        
    def remove_edge(self, i, j):
        self.a[i][j] = False
        #pass
        
    def has_edge(self, i, j):
        return self.a[i][j]
        #pass

    def out_edges(self, i):
        out = list()
        for j in range(self.n):
            if self.a[i][j]:
                out.append(j)
        return out
        #pass
        
    def in_edges(self, i):
        inside = list()
        for j in range(self.n):
            if self.a[j][i]:
                inside.append(j)
        return inside
        #pass
        
    def in_degree(self, i):
        indegree = 0
        for j in range(self.n):
            if self.a[j][i]:
                indegree += 1
        return indegree
        #pass
        
    def out_degree(self, i):
        outdegree = 0
        for j in range(self.n):
            if self.a[i][j]:
                outdegree += 1
        return outdegree
        #pass

    def size(self) -> int :
        return self.n
                  
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.has_edge(i,j):
                    s += f"{i,j}"
        return s


#q = AdjacencyMatrix(4)
#q.remove_edge(1, 2)
#q.has_edge(2,3)
#q.add_edge(0,1)
#q.add_edge(1,2)
#q.add_edge(2,3)
#q.add_edge(3,0)
#q.add_edge(0,2)
#print(q.has_edge(0,1))
#print(q.has_edge(1,3))
#print(q.in_edges(2))
"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue

class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def new_boolean_array(self, n):
        return np.zeros(n, object)
            
    def add_edge(self, i : int, j : int):
        self.adj[i].append(j)
        #pass
        
    def remove_edge(self, i : int, j : int):
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return
        #pass
                
    def has_edge(self, i : int, j: int) ->bool:
        for k in range(self.adj[i].size()):
            if k == j:
                return True
        return False
        #pass
        
    def out_edges(self, i) -> List:
        return self.adj[i]
        #pass

    def in_edges(self, i) -> List:
        out = ArrayStack.ArrayStack()
        for j in range(self.n):
            if self.has_edge(j, i):
                out.append(j)
        return out
        #pass

    def bfs(self, r :int):
        seen = self.new_boolean_array(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] is False:
                    q.add(j)
                    seen[j] = True
        #pass

    def dfs(self, r :int):
        c = self.new_boolean_array(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        c[r] = True
        while s.size() > 0:
            i = s.pop()
            for j in self.out_edges(i):
                if not c[j]:
                    c[j] = True
                    s.push(j)
        #pass

    
    def distance(self, r : int, dest: int):
        seen = self.new_boolean_array(self.n)
        p = np.zeros(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        p[r] = 0
        while s.size() > 0:
            i = s.pop()
            if seen[i] == False:
                seen[i] = True
                neighbors = self.out_edges(i)
                for j in neighbors:
                    if seen[j] == False:
                        s.push(j)
                        p[j] = p[i] + 1
                        if j == dest:
                            return p[j]
        #pass

    def size(self) -> int :
        return self.n
                      
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s


#q = AdjacencyList(4)
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
#print(q.out_edges(0))
#print(q.bfs(0))
#print(q.dfs(0))
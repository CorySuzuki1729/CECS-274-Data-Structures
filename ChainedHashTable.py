from Interfaces import Set
from DLList import DLList
import numpy as np

class ChainedHashTable(Set):
    class Node() :
        def __init__(self, key, value) :
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList) :
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object)
        for i in range(n):
            t[i] = self.dtype()
        return t


    def hash(self, key : int) -> int :
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
        l = self.t[self.hash(key)]
        for i in range(len(l)):
            if l[i].key == key:
                return l[i].value
        return None
        #pass
        
    def add(self, key : object, value : object) :
        if self.find(key) is not None:
            return False
        if (self.n + 1) > len(self.t):
            self.resize()
        self.t[self.hash(key)].append(self.Node(key, value))
        self.n += 1
        return True
        #pass


    def remove(self, key : int)  -> object:
        try:
            if self.find(key) is None:
                raise KeyError()
            l = self.t[self.hash(key)]
            for i in range(len(l)):
                u = l[i]
                if u.key == key:
                    l.remove(i)
                    self.n -= 1
                    if 3 * self.n < len(self.t):
                        self.resize()
                return u.value
            return None
        except KeyError:
            print("Key does not exist. Please try again.")
        #pass
    
    def resize(self):
        if self.n == len(self.t):
            self.d += 1
        else:
            self.d -= 1
        a = self.alloc_table(2**self.d)
        for j in range(len(self.t)):
            for i in range(self.t[j].size()):
                a[self.hash(self.t[j].get(i).key)].add(0, self.t[j].get(i))
        self.t = a
        #pass


    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"





#hashtest = ChainedHashTable()
#hashtest.remove(2)
#print(hashtest.find(2))
#hashtest.add(1, "first")
#hashtest.add(2, "second")
#hashtest.add(3,"fourth")
#print(hashtest.size())
#print(hashtest.find(3))
#hashtest.remove(3)
#print(hashtest.size())
#print(hashtest.find(3))
#hashtest.add(3, "third")
#hashtest.add(4, "fourth")
#hashtest.add(5, "fifth")
#print(hashtest.size())
#print(hashtest.find(3))

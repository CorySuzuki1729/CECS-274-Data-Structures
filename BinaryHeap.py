import numpy as np
from Interfaces import Queue



def left(i : int):
    if i< 0: raise IndexError()
    return 2*i + 1

def right(i: int):
    if i< 0: raise IndexError()
    return 2*(i+1)

def parent(i : int):
    if i< 0: raise IndexError()
    return (i-1)//2

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)

    def resize(self):
        b = self.new_array(max(2 * self.n, 1))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b
        #pass

    def add(self, x : object):
        if len(self.a) < (self.n + 1):
            self.resize()
        self.a[self.n] = x
        self.n += 1
        self.bubble_up(self.n - 1)
        return True
        #pass

    def bubble_up(self, i):
        p = parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
            p = parent(i)
        #pass

    def remove(self):
        try:
            if self.n <= 0:
                raise IndexError()
            x = self.a[0]
            self.a[0] = self.a[self.n - 1]
            self.n -= 1
            self.trickle_down(0)
            if 3 * self.n < len(self.a):
                self.resize()
            return x
        except IndexError:
            print("Index is out of bounds. Please try again.")
        #pass

    def trickle_down(self, i):
        while i >= 0:
            j = -1
            r = right(i)
            if r < self.n and self.a[r] < self.a[i]:
                l = left(i)
                if self.a[l] < self.a[r]:
                    j = l
                else:
                    j = r
            else:
                l = left(i)
                if l < self.n and self.a[l] < self.a[i]:
                    j = l
            if j >= 0:
                self.a[j], self.a[i] = self.a[i], self.a[j]
            i = j
        #pass

    def find_min(self):
        if n == 0: raise IndexError()
        return a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

#test = BinaryHeap()
#test.add(2)
#test.add(1)
#test.add(5)
#print(test.size())
#test.remove()
#test.add(4)
#test.add(1)
#test.add(3)
#print(test.size())
#print(test.remove())
#print(test.remove())
#print(test.remove())
#print(test.remove())
#print(test.remove())
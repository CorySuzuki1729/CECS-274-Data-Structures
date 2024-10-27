from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        if i < (self.n / 2):
            p = self.dummy.next
            for j in range(i):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n, i, -1):
                p = p.prev
        return p
        #pass
        
    def get(self, i) -> np.object:
        try:
            if i < 0 or i >= self.n:
                raise IndexError()
            return self.get_node(i).x
        except IndexError:
            print("Index out of range. Please try again.")
        #pass

    def set(self, i : int, x : np.object) -> np.object:
        try:
            if i < 0 or i >= self.n:
                raise IndexError()
            u = self.get_node(i)
            y = u.x
            u.x = x
            return y
        except IndexError:
            print("Index is out of range. Please try again.")
        #pass

    def add_before(self, w : Node, x : np.object) -> Node:
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
        #pass
            
    def add(self, i : int, x : np.object)  :
        try:
            if i < 0 or i > self.n:
                raise IndexError()
            self.add_before(self.get_node(i), x)
        except IndexError:
            print("Index is out of range. Please try again.")
        #pass

    def _remove(self, w : Node) :
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        #pass
    
    def remove(self, i :int) :
        #try:
            #if i < 0 or i > self.n:
                #raise IndexError()
            self._remove(self.get_node(i))
        #except IndexError:
            #print("Index is out of range. Please try again.")
        #pass

    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        n = self.dummy.next
        p = self.dummy.prev
        while n.x == p.x and n != self.dummy:
            n = n.next
            p = p.prev
        return n == self.dummy
        #pass

    def reverse(self, x) :                         #Hint: Consider modifying references per rubric
        try:
            if self.n == 0:
                raise IndexError()
            current_node = self.dummy
            for i in range(self.n + 1):
                previous_node = current_node.prev
                next_node = current_node.next
                current_node.prev = current_node.next
                current_node.next = previous_node
                current_node = next_node
            return x
        except IndexError:
            print("List is empty, cannot reverse. Please try again.")
        #pass

         
    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __getitem__(self, i) -> object:
        #'''
            #__getitem__: Returns the item in the position i in array format, i.e., l[i]
            #where l is a list instance
            #Input:
                #i: positive integer less than n
            #Return: the item at index i
        #'''
        if isinstance(i, slice):
            raise IndexError("Not implemented. Please use the references next and prev")
        else:
            return self.get(i)


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

#test = DLList()
#test.add(2, 100)
#test.add(-2, 7)
#test.add(0, 4)
#test.add(100, 5)
#test.add(0, 1)
#test.add(1, 3)
#test.add(1, 2)
#test.add(4, 5)
#test.add(0, "b")
#test.add(1, "o")
#test.add(2, "t")
#test.add(0, "e")
#test.add(1, "v")
#test.add(2, "e")
#test.remove(2)
#test.remove(3)
#test.remove(0)
#print(test)
#print(test.get(0))
#print(test.isPalindrome())
#test.reverse(test)
#print(test.reverse(test))
import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        #'''
            #Resize the array
        #'''
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def get(self, i : int) -> np.object:
        if (i < 0) or (i > self.n):
            raise IndexError("Index is out of bounds.")
        return self.a[i]
        #pass
    
    def set(self, i : int, x : np.object) -> object:
        if (i < 0) or (i >= self.n):
            raise IndexError("Index is out of bounds.")
        y = self.a[i]
        self.a[i] = x
        return y
        #pass

    def add(self, i: int, x : np.object) :
        if (i < 0) or (i > self.n + 1):
            raise IndexError("Index is out of bounds.")
        if self.n + 1 > len(self.a):
            self.resize()
        for j in range(i, len(self.a)):
            if (self.a[i] is not None) and (self.n != 0) and (self.a[i] == self.n):
             self.a[j + 1] = self.a[j]
        self.a[i] = x
        self.n += 1


        #'''
            #shift all j > i one position to the right
            #and add element x in position i
        #'''
        #pass

    def remove(self, i : int) -> np.object :
        if self.n == 0 or (i < 0) or (i > self.n):
            raise IndexError("Index is out of bounds!")
        x = self.a[i]
        for j in range(i, self.n - 1):
            self.a[j] = self.a[j + 1]
        self.n -= 1
        if len(self.a) >= (3 * self.n):
            self.resize()
        return x
        #'''
            #remove element i and shift all j > i one
            #position to the left
        #'''
        #pass

    def push(self, x : np.object) :
        self.add(self.n, x)
    
    def pop(self) -> np.object :
        return self.remove(self.n-1)

    def size(self) :
        #'''
            #size: Returns the size of the stack
            #Return: an integer greater or equal to zero representing the number
                    #of elements in the stack
        #'''
        return self.n
        
    def __str__(self) -> str:
        #'''
            #__str__: Returns the content of the string using print(s)
            #where s is an instance of the ArrayStack
            #Return: String with the content of the stack
        #'''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x


#try:
    #array = ArrayStack()
    #array.push(5)
    #array.add(2, 0)           #test for adding an index that is bounded above.
    #array.add(-5, 50)          #test for adding an index that is bounded below.
    #array.pop()           #test for removing from empty stack.
    #print(array)
    #print(array.get(5))
#except IndexError:
    #print("Index is out of bounds. Please re-run code to try again.")

#Note to lab instructor: Before testing main.py, calculator.py, or bookstore,
#comment out try/except for arraystack, arrayqueue, arraylist, as they work for
#their respective files but interferes with the other files' interface.
#Thank you for your understanding.
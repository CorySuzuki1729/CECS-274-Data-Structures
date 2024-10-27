import random 
from Interfaces import Queue 
import ArrayQueue


class RandomQueue(Queue):
    def __init__(self):
        self.queue = ArrayQueue.ArrayQueue()
        self.counter = 0

    def add(self, x : object):
        self.queue.add(x)
        self.counter += 1
        #'''
            #add: Add the value x to the Queue
            #Inputs:
                #x: Object type, i.e., any object
        #'''
        #pass

    def remove(self) -> object:
        new_index = random.randint(self.queue.j, self.counter-1)
        temp = self.queue.a[self.queue.j]
        self.queue.a[self.queue.j] = self.queue.a[new_index]
        self.queue.a[new_index] = temp
        if self.queue.n == 0:
            raise IndexError("Index is out of bounds.")
        x = temp
        self.queue.j = (self.queue.j+1) % len(self.queue.a)
        self.queue.n -= 1
        return x

        #'''
            #remove: remove the next (previously added) value, y, from the
                    #Queue and return y. The Queue’s queueing discipline
                    #decides which element should be removed.
            #Return: Object type
        #'''
        #pass
    
    def size(self) -> int:
        return self.queue.size()

    def __str__(self):
        return str(self.queue)

try:
    arrayrand = RandomQueue()
    #arrayrand.add(1)
    #arrayrand.add(2)
    #arrayrand.add(3)
    #arrayrand.add(4)
    #arrayrand.add(5)
    arrayrand.remove()
    print(arrayrand)

except IndexError:
    print("Index is out of bounds! Please re-run code to try again.")
except ValueError:
    print("Range is also out of bounds! Please re-run code to try again.")








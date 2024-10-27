from Interfaces import Stack
import SLLStack


class MaxStack(Stack) :
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        self.max_stack = SLLStack.SLLStack()
        
    def max(self) ->object:
        return self.max_stack.head.x
        #'''
            #Returns the max element
        #'''
        #pass
    
    def push(self, x : object) :
        self.stack.push(x)
        var = None
        if self.max_stack.size() > 0:
            var = self.max_stack.head.x
        if self.max_stack.size() == 0:
            self.max_stack.push(x)
            return
        else:
            if self.max_stack.head.x < x:
                self.max_stack.push(x)
                return
            else:
                self.max_stack.push(var)
                return
        #'''
            #push: Insert an element in the tail of the stack
            #Inputs:
                #x: Object type, i.e., any object
        #'''
        #pass

    def pop(self) -> object:
        self.max_stack.pop()
        return self.stack.pop()
        #'''
            #pop: Remove the last element in the stack
            #Returns: the object of the tail if it is not empty
        #'''
        #pass

    def size(self) -> int:
        return self.stack.size()

#maxtest = MaxStack()
#maxtest.push(3)
#maxtest.push(1)
#maxtest.push(4)
#maxtest.push(2)
#maxtest.pop()
#maxtest.pop()
#maxtest.pop()
#maxtest.pop()
#print(maxtest.max())
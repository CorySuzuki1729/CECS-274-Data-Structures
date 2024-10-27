from BinarySearchTree import BinarySearchTree
from Interfaces import Set


class BinarySearchTreeWithDuplication(Set):

    def __init__(self, nil=None):
        self.binaryTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        w = self.binaryTree.r
        while w is not None:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.v
        return None

        #pass

    def add(self, key : object, value : object) -> bool:
        if self.find(key) is not None:
            var = self.find(key)
            var.append(value)
            self.remove(key)
            value = var
        else:
            var = []
            var.append(value)
            value = var
        self.binaryTree.add(key, value)
        self.binaryTree.n += 1
        return True
        #pass
    
    def remove(self, x : object) -> bool:
        self.binaryTree.remove(x)
        self.n -= 1
        #pass


#q = BinarySearchTreeWithDuplication()
#q.add(1, "a")
#q.add(1, "b")
#q.add(1, "c")
#q.add(2, "d")
#q.add(3, "e")
#q.add(3, "z")
#q.add(2, "c")
#q.add(3, "d")
#q.add(3, "e")
#print(q.find(1))
#print(q.find(2))
#print(q.find(3))
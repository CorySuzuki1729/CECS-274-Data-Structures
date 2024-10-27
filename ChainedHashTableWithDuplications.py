from Interfaces import Set
from DLList import DLList
from ArrayStack import ArrayStack
import ChainedHashTable 

class ChainedHashTableWithDuplications(Set):
    def __init__(self) :
        self.chainHashTable = ChainedHashTable.ChainedHashTable()
        self.n = 0

    def size(self) -> int:
        return self.n

    def find(self, key : object) -> object :
        sup = DLList()
        l = self.chainHashTable.t[self.chainHashTable.hash(key)].size()
        for i in range(l):
            if self.chainHashTable.t[self.chainHashTable.hash(key)].get(i).key == key:
                sup.append(self.chainHashTable.t[self.chainHashTable.hash(key)].get(i).value)
        return sup
        #pass

    def add(self, key : object, value : object) :
        if self.n == len(self.chainHashTable.t):
            self.chainHashTable.resize()
        self.chainHashTable.t[self.chainHashTable.hash(key)].append(self.chainHashTable.Node(key, value))
        self.n += 1
        #pass


    def remove(self, key : int)  -> object:
        self.chainHashTable.remove(key)
        self.n -= 1
        #pass
    
    
    def __str__(self):
        return self.cht.__str__()

#duphash = ChainedHashTableWithDuplications()
#duphash.add(1, "b")
#duphash.add(1, "a")
#duphash.add(2, "c")
#duphash.add(3, "d")
#duphash.add(3, "e")
#print(duphash.find(1))
#print(duphash.find(2))
#print(duphash.find(3))
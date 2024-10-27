import algorithms
import Book
import SortableBook
import ArrayQueue
import ArrayList
import DLList
import MaxStack
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = ArrayList.ArrayList()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        self.bestsellers = BinaryHeap.BinaryHeap()
        self.indexKey = ChainedHashTable.ChainedHashTable()
        self.indexSortedPrefix = BinarySearchTree.BinarySearchTree()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.similaGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
        

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        with open(fileName,encoding='utf8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.indexKey.add(key, self.bookCatalog.size()-1)
                self.indexSortedPrefix.add(s.title, self.bookCatalog.size()-1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")
            self.similaGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
            for i in range(self.bookCatalog.size()):
                l = self.bookCatalog[i].similar.split()
                for k in range(1, len(l)):
                    j = self.indexKey.find(l[k])
                    if j is not None:
                        self.similaGraph.add_edge(i, j)

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with index i
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, s : str) :
        i = self.indexKey.find(s)
        if i is not None:
            self.shoppingCart.push(self.bookCatalog.get(i))
            start_time = time.time()
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
        else:
            print("Nonexistent key, please try again.")
        #'''
        #addBookByIndex: Inserts into the shopping cart the book with key s
        #input:
            #s: key string
        #'''
        #pass

    def addBookByPrefix(self, s : str) :
        i = self.indexSortedPrefix.find(s)
        if i is not None:
            start_time = time.time()
            b = self.bookCatalog.get(i)
            self.shoppingCart.add(b)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {b} \n{elapsed_time} seconds")

        #'''
        #addBookByPrefix: Inserts into the shopping cart the book with prefix s
        #input:
            #s: Prefix
        #'''
        # Validating the index. Otherwise it  crashes
        #pass

    def pathLength(self, s1: str, s2: str) :
        i = self.indexKey.find(s1)
        j = self.indexKey.find(s2)
        distance = self.similaGraph.distance(i, j)
        return distance

    def searchBookByInfix(self, infix: str) -> int:
        '''
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        returns:
            the number of books that contains infix in its title
        '''
        heap = BinaryHeap.BinaryHeap()
        numberOfBooks = 0

        for u in self.bookCatalog:
            if infix in u.title:
                numberOfBooks += 1
                heap.add(u)

        while heap.size() > 0:
            book = heap.remove()
            index = self.indexKey.find(book.key)
            l = self.similaGraph.out_edges(index)
            print(f"{book.key}: {book.title}")
            for i in l:
                print(f"\t\tSimilar: {self.bookCatalog.get(i).title}")
        return numberOfBooks

    def sortUsingMergeSort(self) :
        algorithms.merge_sort(self.bookSortedCatalog)

    
    def sortUsingQuickSort(self) :
        algorithms.quick_sort(self.bookSortedCatalog)

    def searchBookUsingBinarySearch(self, prefix : str) :
        s = SortableBook.SortableBook(0, prefix, "", 0, None)
        j = algorithms.binary_search(self.bookSortedCatalog, self.bookSortedCatalog.size(), s)
        print(self.bookSortedCatalog[j])

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")
            return u

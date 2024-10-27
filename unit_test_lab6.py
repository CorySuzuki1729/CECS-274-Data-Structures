import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import BookStore
import algorithms



class  SortingTest(unittest.TestCase) :
    
    def test_sorting(self) :
        points = 0.5
        a = []
        try:
            algorithms.merge_sort(a)
            algorithms.quick_sort(a)
            points += 0.5
        except :
            pass
            
        try:
            a = [4,1,3,5,2]
            #print(algorithms.merge_sort(a))
            self.assertAlmostEqual(algorithms.merge_sort(a), [1,2,3,4,5])
            self.assertAlmostEqual(algorithms.quick_sort(a), [1,2,3,4,5])
            points += 1
        except:
            print("Sorting is not correct")
        finally:
       
            print(f"Sorting: {points} Points")
    def test_binarySearch(self) :
        points = 0.5
        a = []  
        try:
            self.assertAlmostEqual(algorithms.binary_search(a,len(a), 1), -1)
            points += 0.5
        except :
            pass       
        try:
            a = [1,2,3,4,5]
            self.assertAlmostEqual(algorithms.binary_search(a,len(a), 3), 2)
            self.assertAlmostEqual(algorithms.binary_search(a,len(a), 0), -1)
            self.assertAlmostEqual(algorithms.binary_search(a,len(a), 1), 0)
            self.assertAlmostEqual(algorithms.binary_search(a,len(a), 5), 4)
            points += 1
        except:
            print("BinarySearch is not correct")
        finally:
       
            print(f"BinarySearch : {points} Points")
 
    def test_BookStore(self) :
        points = 0.5
        try:
            a = BookStore.BookStore()
            a.loadCatalog("../books.txt")
            a.sortUsingMergeSort()
            
            a = BookStore.BookStore()
            a.loadCatalog("../books.txt")
            a.sortUsingQuickSort()
            points += 0.5
            
            a.searchBookUsingBinarySearch("Tear of S")
            a.searchBookUsingBinarySearch("World of Po")
            

            
            points += 1
        except:
            print("BookStore is not correct")
        finally:
            print(f"BookStore: {points} Points")


d = SortingTest()

d.test_binarySearch()
d.test_BookStore()
d.test_sorting()
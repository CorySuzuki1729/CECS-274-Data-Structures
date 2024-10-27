

import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import BinarySearchTree
import BinaryTree
import Calculator
import BookStore
import BinarySearchTreeWithDuplication


class  BinarySearchTreeTest(unittest.TestCase) :
    
    def test_binarytree(self) :
        points = 0.5
        q = BinarySearchTree.BinarySearchTree()
        try:
            self.assertIsNone(q.find(2))
            self.assertAlmostEqual(q.remove(2), False)
        except:
            pass
        finally:
            points += 0.5
            
        try:
            q.add(3, "third")
            q.add(2, "second")
            q.add(1, "first")
            self.assertAlmostEqual(q.size(), 3)
            self.assertAlmostEqual(q.find(2.5), "third")
            q.remove(3)
            self.assertIsNone(q.find(3))
            self.assertAlmostEqual(q.size(), 2)
            q.add(3, "third")
            q.add(5, "fifth")
            q.add(4, "fourth")
            
            self.assertAlmostEqual(q.size(), 5)
            self.assertAlmostEqual(q.find(3.4), "fourth")
            print("In order")
            q.in_order()
            print("Pre oder")
            q.pre_order()
            print("Pos order")
            q.pos_order()
            print("BF Traversal")
            q.bf_traverse()
            self.assertAlmostEqual(q.height(), 4)
            points += 1
        except:
            print("BinarySearchTreeTest is not correct")
        finally:
       
            print(f"BinarySearchTreeTest: {points} Points")
    
    def test_calculator(self) :
        points = 0.5
        s = Calculator.Calculator()
        try:
            self.assertAlmostEqual(s.evaluate(""), "")
        except:
            print("Calculator is not correct")
        finally:
            points += 0.5
        try:
            self.assertAlmostEqual(s.evaluate("((a*b)+(c*d))"), 0)
            s.set_variable("a", 1.3)
            s.set_variable("b", 2.1)
            s.set_variable("c", 2.2)
            s.set_variable("d", 3.0)
            self.assertAlmostEqual(s.evaluate("((a*b)+(c*d))"), 9.33)
            
            points += 1
        except:
            print("Calculator is aa not correct")
        finally:
            print(f"Calculator {points} Points")
       
    def test_BookStore(self) :
        points = 0.5
        try:
            a = BookStore.BookStore()
            self.assertAlmostEqual(a.loadCatalog("../books.txt"), 499813)
            points += 0.5
            a.addBookByPrefix("Tears of the S")
            b = a.removeFromShoppingCart()
            self.assertAlmostEqual(b.title, "Tears of the Sun")
            a.addBookByPrefix("World of Po")
            b = a.removeFromShoppingCart()
            self.assertAlmostEqual(b.title, "World of Pop Hits of 70's")
           
            points += 1
        except:
            print("BookStore is not correct")
        finally:
            print(f"BookStore: {points} Points")

    
    def test_BinarySearchTreeWithDuplication(self) :
        points = 0
        a = BinarySearchTreeWithDuplication.BinarySearchTreeWithDuplication()
        try:
            a = BinarySearchTreeWithDuplication.BinarySearchTreeWithDuplication()
            a.add(1, "a")
            a.add(1, "b")
            a.add(1, "c")
            a.add(2, "d")
            a.add(3, "e")
            a.add(3, "z")
            self.assertAlmostEqual(1,1)
            self.assertAlmostEqual(a.find(1).__str__(), "a,b,c")
            self.assertAlmostEqual(a.find(2).__str__(), "d") 
            self.assertAlmostEqual(a.find(3).__str__(), "e,z")
            points += 2
        except:
            pass
        finally:
            print(f"BinarySearchTreeWithDuplication: {points} Points")
    
    
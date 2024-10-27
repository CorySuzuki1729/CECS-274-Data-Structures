import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)

    def print_expression(self, s : str) -> str :
        t = ''
        token = ["(", "+", "-", "*", ")"]
        for i in s:
            if i.isalpha():
                if self.dict.find(i) is not None:
                    string_val = str(self.dict.find(i))
                    t += string_val
                else:
                    t += i
            if i in token:
                t += i
        return t


    def matched_expression(self, s : str) -> bool :
        match_stack = ArrayStack.ArrayStack()
        for m in range(len(s)):
            if s[m] == "(":
                match_stack.push("(")
            elif match_stack.n == 0 and s[m] == ")":
                return False
            elif match_stack.n > 0 and s[m] == ")":
                match_stack.pop()

        if match_stack.n == 0:
            return True
        else:
            return False

        #pass

    def build_parse_tree(self, exp : str) ->str:
        signs = ['+', '-', '*', '/']
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node("")
        u = t.r
        for item in exp:
            if item == '(':
                u = u.insert_left()
            elif item == ')':
                if u.parent != None:
                    u = u.parent
            elif item in signs:
                u.x = item
                u = u.insert_right()
            elif item not in signs:
                u.x = item
                u = u.parent
        return t
        #pass
        

    def _evaluate(self, u):
        signs = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if u.left is not None and u.right is not None:
            function = signs[u.x]
            return function(self._evaluate(u.left), self._evaluate(u.right))
        elif u.left is None and u.right is None:
            t = self.dict.find(u.x)
            if t is not None:
                return t
            return u.x
        else:
            if u.left is not None:
                return self._evaluate(u.left)
            else:
                return self._evaluate(u.right)
        #pass

    def evaluate(self, exp):
        try:
            parseTree = self.build_parse_tree(exp)
            return round(self._evaluate(parseTree.r), 2)
        except:
            return 0
        



#s = Calculator()
#print(s.matched_expression("((a*b)+(c*d))"))
#print(s.matched_expression("(a*b)+(c*d"))
#print(s.matched_expression(""))
#s.set_variable("a", 1.3)
#s.set_variable("b", 2.1)
#s.set_variable("c", 2.2)
#s.set_variable("d", 3.0)
#print(s.evaluate("((a*b)+(c*d))"))
import re
class Node:
    def __init__(self,parent = None,  right = None, left = None, key = None, value = None):
        self.parent = parent
        self.right = right
        self.left = left
        self.key = key
        self.value = value
    def search(self, k: int):
        sel = self
        while True:
            if sel.key == k:#если ключ узла равен искомому ключу
                return True, sel
            if sel.key > k:
                if sel.left is None:
                    return False, sel
                sel = sel.left
                continue
            if sel.right is None:
                return False, sel
            sel = sel.right
    
    def add(self, k: int, v: str):
        sel = self
        while True:
            if self.key == k:
                return False, self
            if k < self.key:
                if self.left is None:
                    self.left = Node(key=k, value=v, parent=self)
                    return True, self.left
                self = self.left
                continue
            if self.right is None:
                self.right = Node(key=k, value=v, parent=self)
                return True, self.right
            self = self.right
    
    def left_child_check(self):
        if self.parent is None:
            return False
        return self is self.parent.left
    
class SplayTree:
    def __init__(self, r=None):
        self.root = r
    
    def SplayTree_search(self, k:int):
        if self.root is None:
            return False, None
        return self.root.search(k)
    
    def SplayTree_add(self, k:int, v:str):
        if self.root is None:
            self.root = Node(key=k, value=v)
            return True, self.root
        return self.root.add(k, v)
    
    def SplayTree_max(self):{
        
    }
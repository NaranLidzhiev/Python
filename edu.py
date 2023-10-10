from collections import deque
class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None): #конструктор
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def treeInsert(self, key):
        z = TreeNode(key)
        y = None
        x = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def treeMaximum(self, x=None):
        if x is None:
            x = self.root

        while x is not None and x.right is not None:
            x = x.right
        
  
        return x.key
    
    def treeMinimum(self, x=None):
        if x is None:
            x = self.root
        while x is not None and x.left is not None:
            x = x.left
        
        return x.key

    def treeSuccessor(self, x):
        if  x.right != None:
            return self.treeMinimum(x.right)
        y = x.parent
        while  y != None and x == y.right:
            x = y
            y = y.parent
        return y.key
    
    def treeSearch(self,x, k):
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.treeSearch(x.left, k)
        else:
            return self.treeSearch(x.right, k)
    def updateParent(self, x, newX):
        if x.parent:
            if x.parent.left == x:
                x.parent.left = newX
            else:
                x.parent.right = newX
        if newX:
            newX.parent = x.parent


    def breadthFirstSearch(self):
        if self.root is None: #если у 
            return []

        result = []
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            result.append(node.key)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
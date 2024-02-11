class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


#отсортированный обход


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end='')
        inorder(root.right)

def insert(node, key):
    if node is None:
        return TreeNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def minValueNode(node):
    current = node
    while current.left is not None :
        current = current.left
    return current

def maxValueNode(node):
    current = node
    while current.right is not None :
        current = current.right
    return  current

def DeleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = DeleteNode(root.left, key)
    elif key > root.key:
        root.right = DeleteNode(root.right, key)
    else:
        #если у узла один дочерний узел или вообще их нет
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root
            root = None
            return temp

        #Если у узла два дочерних узла
        #помещаем центрированного преемника на место узла, который нужно удалить
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = DeleteNode(root.right, temp.key)

    return root

# Тестим функции
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Отсортированный обход: ", end=' ')
inorder(root)

print("\nПосле удаления 10")
root = DeleteNode(root, 10)

print("Отсортированный обход: ", end=' ')
inorder(root)


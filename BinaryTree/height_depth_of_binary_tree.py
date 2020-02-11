class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maximum(a,b):
    return a if a > b else b

def getHeightOfBinaryTree(root):
    if not root:
        return 0
    
    return 1 + maximum(getHeightOfBinaryTree(root.left),getHeightOfBinaryTree(root.right))

def Main():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left = Node(11)
    root.right.right = Node(12)
    root.left.left.left = Node(21)
    root.left.left.right = Node(20)
    height = getHeightOfBinaryTree(root)
    print(height)


if __name__ == '__main__':
    Main()

        
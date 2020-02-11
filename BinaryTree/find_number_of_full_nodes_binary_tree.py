class Node:
    """docstring for Node."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getNumberOfFullNodes(root):
    if not root:
        return 0
    
    if root.left and root.right:
        return 1 + getNumberOfFullNodes(root.left) + getNumberOfFullNodes(root.right)
    
    else:
        return getNumberOfFullNodes(root.left) + getNumberOfFullNodes(root.right)
    
    

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
    root.left.right.left = Node(61)
    root.left.right.right = Node(65)
    n = getNumberOfFullNodes(root)
    print(n)


if __name__ == '__main__':
    Main()
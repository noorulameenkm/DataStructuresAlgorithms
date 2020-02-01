class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isElementThereInTree(root, x):
    if not root:
        return False
    if root.data == x:
        return True 
    elif isElementThereInTree(root.left, x):
        return True 
    else:
        return isElementThereInTree(root.right, x)

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
    if isElementThereInTree(root, 10):
        print("FOUND IN TREE")
    else:
        print("NOT FOUND IN TREE");


if __name__ == '__main__':
    Main()
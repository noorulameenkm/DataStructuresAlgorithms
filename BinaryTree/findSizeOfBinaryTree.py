class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def findSize(root):
    if not root:
        return 0
    
    return 1 + findSize(root.left) + findSize(root.right)

def Main():
    root = Node(100)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(26)
    root.right.left = Node(110)
    root.right.right = Node(12)
    root.left.left.left = Node(121)
    root.left.left.right = Node(1)
    print(findSize(root))


if __name__ == '__main__':
    Main() 
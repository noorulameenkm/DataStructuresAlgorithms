class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def deleteBinaryTree(root):
    if not root:
        return
    
    deleteBinaryTree(root.left)
    deleteBinaryTree(root.right)

    del root

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
    root = deleteBinaryTree(root)
    print(root)


if __name__ == '__main__':
    Main() 
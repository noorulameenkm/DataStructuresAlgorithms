class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkStructurallySame(root1, root2):
    if not root1 and not root2:
        return True
    
    if (not root1 and root2) or (root1 and not root2):
        return False
    
    return checkStructurallySame(root1.left, root2.left) and checkStructurallySame(root1.right, root2.right)


def Main():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root1 = root

    root2 = Node(11)
    root2.left = Node(12)
    root2.right = Node(13)
    root2.left.left = Node(9)
    root2.left.right = Node(10)

    n = checkStructurallySame(root1, root2)
    if n:
        print('Same')
    else:
        print('Not Same')



""" This program won't compare the values """

if __name__ == '__main__':
    Main()
        
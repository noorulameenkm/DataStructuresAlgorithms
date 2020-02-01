class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def findMax(root):
    if not root:
        return -1

    max_ = root.data
    left_max = findMax(root.left)
    right_max = findMax(root.right)
    if left_max > max_:
        max_ = left_max
    if right_max > max_:
        max_ = right_max
    
    return max_


def Main():
    root = Node(100)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(26)
    root.right.left = Node(11)
    root.right.right = Node(12)
    root.left.left.left = Node(21)
    root.left.left.right = Node(20)
    print(findMax(root))


if __name__ == '__main__':
    Main() 
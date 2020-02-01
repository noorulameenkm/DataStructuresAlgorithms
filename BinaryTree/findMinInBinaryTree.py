class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def findMin(root):
    if not root:
        return 1000

    min_ = root.data
    left_min = findMin(root.left)
    right_min = findMin(root.right)
    if left_min < min_:
        min_ = left_min
    if right_min < min_:
        min_ = right_min
    
    return min_


def Main():
    root = Node(100)
    root.left = Node(200)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(26)
    root.right.left = Node(11)
    root.right.right = Node(1)
    root.left.left.left = Node(21)
    root.left.left.right = Node(20)
    print(findMin(root))


if __name__ == '__main__':
    Main() 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def findSizeIterative(root):
    if not root:
        return 0
    
    size = 0
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        size += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return size


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
    root.left.left.right.left = Node(15)
    print(findSizeIterative(root))


if __name__ == '__main__':
    Main() 
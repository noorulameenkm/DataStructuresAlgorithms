class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def findMaxIterative(root):
    if not root:
        return -1

    max_ = root.data
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.data > max_:
            max_ = node.data
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return max_


def Main():
    root = Node(100)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(26)
    root.right.left = Node(110)
    root.right.right = Node(12)
    root.left.left.left = Node(121)
    root.left.left.right = Node(20)
    print(findMaxIterative(root))


if __name__ == '__main__':
    Main() 
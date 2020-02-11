class Node:
    """docstring for Node."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getNumberOfHalfNodesIterative(root):
    if not root:
        return 0
    
    count = 0
    queue = [root]
    
    while len(queue) > 0:
        node = queue.pop(0)

        if (node.left and not node.right) or (not node.left and node.right):
            count += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return count
    

def Main():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left = Node(11)
    # root.right.right = Node(12)
    root.left.left.left = Node(21)
    root.left.left.right = Node(20)
    root.left.right.left = Node(61)
    # root.left.right.right = Node(65)
    n = getNumberOfHalfNodesIterative(root)
    print(n)


if __name__ == '__main__':
    Main()
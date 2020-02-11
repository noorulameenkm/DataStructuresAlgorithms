class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def getDeepestNode(root):
    if not root:
        return None

    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return node
    

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
    deep_node = getDeepestNode(root)
    if deep_node:
        print(deep_node.data)


if __name__ == '__main__':
    Main()
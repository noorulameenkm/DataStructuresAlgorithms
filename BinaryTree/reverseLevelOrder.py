class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reverseLevelOrderTraversal(root):
    if not root:
        return
    
    queue = [root]
    stack = []
    while len(queue) > 0:
        node = queue.pop(0)
        stack.insert(0, node.data)
        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)
        
    
    while len(stack) > 0:
        print(stack.pop(0), end=' ')
    
    print('\n', end='')
    return



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
    reverseLevelOrderTraversal(root)


if __name__ == '__main__':
    Main() 
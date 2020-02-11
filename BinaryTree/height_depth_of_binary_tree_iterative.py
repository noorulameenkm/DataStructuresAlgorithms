class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def getHeightOfBinaryTreeIterative(root):
    height = 0
    queue = [root, '$']
    while len(queue) > 0:
        el = queue.pop(0)
        if el == '$':
            height += 1
            if len(queue) > 0:
                queue.append('$')
        else:
            node = el
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return height
    

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
    height = getHeightOfBinaryTreeIterative(root)
    print(height)


if __name__ == '__main__':
    Main()

        
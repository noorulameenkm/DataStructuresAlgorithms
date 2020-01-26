import queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def recursiveInOrder(root):
    if root:
        recursiveInOrder(root.left)
        print(root.data, end=' ')
        recursiveInOrder(root.right)


def iterativeInOrder(root):
    if not root:
        return root

    stack = queue.LifoQueue(maxsize=0)
    while True:
        while root:
            stack.put(root)
            root = root.left
        
        if stack.empty():
            break
        else:
            top = stack.get()
            print(top.data, end=' ')
            root = top.right
    print('\n', end='')
    return

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Recursive inOrder Results")
    recursiveInOrder(root)
    print('\nIterative inOrder Results')
    iterativeInOrder(root)

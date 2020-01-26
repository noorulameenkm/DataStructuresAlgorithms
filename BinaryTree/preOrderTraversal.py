import queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def recursivePreOrder(root):
    if root:
        print(root.data, end=' ')
        recursivePreOrder(root.left)
        recursivePreOrder(root.right)


def iterativePreOrder(root):
    if not root:
        return root

    stack = queue.LifoQueue(maxsize=0)
    stack.put(root)
    while not stack.empty():
        top = stack.get()
        print(top.data, end=' ')
        if top.right:
            stack.put(top.right)
        if top.left:
            stack.put(top.left)

    print('\n', end='')
    return

def anotherIterativePreOrder(root):
    stack = queue.LifoQueue(maxsize=0)
    while True:
        while root:
            print(root.data, end=' ')
            stack.put(root)
            root = root.left
        
        if stack.empty():
            break
            
        top = stack.get()
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

    print("Recursive preOrder Results")
    recursivePreOrder(root)
    print('\nIterative preOrder Results')
    iterativePreOrder(root)
    print('Another Iterative preOrder Results')
    anotherIterativePreOrder(root)

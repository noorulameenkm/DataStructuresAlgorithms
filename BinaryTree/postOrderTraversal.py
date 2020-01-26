import queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def recursivePostOrder(root):
    if root:
        recursivePostOrder(root.left)
        recursivePostOrder(root.right)
        print(root.data, end=' ')



def iterativePostOrder(root):
    if not root:
        return root

    stack_1 = queue.LifoQueue(maxsize=0)
    stack_2 = queue.LifoQueue(maxsize=0)

    stack_1.put(root)
    while not stack_1.empty():
        top = stack_1.get()
        stack_2.put(top)
        if top.left:
            stack_1.put(top.left)
        if top.right:
            stack_1.put(top.right)
    
    while not stack_2.empty():
        top = stack_2.get()
        print(top.data, end=' ')

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

    print("Recursive postOrder Results")
    recursivePostOrder(root)
    print('\nIterative postOrder Results')
    iterativePostOrder(root)

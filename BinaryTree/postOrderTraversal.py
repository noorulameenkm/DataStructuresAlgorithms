import queue

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def getSeek(stack):
    if len(stack) > 0:
        return stack[0]
    
    return None

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

def iterativePostOrderWithOneStack(root):
    if not root:
        return root

    stack = []
    while True:
        while root:
            if root.right:
                stack.insert(0, root.right)
            stack.insert(0, root)
            root = root.left

        if len(stack) <= 0:
            break
        
        root = stack.pop(0)

        if root.right and root.right == getSeek(stack):
            stack.pop(0)
            stack.insert(0, root)
            root = root.right            
        
        else:
            print(root.data, end=' ')
            root = None
    
    print('\n', end='')

def anotherIterativePostOrderWithOneStack(root):
    if not root:
        return root
    
    stack = []
    while True:
        while root:
            stack.insert(0, root)
            stack.insert(0, root)
            root = root.left

        
        if len(stack) <= 0:
            break
        
        root = stack.pop(0)
        if root == getSeek(stack):
            root = root.right
        
        else:
            print(root.data, end=' ')
            root = None



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
    print('Iterative PostOrder Traversal with one stack')
    iterativePostOrderWithOneStack(root)
    print('Another Iterative PostOrder Traversal with one stack')
    anotherIterativePostOrderWithOneStack(root)
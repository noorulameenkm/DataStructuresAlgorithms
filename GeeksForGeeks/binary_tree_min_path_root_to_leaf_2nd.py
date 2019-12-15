import queue

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def printNodes(parent,leaf):
    if parent[leaf] is leaf:
        print(leaf, end = ' ')
    
    else:
        printNodes(parent, parent[leaf])
        print(leaf, end =  ' ')
    
    return

def printFirstMinPath(tree):
    q = queue.Queue(maxsize = 0)
    parent = {}
    q.put(tree)
    parent[tree.val] = tree.val
    while not q.empty():
        node = q.get()
        if not node.left and not node.right:
            printNodes(parent, node.val)
            break
        elif not node.left and node.right:
            parent[node.right.val] = node.val
            q.put(node.right)
        elif node.left and not node.right:
            parent[node.left.val] = node.val
            q.put(node.left)
        else:
            parent[node.right.val] = node.val
            parent[node.left.val] = node.val
            q.put(node.left)
            q.put(node.right)
    print('\n', end = '')



if __name__ == '__main__':

    """ 
        Test Case 1
    """
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.left.left = Node(10)
    root.left.left.left.left = Node(13)
    root.left.left.right = Node(11)
    root.left.left.right.right = Node(14)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.left.left = Node(20)
    root.right.left.left.left = Node(21)
    root.right.right = Node(7)
    root.right.right.right = Node(8)

    """ 
        Test Case 2
    """
    # root = Node(1)  
    # root.left = Node(2)  
    # root.right = Node(3)  
    # root.left.left = Node(4)  
    # root.right.left = Node(5)  
    # root.right.right = Node(7)  
    # root.left.left.left = Node(10)  
    # root.left.left.right = Node(11)  
    # root.right.right.left = Node(8)  
    
    printFirstMinPath(root)
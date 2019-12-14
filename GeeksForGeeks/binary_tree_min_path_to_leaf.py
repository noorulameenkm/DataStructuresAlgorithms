import queue

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def minimum(a,b):
    return a if a < b else b

def lengthToLeaf(node):
    if node.right == None and node.left == None:
        return 1
    elif node.right != None and node.left == None:
        return lengthToLeaf(node.right) + 1
    elif node.right == None and node.left != None:
        return lengthToLeaf(node.left) + 1
    else:
        return minimum(lengthToLeaf(node.left), lengthToLeaf(node.right)) + 1

def printFirstMinPath(tree):
    q = queue.Queue(maxsize=0)
    q.put(tree)
    while q.empty() != True:
        node = q.get()
        if node.left == None and node.right != None:
            print(node.val, end = ' ')
            q.put(node.right)
        elif node.left != None and node.right == None:
            print(node.val, end = ' ')
            q.put(node.left)
        elif node.left != None and node.right != None:
            s = lengthToLeaf(node.left)
            m = lengthToLeaf(node.right)
            print(node.val, end = ' ')
            if minimum(s,m) == s:
                q.put(node.left)
            else:
                q.put(node.right)
        else:
            print(node.val)


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(4)
    tree.left.left.left = Node(10)
    tree.left.left.left.left = Node(13)
    tree.left.left.right = Node(11)
    tree.left.left.right.right = Node(14)
    tree.right = Node(3)
    tree.right.left = Node(5)
    tree.right.left.left = Node(20)
    tree.right.left.left.left = Node(21)
    tree.right.right = Node(7)
    tree.right.right.right = Node(8)
    printFirstMinPath(tree)







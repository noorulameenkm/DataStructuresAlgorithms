import queue
from collections import defaultdict

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def calculateSum(leaf_nodes, parent):
    sums = defaultdict(list)

    for node in leaf_nodes:
        path = []
        sumNodes = 0
        nodeVal = node.val

        while not parent[nodeVal] is nodeVal:
            sumNodes = sumNodes + nodeVal
            path.insert(0,nodeVal)
            nodeVal = parent[nodeVal]
        
        sumNodes = sumNodes + nodeVal
        path.insert(0,nodeVal)
        sums[sumNodes] = path

    minVal = min(list(sums.keys()))
    pathToLeaf = sums[minVal]
    print(*pathToLeaf, sep = ' ')



def getLeafNodes(tree):
    leaf_nodes = []
    parent = {}
    q = queue.Queue(maxsize = 0)
    q.put(tree)
    parent[tree.val] = tree.val
    while not q.empty():
        node = q.get()
        if not node.left and not node.right:
            leaf_nodes.append(node)
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
    return (leaf_nodes, parent)


if __name__ == '__main__':
    tree = Node(10)
    tree.left = Node(-2)
    tree.left.left = Node(8)
    tree.left.right = Node(-4)
    tree.right = Node(7)

    leaf_nodes, parent = getLeafNodes(tree)
    calculateSum(leaf_nodes, parent)

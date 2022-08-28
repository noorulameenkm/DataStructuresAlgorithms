from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def lowest_common_ancestor(node1, node2):
    
    # Write your code here
    ancestors = set()

    while node1.parent:
        ancestors.add(node1)
        node1 = node1.parent

    ancestors.add(node1)

    while node2 and node2 not in ancestors:
        node2 = node2.parent
    
    return node2



root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.parent = root
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.left.parent = root.left
root.left.right.parent = root.left
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.left.right.left.parent = root.left.right
root.left.right.right.parent = root.left.right
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.right.left.parent = root.right
root.right.right.parent = root.right
lca = lowest_common_ancestor(root.left, root.left.right.right)
print(lca.val)
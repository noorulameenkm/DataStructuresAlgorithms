# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            root = TreeNode(val)
        else:
            root = insert(root, val)
        
        return root
        
        
def insert(root, val):
    if not root:
        return TreeNode(val)
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
        
    return root
        
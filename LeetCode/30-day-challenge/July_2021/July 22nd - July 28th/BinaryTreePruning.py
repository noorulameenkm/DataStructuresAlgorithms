
"""
    Problem Link:- https://leetcode.com/problems/binary-tree-pruning/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        
        def dfs(root_):
            if not root_:
                return False
            
            left = dfs(root_.left)
            right = dfs(root_.right)
            
            if not left:
                root_.left = None
            
            if not right:
                root_.right = None
            
            return root_.val == 1 or left or right
        
        
        dfs(root)
        
        if root and root.val == 0 and not root.left and not root.right:
            root = None
        
        return root
        
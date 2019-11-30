# Iterative pre-order traversal of binary tree

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
            
        l = []
        stack = [root]
        while len(stack) != 0:
            el = stack.pop(0)
            l.append(el.val)
            if el.right is not None:
                stack.insert(0,el.right)
            if el.left is not None:
                stack.insert(0,el.left)
        
        return l

# Initialising the tree
k = TreeNode(1)
k.left = TreeNode(2)
k.right = TreeNode(3)
sol = Solution()
print(sol.preorderTraversal(k))
        
        
        
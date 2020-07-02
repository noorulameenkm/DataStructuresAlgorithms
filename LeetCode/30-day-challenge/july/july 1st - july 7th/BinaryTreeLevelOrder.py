# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        order = []
        queue = [root, '#']
        level = []
        while len(queue) > 0:
            n = queue.pop(0)
            
            if n == '#':
                if len(queue) > 0:
                    queue.append('#')
                
                order.insert(0, level)
                level = []
            else:
                level.append(n.val)
                
                if n.left:
                    queue.append(n.left)
                
                if n.right:
                    queue.append(n.right)
        
        return order
                
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        queue = [root, '#']
        k = []
        result = []
        while len(queue) > 0:
            nd = queue.pop(0)
            
            if nd == '#':
                if len(queue) > 0:
                    queue.append('#')
                    
                result.append(k)
                k = []
            else:
                k.append(nd.val)
                
                if nd.left:
                    queue.append(nd.left)
                if nd.right:
                    queue.append(nd.right)
                    
        return result
                
            
        
        
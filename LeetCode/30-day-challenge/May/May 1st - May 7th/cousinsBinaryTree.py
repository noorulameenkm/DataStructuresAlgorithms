# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x, y):
        if not root:
            return False
        
        x_details = [None, None]
        y_details = [None, None]
        
        findParentAndLevel(root, x, y, x_details, y_details)
        
        return x_details[0] == y_details[0] and x_details[1] != y_details[1]
    
    
def findParentAndLevel(root, x, y, x_details, y_details):
    queue = [root, '#']
    parent = None
    level = 0
    
    while len(queue) > 0:
        node = queue.pop(0)
        
        if node == '#':
            level += 1
            if len(queue) > 0:
                queue.append('#')
        else:
            if node.left:
                if node.left.val == x:
                    x_details[0] = level + 1
                    x_details[1] = node.val
                
                if node.left.val == y:
                    y_details[0] = level + 1
                    y_details[1] = node.val
                
                queue.append(node.left)
            
            if node.right:
                if node.right.val == x:
                    x_details[0] = level + 1
                    x_details[1] = node.val
                
                if node.right.val == y:
                    y_details[0] = level + 1
                    y_details[1] = node.val
            
                queue.append(node.right)
    
            
        
        
        
"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root):
        if not root:
            return root
        
        queue = deque()
        queue.append(root)
        
        while queue:
            length = len(queue)
            
            i = 0
            while i < length:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
                
                if i < length - 1:
                    node.next = queue[0]
                else:
                    node.next = None
                
                i += 1
        return root
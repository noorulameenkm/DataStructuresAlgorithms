from collections import deque

"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([])
        
        if root is None:
            return root
        
        queue.append(root)
        while queue:
            levelLength = len(queue)
            
            for i in range(levelLength):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                if i == levelLength - 1:
                    node.next = None
                else:
                    node.next = queue[0]
        return root

                    
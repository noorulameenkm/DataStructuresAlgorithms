# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def isEvenOddTree(self, root):
        if not root:
            return False
        
        return checkEvenOdd(root)
    
    
    
def checkEvenOdd(root):
    level = 0
    queue = deque()
    
    queue.append(root)
    
    while queue:
        levelLength = len(queue)
        currentLevel = []
        for _ in range(levelLength):
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
                
            currentLevel.append(currentNode.val)
        
        if level % 2 == 0:
            isStrictlyIncreasing = strictlyIncreasing(currentLevel)
            if not isStrictlyIncreasing:
                return False
        else:
            isStrictlyDecreasing = strictlyDecreasing(currentLevel)
            if not isStrictlyDecreasing:
                return False
            
        level += 1
            
        
    return True


def strictlyIncreasing(arr):
    if len(arr) <= 1:
        return arr[0] % 2 != 0
    
    if arr[0] % 2 == 0:
        return False
    
    for i in range(1, len(arr)):
        if arr[i] % 2 == 0 or  arr[i] <= arr[i - 1]:
            return False
    
    return True


def strictlyDecreasing(arr):
    if len(arr) <= 1:
        return arr[0] % 2 == 0
    
    if arr[0] % 2 != 0:
        return False
    
    for i in range(1, len(arr)):
        if arr[i] % 2 != 0 or arr[i] >= arr[i - 1]:
            return False
    
    return True
        
                    
        
        
        
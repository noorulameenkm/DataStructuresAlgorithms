# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        
        sum_ = getSum(root, 0)
        
        return sum_
    
    

def getSum(root, sum_):
    if not root:
        return None
    
    new_sum_ = 0
    if root.val == 0:
        new_sum_ = sum_ * 10
    else:
        new_sum_ = sum_ * 10 + root.val
        
        
    left = getSum(root.left, new_sum_)
    right = getSum(root.right, new_sum_)
    
    _sum = 0
    if not left and not right:
        _sum = _sum + new_sum_
    elif not left and right:
        _sum = _sum + right
    elif left and not right:
        _sum = _sum + left
    else:
        _sum = left + right
    
    return _sum
        
        
        

# construct input
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(f'Solution is {Solution().sumNumbers(root)}')
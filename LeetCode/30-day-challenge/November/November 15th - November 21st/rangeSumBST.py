# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        
        queue = deque([])
        sum_ = 0
        queue.append(root)
        
        while queue:
            
            pop = queue.popleft()
            
            if pop.val >= low and pop.val <= high:
                sum_ += pop.val
                
            if pop.left and low < pop.val:
                queue.append(pop.left)
            
            if pop.right and high > pop.val:
                queue.append(pop.right)
                
        return sum_



def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    print(Solution().rangeSumBST(root, 7, 15))



main()
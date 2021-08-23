"""
    Problem Link:- https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root, k):
        return self.isExistTwoSum(root, root, k)

    def isExistTwoSum(self, node, root, k):
        if node is None:
            return False

        search_node = self.find(root, k - node.val)
        if search_node and search_node != node:
            return True

        return self.isExistTwoSum(node.left, root, k) or self.isExistTwoSum(node.right, root, k)

    def find(self, root, target):
        if root is None:
            return None

        if root.val == target:
            return root

        if root.val > target:
            return self.find(root.left, target)

        return self.find(root.right, target)


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().findTarget(root, 9))

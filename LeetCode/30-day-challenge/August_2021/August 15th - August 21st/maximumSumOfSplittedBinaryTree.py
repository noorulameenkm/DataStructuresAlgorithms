"""
    Problem Link:- https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximum_sum_of_splited_binary_tree(self, root):

        self.ans = 0
        total = 0

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left * (total - left), right * (total - right))
            return node.val + left + right

        total = dfs(root)
        dfs(root)
        MOD = pow(10, 9) + 7
        return self.ans % MOD


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
print(Solution().maximum_sum_of_splited_binary_tree(root))

"""
    Problem Link:- https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.good_nodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, max_val):
            if node is None:
                return

            if node.val >= max_val:
                self.good_nodes += 1
            max_v = max(max_val, node.val)
            traverse(node.left, max_v)
            traverse(node.right, max_v)

        traverse(root, root.val)
        return self.good_nodes

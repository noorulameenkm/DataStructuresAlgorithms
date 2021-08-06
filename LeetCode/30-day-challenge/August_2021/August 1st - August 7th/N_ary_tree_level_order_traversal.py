from collections import deque

"""
    Problem Link:- https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([])
        queue.append(root)
        level_order = []
        while len(queue) > 0:
            level_length = len(queue)
            level = []
            for _ in range(level_length):
                node = queue.popleft()
                level.append(node.val)

                if node.children:
                    for child in node.children:
                        if child:
                            queue.append(child)

            level_order.append(list(level))

        return level_order

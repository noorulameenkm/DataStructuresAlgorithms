
"""
    Problem Link:- https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def construct(nums, start, end):
    if start <= end:
        middle = start + (end - start) // 2
        root = TreeNode(nums[middle])
        root.left = construct(nums, start, middle - 1)
        root.right = construct(nums, middle + 1, end)
        return root
    else:
        return None



def convert(nums):
    return construct(nums, 0, len(nums) - 1)



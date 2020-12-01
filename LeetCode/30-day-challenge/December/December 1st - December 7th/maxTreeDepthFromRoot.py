# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.treeMaxDepthFromRoot = 0
        
    def maxDepth(self, root):
        self.findMaxDepth(root)
        return self.treeMaxDepthFromRoot
    
    def findMaxDepth(self, currentNode):
        if currentNode is None:
            return 0
        
        leftMaxHeight = self.findMaxDepth(currentNode.left)
        rightMaxHeight = self.findMaxDepth(currentNode.right)
        
        self.treeMaxDepthFromRoot = max(self.treeMaxDepthFromRoot, max(leftMaxHeight, rightMaxHeight) + 1)
        
        return max(leftMaxHeight, rightMaxHeight) + 1



def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().maxDepth(root))

main()
        
        
        
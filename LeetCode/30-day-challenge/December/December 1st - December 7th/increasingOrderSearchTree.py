# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root):
        results = []
        self.constructIncreasingBST(root, results)
        
        if len(results) == 0:
            return None
        if len(results) == 1:
            return TreeNode(results[0])
        
        new_root = TreeNode(results[0])
        current = new_root
        for i in range(1, len(results)):
            current.right = TreeNode(results[i])
            current = current.right
            
        return new_root
        
    def constructIncreasingBST(self, root, result):
        if root:
            self.constructIncreasingBST(root.left, result)
            result.append(root.val)
            self.constructIncreasingBST(root.right, result)



def main():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    Solution().increasingBST(root)


main()

                
        
        
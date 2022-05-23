# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        
        def find_decimal(array_binary):
            num_str = ''.join(array_binary)
            return int(num_str, 2)
        
        def internal(root, current_path, _sum):
            
            current_path.append(str(root.val))
            if root.left is None and root.right is None:
                number = find_decimal(current_path)
                _sum[0] += number
                return
            
            if root.left is not None:
                internal(root.left, current_path, _sum)
                current_path.pop()
            
            if root.right is not None:
                internal(root.right, current_path, _sum)
                current_path.pop()
            
            
        if root is None:
            return 0
        
        sum_ = [0]
        internal(root, [], sum_)
        return sum_[0]


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print(Solution().sumRootToLeaf(root))
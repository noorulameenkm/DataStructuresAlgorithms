class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""
    Time Complexity - O(n)
    Space Complexity - O(n)
"""
def longest_route(root):
    if not root:
        return 0
    
    def height(node):
        if not node:
            return 0
        
        l_height = height(node.left)
        r_height = height(node.right)
        return max(l_height, r_height) + 1
    

    lh = height(root.left)
    rh = height(root.right)
    left_path = longest_route(root.left)
    right_path = longest_route(root.right)

    return max(lh + rh + 1, max(left_path, right_path))



root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.left.left = TreeNode("d")
root.right.left = TreeNode("e")
root.right.right = TreeNode("f")

print("The longest route will pass through", longest_route(root), "checkpoints")
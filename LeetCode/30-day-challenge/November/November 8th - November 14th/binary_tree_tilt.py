# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode):
        if root is None:
            return 0
        else:
            result = findTiltOfRoot(root)
            return result[0]
        

def findTiltOfRoot(root):
    if root is None:
        return [0, 0]
    
    left = findTiltOfRoot(root.left)
    right = findTiltOfRoot(root.right)

    tiltVal = [left[0] + right[0] + abs(left[1] - right[1]), left[1] + right[1] + root.val]

    return tiltVal




def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(Solution().findTilt(root))


main()

        
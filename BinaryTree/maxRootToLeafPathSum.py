import math

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




def findMaxPath(root):
    max_ = -math.inf
    maxpath = [[]]
    findMaxPathRecursive(root, 0, [], [max_], maxpath)
    return maxpath[0]


def findMaxPathRecursive(currentnode, currentsum, currentpath, max_, maxpath):
    if not currentnode:
        return

    currentsum += currentnode.val
    currentpath.append(currentnode.val)
    
    if currentnode.left is None and currentnode.right is None:
        if currentsum > max_[0]:
            max_[0] = currentsum
            maxpath[0] = list(currentpath)
    else:
        findMaxPathRecursive(currentnode.left, currentsum, currentpath, max_, maxpath)

        findMaxPathRecursive(currentnode.right, currentsum, currentpath, max_, maxpath)

    del currentpath[-1]
    currentsum -= currentnode.val





def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(11)
  root.right.right = TreeNode(5)
  print("Max sum path from root to leaf" +
        ": " + str(findMaxPath(root)))


main()  
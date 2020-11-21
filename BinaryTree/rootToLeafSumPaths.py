class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


"""
Time Complexity - O(NlogN)
Space Complexity - O(N)
"""

def find_paths(root, sum_):
  allPaths = []
  find_paths_recursive(root, sum_, [], allPaths)
  return allPaths


def find_paths_recursive(root, sum_, currentPath, allPaths):
  if not root:
    return 
  
  currentPath.append(root.val)

  if root.val == sum_ and root.left is None and root.right is None:
    allPaths.append(list(currentPath))
  else:
    # traverse the left sub-tree
    find_paths_recursive(root.left, sum_ - root.val, currentPath, allPaths)
    # traverse the right sub-tree
    find_paths_recursive(root.right, sum_ - root.val, currentPath, allPaths)

  # remove the current node from the path to backtrack,
  # we need to remove the current node while we are going up the recursive call stack.
  del currentPath[-1]


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()

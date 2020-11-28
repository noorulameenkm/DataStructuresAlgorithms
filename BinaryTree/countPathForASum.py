class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


"""
Time Complexity - O(N * 2) -> O(NlogN) for balanced binary tree
Space Complexity - O(N)
"""

def count_paths(root, S):
  return count_path_recursive(root, S, [])

def count_path_recursive(currentNode, S, currentPath):
  if not currentNode:
    return 0
  
  # add currentNode to the currentPath
  currentPath.append(currentNode.val)

  pathSum, pathCount = 0, 0 
  # find the sums of all sub-paths in the current path list
  for i in range(len(currentPath) - 1, -1, -1):
    pathSum += currentPath[i]
    if pathSum == S:
      pathCount += 1
    
  # traverse the left sub-tree
  pathCount += count_path_recursive(currentNode.left, S, currentPath)
  # traverse the right sub-tree
  pathCount += count_path_recursive(currentNode.right, S, currentPath)

  # remove the current node from the path to backtrack
  # we need to remove the current node while we are going up the recursive call stack
  del currentPath[-1]

  return pathCount
     


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()

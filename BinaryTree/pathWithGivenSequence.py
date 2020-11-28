class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

def find_path(root, sequence):
  if not root:
    return len(sequence) == 0
  
  return find_path_recursive(root, sequence, 0)


def find_path_recursive(current_node, sequence, currentIndex):
  if not current_node:
    return False

  length = len(sequence)
  if currentIndex >= length or sequence[currentIndex] != current_node.val:
    return False
  
  # if the current node is a leaf, add it is the end of the sequence, we have found a path!
  if current_node.val == sequence[currentIndex] and current_node.left is None and current_node.right is None:
    return True
  
  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true
  return find_path_recursive(current_node.left, sequence, currentIndex + 1) or find_path_recursive(current_node.right, sequence, currentIndex + 1)


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()

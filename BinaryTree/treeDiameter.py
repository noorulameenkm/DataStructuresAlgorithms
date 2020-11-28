class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

  def __init__(self):
    self.treeDiameter = 0

  """
  Time Complexity - O(N)
  Space Complexity - O(N)
  """
  def find_diameter(self, root):
    self.calculate_height(root)
    return self.treeDiameter
  
  def calculate_height(self, root):
    if root is None:
      return 0
    
    leftHeight = self.calculate_height(root.left)
    rightHeight = self.calculate_height(root.right)

    # diameter at the current node will be equal to the height of left subtree +
    # the height of right sub-trees + '1' for the current node
    currentDiameter = leftHeight + rightHeight + 1

    # update the global tree diameter
    self.treeDiameter = max(self.treeDiameter, currentDiameter)

    # height of the current node will be equal to the maximum of the hights of
    # left or right subtrees plus '1' for the current node
    return max(leftHeight, rightHeight) + 1

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()








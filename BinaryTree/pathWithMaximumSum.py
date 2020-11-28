import math


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeSum:
  def __init__(self):
    self.maxSum = -math.inf

  """
  Time Complexity - O(N)
  Space Complexity - O(N)
  """
  def find_maximum_path_sum(self, root):
    self.calculateSum(root)
    return self.maxSum

  def calculateSum(self, root):
    if not root:
      return 0
    
    leftMaxSum = self.calculateSum(root.left)
    rightMaxSum = self.calculateSum(root.right)

    # ignore paths with negative sums, since we need to find the maximum sum we should
    # ignore any path which has an overall negative sum.
    leftMaxSum = max(leftMaxSum, 0)
    rightMaxSum = max(rightMaxSum, 0)

    # maximum path sum at the current node will be equal to the sum from the left subtree +
    # the sum from right subtree + val of current node
    currentSum = leftMaxSum + rightMaxSum + root.val

    # update the global maximum sum
    self.maxSum = max(self.maxSum, currentSum)

    # maximum sum of any path from the current node will be equal to the maximum of
    # the sums from left or right subtrees plus the value of the current node
    return max(leftMaxSum, rightMaxSum) + root.val


def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(TreeSum().find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(TreeSum().find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(TreeSum().find_maximum_path_sum(root)))


main()

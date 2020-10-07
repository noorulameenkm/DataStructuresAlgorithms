from collections import deque
import math

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def max_val_level(root):
  result = []
  queue = deque()
  queue.append(root)
  while queue:
    levelLength = len(queue)
    max_ = -math.inf
    for _ in range(levelLength):
      currentNode = queue.popleft()

      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
      
      max_ = max(max_, currentNode.val)
    result.append(max_)
    
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Max Value at Each level: " + str(max_val_level(root)))


main()








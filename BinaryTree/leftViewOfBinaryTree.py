from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

def tree_left_view(root):
  result = []
  queue = deque()
  queue.append(root)

  while queue:
    levelLength = len(queue)
    result.append(queue[0])

    for i in range(levelLength):
      currentNode = queue.popleft()

      if currentNode.left:
        queue.append(currentNode.left)
      
      if currentNode.right:
        queue.append(currentNode.right)

  return result


def tree_left_view2(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    for i in range(0, levelSize):
      currentNode = queue.popleft()
      # if it is the last node of this level, add it to the result
      if i == 0:
        result.append(currentNode)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_left_view(root)
  print("Tree left view: ")
  for node in result:
    print(str(node.val) + " ", end='')

  root2 = TreeNode(12)
  root2.left = TreeNode(7)
  root2.right = TreeNode(1)
  root2.left.left = TreeNode(9)
  root2.right.left = TreeNode(10)
  root2.right.right = TreeNode(5)
  root2.left.left.left = TreeNode(3)
  result = tree_left_view2(root2)
  print("\nTree left view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()

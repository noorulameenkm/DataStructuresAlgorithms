from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

def connect_level_order_siblings(root):
  # TODO: Write your code here
  queue = deque()
  queue.append(root)

  while queue:
    levelLength = len(queue)

    current = queue.popleft()
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

    for i in range(levelLength - 1):
      next_ = queue.popleft()
      if next_.left:
        queue.append(next_.left)
      if next_.right:
        queue.append(next_.right)

      current.next = next_
      current = next_
    
    current.next_ = None

  return


def connect_level_order_siblings2(root):
  if root is None:
    return

  queue = deque()
  queue.append(root)
  while queue:
    previousNode = None
    levelSize = len(queue)
    # connect all nodes of this level
    for _ in range(levelSize):
      currentNode = queue.popleft()
      if previousNode:
        previousNode.next = currentNode
      previousNode = currentNode

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

 

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()

  root2 = TreeNode(12)
  root2.left = TreeNode(7)
  root2.right = TreeNode(1)
  root2.left.left = TreeNode(9)
  root2.right.left = TreeNode(10)
  root2.right.right = TreeNode(5)
  connect_level_order_siblings2(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()

main()

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

def connect_all_siblings(root):
  # TODO: Write your code here
  queue = deque()
  queue.append(root)

  while queue:
    current = queue.popleft()

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

    if queue:
      current.next = queue[0]

  return


def connect_all_siblings2(root):
  if root is None:
    return

  queue = deque()
  queue.append(root)
  currentNode, previousNode = None, None
  while queue:
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
  connect_all_siblings(root)
  root.print_tree()


  print()

  root2 = TreeNode(12)
  root2.left = TreeNode(7)
  root2.right = TreeNode(1)
  root2.left.left = TreeNode(9)
  root2.right.left = TreeNode(10)
  root2.right.right = TreeNode(5)
  connect_all_siblings2(root2)
  root2.print_tree()


main()

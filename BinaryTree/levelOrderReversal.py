from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  # TODO: Write your code here
  queue = deque()
  queue.append(root)

  while queue:
    levelLength = len(queue)
    currentlevel = []
    for _ in range(levelLength):
      currentNode = queue.popleft()

      currentlevel.append(currentNode.val)
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    
    result.insert(0, currentlevel)
    currentlevel = []

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  # TODO: Write your code here
  queue = deque([root, '#'])
  nodeValues = []
  while len(queue) > 0:
    popped = queue.popleft()

    if popped == '#':
      if len(queue) > 0:
        queue.append('#')
        
      result.append(nodeValues)
      nodeValues = []
    else:
      nodeValues.append(popped.val)
      if popped.left:
        queue.append(popped.left)
      if popped.right:
        queue.append(popped.right)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()


def traverse2(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node to the current level
      currentLevel.append(currentNode.val)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(currentLevel)

  return result


def main2():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse2(root)))


main2()
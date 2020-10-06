from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  # TODO: Write your code here
  level = 0
  queue = deque()
  queue.append(root)

  while queue:

    currentLevel = []
    levelLength = len(queue)
    for _ in range(levelLength):
      currentNode = queue.popleft()
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

      currentLevel.append(currentNode.val)
    
    if level % 2 != 0:
      currentLevel = currentLevel[::-1]
    
    result.append(currentLevel)
    level += 1
    
  return result


def traverse2(root):
  result = []
  queue = deque()
  queue.append(root)
  leftToRight = True

  while queue:
    currentLevel = deque()
    levelLength = len(queue)
    for _ in range(levelLength):
      currentNode = queue.popleft()
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
      
      if leftToRight:
          currentLevel.append(currentNode.val)
      else:
          currentLevel.appendleft(currentNode.val)
    
    result.append(list(currentLevel))
    leftToRight = not leftToRight
    
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))
  print("Zigzag traversal2: " + str(traverse2(root)))


main()

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def getAllPaths(root):
    allPaths = []
    findAllPathsRecursive(root, [], allPaths)
    return allPaths

def findAllPathsRecursive(currentNode, currentpath, allPaths):
    if not currentNode:
        return
    
    currentpath.append(currentNode.val)
    if currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentpath))
    else:
        findAllPathsRecursive(currentNode.left, currentpath, allPaths)
        findAllPathsRecursive(currentNode.right, currentpath, allPaths)
    
    del currentpath[-1]




def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree root to leaf paths" +
        ": " + str(getAllPaths(root)))


main()


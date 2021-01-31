
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def find_unique_trees(n):
  result = []
  if n <= 0:
    return result
  
  return find_unique_trees_(1, n)


"""
Time Complexity - O(N * 2^N)
Space Complexity - O(2^N)
"""
def find_unique_trees_(start, end):

  result = []
  # base condition, return 'None' for an empty sub-tree
  # consider n = 1, in this case we will have start = end = 1, this means we should have only one tree
  # we will have two recursive calls, findUniqueTreesRecursive(1, 0) & (2, 1)
  # both of these should return 'None' for the left and the right child
  if start > end:
    result.append(None)
    return result
  
  for i in range(start, end + 1):
    # making 'i' the root of the tree
    leftSubtree = find_unique_trees_(start, i - 1)
    rightSubtree = find_unique_trees_(i + 1, end)

    for left in leftSubtree:
      for right in rightSubtree:
        root = TreeNode(i)
        root.left = left
        root.right = right

        result.append(root)

  return result



def main():
  print("Total trees: " + str(find_unique_trees(2)))
  print("Total trees: " + str(find_unique_trees(3)))


main()


"""
This problem follows the Subsets pattern and is quite similar to Evaluate Expression. Following a similar approach, we can iterate from 1 to ‘n’ and consider each number as the root of a tree. All smaller numbers will make up the left sub-tree and bigger numbers will make up the right sub-tree. 
We will make recursive calls for the left and right sub-trees
"""


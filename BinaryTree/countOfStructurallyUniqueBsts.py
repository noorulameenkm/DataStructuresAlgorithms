class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


"""
Time Complexity - O(N * 2 ^ N)
Space Complexity - O(2 ^ N)
"""
def count_trees(n):
  count = 0
  if n <= 1:
    return 1
  
  for i in range(1, n + 1):
    # making 'i' root of the tree
    countLeftSubtrees = count_trees(i - 1)
    countRightSubtrees = count_trees(n - i)
    count += (countRightSubtrees * countLeftSubtrees)

  return count 


"""
Time Complexity - O(N ^ 2)
Space Complexity - O(N)
"""
def count_trees_memoization(n):
    return count_trees_memoization_recursive({}, n)


def count_trees_memoization_recursive(map, n):
    if n in map:
        return map[n]

    if n <= 1:
        return 1

    count = 0
    for i in range(1, n + 1):
        countLeftSubtrees = count_trees_memoization_recursive(map, i - 1)
        countRightSubtrees = count_trees_memoization_recursive(map, n - i)
        count += (countLeftSubtrees * countRightSubtrees)

    map[n] = count

    return map[n]

def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))

  print("Total trees: " + str(count_trees_memoization(2)))
  print("Total trees: " + str(count_trees_memoization(3)))


main()

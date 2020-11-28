class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

def find_sum_of_path_numbers(root):
  sums = []
  current_sum = [0]
  find_sum_path_recursive(root, current_sum, sums)
  return sum(sums)

def find_sum_path_recursive(current_node, current_sum, sums):
  if not current_node:
    return
  
  current_sum[0] = (current_sum[0] * 10) + current_node.val

  if current_node.left is None and current_node.right is None:
    sums.append(current_sum[0])
  else:
    find_sum_path_recursive(current_node.left, current_sum, sums)
    find_sum_path_recursive(current_node.right, current_sum, sums)
  
  current_sum[0] = (current_sum[0] - current_node.val) // 10


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""
def find_sum_of_path_numbers2(root):
    return find_sum_path_recursive2(root, 0)


def find_sum_path_recursive2(current_node, pathSum):
    if current_node is None:
        return 0
    
    pathSum = (pathSum * 10) + current_node.val

    if current_node.left is None and current_node.right is None:
        return pathSum
    
    return find_sum_path_recursive2(current_node.left, pathSum) + find_sum_path_recursive2(current_node.right, pathSum)
  




def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers2(root)))


main()

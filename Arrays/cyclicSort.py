"""
Time Complexity =  O(n) + O(n-1) = O(n)
Space Complexity = O(1)
"""


def cyclic_sort(nums):
  # TODO: Write your code here
  i = 0
  while i < len(nums):
    j = nums[i] - 1 # correct location of nums[i] is 'j'
    if i != j:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  return nums



def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()


"""
 Time Complexity - O(N * 2^N)
 Space Complexity - O(N * 2^N)
"""
def find_subsets(nums):
  subsets = []
  subsets.append([])
  nums = sorted(nums)
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0

    if i > 0 and nums[i] == nums[i - 1]:
      startIndex = endIndex
    endIndex = len(subsets)

    for j in range(startIndex, endIndex):
      list_ = list(subsets[j])
      list_.append(nums[i])
      subsets.append(list_)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

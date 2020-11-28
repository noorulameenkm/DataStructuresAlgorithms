"""
Time Complexity - O(N)
Space Complexity - O(1)
"""
def find_missing_number(nums):
  i = 0
  while i < len(nums):
    j = nums[i]
    if nums[i] < len(nums) and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  # find the first number missing from its index, that will be our required number
  i = 0
  while i < len(nums):
    if i != nums[i]:
      break
    
    i += 1

  return i


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))

main()
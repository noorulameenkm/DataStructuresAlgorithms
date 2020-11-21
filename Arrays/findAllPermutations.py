from collections import deque

"""
Time Complexity - O(N * N!)
Space Complexity - O(N * N!)
"""

def find_permutations(nums):
  result = []
  numsLength = len(nums)
  permutations = deque()
  permutations.append([])
  for num in nums:
    for _ in range(len(permutations)):
      currentPermutation = permutations.popleft()
      for j in range(len(currentPermutation) + 1):
        newPermutations = list(currentPermutation)
        newPermutations.insert(j, num)

        if len(newPermutations) == numsLength:
          result.append(newPermutations)
        else:
          permutations.append(newPermutations)

  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

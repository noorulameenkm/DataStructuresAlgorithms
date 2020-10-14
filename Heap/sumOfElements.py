from heapq import *

"""
Time complexity - O(N∗logK2)
Space Complexity - O(k2)
"""

def find_sum_of_elements(nums, k1, k2):
  if k2 > len(nums) or k1 > len(nums):
    return 0
  
  minheap = []

  for i in range(k2):
    heappush(minheap, -nums[i])
  
  for i in range(k2, len(nums)):
    if -nums[i] > minheap[0]:
      heappop(minheap)
      heappush(minheap, -nums[i])
  
  heappop(minheap)

  sum_ = 0

  for i in range(k2-k1-1):
    sum_ += -heappop(minheap)

  return sum_

def find_sum_of_elements2(nums, k1, k2):
  minHeap = []
  # insert all numbers to the min heap
  for num in nums:
    heappush(minHeap, num)

  # remove k1 small numbers from the min heap
  for _ in range(k1):
    heappop(minHeap)

  elementSum = 0
  # sum next k2-k1-1 numbers
  for _ in range(k2 - k1 - 1):
    elementSum += heappop(minHeap)

  return elementSum


def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements2([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements2([3, 5, 8, 7], 1, 4)))


main()

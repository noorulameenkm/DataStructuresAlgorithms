from heapq import *

"""
Time Complexity - O(N∗logN+KlogN)
Improved - We can optimize the above algorithm and only push ‘K’ elements in the heap, as in the worst 
case we will be extracting ‘K’ elements from the heap. This optimization will reduce the overall time 
complexity to O(N*logK + KlogK).
Space Complexity - O(N)
"""

def find_maximum_distinct_elements(nums, k):
  distinct = 0
  # if k greater than length of nums
  if len(nums) <= k:
      return distinct

  frequency = {}
  # find the frequency of each number
  for num in nums:
      frequency[num] = frequency.get(num, 0) + 1

  minHeap = []
  # insert all numbers with frequency greater than '1' into the min-heap
  for num, frequency in frequency.items():
      if frequency == 1:
            distinct += 1
      else:
            heappush(minHeap, (frequency, num))

  while k > 0 and minHeap:
      frequency, num = heappop(minHeap)
      
      # we have to remove all the duplicates by leaving the original
      k -= (frequency - 1)

      if k >= 0:
            distinct += 1

  # if k > 0, this means we have to remove some distinct numbers
  if k > 0:
      distinct -= k

  return distinct


def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()


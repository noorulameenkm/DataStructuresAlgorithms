from heapq import *
import math


"""
Time complexity - O(N * logM) N is the total number of elements in all arrays and M is the number of lists
Space Complexity - O(M)
"""

def find_smallest_range(lists):
  minheap = []
  rangeStart, rangeEnd = 0, math.inf
  currentmax = -math.inf

  for list_ in lists:
    heappush(minheap, (list_[0], 0, list_))
    currentmax = max(currentmax, list_[0])

  # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
  # if the array of the top element has more elements, insert the next element in the heap
  """
  We can finish searching the minimum range as soon as an array is completed or, 
  in other terms, the heap has less than ‘M’ elements.
  """
  while len(minheap) == len(lists):
    number, index, list_ = heappop(minheap)
    if rangeEnd - rangeStart > currentmax - number:
      rangeStart = number
      rangeEnd = currentmax
    
    if index + 1 < len(list_):
      heappush(minheap, (list_[index + 1], index + 1, list_))
      currentmax = max(currentmax, list_[index + 1])
    

  return [rangeStart, rangeEnd]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()


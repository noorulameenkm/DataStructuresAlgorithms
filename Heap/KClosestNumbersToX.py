from heapq import *
from collections import deque

"""
Time complexity = O(logN + k * logK)
Space Complexity = O(K)
"""

def find_closest_elements(arr, K, X):
  result = []
  index = binary_search(arr, X)
  minHeap = []
  low, high = index - K, index + K
  # 'low' should not be less than zero
  # 'high' should not be greater the size of the array
  low, high = max(low, 0), min(high, len(arr) - 1)
  # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
  for i in range(low, high + 1):
        heappush(minHeap, (abs(arr[i] - X), arr[i]))

  # we need the top 'K' elements having smallest difference from 'X'
  result = []
  for _ in range(K):
        result.append(heappop(minHeap)[1])

  result.sort()

  return result

"""
Time Complexity = O(logN+K).
Space Complexity = If we ignoring the space required for the output list, the algorithm runs in constant space O(1)O(1).
"""

def find_closest_elements2(arr, K, X):
    result = []
    index = binary_search(arr, X)
    queue = deque()

    low, high = index, index + 1
    i = 0
    for _ in range(K):
        if low >= 0 and high <= len(arr) - 1:
            lowDiff = abs(arr[low] - X)
            highDiff = abs(arr[high] - X)

            if lowDiff < highDiff:
                queue.appendleft(arr[low])
                low -= 1
            else:
                queue.append(arr[high])
                high += 1

        elif low >= 0:
            queue.appendleft(arr[low])
            low -= 1
        elif high <= len(arr) - 1:
            queue.append(arr[high])
            high += 1

    result = list(queue)

    return result
        

def binary_search(arr, target):
      low, high = 0, len(arr) - 1
      while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                  return mid
            elif target > arr[mid]:
                  low = mid + 1
            else:
                  high = mid - 1

      if low > 0:
            return low - 1
      return low


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))
  print('-------------------------------------------------------')
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements2([5, 6, 7, 8, 9], 3, 7))) 
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements2([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements2([2, 4, 5, 6, 9], 3, 10)))

main()

import math

"""
Time Complexity - O(logN)
Space Complexity - O(1)
"""

def search_min_diff_element(arr, key):
  start, end = 0, len(arr) - 1
  if key < arr[start]:
    return arr[start]
  
  if key > arr[end]:
    return arr[end]

  while start <= end:
    mid = start + (end - start) // 2

    if arr[mid] == key:
      return arr[mid]
    elif key > arr[mid]:
      start = mid + 1
    else:
      end = mid - 1

  # at the end of the while loop, 'start == end+1'
  # we are not able to find the element in the given array
  # return the element which is closest to the 'key'
  if (arr[start] - key) < (key - arr[end]):
    return arr[start]
  
  return arr[end]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()

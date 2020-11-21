"""
Space Complexity - O(1)
Time Compexity - O(logN)
"""
def search_bitonic_array(arr, key):
  start, end = 0, len(arr) - 1
  maxIndex = find_max(arr)
  index = binary_search(arr, 0, maxIndex, key)
  if index == -1:
    index = binary_search(arr, maxIndex + 1, len(arr) - 1, key)
  
  return index
  
"""
Space Complexity - O(1)
Time Compexity - O(logN)
"""
def find_max(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2

    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  # at the end of the while loop, 'start == end'
  return start

"""
Space Complexity - O(1)
Time Compexity - O(logN)
"""
def binary_search(arr, start, end, key):
  while start <= end:
    mid = start + (end - start) // 2

    if arr[mid] == key:
      return mid
    elif arr[start] < arr[end]: # Ascending order
      if key > arr[mid]:
        start = mid + 1
      else:
        end = mid - 1
    else: # descending order
      if key > arr[mid]:
        end = mid - 1
      else:
        start = mid + 1

  return -1

def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()

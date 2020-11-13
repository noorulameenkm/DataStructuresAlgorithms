"""
Time complexity - O(log N)
Space complexity - O(1)
"""

def find_range(arr, key):
  result = [- 1, -1]
  result[0] = binarySearch(arr, key, False)
  if result[0] != -1:
    result[1] = binarySearch(arr, key, True)

  return result

def binarySearch(arr, key, findMax):
  keyIndex = -1
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2

    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:
      keyIndex = mid
      if findMax:
        start = mid + 1
      else:
        end = mid - 1

  return keyIndex



def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()

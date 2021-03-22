"""
  Time Complexity - O(logN)
  Space Complexity - O(1)
"""
def first_not_smaller(arr, target):
  n = len(arr)
  start, end = 0, n - 1
  index = -1
  while start <= end:
    mid = start + ((end - start) // 2)
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      index = mid
      end = mid - 1
    else:
      start = mid + 1

  return index


if __name__ == '__main__':
    print(first_not_smaller([1, 3, 3, 5, 8, 8, 10],2))
    print(first_not_smaller([0],0))
    print(first_not_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],10))
    print(first_not_smaller([1, 1, 1, 1, 4, 5],3))
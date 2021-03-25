def find_min_rotated(arr):
  start, end = 0, len(arr) - 1
  index = -1
  while start <= end:
    mid = start + ((end - start) // 2)
    if arr[mid] > arr[-1]:
      start = mid + 1
    else:
      index = mid
      end = mid - 1

  return index



if __name__ == '__main__':
    print("Find minimum rotated :", find_min_rotated([30, 40, 50, 10, 20]))
    print("Find minimum rotated :", find_min_rotated([0, 1, 2, 3, 4, 5]))
    print("Find minimum rotated :", find_min_rotated([0]))
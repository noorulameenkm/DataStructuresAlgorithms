def find_first_occurrence(arr, target):
  n = len(arr)
  start, end = 0, n - 1
  index = -1
  while start <= end:
    mid = start + ((end - start) // 2)
    if arr[mid] == target:
      index = mid
      end = mid - 1
    elif target > arr[mid]:
      start = mid + 1
    else:
      end = mid - 1

  return index



if __name__ == '__main__':
    print("First occurance :",find_first_occurrence(str([1, 3, 3, 3, 3, 6, 10, 10, 10, 100]),str(3)))
    print("First occurance :",find_first_occurrence(str([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),str(1)))
    print("First occurance :",find_first_occurrence(str([1, 22, 22, 33, 50, 100, 20000]),str(33)))
    print("First occurance :",find_first_occurrence(str([4, 6, 7, 7, 7, 20]),str(8)))
    print("First occurance :",find_first_occurrence(str([6, 7, 9, 10, 10, 10, 90]),str(10)))
    print("First occurance :",find_first_occurrence(str([4]),str(4)))
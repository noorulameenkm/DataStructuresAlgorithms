def peak_of_mountain_array(arr):
  if len(arr) < 3:
    return -1

  start, end = 0, len(arr) - 1
  index = -1
  while start <= end:
    mid = start + ((end - start) // 2)

    if mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]:
      index = mid
      end = mid - 1
    else:
      start = mid + 1
  
  return index



if __name__ == '__main__':
    print("Find Peak of mountain :", peak_of_mountain_array([0, 1, 2, 3, 2, 1, 0]))
    print("Find Peak of mountain :", peak_of_mountain_array([0, 10, 3, 2, 1, 2]))
    print("Find Peak of mountain :", peak_of_mountain_array([0, 10, 0]))
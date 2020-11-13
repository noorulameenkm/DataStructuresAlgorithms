def search_ceiling_of_a_number(arr, key):
  start, end = 0, len(arr) - 1

  if key < arr[start]:
    return - 1

  while start <= end:
    mid = start + (end - start) // 2

    if arr[mid] == key:
      return mid
    elif key > arr[mid]:
      start = mid + 1
    else:
      end = mid - 1

  return end


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()

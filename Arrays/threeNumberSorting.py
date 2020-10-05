def dutch_flag_sort(arr):
  start, end, i = 0, len(arr) - 1, 0
  while i <= end:
    if arr[i] == 0:
      arr[i], arr[start] = arr[start], arr[i]
      i += 1
      start += 1
    elif arr[i] == 1:
      i += 1
    else:
      arr[i], arr[end] = arr[end], arr[i]
      end -= 1
      # i += 1

  return 


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()

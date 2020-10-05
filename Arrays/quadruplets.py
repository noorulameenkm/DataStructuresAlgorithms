def search_quadruplets(arr, target):
  quadruplets = []
  arr.sort()
  for i in range(len(arr) - 3):
    # skip same element to avoid duplicate quadruplets
    if i > 0 and arr[i] == arr[i - 1]:
      continue
    for j in range(i + 1, len(arr) - 2):
      # skip same element to avoid duplicate quadruplets
      if j > i + 1 and arr[j] == arr[j - 1]:
        continue
      search_pairs(arr, i, j, target, quadruplets)
  return quadruplets


def search_pairs(arr, first, second, target, quadruplets):
  start, end = second + 1, len(arr) - 1

  while start < end:
    current = arr[first] + arr[second] + arr[start] + arr[end]

    if current > target:
      end -= 1
    elif current < target:
      start += 1
    else:
      quadruplets.append([arr[first], arr[second], arr[start], arr[end]])
      start += 1
      end -= 1
      while start < end and arr[start] == arr[start - 1]:
        start += 1
      while end > start and arr[end] == arr[end + 1]:
        end -= 1



def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
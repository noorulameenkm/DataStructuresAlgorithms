def triplet_with_smaller_sum(arr, target):
  arr.sort()
  triplets = []
  for i in range(len(arr) - 2):
    findAllTriplets(arr, i + 1, target - arr[i], triplets)

  return triplets

def findAllTriplets(arr, left, target, triplets):
  right = len(arr) - 1
  first = left - 1

  while left < right:
    current = arr[left] + arr[right]

    if current < target:# found the triplet
      # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
      # left and right to get a sum less than the target sum
      for i in range(right, left, -1):
          triplets.append([arr[first], arr[left], arr[i]])
      left += 1
    else:
      right -= 1


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
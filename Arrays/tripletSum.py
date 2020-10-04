def search_triplets(arr):
  triplets = []
  arr.sort()
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i - 1]:
      continue
    
    two_pair(arr, -arr[i], i + 1, triplets)

  return triplets


def two_pair(arr, target_sum, start, triplets):
  end = len(arr) - 1
  
  while start < end:
    if arr[start] + arr[end] < target_sum:
      start += 1
    elif arr[start] + arr[end] > target_sum:
      end -= 1
    else:
      triplets.append([-target_sum, arr[start], arr[end]])
      start += 1
      end -= 1
      while start < end and arr[start] == arr[start - 1]:
        start += 1
      while start < end and arr[end] == arr[end + 1]:
        end -= 1


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))

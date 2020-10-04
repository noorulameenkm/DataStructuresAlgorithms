from collections import deque

def find_subarrays(arr, target):
  result = []
  start = 0
  product = 1
  for end in range(len(arr)):
    product *= arr[end]

    while product >= target and start < end:
        product = product // arr[start]
        start += 1

    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from left to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(end, start - 1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
    
  return result




def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()
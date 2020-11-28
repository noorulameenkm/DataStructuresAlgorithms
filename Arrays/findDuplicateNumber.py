"""
Time Complexity - O(N)
Space Complexity - O(1)
"""
def find_duplicate(nums):
  i = 0
  n = len(nums)
  while i < n:
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        return nums[i]
    else:
      i += 1
  
  return -1


"""
Time Complexity - O(N)
Space Complexity - O(1)
"""
def find_duplicate2(arr):
    slow, fast = arr[0], arr[arr[0]]

    if slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    # find cycle length
    current = arr[arr[slow]]
    cyclelength = 1
    while current != arr[slow]:
        current = arr[current]
        cyclelength += 1
    
    return find_start(arr, cyclelength)

def find_start(arr, length):
    pointer1, pointer2 = arr[0], arr[0]
    # move pointer2 ahead 'cycleLength' steps
    while length > 0:
        pointer2 = arr[pointer2]
        length -= 1

    while pointer1 != pointer2:
        pointer1 = arr[pointer1]
        pointer2 = arr[pointer2]

    return pointer1


def main():
  # Method1
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))

  # Method2
  print(find_duplicate2([1, 4, 4, 3, 2]))
  print(find_duplicate2([2, 1, 3, 3, 5, 4]))
  print(find_duplicate2([2, 4, 1, 4, 4]))

main()
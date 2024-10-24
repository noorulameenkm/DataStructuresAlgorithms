# Pattern:- Sliding Window
def length_of_longest_substring(arr, k):
  maxLength, start, ones = 0, 0, 0
  for end in range(len(arr)):
    num = arr[end]
    if num == 1:
      ones += 1
    
    currentLength = end - start + 1
    if (currentLength - ones) > k:
      rem_num = arr[start]
      if rem_num == 1:
        ones -= 1

      start += 1

    maxLength = max(maxLength, end - start + 1)
  return maxLength




def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
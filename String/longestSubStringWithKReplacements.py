def length_of_longest_substring(str1, k):
  # TODO: Write your code here
  start, maxLength, maxRepeating = 0, 0, 0
  frequency = {}
  for end in range(len(str1)):
    char = str1[end]

    if char not in frequency:
      frequency[char] = 0
    frequency[char] += 1

    maxRepeating = max(maxRepeating, frequency[char])

    currLength = end - start + 1
    if (currLength - maxRepeating) > k:
      rem_char = str1[start]
      frequency[rem_char] -= 1
      start += 1

    maxLength = max(maxLength, end - start + 1)
  return maxLength



def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()
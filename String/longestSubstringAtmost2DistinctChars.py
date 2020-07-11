def longest_substring_with_k_distinct(str1):
  start, maxLength = 0, 0
  frequency = {}
  length = 0
  for end in range(len(str1)):
    character = str1[end]

    if character not in frequency:
      frequency[character] = 0
    frequency[character] += 1

    length += 1

    while len(frequency) > 2:
      rem_char = str1[start]
      start += 1
      frequency[rem_char] -= 1
      length -= 1
      if frequency[rem_char] == 0:
        del frequency[rem_char]
      
      
    maxLength = max(maxLength, length)


  return maxLength


print(f"Length of the longest substr1ing: {longest_substring_with_k_distinct('araaci')}")
print(f"Length of the longest substr1ing: {longest_substring_with_k_distinct('araaci')}")
print(f"Length of the longest substr1ing: {longest_substring_with_k_distinct('cbbebi')}")

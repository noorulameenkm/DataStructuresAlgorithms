def find_string_anagrams(str1, pattern):
  result_indexes = []
  start, matched, frequency = 0, 0, {}
  
  for pat in pattern:
    if pat not in frequency:
      frequency[pat] = 0
    frequency[pat] += 1


  for end in range(len(str1)):

    char = str1[end]

    if char in frequency:
      frequency[char] -= 1
      if frequency[char] == 0:
        matched += 1

    if matched == len(frequency):
      result_indexes.append(start)

    if end >= len(pattern) - 1:
      rem_char = str1[start]
      start += 1
      
      if rem_char in frequency:
        if frequency[rem_char] == 0:
          matched -= 1
        frequency[rem_char] += 1

  return result_indexes


def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()


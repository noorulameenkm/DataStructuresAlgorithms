def find_word_concatenation(str1, words):
  result_indices = []
  if len(words) == 0 or len(words[0]) == 0:
    return []

  words_length = len(words)
  word_length = len(words[0])
  word_frequency = {}
  for word in words:
    if word not in word_frequency:
      word_frequency[word] = 0
    word_frequency[word] += 1
  
  word_seen = {}

  for i in range((len(str1) - words_length * word_length) + 1):
    word_seen = {}
    for j in range(words_length):
      start_index = i + j * word_length
      word = str1[start_index: start_index + word_length]

      if word not in word_frequency:
        break
      
      if word not in word_seen:
        word_seen[word] = 0
      word_seen[word] += 1

      if word_seen[word] > word_frequency.get(word, 0):
        break

      if j + 1 == words_length:
        result_indices.append(i)

  return result_indices



def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()



# Time Complexity O(N * M * Len) -> N: number of chars in str1, M: #words, Len: length of the word
# Space Complexity O(M + N) -> 2 hashMaps and the result array
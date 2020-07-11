def non_repeat_substring(str1):
  # TODO: Write your code here
  start, maxLength = 0, 0
  index_map = {}
  for end in range(len(str1)):
    character = str1[end]

    if character in index_map:
        # start from max of either start or next char of the repeating char's first occurence
        # 1. check whether the first occurences of repeating char part of the current substring
        # 2. if it is part of the substring then start from the next char of first occurence of the repeating char
        # 3. else use the start as the existing start
        start = max(start, index_map[character] + 1) 
    index_map[character] = end
    maxLength = max(maxLength, end - start + 1)
  return maxLength




def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbcadeyu")))



main()

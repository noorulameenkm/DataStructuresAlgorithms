import math 
def find_substring(str1, pattern):
  # TODO: Write your code here
  start, matched, minLength, minLengthString, frequency = 0, 0, math.inf, "", {}

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
    
    while matched == len(pattern):
      # minLength = min(minLength, end - start + 1)
      currentLength = end - start + 1
      if currentLength < minLength:
        minLength = currentLength
        minLengthString = str1[start: end + 1]

      rem_char = str1[start]
      start += 1

      if rem_char in frequency:
        if frequency[rem_char] == 0:
          matched -= 1
        frequency[rem_char] += 1

  return minLengthString



def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("abdabca", "abc"))
  print(find_substring("adcad", "abc"))

main()

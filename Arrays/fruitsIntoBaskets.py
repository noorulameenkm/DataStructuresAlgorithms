def fruits_into_baskets(fruits):
  # TODO: Write your code here
  maxLength, length = 0, 0
  start = 0
  frequency = {}
  for end in range(len(fruits)):
    length += 1

    if fruits[end] not in frequency:
      frequency[fruits[end]] = 0
    frequency[fruits[end]] += 1

    while len(frequency) > 2:
      rem_char = fruits[start]
      start += 1
      frequency[rem_char] -= 1
      if frequency[rem_char] == 0:
        del frequency[rem_char]
      
      length -= 1

    maxLength = max(length, maxLength)

  return maxLength


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
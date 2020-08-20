from collections import deque
class Abbreviation:
  def __init__(self, string, start, count):
    self.string = string
    self.start = start
    self.count = count

def generate_generalized_abbreviation(word):
  result = []
  # TODO: Write your code here
  queue = deque()
  queue.append(Abbreviation(list(), 0, 0))

  while queue:
    current = queue.popleft()
    if current.start == len(word):
      if current.count != 0:
        current.string.append(str(current.count))
      result.append(''.join(current.string))
    else:
      queue.append(Abbreviation(list(current.string), current.start + 1, current.count + 1))


      if current.count != 0:
        current.string.append(str(current.count))

      newWord = list(current.string)
      newWord.append(word[current.start])
      queue.append(Abbreviation(newWord, current.start + 1, 0))

  return result


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()


"""
    Time complexity:- O(N * 2^N)
    Space complexity:- O(N * 2^N)
"""



def generate_generalized_abbreviation2(word):
  result = []
  generate_abbreviation_recursive(word, list(), 0, 0, result)
  return result


def generate_abbreviation_recursive(word, abWord, start, count, result):

  if start == len(word):
    if count != 0:
      abWord.append(str(count))
    result.append(''.join(abWord))
  else:
    # continue abbreviating by incrementing the current abbreviation count
    generate_abbreviation_recursive(
      word, list(abWord), start + 1, count + 1, result)

    # restart abbreviating, append the count and the current character to the string
    if count != 0:
      abWord.append(str(count))
    newWord = list(abWord)
    newWord.append(word[start])
    generate_abbreviation_recursive(word, newWord, start + 1, 0, result)


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation2("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation2("code")))


main()


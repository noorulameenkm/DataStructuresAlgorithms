from collections import deque
class Abbreviation:
  def __init__(self, string, start, count):
    self.string = string
    self.start = start
    self.count = count


"""
    Time complexity:- O(N * 2^N)
    Space complexity:- O(N * 2^N)
"""
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



"""
This problem follows the Subsets pattern and can be mapped to Balanced Parentheses. We can follow a similar BFS approach.

Let’s take Example-1 mentioned above to generate all unique generalized abbreviations. Following a BFS approach, we will abbreviate one character at a time. At each step we have two options:

 - Abbreviate the current character, or
 - Add the current character to the output and skip abbreviation.

Following these two rules, let’s abbreviate BAT:
 1. Start with an empty word: “”
 2. At every step, we will take all the combinations from the previous step and apply the two abbreviation rules to the next character.
 3. Take the empty word from the previous step and add the first character to it. We can either abbreviate the character or add it (by skipping abbreviation). This gives us two new words: _, B.
 4. In the next iteration, let’s add the second character. Applying the two rules on _ will give us _ _ and 1A. Applying the above rules to the other combination B gives us B_ and BA.
 5. The next iteration will give us: _ _ _, 2T, 1A_, 1AT, B _ _, B1T, BA_, BAT
 6. The final iteration will give us:3, 2T, 1A1, 1AT, B2, B1T, BA1, BAT
"""



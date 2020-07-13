from collections import deque

class Paranthesis:
  def __init__(self, string, openCount, closeCount):
    self.string = string
    self.openCount = openCount
    self.closeCount = closeCount
  

def generate_valid_parentheses(num):
  result = []
  queue = deque()
  queue.append(Paranthesis("", 0, 0))

  while queue:
    paranthesis = queue.popleft()

    if paranthesis.openCount == num and paranthesis.closeCount == num:
      result.append(paranthesis.string)
    else:
      if paranthesis.openCount < num:
        queue.append(Paranthesis(paranthesis.string + '(', paranthesis.openCount + 1, paranthesis.closeCount))
      if paranthesis.openCount > paranthesis.closeCount:
        queue.append(Paranthesis(paranthesis.string + ')', paranthesis.openCount, paranthesis.closeCount + 1))

  return result


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))

main()




def generate_valid_parentheses(num):
  result = []
  parenthesesString = [0 for x in range(2*num)]
  generate_valid_parentheses_rec(num, 0, 0, parenthesesString, 0, result)
  return result


def generate_valid_parentheses_rec(num, openCount, closeCount, parenthesesString, index, result):

  # if we've reached the maximum number of open and close parentheses, add to the result
  if openCount == num and closeCount == num:
    result.append(''.join(parenthesesString))
  else:
    if openCount < num:  # if we can add an open parentheses, add it
      parenthesesString[index] = '('
      generate_valid_parentheses_rec(
        num, openCount + 1, closeCount, parenthesesString, index + 1, result)

    if openCount > closeCount:  # if we can add a close parentheses, add it
      parenthesesString[index] = ')'
      generate_valid_parentheses_rec(
        num, openCount, closeCount + 1, parenthesesString, index + 1, result)


def main2():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))
main2()


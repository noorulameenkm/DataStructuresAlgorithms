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

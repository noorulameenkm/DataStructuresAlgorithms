from collections import deque

class Paranthesis:
  def __init__(self, string, openCount, closeCount):
    self.string = string
    self.openCount = openCount
    self.closeCount = closeCount
  

"""
Time Complexity - O(N * 2 ^ N)
Space Complexity - O(N * 2 ^ N)
"""

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



"""
This problem follows the Subsets pattern and can be mapped to Permutations. We can follow a similar BFS approach.

Let’s take Example-2 mentioned above to generate all the combinations of balanced parentheses. Following a BFS approach, we will keep adding open parentheses ( or close parentheses ). 
At each step we need to keep two things in mind:

1. We can’t add more than ‘N’ open parenthesis.
2. To keep the parentheses balanced, we can add a close parenthesis ) only when we have already 
added enough open parenthesis (. For this, we can keep a count of open and close parenthesis with 
every combination.


steps: 
1. Start with an empty combination: “”
2. At every step, let’s take all combinations of the previous step and 
add ( or ) keeping the above-mentioned two rules in mind.
3. For the empty combination, we can add ( since the count of open parenthesis will be 
less than ‘N’. We can’t add ) as we don’t have an equivalent open parenthesis, so our list of 
combinations will now be: “(”
4. For the next iteration, let’s take all combinations of the previous set. For “(” we can add another 
( to it since the count of open parenthesis will be less than ‘N’. We can also add ) 
as we do have an equivalent open parenthesis, so our list of combinations will be: “((”, “()”
5. In the next iteration, for the first combination “((”, we can add another ( to it as the count of 
open parenthesis will be less than ‘N’, we can also add ) as we do have an equivalent open parenthesis.
 This gives us two new combinations: “(((” and “(()”. For the second combination “()”, we can add another 
 ( to it since the count of open parenthesis will be less than ‘N’. We can’t add ) as we don’t have an equivalent 
 open parenthesis, so our list of combinations will be: “(((”, “(()”, ()("
6. Following the same approach, next we will get the following list of combinations: “((()”, “(()(”, “(())”, “()((”, “()()”
7. Next we will get: “((())”, “(()()”, “(())(”, “()(()”, “()()(”
8. Finally, we will have the following combinations of balanced parentheses: “((()))”, “(()())”, “(())()”, “()(())”, “()()()”
9. We can’t add more parentheses to any of the combinations, so we stop here.

"""

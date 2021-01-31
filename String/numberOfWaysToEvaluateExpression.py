"""
Time Complexity - O(N * 2^N)
Space Complexity - O(2^N)
"""
def diff_ways_to_evaluate_expression(input):
  result = []
  if '+' not in input and '-' not in input and '*' not in input:
    result.append(int(input))
  else:
    for i in range(len(input)):
      char = input[i]
      if not char.isdigit():
        left_result = diff_ways_to_evaluate_expression(input[0:i])
        right_result = diff_ways_to_evaluate_expression(input[i+1:])
        for left in left_result:
          for right in right_result:
            if char == '+':
              result.append(left + right)
            elif char == '-':
              result.append(left - right)
            elif char == '*':
              result.append(left * right)


  return result


def diff_ways_to_evaluate_expression_memoization(input):
    return diff_ways_to_evaluate_expression_memoization_recursive(input, {})


def diff_ways_to_evaluate_expression_memoization_recursive(input, map):
    if input in map:
        return map[input]
    
    result = []
    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            char = input[i]
            if not char.isdigit():
                left_result = diff_ways_to_evaluate_expression_memoization_recursive(input[0:i], map)
                right_result = diff_ways_to_evaluate_expression_memoization_recursive(input[i+1:], map)
                for left in left_result:
                    for right in right_result:
                        if char == '+':
                            result.append(left + right)
                        elif char == '-':
                            result.append(left - right)
                        elif char == '*':
                            result.append(left * right)

    map[input] = result

    return result



def main():
    print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))

    print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression_memoization("1+2*3")))

    print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression_memoization("2*3-4-5")))


main()



"""
Approach

This problem follows the Subsets pattern and can be mapped to Balanced Parentheses. We can follow a similar BFS approach.
Let’s take Example-1 mentioned above to generate different ways to evaluate the expression.
1. We can iterate through the expression character-by-character.
2. we can break the expression into two halves whenever we get an operator (+, -, *).
3. The two parts can be calculated by recursively calling the function.
4. Once we have the evaluation results from the left and right halves, we can combine them to produce all results.
"""

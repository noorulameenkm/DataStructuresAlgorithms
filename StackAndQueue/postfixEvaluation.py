from Stack import Stack


"""
Time Complexity - O(N)
Space Complexity - O(N)
"""

def evaluate_post_fix(exp):
    # Write your code here
    stack = Stack()
    operations = {'+': add, '-':sub, '*': multiply, '/': divide }
    for e in exp:
        if e in operations:
            op_2 = stack.pop()
            op_1 = stack.pop()
            res = operations[e](op_1, op_2)
            stack.push(res)
        else:
            stack.push(float(e))
            
    return stack.pop()


def evaluate_post_fix_2(exp):
    stack = Stack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
            else:
                # use top two numbers and evaluate
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        # final answer should be a number
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid Sequence"



def add(num_1, num_2):
    return num_1 + num_2

def sub(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2



def main():
    # first approach
    print(evaluate_post_fix("921*-8-4+"))
    print(evaluate_post_fix("642/+"))
    # second Approach
    print(str(evaluate_post_fix_2("921*-8-4+")))
    print(str(evaluate_post_fix_2("921*-8--4+")))

main()

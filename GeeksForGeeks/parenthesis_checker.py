class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(len(self.stack) - 1)
        else:
            return -1

    def popAll(self):
        while len(self.stack) != 0:
            print(self.stack.pop(len(self.stack) - 1), end = ' ')


def checkParenthesis(exp):
    stack = Stack()
    for parenthesis in exp:
        if parenthesis == '[' or parenthesis == '{' or parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ']':
            pop_val = stack.pop()
            if pop_val == -1 or pop_val != '[':
                return 'not balanced'

        elif parenthesis == ')':
            pop_val = stack.pop()
            if pop_val == -1 or pop_val != '(':
                return 'not balanced'

        elif parenthesis == '}':
            pop_val = stack.pop()
            if pop_val == -1 or pop_val != '{':
                return 'not balanced'

    if stack.pop() == -1:
        return 'balanced'
    else:
        return 'not balanced'

    
def Main():
    test_cases = int(input())
    for t_case in range(test_cases):
        exp = input()
        print(checkParenthesis(exp))


if __name__ == '__main__':
    Main()
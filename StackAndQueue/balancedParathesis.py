from Stack import Stack


"""
Time Complexity - O(n)
Space Complexity - O(n)
"""

def is_balanced(exp):
    # Write your code here
    stack = Stack()
    for char in exp:
        if char == '(' or char == '[' or char == '{':
            stack.push(char)
        elif stack.is_empty():
            return False
        else:
            poped = stack.pop()
            if char == ')' and poped != '(':
                return False
            if char == ']' and poped !=  '[':
                return False
            if char == '}' and poped != '{':
                return False

    if not stack.is_empty():
        return False
    
    return True





def main():
    print(is_balanced("{[()]}"))
    print(is_balanced("{[([({))]}}"))
    print(is_balanced(""))


main()
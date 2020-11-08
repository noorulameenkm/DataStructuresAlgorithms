from Stack import Stack


"""
Time Complexity - O(n)
Space Complexity - O(n)
"""

def next_greater_element(lst):
    # Write your code here
    stack = Stack()
    res = [-1 for i in range(len(lst))]
    for i in range(len(lst) - 1, -1, -1):
        if not stack.is_empty():
            while not stack.is_empty() and stack.top() <= lst[i]:
                stack.pop()

        if not stack.is_empty():
            res[i] = stack.top()

        stack.push(lst[i])

    return res



def main():
    print(next_greater_element([4, 6, 3, 2, 8, 1]))
    print(next_greater_element([4, 8, 14, 2, 16, 18, 9, 5]))
    print(next_greater_element([13, 3, 12, 16, 15, 11, 1, 2]))



main()

from Stack import Stack

def sort_stack(stack):
    # Write your code here
    n = stack.size()
    for i in range(n - 1):
        for j in range(i + 1, n):
            if stack.stack[j] > stack.stack[i]:
                stack.stack[i], stack.stack[j] = stack.stack[j], stack.stack[i]

    return stack



def sort_stack2(stack):

    temp_stack = Stack()

    while stack.is_empty() is False:

        value = stack.pop()

        if temp_stack.top() is not None and value >= int(temp_stack.top()):
            # if value is not none and larger, push it at the top of temp_stack
            temp_stack.push(value)
        else:
            while temp_stack.is_empty() is False:
                stack.push(temp_stack.pop())
            # place value as the smallest element in temp_stack
            temp_stack.push(value)

    # Transfer from temp_stack => stack
    while temp_stack.is_empty() is False:
        stack.push(temp_stack.pop())

    return stack


def sort_stack3(stack):

    if (not stack.is_empty()):
    
        # Pop the top element off the stack
        value = stack.pop()
        
        # Sort the remaining stack recursively
        sort_stack(stack)
        
        # Push the top element back into the sorted stack 
        insert(stack, value)
    
 
def insert(stack, value):
    if (stack.is_empty() or value < stack.top()):
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)




def main():
    stack = Stack()

    stack.push(10)
    stack.push(3)
    stack.push(8)
    stack.push(6)
    stack.push(9)
    stack.push(1)

    print('before sorting')
    stack.print()

    sortedStack = sort_stack(stack)

    print('after sorting')
    sortedStack.print()


    # Second Approach
    stack2 = Stack()

    stack2.push(10)
    stack2.push(3)
    stack2.push(8)
    stack2.push(6)
    stack2.push(9)
    stack2.push(1)

    print('before sorting')
    stack2.print()

    sortedStack2 = sort_stack(stack2)

    print('after sorting')
    sortedStack2.print()


    # Third approach


    stack3 = Stack()

    stack3.push(10)
    stack3.push(3)
    stack3.push(8)
    stack3.push(6)
    stack3.push(9)
    stack3.push(1)

    print('before sorting')
    stack3.print()

    sortedStack3 = sort_stack(stack3)

    print('after sorting')
    sortedStack3.print()

main()
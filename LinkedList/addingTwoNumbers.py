from math import fabs

# Node class
class Node:
    def __init__(self,val, next = None):
        self.val = val
        self.next = next


def printList(lst):
    while lst:
        print(lst.val, end=' ')
        lst = lst.next
    print('\n', end='')

def length(lst):
    length = 0
    while lst:
        length += 1
        lst = lst.next

    return length

def addNumbers(lst1,lst2):

    carry = 0

    if not lst1:
        return (None,carry)
    
    result, carry = addNumbers(lst1.next, lst2.next)

    # adding both digits
    sum_ = lst1.val + lst2.val + carry
    value = sum_ % 10
    carry = int(sum_ / 10)
    result = Node(value, result)

    return (result, carry)

def addRemainingNumbers(lst, result, diff, carry):
    if not lst or not diff:
        return (result, carry)

    diff -= 1
    result, carry = addRemainingNumbers(lst.next, result, diff, carry)

    # adding lst val and carry
    sum_ = lst.val + carry
    value = sum_ % 10
    carry = int(sum_ / 10)
    result = Node(value, result)

    return (result, carry)

def addListNumbers(lst1,lst2):
    l1 = length(lst1)
    l2 = length(lst2)
    current = None
    if l1 < l2:
        current = lst1
        lst1 = lst2
        lst2 = current

    current = lst1
    diff = int(fabs(l1 - l2))
    
    # Traverse the longest list till both the list lengths are equal
    while diff:
        current = current.next
        diff -= 1
    
    result, carry = addNumbers(current, lst2)
    diff = int(fabs(l1 - l2))
    result, carry = addRemainingNumbers(lst1, result, diff, carry)

    if carry:
       result = Node(carry, result)
    
    return result


if __name__ == '__main__':
    lst1 = Node(1)
    lst1.next = Node(9)
    lst1.next.next = Node(9)
    lst1.next.next.next = Node(5)

    lst2 = Node(1)
    lst2.next = Node(9)
    lst2.next.next = Node(9)
    lst2.next.next.next = Node(8)   

    print('List1 is ', end=' ')
    printList(lst1)
    print('List2 is ', end=' ')
    printList(lst2)
    added_list = addListNumbers(lst1,lst2)
    print('Added List is ', end=' ')
    printList(added_list)

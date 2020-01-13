class Node:
    def __init__(self, val):
        self. val = val
        self.next = None

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next

    print('\n', end='')

def getLength(head):
    fast = head
    while fast and fast.next:
        fast = fast.next.next

    if not fast:
        return 0 # Even numbers
    else:
        return 1 # Odd numbers

def findMidPrev(head):
    fast = slow = prev = head
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    return [prev, slow]


def reverseList(head):
    if not head.next:
        return head
    
    secondElement = head.next

    head.next = None
    rev = reverseList(secondElement)
    secondElement.next = head

    return rev


def isPalindrome(head1, head2):
    if not head1 and not head2:
        return True
    if not head1:
        return False
    if not head2:
        return False
    
    if head1.val != head2.val:
        return False
    
    return isPalindrome(head1.next, head2.next)

def checkPalindrome(head):
    length = getLength(head)
    if length == 0:   
        prev, mid = findMidPrev(head)
        head1 = head
        head2 = mid
        prev.next = None
    else:
        prev, mid = findMidPrev(head)
        head1 = head
        head2 = mid.next
        prev.next = None
    
    return isPalindrome(head1, reverseList(head2))

if __name__ == '__main__':
    head = Node('M')
    head.next = Node('A')
    head.next.next = Node('L')
    head.next.next.next = Node('A')
    head.next.next.next.next = Node('Y')
    head.next.next.next.next.next = Node('A')
    head.next.next.next.next.next.next = Node('L')
    head.next.next.next.next.next.next.next = Node('A')
    head.next.next.next.next.next.next.next.next = Node('M')

    # second test case

    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(2)
    head2.next.next.next = Node(1)

    printLinkedList(head2)
    if checkPalindrome(head2):
        print('IT IS PALINDROME')
    else:
        print('IT IS NOT PALINDROME')

    
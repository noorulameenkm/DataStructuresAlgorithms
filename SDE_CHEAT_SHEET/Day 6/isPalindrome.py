class Node:
    def __init__(self, val):
        self. val = val
        self.next = None

def isPalindrome(head):
    if not head:
        return True

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    reversed_ = None
    if fast is None:
        reversed_ = reverseList(slow)
    else:
        reversed_ = reverseList(slow.next)
    
    first, second = head, reversed_
    while second is not None:
        if second.val != first.val:
            return False
        
        first = first.next
        second = second.next
    
    return True



def reverseList(head):
    if not head.next:
        return head
    
    secondElement = head.next

    head.next = None
    rev = reverseList(secondElement)
    secondElement.next = head

    return rev


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)

    print(isPalindrome(head))

main()
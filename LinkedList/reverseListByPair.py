class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end = ' ')
        temp = temp.next
    print('\n', end='')

def reverseByPair(head):
    if not head:
        return None
    if not head.next:
        return head
    
    temp = head.next
    head.next = temp.next
    temp.next = head
    head = temp
    head.next.next = reverseByPair(head.next.next)
    return head 



def reverseByPairIterative(A):
    if A is None:
        return A
    
    if A.next is None:
        return A
    
    current = A
    newHead = None
    prev = None
    while current is not None and current.next is not None:
        head = current.next
        temp = head.next
        current.next = temp
        head.next = current
        
        if prev is not None:
            prev.next = head
        
        prev = current
        
        if newHead is None:
            newHead = head
        
        current = temp
    
    return newHead


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    printLinkedList(head)
    head = reverseByPair(head)
    printLinkedList(head)
    printLinkedList(head)
    head = reverseByPair(head)
    printLinkedList(head)

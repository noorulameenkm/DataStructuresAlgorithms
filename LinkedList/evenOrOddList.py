class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next

    print('\n', end='')

def evenOrOdd(head):
    fptr = head
    while fptr and fptr.next:
        fptr = fptr.next.next

    if not fptr:
        return 'EVEN'
    else:
        return 'ODD'
    
    

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    printLinkedList(head)
    print(evenOrOdd(head))

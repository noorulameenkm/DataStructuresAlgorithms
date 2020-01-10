class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def printListReverse(head):
    if not head:
        return
    printListReverse(head.next)
    print(head.val, end=' ')

    
def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next
    print('\n', end='')
    
    


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    printLinkedList(head)
    printListReverse(head)
    print('\n', end='')
    

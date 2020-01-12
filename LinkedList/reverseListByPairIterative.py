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


def reverseByPair(head):
    current = head
    temp2 = None
    prev = None
    while current and current.next:
        temp = current.next
        current.next = temp.next
        temp.next = current
        if not temp2:
            temp2 = temp
        else:
            prev.next = temp

        prev = current
        current = current.next
    return temp2

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
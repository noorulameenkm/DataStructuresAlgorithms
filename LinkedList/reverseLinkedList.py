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


def reverseLinkedList(head):
    currentp = head
    prevp = None
    nextp = head
    while currentp:
        nextp = currentp.next
        currentp.next = prevp
        prevp = currentp
        currentp = nextp
    
    head = prevp
    return head


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    printLinkedList(head)
    head = reverseLinkedList(head)
    printLinkedList(head)
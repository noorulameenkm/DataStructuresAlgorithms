class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next

    print('\n', end='')
    
def reverseLinkedList(head):
    if not head:
        return None
    if not head.next:
        return head

    secondElement = head.next
    head.next = None
    reverse = reverseLinkedList(secondElement)
    secondElement.next = head
    return reverse


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head = reverseLinkedList(head)
    printLinkedList(head)
    
    

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

def mergeLists(head1, head2):
    newNode = Node(-1)
    newNode.next = None
    temp = newNode
    while head1 and head2:    
        if head1.val <= head2.val:
            temp.next = head1
            temp = temp.next
            head1 = head1.next
        else:
            temp.next = head2
            temp = temp.next
            head2 = head2.next

    if not head1:
        temp.next = head2
    elif not head2:
        temp.next = head1

    return newNode.next
    
    
            

if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(6)
    head1.next.next = Node(10)
    head1.next.next.next = Node(12)
    head1.next.next.next.next = Node(15)
    printLinkedList(head1)
    head2 = Node(2)
    head2.next = Node(5)
    head2.next.next = Node(7)
    head2.next.next.next = Node(8)
    head2.next.next.next.next = Node(13)
    head2.next.next.next.next.next = Node(16)
    head2.next.next.next.next.next.next = Node(17)
    printLinkedList(head2)
    head = mergeLists(head1, head2)
    printLinkedList(head)

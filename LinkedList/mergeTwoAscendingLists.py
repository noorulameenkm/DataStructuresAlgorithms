class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def Merge(head1, head2):
    newNode = Node(-1)
    temp = newNode
    while head1 and head2:
        temp.next = head1
        head1 = head1.next
        temp = temp.next
        temp.next = head2
        head2 = head2.next
        temp = temp.next

    if not head1:
        temp.next = head2
    else:
        temp.next = head1

    return newNode.next

def printLinkedList(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    
    print('\n', end='')

if __name__ == '__main__':
    head = Node('A1')
    head.next = Node('A2')
    head.next.next = Node('A3')
    head.next.next.next = Node('A4')
    head.next.next.next.next = Node('A5')

    head2 = Node('B1')
    head2.next = Node('B2')
    head2.next.next = Node('B3')
    head2.next.next.next = Node('B4')
    head2.next.next.next.next = Node('B5')

    m_head = Merge(head, head2)
    printLinkedList(m_head);
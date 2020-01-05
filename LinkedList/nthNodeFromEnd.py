class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end = ' ')
        temp = temp.next

def nthNodeFromEnd(n, head):
    temp = head
    Ptr1 = temp
    Ptr2 = temp
    i = 0
    while i < n:
        Ptr1 = Ptr1.next
        i = i + 1
    
    while Ptr1:
        Ptr2 = Ptr2.next
        Ptr1 = Ptr1.next

    print(Ptr2.val)
        

if __name__ == '__main__':
    head = Node(5)
    head.next = Node(1)
    head.next.next = Node(17)
    head.next.next.next = Node(4)
    printLinkedList(head)
    print('')
    nthNodeFromEnd(4, head)

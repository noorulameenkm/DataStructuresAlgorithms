class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def findMidLastPointers(head):
    midLastPointers = []
    slowPtr = head
    fastPtr = head
    i = 0
    while fastPtr.next != head:
        if i == 0:
            fastPtr = fastPtr.next
            i = 1
        elif i == 1:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
            i = 0

    midLastPointers.append(slowPtr)
    midLastPointers.append(fastPtr)
    return midLastPointers
    
    


def splitCircularList(head):
    mid, last = findMidLastPointers(head)

    temp = mid.next
    #first List
    mid.next = head

    #second List
    last.next = temp
    head2 = temp

    return [head, head2]
    

def printLinkedList(head):
    temp = head
    while temp.next != head:
        print(temp.val, end=' ')
        temp = temp.next

    print(temp.val)
    return


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head
    head1, head2 = splitCircularList(head)
    printLinkedList(head1)
    printLinkedList(head2)


from heapq import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None


    def __lt__(self, other):
        return self.data < other.data




def flatenList(head):
    minheap = []
    current = head
    newhead = newTail = None
    while current is not None:
        heappush(minheap, current)
        current = current.next
    
    while minheap:
        pop = heappop(minheap)

        node = Node(pop.data)
        if newhead is None:
            newhead = node
            newTail = node
        else:
            newTail.bottom = node
            newTail = newTail.bottom
        
        if pop.bottom is not None:
            heappush(minheap, pop.bottom)
    
    return newhead


def mergeSortedList2(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    temp1, temp2 = head1, head2
    
    if head2.data < head1.data:
        head1, head2 = head2, head1

    res = head1

    while head1 is not None and head2 is not None:
        prev = None

        while head1 is not None and head1.data <= head2.data:
            prev = head1
            head1 = head1.bottom
        
        prev.bottom = head2
        head1, head2 = head2, head1

    temp1.next = temp2.next = None
    return res

def mergeSortedList(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    
    if head2.data < head1.data:
        head1, head2 = head2, head1

    res = head1

    while head1 is not None and head2 is not None:
        prev = None

        while head1 is not None and head1.data <= head2.data:
            prev = head1
            head1 = head1.bottom
        
        prev.bottom = head2
        head1, head2 = head2, head1

    return res

def flatenList2(head):
    if head is None or head.next is None:
        return head
    
    res = head
    head = head.next
    
    while head is not None:
        res = mergeSortedList(res, head)
        head = head.next 

    return res


def flatenList3(head):
    if head is None or head.next is None:
        return head

    head.next = flatenList3(head.next)

    head = mergeSortedList2(head, head.next)

    return head


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.bottom

    print()



def main():
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(19)
    head.next.next.next = Node(28)

    head.bottom = Node(7)
    head.bottom.bottom = Node(8)
    head.bottom.bottom.bottom = Node(30)

    head.next.bottom = Node(20)

    head.next.next.bottom = Node(22)
    head.next.next.bottom.bottom = Node(50)

    head.next.next.next.bottom = Node(35)
    head.next.next.next.bottom.bottom = Node(40)
    head.next.next.next.bottom.bottom.bottom = Node(45)

    # newhead = flatenList(head)
    # newhead = flatenList2(head)
    newhead = flatenList3(head)
    printList(newhead)


main()



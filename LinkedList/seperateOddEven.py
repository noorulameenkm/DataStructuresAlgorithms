class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def seperateOddAndEven(head):
    OddList = EvenList = OddEnd = EvenEnd = None
    iterator = head
    if not head:
        return None
    else:
        while iterator:
            if iterator.val % 2 == 0:
                # Do something for EvenList
                if not EvenList:
                    EvenList = Node(iterator.val)
                    EvenEnd = EvenList
                else:
                    EvenEnd.next = Node(iterator.val)
                    EvenEnd = EvenEnd.next
            else:
                # Do something for Odd List
                if not OddList:
                    OddList = Node(iterator.val)
                    OddEnd = OddList
                else:
                    OddEnd.next = Node(iterator.val)
                    OddEnd = OddEnd.next

            iterator = iterator.next
        
        EvenEnd.next = OddList
        return EvenList

def printList(head):
    while head:
        print(head.val, end=' ')
        head = head.next

    print('\n', end='')


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    printList(head)
    head = seperateOddAndEven(head)
    if not head:
        print('List is empty')
    else:
        printList(head)
    






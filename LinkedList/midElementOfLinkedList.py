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
    
def midElementList(head):
   slowptr = fastptr = temp = head
   i = 0
   while fastptr.next:
        if i == 0:
            fastptr = fastptr.next
            i = 1
        elif i == 1:
            fastptr = fastptr.next
            slowptr = slowptr.next
            i = 0

   return slowptr
            

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    printLinkedList(head)
    mid = midElementList(head)
    if mid:
        print(mid.val)
    else:
        print('Mid Element Not Found')

class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next


def cloneList(head):
    d = {}
    temp = head
    while temp:
        y = Node(temp.val)
        d[temp] = y
        temp = temp.next
    
    temp = head
    while temp:
        try:
            y = d[temp]
            y.next = d[temp.next]
        except:
            y.next = None
        finally:
            temp = temp.next

    return d[head]

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
    printList(head)
    head2 = cloneList(head)
    printList(head2)
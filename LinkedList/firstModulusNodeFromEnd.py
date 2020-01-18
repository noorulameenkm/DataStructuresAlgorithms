class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def findFirstModulusNodeFromEnd(head, k):
    i = 0
    if k <= 0:
        return None

    ptr1 = ptr2 = head
    while ptr1 and i < k:
        ptr1 = ptr1.next
        i += 1

    if not ptr1:
        return None

    while ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr2

def Main(head):
    k = int(input())
    modulusNode = findFirstModulusNodeFromEnd(head,k)
    if modulusNode:
        print(modulusNode.val)
    else:
        print('No Modulus Node')

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next.next.next.next = Node(10)
    head.next.next.next.next.next.next.next.next.next.next = Node(11)
    head.next.next.next.next.next.next.next.next.next.next.next = Node(12)
    head.next.next.next.next.next.next.next.next.next.next.next.next = Node(13)
    head.next.next.next.next.next.next.next.next.next.next.next.next.next = Node(14)
    head.next.next.next.next.next.next.next.next.next.next.next.next.next.next = Node(15)
    head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = Node(16)
    head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = Node(17)
    head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = Node(18)
    head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = Node(19)
    Main(head)
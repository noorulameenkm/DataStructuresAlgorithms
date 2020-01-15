
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def kPlusOnetheNode(head, k):
    i = 0
    if not head:
        return None

    kth = head
    while i < k and kth:
        kth = kth.next
        i += 1

    if i == k and kth:
        return kth
    else:
        head.next

def hasKNodes(head, k):
    i = 0
    while i < k and head:
        head = head.next
        i += 1

    if i == k:
        return True
    
    return False


def Main(head, k):

    if k == 0 or k == 1:
        return head
    
    current = head
    temp = next_ = None

    if(hasKNodes(current,k-1)):
        newHead = kPlusOnetheNode(current, k-1)
    else:
        newHead = head

    m = 0
    while current and hasKNodes(current, k):

        temp = kPlusOnetheNode(current, k)
        lastNode = current

        i = 0
        while i < k:
            next_ = current.next
            current.next = temp
            if i + 1 >= k:
                firstNode = current        
            temp = current
            current = next_
            i += 1
        
        if m > 0:
            prevLastNode.next = firstNode
        
        prevLastNode = lastNode
        m += 1

    return newHead


def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next

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
    printLinkedList(head)
    head = Main(head, 4)
    printLinkedList(head)



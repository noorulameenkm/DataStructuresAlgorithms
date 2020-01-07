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


def insertToList(head, n):
    temp = head
    prev = head
    count = 0

    while temp and temp.val < n:
        prev = temp
        temp = temp.next
        count += 1
    
    if temp:
        newNode = Node(n)
        newNode.next = temp
        if count > 0:
            prev.next = newNode
        if count == 0:
            head = newNode
    else:
        prev.next = Node(n)
    
    return head

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    printLinkedList(head)
    head = insertToList(head, 3)
    printLinkedList(head)
    head = insertToList(head, 6)
    printLinkedList(head)
    head = insertToList(head, 0)
    printLinkedList(head)
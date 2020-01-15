class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def generateList(n):
    head = Node(1)
    temp = head
    i = 2
    while i <= n:
        temp.next = Node(i)
        temp = temp.next
        i += 1

    temp.next = head
    return head
    

def printLinkedList(head):
    temp = head
    while temp.next != head:
        print(temp.val, end=' ')
        temp = temp.next
    
    print(temp.val)

def findWinner(head, m, n):
    for i in range(n - 1):
        for j in range(m - 1):
            head = head.next
        head.next = head.next.next
    return head

def Main():
    n = int(input())
    m = int(input())

    head = generateList(n)
    printLinkedList(head)
    leader = findWinner(head, m, n)
    print(leader.val)

if __name__ == '__main__':
    Main()
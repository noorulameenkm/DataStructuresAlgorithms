class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def findModulusNode(head, k):
    i = 1
    if k <= 0:
        return None
        
    modulus_node = None
    while head:
        if i % k == 0:
            modulus_node = head
        
        head = head.next
        i += 1
    
    return modulus_node

def Main(head):
    k = int(input())
    modulus_node = findModulusNode(head,k)
    if modulus_node:
        print(modulus_node.val)
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
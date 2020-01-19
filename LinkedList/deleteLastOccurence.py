class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    
def deleteLastOccurence(lst, k):
    prev = del_prev = last = None
    curr = lst

    while curr:
        if curr.val == k:
            del_prev = prev
            last = curr
        
        prev = curr
        curr = curr.next
    
    if not last:
        return None
    
    if not del_prev and last:
        return last.next
    
    del_prev.next = last.next
    return lst


def printList(lst):
    while lst:
        print(lst.val, end=' ')
        lst = lst.next
    
    print('\n', end='')

if __name__ == '__main__':
    lst = Node(1)
    lst.next = Node(2)
    lst.next.next = Node(3)
    lst.next.next.next = Node(5)
    lst.next.next.next.next = Node(2)
    lst.next.next.next.next.next = Node(2)
    print('Before Deletion')
    printList(lst)
    head = deleteLastOccurence(lst, 2)
    if head:
        print('After Deletion')
        printList(head)
    else:
        print('Key Not Found');


    
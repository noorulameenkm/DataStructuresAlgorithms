class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def printList(lst):
    while lst:
        print("data = ", lst.val, "random data = ", lst.random.val)
        lst = lst.next
    

def cloneList(lst):

    curr = lst
    while curr:
        temp = Node(curr.val)
        temp.next = curr.next
        curr.next = temp
        curr = curr.next.next
    
    curr = lst
    while curr:
        curr.next.random = curr.random.next
        curr = curr.next.next
    
    curr = lst
    duplicate_lst = lst.next
    while curr.next:
        temp = curr.next
        curr.next = curr.next.next
        curr = temp

    return duplicate_lst

if __name__ == '__main__':
    lst = Node(1)
    lst.next = Node(2)
    lst.next.next = Node(3)
    lst.next.next.next = Node(4)
    lst.next.next.next.next = Node(5)

    lst.random = lst.next.next
    lst.next.random = lst
    lst.next.next.random = lst.next.next.next.next
    lst.next.next.next.random = lst.next.next.next.next
    lst.next.next.next.next.random = lst.next

    printList(lst)
    cloned_list = cloneList(lst)
    print("Duplicated List")
    printList(cloned_list)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def findLoopExistOrNot(head):
    temp = head
    slow_ptr = head
    fast_ptr = head
    loop_found = False
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            loop_found = True
            print('Loop Exist')
            break
    
    if not loop_found:
        print('Loop Doesn\'t Exist')


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = head
    findLoopExistOrNot(head)
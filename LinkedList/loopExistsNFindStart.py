class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def loopExistsThenFindStart(head):
    temp = head
    slow_ptr = head
    fast_ptr = head
    loop_found = False
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            loop_found = True
            break


    if loop_found:
        slow_ptr = head
        while fast_ptr is not slow_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        return slow_ptr
    else:
        return None


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next
    startNode = loopExistsThenFindStart(head)
    if startNode:
        print(startNode.val)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def loopExistsThenFindLength(head):
    temp = head
    slow_ptr = head
    fast_ptr = head
    loop_found = False
    count = 0
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            loop_found = True
            break


    if loop_found:
        fast_ptr = fast_ptr.next
        count += 1
        while fast_ptr is not slow_ptr:
            fast_ptr = fast_ptr.next
            count += 1

        return count
    else:
        return None


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next
    length = loopExistsThenFindLength(head)
    if length:
        print(length)
    else:
        print('Loop Doesn\'t Exists')
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def intersectionOfTwoLists(head1, head2):
    dictionary = {}
    while head1 is not None:
        dictionary[head1] = True
        head1 = head1.next

    while head2 is not None:
        if head2 in dictionary:
            return head2
        
        head2 = head2.next


def intersectionOfTwoLists2(head1, head2):
    while head1 is not None:
        current = head2
        while current is not None:
            if current == head1:
                return current
            
            current = current.next
        
        head1 = head1.next


def intersectionOfTwoLists3(head1, head2):
    l1, l2 = 0, 0
    c1, c2 = head1, head2

    while c1 is not None or c2 is not None:
        if c1 is not None:
            l1 += 1
            c1 = c1.next
        
        if c2 is not None:
            l2 += 1
            c2 = c2.next
    
    diff = 0
    if l1 > l2:
        c1 = head1
        c2 = head2
        diff = l1 - l2
    else:
        c1 = head2
        c2 = head1
        diff = l2 - l1

    i = 0
    while i < diff:
        c1 = c1.next
        i += 1
    
    while c1 != c2:
        c1 = c1.next
        c2 = c2.next
    
    return c1


def intersectionOfTwoLists4(head1, head2):

    a, b = head1, head2

    while a != b:
        a = head2 if a is None else a.next
        b = head1 if b is None else b.next
    
    return a






def main():
    head1 = ListNode(4)
    head1.next = ListNode(1)
    head1.next.next = ListNode(8)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)

    head2 = ListNode(5)
    head2.next = ListNode(6)
    head2.next.next = ListNode(1)
    head2.next.next.next = head1.next.next
    head2.next.next.next.next = head1.next.next.next
    head2.next.next.next.next.next = head1.next.next.next.next

    node = intersectionOfTwoLists(head1, head2)

    print(f'value is {node.val}')

    node = intersectionOfTwoLists2(head1, head2)

    print(f'value is {node.val}')

    node = intersectionOfTwoLists3(head1, head2)

    print(f'value is {node.val}')

    node = intersectionOfTwoLists4(head1, head2)

    print(f'value is {node.val}')

main()
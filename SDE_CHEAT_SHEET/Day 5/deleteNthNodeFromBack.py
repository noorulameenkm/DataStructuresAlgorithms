# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        
        current = head
        prev = next_ = None
        
        i = 0
        while i < n:
            current = current.next
            i += 1
        
        next_ = head
        while current is not None:
            prev = next_
            next_ = next_.next
            current = current.next
        
        if prev is None:
            return head.next
        
        prev.next = next_.next
        
        return head


def removeNthNode(head, n):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    
    i = 0
    prev = None
    current = head
    while i < (length - n):
        prev = current
        current = current.next
        i -= 1
    
    if prev is None:
        return head.next
    
    prev.next = current.next
    return head


def printList(head):
    while head.next is not None:
        print(head.val, end=' ')
        head = head.next

    if head:
        print(head.val)



def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print('Before deleting the node')
    printList(head)
    newHead = Solution().removeNthFromEnd(head, 2)
    print('After deleting the node')
    printList(newHead)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    
    print('Before deleting the node')
    printList(head2)
    newHead2 = Solution().removeNthFromEnd(head2, 2)
    print('After deleting the node')
    printList(newHead2)


main()
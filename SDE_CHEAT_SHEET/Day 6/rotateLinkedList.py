# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        length = 0 
        current = head
        
        while current is not None:
            length += 1
            current = current.next
        
        rotations = k % length
        
        if rotations == 0:
            return head
        
        newhead = None
        first, second = head, head
        i = 0
        while i < rotations:
            first = first.next
            i += 1
        
        while first.next is not None:
            first = first.next
            second = second.next
        
        newhead = second.next
        first.next = head
        second.next = None
        
        return newhead


class Solution2:
    def rotateList(self, head, k):
        if head is None or head.next is None:
            return head
        
        length = 1 
        current = head
        while current.next is not None:
            length += 1
            current = current.next
        
        current.next = head

        k = k % length

        if k == 0:
            return head

        i = 0
        k = length - k
        current = head
        while i < k - 1:
            current = current.next
            i += 1

        head = current.next
        current.next = None 

        return head           

def printList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    
    print()

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print('Before rotating list')
    printList(head)
    newhead = Solution().rotateRight(head, 2)
    print('After rotating list')
    printList(newhead)

    print('Before rotating list')
    printList(newhead)
    newhead2 = Solution().rotateRight(newhead, 2)
    print('After rotating list')
    printList(newhead2)


main()
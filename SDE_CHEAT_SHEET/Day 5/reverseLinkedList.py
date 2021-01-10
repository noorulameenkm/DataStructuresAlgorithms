class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        
        prev = None
        current = head
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        
        return prev
        

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
    
    printList(head)
    newHead = Solution().reverseList(head)
    printList(newHead)

main()
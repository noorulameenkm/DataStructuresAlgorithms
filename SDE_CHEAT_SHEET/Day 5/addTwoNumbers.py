# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        
        carry, head, current, rest_list = 0, None, None, None
        
        while l1 and l2:
            sum_ = l1.val + l2.val + carry
            node = ListNode(sum_ % 10)
            carry = sum_ // 10
            
            if head is None:
                head = node
                current = head
            else:
                current.next = node
                current = current.next
                
            l1 = l1.next
            l2 = l2.next
            
        
        if l1 is not None:
            rest_list = l1
        
        if l2 is not None:
            rest_list = l2
        
        
        while rest_list:
            sum_ = rest_list.val + carry
            node = ListNode(sum_ % 10)
            carry = sum_ // 10
            current.next = node
            current = current.next
            rest_list = rest_list.next
            
        if carry > 0:
            node = ListNode(carry)
            current.next = node
        
        return head
        

def printList(head):
    while head.next is not None:
        print(head.val, end=' ')
        head = head.next

    if head:
        print(head.val)


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    head = Solution().addTwoNumbers(l1, l2)
    printList(head)

    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)

    head = Solution().addTwoNumbers(l1, l2)
    printList(head)



        
main()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        slowPtr = head
        fastPtr = head
        
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        
        return slowPtr
        
    



def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    midNode = Solution().middleNode(head)

    if midNode:
        print(midNode.val)

main()
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        
        slow, fast = head, head
        
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

def hasCycle2(head):
    current = head
    hashTable = {}

    while current is not None:
        if current in hashTable:
            return True
        else:
            hashTable[current] = True
        
        current = current.next
    
    return False
            
        

def main():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    print(Solution().hasCycle(head))

    print(hasCycle2(head))

main()
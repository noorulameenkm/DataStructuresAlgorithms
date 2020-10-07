# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printList(self):
        temp = self
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next
        print('\n', end='')

class Solution:
    def rotateRight(self, head, k):
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        if length <= 1:
            return head
        
        if k >= length:
            k = k % length
            
        
        firstPtr = secondPtr = head
        while k > 0:
            k -= 1
            secondPtr = secondPtr.next
        
        while secondPtr.next:
            secondPtr = secondPtr.next
            firstPtr = firstPtr.next
        
        secondPtr.next = head
        if firstPtr.next:
            head = firstPtr.next
        else:
            head = head
            
        firstPtr.next = None
        
        return head
        
        

def main():
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.printList()
    head = Solution().rotateRight(head, 2)
    head.printList()

main()

        
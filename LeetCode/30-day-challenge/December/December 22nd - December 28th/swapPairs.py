# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        if not head.next:
            return head
        
        temp = head.next
        head.next = temp.next
        temp.next = head
        head = temp
        head.next.next = self.swapPairs(head.next.next)
        return head

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end = ' ')
        temp = temp.next
    print('\n', end='')

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    printLinkedList(head)
    head = Solution().swapPairs(head)
    printLinkedList(head)
            
            
            
            
        
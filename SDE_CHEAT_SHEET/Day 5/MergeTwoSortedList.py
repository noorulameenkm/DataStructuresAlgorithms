from heapq import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val
    
class Solution:
    def mergeTwoLists(self, l1, l2):
        minheap = []
        newHead = None
        current = None
        
        heappush(minheap, l1)
        heappush(minheap, l2)
        
        while minheap:
            pop = heappop(minheap)
            if newHead is None:
                newHead = ListNode(pop.val)
                current = newHead
            else:
                current.next = ListNode(pop.val)
                current = current.next
            
            if pop.next is not None:
                heappush(minheap, pop.next)
                
        return newHead

    
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        minheap = []
        newHead = None
        current = None
        
        if l1:
            heappush(minheap, (l1.val, 1))
            l1 = l1.next
            
        if l2:
            heappush(minheap, (l2.val, 2))
            l2 = l2.next
        
        while minheap:
            val, index = heappop(minheap)
            if newHead is None:
                newHead = ListNode(val)
                current = newHead
            else:
                current.next = ListNode(val)
                current = current.next
            
            if index == 1 and l1 is not None:
                heappush(minheap, (l1.val, 1))
                l1 = l1.next
            
            if index == 2 and l2 is not None:
                heappush(minheap, (l2.val, 2))
                l2 = l2.next
            
                
        return newHead

def sortTwoList(l1, l2):
    if l1 is None and l2 is None:
        return None
    elif l1 is None:
        return l2
    elif l2 is None:
        return l1

    newHead = current = None
    while l1 is not None and l2 is not None:
        smallest = None
        if l1.val < l2.val:
            smallest = l1.val
            l1 = l1.next
        else:
            smallest = l2.val
            l2 = l2.next

        if newHead is None:
            newHead = ListNode(smallest)
            current = newHead
        else:
            current.next = ListNode(smallest)
            current = current.next
    
    while l1 is not None:
        current.next = ListNode(l1.val)
        current = current.next
        l1 = l1.next
    
    while l2 is not None:
        current.next = ListNode(l2.val)
        current = current.next
        l2 = l2.next

    return newHead


def mergeTwoLists2(l1, l2):
    if l1 is None or l2 is None:
        return None
    elif l1 is None:
        return l2
    elif l2 is None:
        return l1

    if l2.val < l1.val:
        l1, l2 = l2, l1

    res = l1

    while l1 is not None and l2 is not None:
        temp = None

        while l1 is not None and l1.val <= l2.val:
            temp = l1
            l1 = l1.next
        
        temp.next = l2

        l1, l2 = l2, l1
    
    return res

def printList(head):
    while head.next is not None:
        print(head.val, end=' ')
        head = head.next

    if head:
        print(head.val)


def main():
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)
    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    # Method 1
    newHead = Solution().mergeTwoLists(head1, head2)
    printList(newHead)

    # Method 2
    newHead2 = Solution2().mergeTwoLists(head1, head2)
    printList(newHead2)

    # Method 3
    newHead3 = sortTwoList(head1, head2)
    printList(newHead3)

    # Method 4
    newHead4 = mergeTwoLists2(head1, head2)
    printList(newHead4)    


main()



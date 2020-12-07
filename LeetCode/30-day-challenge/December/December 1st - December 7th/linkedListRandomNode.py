import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        """
        if self.head is None:
            return
        
        if self.head and self.head.next is None:
            return self.head.val
        
        # Use a different seed value so that we don't get  
        # same result each time we run this program 
        random.seed()

        # Initialize result as first node 
        result = self.head.val

        # Iterate from the (k+1)th element nth element 
        # because we iterate from (k+1)th element, or  
        # the first node will be picked more easily
        current = self.head.next
        n = 2
        while current is not None:

            # change result with probability 1/n
            if random.randrange(n) == 0:
                result = current.val
                
            current = current.next
            n += 1
            
        return result


def main():
    head = ListNode(5)
    head.next = ListNode(20)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(30)

    sol = Solution(head)
    print(sol.getRandom())



main()
class Node:
    def __init__(self, val):
        self. val = val
        self.next = None


def startingPointOfLoop(head):
    hashSet = set()

    current = head

    while current is not None:
        if current not in hashSet:
            hashSet.add(current)
        else:
            return current
        
        current = current.next
    
    return None


class Solution:
    def detectCycle(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
            
        if fast is None or fast.next is None:
            return None
        
        current = head
        
        while slow != current:
            slow = slow.next
            current = current.next
            
        return slow


def main():
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(-4)
    head.next.next.next.next = head.next

    start = startingPointOfLoop(head)
    if start is not None:
        print(start.val)
    else:
        print('Loop Doesn\'t exist')

    start = Solution().detectCycle(head)
    if start is not None:
        print(start.val)
    else:
        print('Loop Doesn\'t exist')

main()
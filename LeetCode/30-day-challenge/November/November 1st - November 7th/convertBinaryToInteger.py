class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next
        
        num = 0
        index = 1
        for i in range(len(array) - 1, -1, -1):
            binary = array[i]
            
            if binary == 1:
                num += index
            index *= 2
            
        return num


"""
* Initialize result number to be equal to head value: num = head.val. This operation is safe because the list is guaranteed to be non-empty.

* Parse linked list starting from the head: while head.next:

* The current value is head.next.val. Update the result by shifting it by one to the left and adding the current value: num = num * 2 + head.next.val.
    Return num.
"""

def getdecimal(head):
    num = head.val

    while head.next:
        num = num * 2 + head.next.val
        head = head.next

    return num



"""
* Initialize result number to be equal to head value: num = head.val. This operation is safe because the list is guaranteed to be non-empty.

* Parse linked list starting from the head: while head.next:

* The current value is head.next.val. Update the result by shifting it by one to the left and adding the current value using logical OR: num = (num << 1) | head.next.val.
    Return num
"""

def getdecimal2(head):
    num = head.val

    while head.next:
        num = (num << 1) | head.next.val
        head = head.next

    return num 




def main():
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)

    print(Solution().getDecimalValue(head))
    print(getdecimal(head))
    print(getdecimal2(head))

main()

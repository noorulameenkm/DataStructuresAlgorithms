# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def reverseBetween(A, B, C):
    if A is None:
        return A
    
    if A.next is None:
        return A
        
    i = 1
    current = A
    startPrev = None
    while i < B and current is not None:
        startPrev = current
        current = current.next
        i += 1
        
    prev = None
    startCopy = current
    while i <= C and current is not None:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
        i += 1
    
    if startPrev is not None:
        startPrev.next = prev
    
    startCopy.next = current
    
    if B == 1:
        return prev
    else:
        return A


def print_list(head):
    current = head
    while current.next:
        print(current.val, end=' ') 
        current = current.next
    
    if current:
        print(current.val)
    
    


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print('Before reverse')
    print_list(head)
    result = reverseBetween(head, 2, 3)
    print('After reverse')
    print_list(result)

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print('Before reverse')
    print_list(head)
    result = reverseBetween(head, 1, 2)
    print('After reverse')
    print_list(result)






main()
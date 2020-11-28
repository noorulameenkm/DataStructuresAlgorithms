class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


    def print_list(self):
        head = self
        while head and head.next:
            print(head.val, end=' ')
            head = head.next
        
        print(head.val)


def reverse_based_on_size(head):
    length = 0
    if head is None:
        return None
    
    current = head
    while current is not None:
        length += 1
        current = current.next
    
    if length % 2 == 0:
        head = reverse_sub_list(head, 1, length // 2)
        head = reverse_sub_list(head, (length // 2) + 1, length)
    else:
        head = reverse_sub_list(head, 1, length // 2)
        head = reverse_sub_list(head, (length // 2) + 2, length)

    return head
    

def reverse_sub_list(head, p, q):
    if not head or p != q:
        prev1, current = None, head
        i = 1 
        while i < p:
            prev1 = current
            current = current.next
            i += 1
        
        last = current
        while i < q:
            last = last.next
            i += 1
        
        next1 = last.next
        currentCopy = current
        prev = None
        while current != next1:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        
        currentCopy.next = next1
        if prev1:
            prev1.next = prev
        else:
            head = prev
  
    return head






def main():
   head = Node(1)
   head.next = Node(2)
   head.next.next = Node(3)
   head.next.next.next = Node(4)
   head.next.next.next.next = Node(5)

   print("Linked List before reversing: ", end="")
   head.print_list()
   result = reverse_based_on_size(head)
   print("Linked List after reversing: ", end="")
   result.print_list()

   head2 = Node(1)
   head2.next = Node(2)
   head2.next.next = Node(3)
   head2.next.next.next = Node(4)
   head2.next.next.next.next = Node(5)
   head2.next.next.next.next.next = Node(6)

   print("Linked List before reversing: ", end="")
   head2.print_list()
   result = reverse_based_on_size(head2)
   print("Linked List after reversing: ", end="")
   result.print_list()


main()
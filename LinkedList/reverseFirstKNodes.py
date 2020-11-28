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



def reverse_first_k_nodes(head, k):
    current = head
    currentCopy = current
    prev = None
   
    i = 0
    while current is not None and i < k:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
        i += 1
    
    currentCopy.next = current
    return prev




def main():
   head = Node(1)
   head.next = Node(2)
   head.next.next = Node(3)
   head.next.next.next = Node(4)
   head.next.next.next.next = Node(5)

   print("print list before reversing: ", end="")
   head.print_list()
   result = reverse_first_k_nodes(head, 3)
   print("Print list after reversing: ", end="")
   result.print_list()
   print("print list before reversing: ", end="")
   result.print_list()
   result = reverse_first_k_nodes(result, 5)
   print("Print list after reversing: ", end="")
   result.print_list()


main()


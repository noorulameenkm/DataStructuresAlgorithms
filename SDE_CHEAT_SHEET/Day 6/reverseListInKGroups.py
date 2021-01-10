class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()



def reverseKGroups(head, k):
    if not head or k <= 1:
        return head
    
    length = 0
    current = head
    newHead = None
    while current is not None:
        length = length + 1
        current = current.next
    
    current, prev = head, None

    while length >= k:

        last_node_of_previous = prev
        last_node_of_current = current

        i = 0
        nex = None
        while i < k:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
            i += 1

        if last_node_of_previous is not None:
            last_node_of_previous.next = prev
        else:
            newHead = prev


        last_node_of_current.next = current
        prev = last_node_of_current
        length -= k

    return newHead




def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverseKGroups(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()

main()
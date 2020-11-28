from __future__ import print_function


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


"""
Time Complexity - O(N)
Space Complexity - O(1)
"""
def reverse_alternate_k_elements(head, k):
  if head is None and k <= 1:
    return head

  current, prev = head, None
  while True:
    last_node_of_previous = prev
    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sublist = current
    next = None
    i = 0
    while current is not None and i < k:
      next = current.next
      current.next = prev
      prev = current
      current = next
      i += 1

    # connect with the previous part
    if last_node_of_previous is not None:
      last_node_of_previous.next = prev
    else:
      head = prev

    # connect with the next part
    last_node_of_sublist.next = current
    prev = last_node_of_sublist
    
    i = 0
    while current is not None and i < k:
      prev = current
      current = current.next
      i += 1

    if current is None:
      break

  return head


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
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

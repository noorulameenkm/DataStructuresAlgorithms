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


def reverse_sub_list2(head, p, q):
  if p == q:
    return head

  # after skipping 'p-1' nodes, current will point to 'p'th node
  current, previous = head, None
  i = 0
  while current is not None and i < p - 1:
    previous = current
    current = current.next
    i += 1

  # we are interested in three parts of the LinkedList, the part before index 'p',
  # the part between 'p' and 'q', and the part after index 'q'
  last_node_of_first_part = previous
  # after reversing the LinkedList 'current' will become the last node of the sub-list
  last_node_of_sub_list = current
  next = None  # will be used to temporarily store the next node

  i = 0
  # reverse nodes between 'p' and 'q'
  while current is not None and i < q - p + 1:
    next = current.next
    current.next = previous
    previous = current
    current = next
    i += 1

  # connect with the first part
  if last_node_of_first_part is not None:
    # 'previous' is now the first node of the sub-list
    last_node_of_first_part.next = previous
  # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
  else:
    head = previous

  # connect with the last part
  last_node_of_sub_list.next = current
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()
  print("Nodes of original LinkedList: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 1, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()
  print("Nodes of original LinkedList: ", end='')
  result.print_list()
  result = reverse_sub_list(result, 1, 5)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()

  print("Second Method")

  head2 = Node(1)
  head2.next = Node(2)
  head2.next.next = Node(3)
  head2.next.next.next = Node(4)
  head2.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head2.print_list()
  result = reverse_sub_list2(head2, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()
  print("Nodes of original LinkedList: ", end='')
  head2.print_list()
  result = reverse_sub_list(head2, 1, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()
#   print("Nodes of original LinkedList: ", end='')
#   head2.print_list()
#   result = reverse_sub_list(head2, 1, 5)
#   print("Nodes of reversed LinkedList are: ", end='')
#   result.print_list()


main()

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
def rotate(head, rotations):
  if head is None or head.next is None or rotations <= 0:
    return head

  length = 1
  current = head
  while current.next:
    length += 1
    current = current.next

  current.next = head

  current = head
  rotations %= length
  skiplength = length - rotations
  for i in range(skiplength - 1):
    current = current.next

  head = current.next
  current.next = None
  
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()

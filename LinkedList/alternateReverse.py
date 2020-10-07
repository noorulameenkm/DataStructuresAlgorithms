from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  rightHead = reverse(slow)
  leftHead = head

  while leftHead is not None and rightHead is not None:
    leftNext = leftHead.next
    rightNext = rightHead.next

    leftHead.next = rightHead
    rightHead.next = leftNext

    leftHead = leftNext
    rightHead = rightNext

   
  if leftHead.next:
    leftHead.next = None


def reverse(head):
  prev = None
  while head:
    next_ = head.next
    head.next = prev
    prev = head
    head = next_

  return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def findLengthCycle(head):
  slowPtr = fastPrt = head
  while fastPrt and fastPrt.next:
    slowPtr = slowPtr.next
    fastPrt = fastPrt.next.next

    if slowPtr == fastPrt:
      current = slowPtr
      length = 0
      while True:
        current = current.next
        length += 1
        if current == slowPtr:
          return length


def find_cycle_start(head):
  k = findLengthCycle(head)
  ptr1 = ptr2 = head
  # move pointer2 ahead k nodes
  while k > 0:
    ptr2 = ptr2.next
    k -= 1

  # increment both pointers until they meet at the start of the cycle
  while ptr1 != ptr2:
    ptr1 = ptr1.next
    ptr2 = ptr2.next

  return ptr2


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

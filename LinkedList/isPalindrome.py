class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  # TODO: Write your code here
  middle_ = middle(head)
  middleafter = reverse(middle_.next)
  copy_middle_after = middleafter
  start = head
  while start and middleafter:
    if start.value != middleafter.value:
      return False

    start = start.next
    middleafter = middleafter.next

  reverse(copy_middle_after)

  if start is None or middleafter is None:
    return True
  else:
    return False

def middle(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow

def reverse(head):
  prev = None
  current = head
  next_ = current.next
  while current:
    next_ = current.next
    current.next = prev
    prev = current
    current = next_
    

  return prev

  


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()








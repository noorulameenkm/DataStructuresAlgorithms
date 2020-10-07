class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  # TODO: Write your code here
  slow = fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next


  return slow


# current start from the third node 
def find_mid(head):
    if head is None:
        return -1
    current_node = head
    if current_node.next is None:
        # Only 1 element exist in array so return its value.
        return current_node.value

    mid_node = current_node
    current_node = current_node.next.next
    # Move mid_node (Slower) one step at a time
    # Move current_node (Faster) two steps at a time
    # When current_node reaches at end, mid_node will be at the middle of List
    while current_node:
        mid_node = mid_node.next
        current_node = current_node.next
        if current_node:
            current_node = current_node.next
    if mid_node:
        return mid_node.value
    return -1


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  print("Middle Node: " + str(find_mid(head)))


main()

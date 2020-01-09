class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next

    print('\n', end='')


def findLength(head):
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next

    return length


def findJoiningUsingLength(head_1, head_2):
    l_1 = findLength(head_1)
    l_2 = findLength(head_2)
    temp_1 = None
    temp_2 = None
    diff = 0
    if min(l_1, l_2) is l_1:
        temp_1 = head_2
        temp_2 = head_1
        diff = l_2 - l_1
    else:
        temp_1 = head_1
        temp_2 = head_2
        diff = l_1 - l_2

    while diff and temp_1:
        temp_1 = temp_1.next
        diff -= 1

    while temp_1 is not temp_2:
        temp_1 = temp_1.next
        temp_2 = temp_2.next

    return temp_1.val


if __name__ == '__main__':
    head_1 = Node(1)
    head_1.next = Node(2)
    head_1.next.next = Node(3)
    head_2 = Node(10)
    head_2.next = Node(9)
    head_2.next.next = head_1.next.next.next = Node(5)
    head_1.next.next.next.next = Node(11)
    head_1.next.next.next.next.next = Node(12)
    print(findJoiningUsingLength(head_1, head_2))
    
from mergeSortedListsIterative import mergeLists, Node


def merge_n_sorted_lists(lists):
    res = lists[0]
    for i in range(1, len(lists)):
        res = mergeLists(res, lists[i])

    return res


def display(head):
    temp = head
    while temp:
        print(temp.val, end="")
        temp = temp.next
        if temp:
            print(", ", end="")
    print("")


r1 = Node(11)
r1.next = Node(41)
r1.next.next = Node(51)

r2 = Node(21)
r2.next = Node(23)
r2.next.next = Node(42)

r3 = Node(25)
r3.next = Node(56)
r3.next.next = Node(66)
r3.next.next.next = Node(72)

res = merge_n_sorted_lists([r1, r2, r3])
display(res)

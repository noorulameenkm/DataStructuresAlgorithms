from node import Node


def count_nextSiblings(root):
    count = 0

    while root:
        root = root.nextSibling
        count += 1

    return count



if __name__ == '__main__':
    root = Node(1)
    root.firstChild = Node(2)
    root.firstChild.nextSibling = Node(3)
    root.firstChild.nextSibling.nextSibling = Node(4)
    root.firstChild.nextSibling.nextSibling.nextSibling = Node(5)

    # printing the count of nextSiblings of root
    print(count_nextSiblings(root))

    # printing the count of next Sibling of root's firstChild
    print(count_nextSiblings(root.firstChild))

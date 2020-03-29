from node import Node


def is_isomorphic(root1, root2):
    if not root1 and not root2:
        return True
    if (not root1 and root2) or (root1 and not root2):
        return False
    
    return is_isomorphic(root1.firstChild, root2.firstChild) and is_isomorphic(root1.nextSibling, root2.nextSibling)


if __name__ == '__main__':

    # tree_1
    root1 = Node(1)
    root1.firstChild = Node(2)
    root1.firstChild.firstChild = Node(10)
    root1.firstChild.nextSibling = Node(3)
    root1.firstChild.nextSibling.nextSibling = Node(4)
    root1.firstChild.nextSibling.nextSibling.nextSibling = Node(5)
    root1.firstChild.firstChild.nextSibling = Node(6)
    root1.firstChild.firstChild.nextSibling.nextSibling = Node(7)

    # tree_2
    root2 = Node(11)
    root2.firstChild = Node(12)
    root2.firstChild.firstChild = Node(13)
    root2.firstChild.nextSibling = Node(14)
    root2.firstChild.nextSibling.nextSibling = Node(15)
    root2.firstChild.nextSibling.nextSibling.nextSibling = Node(16)
    root2.firstChild.firstChild.nextSibling = Node(17)
    root2.firstChild.firstChild.nextSibling.nextSibling = Node(18)

    if is_isomorphic(root1, root2):
        print("Both the trees are isomorphic")
    else:
        print("Both the trees are not isomorphic")
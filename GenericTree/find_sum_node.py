from node import Node



def sum_of_generic_tree(root):
    if not root:
        return 0
    
    return root.data + sum_of_generic_tree(root.firstChild) + sum_of_generic_tree(root.nextSibling)



if __name__ == '__main__':
    root = Node(1)
    root.firstChild = Node(2)
    root.firstChild.firstChild = Node(10)
    root.firstChild.nextSibling = Node(3)
    root.firstChild.nextSibling.nextSibling = Node(4)
    root.firstChild.nextSibling.nextSibling.nextSibling = Node(5)
    root.firstChild.firstChild.nextSibling = Node(6)
    root.firstChild.firstChild.nextSibling.nextSibling = Node(7)

    print(sum_of_generic_tree(root))
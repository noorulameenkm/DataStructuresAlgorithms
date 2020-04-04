from node import Node


def findAnElement(root, el):
    
    while root:
        if root.data == el:
            return root
        if el < root.data:
            root = root.left
        else:
            root = root.right
    
    return None
       


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(17)

    el = findAnElement(root, 10)
    if el:
        print(el.data)
    else:
        print('Not Found')




    

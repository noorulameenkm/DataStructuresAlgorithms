from node import Node


def findSmallest(root):
    if not root:
        return None
     
    while root.left:
        root = root.left
    
    return root

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(17)

    smallest = findSmallest(root)
    if smallest:
        print(smallest.data)
    else:
        print('No smallest element')

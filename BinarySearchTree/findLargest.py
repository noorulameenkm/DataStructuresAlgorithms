from node import Node


def findLargest(root):
    if not root:
        return None
     
    while root.right:
        root = root.right
    
    return root

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(17)

    largest = findLargest(root)
    if largest:
        print(largest.data)
    else:
        print('No larger element')

from node import Node


def print_All_Ancestors(root, node):
    if not root:
        return False

    if root.left == node or root.right == node or print_All_Ancestors(root.left, node) or print_All_Ancestors(root.right, node):
        print(root.data, end = ' ')
        return True
    
    return False
    


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print_All_Ancestors(root, root.right.right)
    
    print('\n', end='')
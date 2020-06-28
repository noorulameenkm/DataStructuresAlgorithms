from node import Node 



def isBST(root, left = None, right = None):
    if not root:
        return True
    
    if left and root.data < left.data:
        return False

    if right and root.data > right.data:
        return False

    return isBST(root.left, left, root) and isBST(root.right, root, right)





if __name__ == '__main__':
    root = Node(6)
    root.left = Node(2)
    # root.left.right = Node(9)
    root.left.left = Node(1)
    root.right = Node(8)

    if isBST(root, None, None):
        print('Tree is a BST')
    else:
        print('Tree is not a BST')
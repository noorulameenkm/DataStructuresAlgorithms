from node import Node


def preOrder(root):
    if root:
        print(root.data, end = ' ')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end = ' ')

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end = ' ')
        inOrder(root.right)
        


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(17)

    print('PreOrder BST')
    preOrder(root)
    print('\n',end='')
    print('PostOrder BST')
    postOrder(root)
    print('\n',end='')
    print('InOrder BST')
    inOrder(root)
    print('\n',end='')


    

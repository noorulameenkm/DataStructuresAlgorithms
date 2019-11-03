def printTreePreorder(root):
    if root is not None:
        print(root.getNodeVal(), end=' ')
        printTreePreorder(root.left)
        printTreePreorder(root.right)

def printTreePostorder(root):
    if root is not None:
        printTreePostorder(root.left)
        printTreePostorder(root.right)
        print(root.getNodeVal(), end=' ')

def printTreeInorder(root):
    if root is not None:
        printTreeInorder(root.left)
        print(root.getNodeVal(), end=' ')
        printTreeInorder(root.right)
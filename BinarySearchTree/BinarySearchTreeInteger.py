from TreeFunctions import printTreeInorder, printTreePostorder, printTreePreorder 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getNodeVal(self):
        return self.data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertNode(self,nodeVal):
        if self.root is None:
            self.root = Node(nodeVal)
        else:
            self.root = searchAndInsert(self.root,nodeVal)

    def Inorder(self):
        printTreeInorder(self.root)

    def Preorder(self):
        printTreePreorder(self.root)

    def Postorder(self):
        printTreePostorder(self.root)

    
def searchAndInsert(root,nodeVal):
    if root is None:
        return Node(nodeVal)
    elif root.getNodeVal() < nodeVal:
        root.right = searchAndInsert(root.right, nodeVal)
        return root
    else:
        root.left = searchAndInsert(root.left, nodeVal)
        return root


def Main():
    tree = BinarySearchTree()
    inputList = input('Enter the elements in space-seperated manner ')
    for num in inputList.split(' '):
        try:
            tree.insertNode(int(num))
        except:
            pass
    
    tree.Inorder()
    print('\n', end='')
    tree.Preorder()
    print('\n', end='')
    tree.Postorder()
    print('\n', end='')

    


if __name__ == '__main__':
    Main()
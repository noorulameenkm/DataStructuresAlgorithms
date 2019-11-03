from TreeFunctions import printTreeInorder, printTreePostorder, printTreePreorder

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

    def getNodeVal(self):
        return self.data


class BinaryTreeInteger:
    def __init__(self):
        self.root = None

    def addNode(self,nodeVal,nodeParent, nodePos):
        newNode = Node(nodeVal)
        if self.root is None:
            self.root = newNode
        else:
            self.root = searchAndInsert(self.root,nodeVal,nodeParent,nodePos)
    
    def printInorder(self):
        printTreeInorder(self.root)

    def printPostorder(self):
        printTreePostorder(self.root)

    def printPreorder(self):
        printTreePreorder(self.root)
        
            
def searchAndInsert(root,val,nodeParent,nodePos):   
    if root is not None:
        if root.getNodeVal() == nodeParent:
            if nodePos == 'R':
                root.right = Node(val)
            else:
                root.left = Node(val)
            return root
        else:
            root.left = searchAndInsert(root.left, val, nodeParent, nodePos)
            root.right = searchAndInsert(root.right, val, nodeParent, nodePos)
            return root
    else:
        return None


def Main():
    tree = BinaryTreeInteger()
    n = int(input('Enter the number of elements you want to insert '))
    for i in range(n):
        nodeVal = int(input('Enter the node value '))
        rootOrNot = input('Is the node root ')
        if rootOrNot.lower() == 'yes':
            tree.addNode(nodeVal, 0, 'R')
        else:
            parentNode = int(input('Enter the parent Node '))
            childPos = input('Enter the position of the child, R or L ')
            tree.addNode(nodeVal, parentNode, childPos.upper())
            
    tree.printPreorder()
    print('\n', end='')
    tree.printInorder()
    print('\n', end='')
    tree.printPostorder()
    print('\n', end='')



if __name__ == '__main__':
    Main()

    
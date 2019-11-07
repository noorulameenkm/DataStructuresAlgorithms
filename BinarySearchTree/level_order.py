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

    def levelOrder(self):
        printLevelOrder(self.root)

    def levelOrderDelimiter(self):
        printLevelOrderWithDelimiter(self.root)


def searchAndInsert(root,nodeVal):
    if root is None:
        return Node(nodeVal)
    elif root.getNodeVal() < nodeVal:
        root.right = searchAndInsert(root.right, nodeVal)
        return root
    else:
        root.left = searchAndInsert(root.left, nodeVal)
        return root

def printLevelOrder(root):
    if root is not None:
        nodes = [root]
        while len(nodes) != 0:
            dequed = nodes.pop(0)

            if dequed.left is not None:
                nodes.append(dequed.left)
            if dequed.right is not None:
                nodes.append(dequed.right)

            print(dequed.data, end=' ')


def printLevelOrderWithDelimiter(root):
    if root is not None:
        nodes = [root, '$']
        while len(nodes) != 0:
            dequed = nodes.pop(0)
            if dequed is '$':
                print(dequed, end=" ")
                if len(nodes) != 0 and nodes[0] is not '$':
                    nodes.append('$')
            else:
                if dequed.left is not None:
                    nodes.append(dequed.left)
                if dequed.right is not None:
                    nodes.append(dequed.right)
               
                print(dequed.data, end=" ")



def Main():
    tree = BinarySearchTree()
    inputList = input('Enter the elements in space-seperated manner ')
    for num in inputList.split(' '):
        try:
            tree.insertNode(int(num))
        except:
            pass

    tree.levelOrder()
    print('\n', end = '')
    tree.levelOrderDelimiter()
    print('\n', end = '')
    

if __name__ == '__main__':
    Main()
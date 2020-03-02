from node import Node 


def printList(root):
    if root != None:
        printList(root.left)
        print(root.data, end=' ')
        printList(root.right)


def convertToMirror(root):
    if root:
        # Swap the subtrees
        temp = root.left
        root.left = root.right
        root.right = temp

        #recursively call with subtrees
        convertToMirror(root.left)
        convertToMirror(root.right)




def Main():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(3)
    root.left.left = Node(9)
    root.left.right = Node(12)
    printList(root)
    convertToMirror(root)
    print('\n', end='')
    printList(root)
    print('\n', end='')

if __name__ == '__main__':
    Main()
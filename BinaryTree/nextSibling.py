from node import Node


def fillNextSiblings(root):
    if not root:
        return
    
    if root.left:
        root.left.nextsibling = root.right
    if root.right:
        root.right.nextsibling = root.left
    
    fillNextSiblings(root.left)
    fillNextSiblings(root.right)


def printAllNextSiblings(root):
    if root:
        print(root.data, end = ' ')
        
        if root.nextsibling:
            print(root.nextsibling.data)
        else:
            print('None')
        
        printAllNextSiblings(root.left)
        printAllNextSiblings(root.right)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    fillNextSiblings(root)
    printAllNextSiblings(root)
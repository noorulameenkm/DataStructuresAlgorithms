from node import Node


def construct_tree(preOrder, inOrder, startInd, endInd):
    if startInd > endInd:
        return None
    
    data = preOrder[construct_tree.preIndex]
    newNode = Node(data)

    construct_tree.preIndex += 1

    if startInd == endInd:
        return newNode
    
    index = findIndex(inOrder, startInd, endInd, data)

    newNode.left = construct_tree(preOrder, inOrder, startInd, index - 1)
    newNode.right = construct_tree(preOrder, inOrder, index + 1, endInd)

    return newNode


def findIndex(inOrder, startInd, endInd, data):
    for i in range(startInd, endInd + 1):
        if inOrder[i] == data:
            return i


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data, end=' ')
        printInOrder(root.right)


if __name__ == '__main__':
    
    construct_tree.preIndex = 0
    preOrder = [1,2,4,5,3,6,7]
    inOrder = [4,2,5,1,6,3,7]
    root = construct_tree(preOrder,inOrder, 0, len(inOrder) - 1)
    printInOrder(root)
    print('\n', end='')

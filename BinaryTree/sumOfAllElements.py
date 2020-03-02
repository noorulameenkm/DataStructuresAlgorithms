from node import Node 


def printList(root):
    if root != None:
        printList(root.left)
        print(root.data, end=' ')
        printList(root.right)


def findSumOfAllElements(root):
    if not root:
        return 0
    
    return root.data + findSumOfAllElements(root.left) + findSumOfAllElements(root.right)

def findSumOfAllElementsNonRecursive(root):
    if not root:
        return 0

    queue = [root]
    sum_ = 0

    while len(queue) > 0:
        node = queue.pop(0)

        sum_ += node.data

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        
    return sum_

def Main():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(3)
    root.left.left = Node(9)
    root.left.right = Node(12)
    root.right.left = Node(15)
    root.right.right = Node(18)
    printList(root)
    print('\n', end='')
    print(findSumOfAllElements(root))
    print(findSumOfAllElementsNonRecursive(root))


if __name__ == '__main__':
    Main()
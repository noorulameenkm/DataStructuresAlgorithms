from node import Node 


def printList(root):
    if root != None:
        printList(root.left)
        print(root.data, end=' ')
        printList(root.right)


def isSumPathExist(root, sum_):
    if not root:
        return sum_ == 0
    else:
        sum_ = sum_ - root.data
        if sum_ == 0:
            return True

        return isSumPathExist(root.left, sum_) or isSumPathExist(root.right, sum_)

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
    print(isSumPathExist(root, 27))


if __name__ == '__main__':
    Main()
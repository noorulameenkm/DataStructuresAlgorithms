class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None 
    
    def getVal(self):
        return self.data 


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = insertNode(self.root, val)

    def maxValNode(self, x, y):
        maxValBetweenNode(self.root, x, y)



def insertNode(root, val):
    if root is None:
        return Node(val)
    elif root.getVal() > val:
        root.left = insertNode(root.left, val)
        return root
    else:
        root.right = insertNode(root.right, val)
        return root


def maxValBetweenNode(root, x, y):
    if x == root.getVal() or y == root.getVal():
        searchVal = y if root.getVal() == x else x
        if searchVal < root.getVal():
            print(root.getVal())
        else:
            print(getMaxVal(root, searchVal, root.getVal()))
    elif (x > root.getVal() and y < root.getVal()) or (y > root.getVal() and x < root.getVal()):
        searchVal = x if root.getVal() < x else y
        print(getMaxVal(root, searchVal, root.getVal()))
    elif x > root.getVal() and y > root.getVal():
        maxValBetweenNode(root.right, x, y)
    else:
        maxValBetweenNode(root.left, x, y)


def getMaxVal(root, val, max_val):
    if val == root.getVal():
        max_val = max_val if max_val > root.getVal() else root.getVal()
        return max_val
    elif val > root.getVal():
        max_val = max_val if root.getVal() < max_val else root.getVal()
        return getMaxVal(root.right, val, max_val)
    else:
        max_val = max_val if root.getVal() < max_val else root.getVal()
        return max_val


def Main():
    n = int(input())
    input_line = input()
    input_array_numbers = [int(num) for num in input_line.split(" ") if num != '']
    tree = BinarySearchTree()
    for num in input_array_numbers:
        tree.insert(num)

    x_y = input().split(" ")
    x = int(x_y[0])
    y = int(x_y[1])
    tree.maxValNode(x,y)


if __name__ == "__main__":
    Main()


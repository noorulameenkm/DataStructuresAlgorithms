
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = insertIntoTree(self.root, data)
    
    def preOrder(self):
        printPreOrder(self.root)
        print('\n', end='')
    

def printPreOrder(root):
    if root:
        print(root.data, end=' ')
        printPreOrder(root.left)
        printPreOrder(root.right)

def insertIntoTree(root, data):
    newNode = Node(data)
    if not root:
        return newNode
    
    nodes = [root]
    while len(nodes) > 0:
        node = nodes.pop(0)
        if not node.left:
            node.left = newNode
            return root
        
        nodes.append(node.left)

        if not node.right:
            node.right = newNode
            return root
        
        nodes.append(node.right)

def initBinaryTree():
    try:
        tree = BinaryTree()
        return tree
    except Exception as e:
        raise e
    

def Main(tree):
    options = {
        1: 'INS',
        2: 'EXIT'
    }

    while True:
        print('1. Insert Element')
        print('2. Exit')
        inp = int(input("Please select one option"))
        choice = options.get(inp, 'dafault')
        if choice is 'INS':
            ins_el = int(input("Please enter the value to be inserted"))
            tree.insert(ins_el)
        elif choice in ['default', 'EXIT']:
            break
    
    print('Thanks for being there')
    return


if __name__ == '__main__':
    tree = initBinaryTree()
    Main(tree)
    tree.preOrder()






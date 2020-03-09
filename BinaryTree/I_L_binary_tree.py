from node import Node

def construct_tree(preorder):
    if construct_tree.preOrderIndex >= len(preorder):
        return None
    
    current_index = construct_tree.preOrderIndex
    data = preorder[current_index]
    newNode = Node(data)
    construct_tree.preOrderIndex += 1

    if data == 'L':
        return newNode
    
    newNode.left = construct_tree(preorder)
    newNode.right = construct_tree(preorder)
    
    return newNode

def print_preorder(root):
    if root:
        print(root.data, end = ' ')
        print_preorder(root.left)
        print_preorder(root.right)

if __name__ == '__main__':
    preorder = 'ILILL'
    construct_tree.preOrderIndex = 0
    root = construct_tree(preorder)
    print_preorder(root)
    print('\n', end='')

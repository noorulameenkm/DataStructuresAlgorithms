from node import Node



def LCA(root, node_1, node_2):
    if root is None:
        return None

    
    if (node_1.data < root.data and node_2.data > root.data) or (node_1.data > root.data and node_2.data < root.data) or root.data == node_1.data or root.data == node_2.data:
        return root

    if node_1.data < root.data:
        return LCA(root.left, node_1, node_2)
    
    return LCA(root.right, node_1, node_2)

    


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.left.right.left = Node(6)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(17)


    lcs_node = LCA(root, root, root.right.right)

    if lcs_node is not None:
        print(f'LCA Data is {lcs_node.data}')
    else:
        print(f'No LCS found')

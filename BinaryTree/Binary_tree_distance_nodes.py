from node import Node 




def LCA(root, node_1, node_2):
    if not root:
        return None
    
    if root.data == node_1.data or root.data == node_2.data:
        return root
    

    left = LCA(root.left, node_1, node_2)
    right = LCA(root.right, node_1, node_2)

    if left and right:
        return root

    return left if left else right


""""
Alternative solution fod distance is 
D(n1,n2) = D(root, n1) + D(root, n2) - 2 * D(root, lca)
"""

def Distance(lca, node):
    if not lca:
        return None
    
    if lca.data == node.data:
        return 0
    
    left = Distance(lca.left, node)
    l = 1 + left if left is not None else None

    right = Distance(lca.right, node)
    r = 1 + right if right is not None else None

    return l if l else r




if __name__ == '__main__':
    
    # Construct Tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.left.right = Node(8)
    root.right.right = Node(7)


    lca_node = LCA(root, root.left.left, root.left.right)

    if not lca_node:
        print('No Distance exist')
    else:
        one = Distance(lca_node, root.left.left)
        two = Distance(lca_node, root.left.right)
        if one and two:
            print(f'Distance is {one + two}')
        else:
            print('Distance not exist')
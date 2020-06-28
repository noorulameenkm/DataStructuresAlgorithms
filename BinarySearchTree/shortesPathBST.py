from node import Node 


def LCA(root, node_1, node_2):
    if not root:
        return None
    
    if root.data == node_1.data or root.data == node_2.data or (node_1.data < root.data and node_2.data > root.data) or (node_1.data > root.data and node_2.data < root.data):
        return root
    

    if node_1.data < root.data:
       return LCA(root.left, node_1, node_2)
    
    return LCA(root.right, node_1, node_2)



""""
Alternative solution fod distance is 
D(n1,n2) = D(root, n1) + D(root, n2) - 2 * D(root, lca)
"""

def Distance(lca, node):
    if not lca:
        return None
    
    if lca.data == node.data:
        return 0
    
    if node.data < lca.data:
        d = Distance(lca.left, node)
        d = 1 + d if d is not None else None
        return d
    
    d = Distance(lca.right, node)
    d = 1 + d if d is not None else None
    return d
    



if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.left.right.left = Node(6)
    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(17)


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
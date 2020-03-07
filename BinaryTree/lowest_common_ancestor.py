from node import Node

def LCA(root, node1, node2):
    if not root:
        return None
    
    if root == node1 or root == node2:
        return root
    
    left = LCA(root.left, node1, node2)
    right = LCA(root.right, node1, node2)

    if left and right:
        return root
    
    return left if left else right


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)

    lca_node = LCA(root, root.right.left, root.right.right)

    if lca_node:
        print(lca_node.data)
    else:
        print('No Node')
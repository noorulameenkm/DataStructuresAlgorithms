from node import Node



def isQuasiIsomorphic(root1, root2):
    if not root1 and not root2:
        return True
    if (not root1 and root2) or (root1 and not root2):
        return False
    return (isQuasiIsomorphic(root1.left, root2.left) and isQuasiIsomorphic(root1.right, root2.right)) or (isQuasiIsomorphic(root1.left, root2.right) and isQuasiIsomorphic(root1.right, root2.left))
            


if __name__ == '__main__':

    # tree_1
    root_1 = Node(1)
    root_1.left = Node(2)
    root_1.right = Node(3)
    root_1.left.left = Node(4)
    root_1.left.right = Node(5)
    root_1.left.right.left = Node(7)
    root_1.right.left = Node(6)
    root_1.right.left.left = Node(8)

    # tree_2
    root_2 = Node(1)
    root_2.left = Node(5)
    root_2.left.left = Node(3)
    root_2.left.left.right = Node(7)
    root_2.right = Node(6)
    root_2.right.left = Node(8)
    root_2.right.left.left = Node(4)
    root_2.right.right = Node(2)

    if isQuasiIsomorphic(root_1, root_2):
        print("Trees are quasi isomorphic");
    else:
        print("Trees are not quasi isomorphic");
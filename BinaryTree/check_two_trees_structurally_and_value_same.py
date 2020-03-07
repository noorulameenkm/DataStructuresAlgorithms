from node import Node 




def is_trees_same(root1, root2):
    
    # if root1 and root2 are None then return True
    if not root1 and not root2:
        return True
    
    # if either of the root in None and the other is not None
    # then return False
    if (not root1 and root2) or (root1 and not root2):
        return False
    
    # if 2 root's aren't None, then check the value
    # if values aren't same then return False
    if root1.data != root2.data:
        return False
    
    # if the values are same return the recursive of the 
    # function with root1.left, root2.right and root1.right and root2.left
    return is_trees_same(root1.left, root2.right) and is_trees_same(root1.right, root2.left)



if __name__ == '__main__':

    # tree_1
    root1 = Node(10)
    root1.left = Node(20)
    root1.right = Node(3)
    root1.left.left = Node(9)
    root1.left.right = Node(12)

    # tree_2
    root2 = Node(10)
    root2.left = Node(3)
    root2.right = Node(20)
    root2.right.left = Node(12)
    root2.right.right = Node(9)

    if is_trees_same(root1, root2):
        print('Trees are Same')
    else:
        print('Trees are not same')

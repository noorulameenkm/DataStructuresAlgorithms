class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


"""
    Time complexity - O(n)
    Space Complexity - O(n)
"""
def lowest_common_ancestor(root, a, b):
    stack = []
    stack.append(root)
    parents = {root: None}

    while a not in parents or b not in parents:
        node = stack.pop()

        for child in node.children:
            parents[child] = node
            stack.append(child)
        
    ancestors = set()

    while a:
        ancestors.add(a)
        a = parents[a]
    
    while b not in ancestors:
        b = parents[b]
    
    return b.val



# Driver Code

root = TreeNode(1)
root.children.append(TreeNode(2))
root.children.append(TreeNode(3))
root.children.append(TreeNode(4)) 
root.children[0].children.append(TreeNode(5)) 
root.children[0].children[0].children.append(TreeNode(10)) 
root.children[0].children.append(TreeNode(6)) 
root.children[0].children[1].children.append(TreeNode(11))
root.children[0].children[1].children.append(TreeNode(12))
root.children[0].children[1].children.append(TreeNode(13)) 
root.children[2].children.append(TreeNode(7))
root.children[2].children.append(TreeNode(8))
root.children[2].children.append(TreeNode(9))

a = root.children[0].children[1].children[2]
b = root.children[0].children[0].children[0]
LCA = lowest_common_ancestor(root, a, b)
print("\"", LCA, "\"", "is the lowest common ancestor of the nodes", "\"", a.val, "\"", "and", "\"", b.val, "\"")
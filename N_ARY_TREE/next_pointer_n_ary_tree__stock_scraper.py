from calendar import c


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.children = []



"""
    Time Complexity - O(n)
    Space Complexity - O(n)
"""
def traversing_dom_tree(root):
    if not root:
        return root
    

    def process_child(child_node, prev, leftmost):
        if prev:
            prev.next = child_node
        else:
            leftmost = child_node

        prev = child_node
        return prev, leftmost
    
    leftmost = root
    while leftmost:

        prev, curr = None, leftmost

        leftmost = None

        while curr:
            print(curr.val)
            for child in curr.children:
                prev, leftmost = process_child(child, prev, leftmost)

            curr = curr.next
    
    return root




root = TreeNode("body")
root.children.append(TreeNode("div"))
root.children.append(TreeNode("h1"))
root.children.append(TreeNode("div")) 
root.children[0].children.append(TreeNode("h2")) 
root.children[0].children[0].children.append(TreeNode("ul")) 
root.children[0].children.append(TreeNode("h3")) 
root.children[0].children[1].children.append(TreeNode("a"))
root.children[0].children[1].children.append(TreeNode("p"))
root.children[0].children[1].children.append(TreeNode("table")) 
root.children[2].children.append(TreeNode("p"))
root.children[2].children.append(TreeNode("a"))
root.children[2].children.append(TreeNode("p"))

res = traversing_dom_tree(root)
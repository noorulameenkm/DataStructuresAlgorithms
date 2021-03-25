def visible_tree_node(root):
    count = findVisibleNodes(root, None)
    return count


def findVisibleNodes(root, maxVal):
    count = 0

    if not root:
        return 0
    
    if maxVal is None or root.val >= maxVal:
        count += 1
    
    maxVal = root.val if maxVal is None else max(maxVal, root.val)
    count_left = findVisibleNodes(root.left, maxVal)
    count_right = findVisibleNodes(root.right, maxVal)

    return count + count_left + count_right


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes):
    val = next(nodes)
    if not val or val == 'x': return
    cur = Node(int(val))
    cur.left = build_tree(nodes)
    cur.right = build_tree(nodes)
    return cur


if __name__ == '__main__':
    ## Driver Code
    inputs = ["5 4 3 x x 8 x x 6 x x", "-100 x -500 x -50 x x", "9 8 11 x x 20 x x 6 x x"]
    for i in range(len(inputs)):
        root = build_tree(iter(inputs[i].split()))
        print("Visible tree node :",visible_tree_node(root))
    

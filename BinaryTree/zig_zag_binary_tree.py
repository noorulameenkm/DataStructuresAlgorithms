from node import Node


def print_zigzag(root):
    if not root:
        return
    
    left_to_right = True
    current_level = [root]
    next_level = []
    while len(current_level) > 0:
        current_node = current_level.pop(0)

        print(current_node.data, end = ' ')

        if left_to_right:
            if current_node.left:
                next_level.insert(0, current_node.left)
            if current_node.right:
                next_level.insert(0, current_node.right)   
        else:
            if current_node.right:
                next_level.insert(0, current_node.right)
            if current_node.left:
                next_level.insert(0, current_node.left)
        
        if len(current_level) == 0:
            left_to_right = not left_to_right
            current_level = next_level
            next_level = []
    

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    print_zigzag(root)
    print('\n', end = '')
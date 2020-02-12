class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findTheMaxSumLevel(root):
    if not root:
        return -1
    
    max_sum = 0
    level = 0
    sum_ = 0
    queue = [root, '$']
    while len(queue) > 0:
        node = queue.pop(0)

        if node == '$':
            if sum_ > max_sum:
                max_sum = sum_
                max_level = level
            
            sum_ = 0
            level += 1
            if len(queue) > 0:
                queue.append('$')
        
        else:
            sum_ = sum_ + node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    return max_level

def Main():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left = Node(11)
    root.right.right = Node(12)
    root.left.left.left = Node(21)
    root.left.left.right = Node(20)
    root.left.right.left = Node(61)
    root.left.right.right = Node(65)
    level_ = findTheMaxSumLevel(root)
    print(level_)


if __name__ == '__main__':
    Main()
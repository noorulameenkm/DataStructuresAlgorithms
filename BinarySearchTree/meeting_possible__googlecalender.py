class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


"""
    Time complexity - O(n ^ 2) in the worst case, O(n * logn) if we use self-balancing binary tree
    Space complexity - O(n)
"""
class BinarySearchTree:
    def __init__(self):
        self.root = None
    

    def insert_node(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        
        return self.add_node(self.root, Node(start, end))
    
    def add_node(self, current_node, new_node):
        
        if new_node.start >= current_node.end:
            if current_node.right is None:
                current_node.right = new_node
                return True
            return self.add_node(current_node.right, new_node)
        elif new_node.end <= current_node.start:
            if current_node.left is None:
                current_node.left = new_node
                return True
            return self.add_node(current_node.left, new_node)
        else:
            return False
    

def check_meeting(meeting_times, new_meeting):
    tree = BinarySearchTree()
    for meeting in meeting_times:
        tree.insert_node(meeting[0], meeting[1])
    
    return tree.insert_node(new_meeting[0], new_meeting[1])



meeting_times = [[1, 3], [4, 6], [8, 10], [10, 12], [13, 15]]
new_meeting = [7, 8]
print(check_meeting(meeting_times, new_meeting))
new_meeting = [9, 11]
print(check_meeting(meeting_times, new_meeting))
from Graph import Graph
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}


# Time Complexity - O(V + E)
def is_tree(g):

    visited = [False] * g.vertices

    if check_cycle(g, 0, visited, -1) is True:
        return False
    
    for i in range(len(visited)):
        if visited[i] is False:
            return False
        
    return True


def check_cycle(g, node, visited, parent):
    visited[node] = True

    adjacent = g.array[node].head_node
    while adjacent is not None:
        if visited[adjacent.data] is False:
            if check_cycle(g, adjacent.data, visited, node) is True:
                return True
        elif adjacent.data is not parent:
            return True
        
        adjacent = adjacent.next_element
    
    return False


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)


print(is_tree(g))
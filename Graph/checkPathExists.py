from Graph import Graph
from collections import deque
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}


def check_path(g, source, destination):
    queue = deque()
    visited = [False] * g.vertices
    queue.append(source)
    visited[source] = True
    while queue:
        node = queue.popleft()
        if node is destination:
            return True
        temp = g.array[node].head_node
        while temp is not None:
            if visited[temp.data] is False:
                queue.append(temp.data)
                visited[temp.data] = True

            temp = temp.next_element
    
    return False

# Make helper functions here


g1 = Graph(9)
g1.add_edge(0, 2)
g1.add_edge(0, 5)
g1.add_edge(2, 3)
g1.add_edge(2, 4)
g1.add_edge(5, 3)
g1.add_edge(5, 6)
g1.add_edge(3, 6)
g1.add_edge(6, 7)
g1.add_edge(6, 8)
g1.add_edge(6, 4)
g1.add_edge(7, 8)
g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(2, 3)

print(check_path(g1, 0, 7))
print(check_path(g2, 3, 0))
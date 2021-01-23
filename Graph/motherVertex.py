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


"""
Time Complexity - O(v(v + E))
"""
def find_mother_vertex(g):
    # Write - Your - Code
    number_of_vertices_reached = 0
    for i in range(g.vertices):
        number_of_vertices_reached = performBFS(g, i)
        if (number_of_vertices_reached is g.vertices):
            return i

    return -1

# Create helper functions here
def performBFS(g, source):
    visited = [False] * g.vertices
    stack = deque()
    stack.appendleft(source)
    visited[source] = True
    number_of_vertices_reached = 0

    while stack:
        current = stack.popleft()
        head = g.array[current].head_node
        while head is not None:
            if visited[head.data] is False:
                stack.appendleft(head.data)
                visited[head.data] = True
                number_of_vertices_reached += 1
            head = head.next_element
        
    return number_of_vertices_reached + 1


"""
 Time complexity - O(V + E)
"""
def find_mother_vertex2(graph):
    visited = [False] * graph.vertices

    last_v = 0

    for i in range(g.vertices):
        if visited[i] is False:
            perform_DFS(graph, i, visited)
            last_v = i

    visited = [False] * graph.vertices
    perform_DFS(graph, last_v, visited)
    if any(i is False for i in visited):
        return -1
    else:
        return last_v


def perform_DFS(graph, node, visited):

    visited[node] = True
    temp = graph.array[node].head_node

    while temp is not None:
        if visited[temp.data] is False:
            perform_DFS(graph, temp.data, visited)
        
        temp = temp.next_element


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 0)
g.add_edge(3, 1)
print(find_mother_vertex(g))
print(find_mother_vertex2(g))
from Graph import Graph
from collections import deque

def find_min(g, a, b):
    result = 0
    num_of_vertices = g.vertices
    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you enqueue it into queue
    visited = [False] * num_of_vertices

    # For keeping track of distance of current_node from source
    distance = [0] * num_of_vertices

    # Create Queue for Breadth First Traversal and enqueue source in it
    queue = deque()
    queue.append(a)
    visited[a] = True
    # Traverse while queue is not empty
    while queue:
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.popleft()
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        # and also update their distance from `a`
        # by adding 1 in current_nodes's distance
        temp = g.array[current_node].head_node
        while (temp is not None):
            if (not visited[temp.data]) or (temp.data is b):
                queue.append(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1
                if temp.data is b:
                    return distance[b]
            temp = temp.next_element
    # end of while
    return -1



g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)
print(find_min(g, 1, 5))

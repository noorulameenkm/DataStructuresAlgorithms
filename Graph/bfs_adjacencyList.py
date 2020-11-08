from Graph import Graph
from collections import deque


def bfs_traversal_helper(g, source, visited):
    queue = deque()
    queue.append(source)
    result = ""
    visited[source] = True
    while queue:
        current = queue.popleft()
        result += str(current)

        head = g.array[current].head_node

        while head is not None:
            if visited[head.data] is False:
                visited[head.data] = True
                queue.append(head.data)
            head = head.next_element

    return result, visited



"""
Time Complexity - O(V + E)
"""

def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    
    visited = [False for i in range(num_of_vertices)]
    # Write - Your - Code
    # For the above graph, it should return "01234" or "02143" etc    
    result, visited = bfs_traversal_helper(g, source, visited)
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new

    return result
        

def main():
    graph = Graph(5)

    # Add edge
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    result = bfs_traversal(graph, 0)
    print(result)


main()
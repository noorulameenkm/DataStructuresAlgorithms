from Graph import Graph
from collections import deque


def dfs_traversal_helper(g, source, visited):
    queue = deque()
    queue.appendleft(source)
    result = ""
    visited[source] = True
    while queue:
        current = queue.popleft()
        result += str(current)

        head = g.array[current].head_node

        while head is not None:
            if visited[head.data] is False:
                visited[head.data] = True
                queue.appendleft(head.data)
            head = head.next_element

    return result, visited



"""
Time Complexity - O(V + E)
"""

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    
    visited = [False for i in range(num_of_vertices)]
    # Write - Your - Code
    # For the above graph, it should return "01234" or "02143" etc    
    result, visited = dfs_traversal_helper(g, source, visited)
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new

    return result
        

def main():
    graph = Graph(7)

    # Add edge
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)

    result = dfs_traversal(graph, 1)
    print(result)


main()
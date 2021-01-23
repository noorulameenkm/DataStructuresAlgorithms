from Graph import Graph



"""
Time Complexity - O(V + E)
"""
def detectCycle(graph):
    visited = [False] * graph.vertices
    rec_node_stack = [False] * graph.vertices

    for node in range(graph.vertices):
        if detect_cycle_rec(graph, node, visited, rec_node_stack):
            return True
        
    return False


def detect_cycle_rec(graph, node, visited, rec_node_stack):
    if rec_node_stack[node]:
        return True
    
    if visited[node]:
        return False
    
    rec_node_stack[node] = True
    visited[node] = True

    head_node = graph.array[node].head_node
    while head_node is not None:
        adjacent = head_node.data
        if detect_cycle_rec(graph, adjacent, visited, rec_node_stack):
            return True
        
        head_node = head_node.next_element
    
    rec_node_stack[node] = False
    return False



g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(3, 0)
g2 = Graph(3)
g2.add_edge(0, 1)
g2.add_edge(1, 2)

print(detectCycle(g1))
print(detectCycle(g2))


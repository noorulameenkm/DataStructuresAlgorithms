from Graph import Graph
def remove_edge(graph, source, destination):
    """
    A function to remove an edge
    :param graph: A graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """

    # Write your code here!
    g = graph.array
    source_head = g[source].head_node
    if source_head is None:
        return
    
    if source_head.data == destination:
        g[source].head_node = source_head.next_element
        return
    
    prev = None
    while source_head is not None and source_head.data != destination:
        prev = source_head
        source_head = source_head.next_element
    
    if source_head is None:
        return
    
    next_ = source_head.next_element
    prev.next_element = next_
    


def main():
    graph = Graph(7)

    # Add edge
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)

    print('----------------------Before deleting edge---------------------------')
    graph.print_graph()
    remove_edge(graph, 1, 3)
    print('----------------------After deleting edge---------------------------')
    graph.print_graph()


main()
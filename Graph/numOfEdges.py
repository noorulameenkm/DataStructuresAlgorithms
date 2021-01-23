from Graph import Graph



# Time complexity - O(V + E)
def number_of_edges(g):
    sum_ = 0
    for i in range(g.vertices):
        temp = g.array[i].head_node
        while temp is not None:
            sum_ += 1
            temp = temp.next_element

    return sum_


# Time Complexity - O(V + E)
def number_of_edges2(graph):
    return sum([graph.array[i].length() for i in range(g.vertices)])




g = Graph(9)
g.add_edge(0, 2)
g.add_edge(0, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(6, 7)
g.add_edge(6, 8)
g.add_edge(6, 4)
g.add_edge(7, 8)



g2 = Graph(7)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(3, 4)
g2.add_edge(3, 5)
g2.add_edge(2, 5)
g2.add_edge(2, 4)
g2.add_edge(4, 6)
g2.add_edge(4, 5)
g2.add_edge(6, 5)


# First Approach
print(number_of_edges(g))
print(number_of_edges(g2))

# Second Approach
print(number_of_edges(g))
print(number_of_edges(g2))


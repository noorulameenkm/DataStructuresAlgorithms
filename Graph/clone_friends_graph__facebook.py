from random import shuffle
from collections import defaultdict

"""
Time Complexity - O(n), n -> number of vertices
Space Complexity - O(n)
"""

class Node:
    def __init__(self, d):
        self.data = d
        self.friends = []


# this is un-directed graph i.e.
# if there is an edge from x to y
# that means there must be an edge from y to x
# and there is no edge from a node to itself
# hence there can maximum of (nodes * nodes - nodes) / 2 edges in this graph

def create_test_graph_directed(nodes_count, edges_count):
    vertices = []
    for i in range(0, nodes_count):
        vertices += [Node(i)]

    all_edges = []
    for i in range(0, edges_count):
        for j in range(i + 1, nodes_count):
            all_edges.append((i, j))

    shuffle(all_edges)

    for i in range(min(edges_count, len(all_edges))):
        edge = all_edges[i]
        vertices[edge[0]].friends += [vertices[edge[1]]]
        vertices[edge[1]].friends += [vertices[edge[0]]]

    return vertices

def clone_rec(root, nodes_completed):
    if root == None:
        return None

    new_node = Node(root.data)
    nodes_completed[root] = new_node

    for friend in root.friends:
        x = nodes_completed.get(friend)
        if x == None:
            new_node.friends += [clone_rec(friend, nodes_completed)]
        else:
            new_node.friends += [x]
    return new_node

def clone(root):
    nodes_completed = defaultdict(None)
    new_root = clone_rec(root, nodes_completed)
    return new_root

def print_graph_rec(root, visited_nodes):
  if root == None or root in visited_nodes:
    return

  visited_nodes.add(root)

  print(str(root.data), end = ": {")
  for n in root.friends:
    print(str(n.data), end = " ")
  print("}")

  for n in root.friends:
    print_graph_rec(n, visited_nodes)

def print_graph(root):
  visited_nodes = set()
  print_graph_rec(root, visited_nodes)

vertices = create_test_graph_directed(7, 18)
print_graph(vertices[0])
cp = clone(vertices[0])

print("\nAfter copy.")
print_graph(cp)

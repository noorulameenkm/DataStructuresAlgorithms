from collections import deque

"""
Time Complexity = O(V+E) where V ->  number of vertices and E -> number of edges
Space Complexity = O(V+E) where V ->  number of vertices and E -> number of edges
"""

def isDAGHasCycle(vertices, edges):
  sortedOrder = []
  if vertices <= 0:
      return False

  # a. initialize the graph
  in_degrees = { i: 0 for i in range(vertices)} # count of incoming edges
  graph = { i: [] for i in range(vertices) } # adjacency list graph

  # b. build the graph
  for edge in edges:
      parent, child = edge[0], edge[1]
      graph[edge[0]].append(edge[1]) # put the child into it's parent's list
      in_degrees[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for vertex, degrees in in_degrees.items():
      if degrees == 0:
            sources.append(vertex)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
      source = sources.popleft()
      childs = graph[source] # get the node's children to decrement their in-degrees
      for child in childs:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                  sources.append(child)
      sortedOrder.append(source)

  # topological sort is not possible as the graph has a cycle
  if len(sortedOrder) != vertices: # topological sort is not possible as the graph has a cycle
    return True
   
  return False


def main():
  print("Topological sort: " +
        str(isDAGHasCycle(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(isDAGHasCycle(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(isDAGHasCycle(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()

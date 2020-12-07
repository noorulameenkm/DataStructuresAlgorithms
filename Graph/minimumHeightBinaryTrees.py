from collections import deque


"""
Time Complexity - O(V + E)
Space Complexity - O(V + E)
"""
def find_trees(nodes, edges):
      if nodes <= 0:
          return []
      
      # with only one node, since its in-degrees will be 0, therefore, we need to handle it separately
      if nodes == 1:
          return [0]
      
      # a. Initialize the graph
      graph = {  i: [] for i in range(nodes) }
      in_degrees = { i: 0 for i in range(nodes) }

      # b. build the graph
      for edge in edges:
          node1, node2 = edge
          # increment the in-degrees of both the nodes
          in_degrees[node2] += 1
          in_degrees[node1] += 1
          # since this is an undirected graph, therefore, add a link for both the nodes
          graph[node1].append(node2)
          graph[node2].append(node1)
      
      leaves = deque()
      # c. Find all leaves i.e., all nodes with 0 in-degrees
      for key in in_degrees:
          if in_degrees[key] == 1:
              leaves.append(key)

      
      # d. Remove leaves level by level and subtract each leave's children's in-degrees.
      # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
      # Any node that has already been a leaf cannot be the root of a minimum height tree, because
      # its adjacent non-leaf node will always be a better candidate.
      totalNodes = nodes
      while totalNodes > 2:
          leavesize = len(leaves)
          totalNodes -= leavesize
          for i in range(leavesize):
              vertex = leaves.popleft()
              # get the node's children to decrement their in-degrees
              childs = graph[vertex]
              for child in childs:
                  in_degrees[child] -= 1
                  if in_degrees[child] == 1:
                        leaves.append(child)
      
      return list(leaves)



def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))


main()

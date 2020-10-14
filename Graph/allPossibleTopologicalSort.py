from collections import deque

"""
Time Complexity - O(V!∗E)
Space Complexity - O(V!∗E)
"""

def print_orders(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return False
  
  in_degree = { i: 0 for i in range(tasks) }
  graph = { i: [] for i in range(tasks) }

  for prerequisite in prerequisites:
    task_1, task_2 = prerequisite

    graph[task_1].append(task_2)
    in_degree[task_2] += 1

  sources = deque() 
  for task, degree in in_degree.items():
    if degree == 0:
      sources.append(task)

  print_all_topological_sort(graph, in_degree, sources, sortedOrder)



def print_all_topological_sort(graph, in_degree, sources, sortedOrder):
  if sources:
    for vertex in sources:
      sortedOrder.append(vertex) 
      sourceForNextCall = deque(sources) # make a copy of sources
      # only remove the current source, all other sources should remain in the queue for the next call
      sourceForNextCall.remove(vertex)
      # get the node's children to decrement their in-degrees
      for child in graph[vertex]:
        in_degree[child] -= 1
        if in_degree[child] == 0:
          sourceForNextCall.append(child)
      # recursive call to print other orderings from the remaining (and new) sources
      print_all_topological_sort(graph, in_degree, sourceForNextCall, sortedOrder)

      # backtrack, remove the vertex from the sorted order and put all of its children back to consider
      # the next source instead of the current vertex
      sortedOrder.remove(vertex)
      for child in graph[vertex]:
        in_degree[child] += 1
      
  if len(sortedOrder) == len(in_degree):
    print(sortedOrder)



def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()

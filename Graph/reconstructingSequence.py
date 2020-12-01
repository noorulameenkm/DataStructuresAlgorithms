from collections import deque

"""
Time Complexity - O(V + N)
Space Complexity - O(V + N)
"""
def can_construct(originalSeq, sequences):
      if len(originalSeq) <= 0:
            return False
      
      sortedOrder = []

      # a. Initialize the graph
      graph = {} # count of incoming edges
      in_degrees = {} # adjacency list graph
      for sequence in sequences:
            for num in sequence:
                  graph[num] = []
                  in_degrees[num] = 0
      
      # b. Build the graph
      for sequence in sequences:
            for i in range(len(sequence) - 1):
                  parent, child = sequence[i], sequence[i + 1]
                  graph[parent].append(child)
                  in_degrees[child] += 1

      # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
      if len(originalSeq) != len(in_degrees):
            return False
      
      # c. Find all sources i.e., all vertices with 0 in-degrees
      sources = deque()
      for s, count in in_degrees.items():
            if count == 0:
                  sources.append(s)
      
      # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
      # if a child's in-degree becomes zero, add it to the sources queue
      while sources:
            if len(sources) > 1:
                  return False # more than one sources mean, there is more than one way to reconstruct the sequence
            
            if originalSeq[len(sortedOrder)] != sources[0]:
                  return False # the next source(or number) is different from the original sequence
            
            source = sources.popleft()
            childs = graph[source]
            for child in childs: # get the node's children to decrement their in-degrees
                  in_degrees[child] -= 1
                  if in_degrees[child] == 0:
                        sources.append(child)
            
            sortedOrder.append(source)
      
      # if sortedOrder's size is not equal to original sequence's size, there is no unique way to construct
      return len(originalSeq) == len(sortedOrder)


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()

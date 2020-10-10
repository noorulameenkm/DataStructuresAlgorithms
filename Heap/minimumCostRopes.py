from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
  result = []
  # TODO: Write your code here
  minHeap = []
  for i in range(len(ropeLengths)):
    heappush(minHeap, ropeLengths[i])

  # go through the values of the heap, in each step take top (lowest) rope lengths from the min heap
  # connect them and push the result back to the min heap.
  # keep doing this until the heap is left with only one rope
  result = temp = 0
  while len(minHeap) > 1:
    temp = heappop(minHeap) + heappop(minHeap)
    result += temp
    heappush(minHeap, temp )
      
  return result


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()


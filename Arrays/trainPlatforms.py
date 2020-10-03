from heapq import *


class Train:
  def __init__(self, start, end):
    self.start = start
    self.end = end
  
  def __lt__(self, train):
    return self.end < train.end

def min_platforms(trains):
  trains.sort(key=lambda x: x.start)

  minRooms = 0
  minHeap = []
  for train in trains:

    while len(minHeap) > 0 and train.start >= minHeap[0].end:
      heappop(minHeap)

    heappush(minHeap, train)
    minRooms = max(minRooms, len(minHeap))
  
  return minRooms


def main():
  print("Minimum meeting rooms required: " + str(min_platforms(
    [Train(4, 5), Train(2, 3), Train(2, 4), Train(3, 5)])))
  print("Minimum meeting rooms required: " +
        str(min_platforms([Train(1, 4), Train(2, 5), Train(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_platforms([Train(6, 7), Train(2, 4), Train(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_platforms([Train(1, 4), Train(2, 3), Train(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_platforms(
    [Train(4, 5), Train(2, 3), Train(2, 4), Train(3, 5)])))


main()


# Given a list of intervals, find the point where the maximum number of intervals overlap.

from heapq import *

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


"""
Time Complexity - O(NlogN)
Space complexity - O(N)
"""

def find_next_interval(intervals):
  result = [-1 for _ in range(len(intervals))]

  maxStartHeap, maxEndHeap = [], []
  for i in range(len(intervals)):
    heappush(maxStartHeap, (-intervals[i].start, i))
    heappush(maxEndHeap, (-intervals[i].end, i))

  # go through all the intervals to find each interval's next interval
  for _ in range(len(intervals)):
    # let's find the next interval of the interval which has the highest 'end'
    topEnd, endIndex = heappop(maxEndHeap)
    if -maxStartHeap[0][0] >= -topEnd:
      topStart, startIndex = heappop(maxStartHeap)

      # find the the interval that has the closest 'start'
      while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
        topStart, startIndex = heappop(maxStartHeap)
      
      result[endIndex] = startIndex
      # put the interval back as it could be the next interval of other intervals
      heappush(maxStartHeap, (topStart, startIndex))

  
  return result


def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(5, 6), Interval(1, 5), Interval(7,8)])
  print("Next interval indices are: " + str(result))


main()

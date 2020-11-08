from heapq import *


"""
Time Complexity - O(N * logN)
Space Complexity - O(N)
"""

def schedule_tasks(tasks, k):
  intervalCount = 0
  # TODO: Write your code here
  frequency, maxHeap = {}, []
  for task in tasks:
    frequency[task] = frequency.get(task, 0) + 1

  for char, count in frequency.items():
    heappush(maxHeap, (-count, char))

  
  intervalCount = 0
  while maxHeap:
    waitingList = []
    n = k + 1

    while n > 0 and maxHeap:
      count, char = heappop(maxHeap)
      intervalCount += 1

      if -count > 1:
        waitingList.append((count + 1, char))


      n -= 1
    
    
    for item in waitingList:
      heappush(maxHeap, item)

    if maxHeap:
      intervalCount += n

  
  return intervalCount

  

  return intervalCount


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()


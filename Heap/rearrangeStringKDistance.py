from heapq import *
from collections import deque


"""
Time Complexity - O(N * logN)
Space Complexity - O(N)
"""

def reorganize_string(str_, k):
  frequency_ = {}
  for character in str_:
    frequency_[character] = frequency_.get(character, 0) + 1

  maxHeap = []

  for char, frequency in frequency_.items():
    heappush(maxHeap, (-frequency, char))

  result = ""
  queue = deque()
  while maxHeap:
    frequency, character = heappop(maxHeap)

    result += character
    queue.append((frequency + 1, character))

    if len(queue) == k:
      frequency, character = queue.popleft()
      if -frequency > 0:
        heappush(maxHeap, (frequency, character))

  
  return result if len(result) == len(str_) else ""


def main():
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()

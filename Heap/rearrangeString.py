from heapq import *


"""
Time Complexity - O(N * logN)
Space Complexity - O(N)
"""

def rearrange_string(str_):
  # TODO: Write your code here
  maxHeap, frequency = [], {}
  for s in str_:
    frequency[s] = frequency.get(s, 0) + 1
  
  result = ""
  for s, frequency in frequency.items():
    heappush(maxHeap, (-frequency, s))

  prevChar, prevFrequency = None, 0

  while maxHeap:

    frequency, char = heappop(maxHeap)

    if prevChar and -prevFrequency > 0:
      heappush(maxHeap, (prevFrequency, prevChar))
    
    result += char
    prevChar = char
    prevFrequency = frequency + 1

  
  return result if len(str_) == len(result) else ""


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()


from heapq import *
from collections import Counter


def rearrange_string2(s):
  frequency = Counter(s).most_common()
  n = len(s)
  for _, val in frequency:
    if val > ((n + 1) // 2):
      return ""
  
  sorted_dict = dict(sorted(frequency, key= lambda x: x[1], reverse=True))
  
  
  res = [""] * n
  p = n
  while p > 0:

    i = 0
    while i < n and res[i] != "":
      i += 1

    for key, val in sorted_dict.items():
      while i < n and val > 0:
        res[i] += key
        i += 2
        val -= 1
        p -= 1
      
      sorted_dict[key] = val
    
  return "".join(res)
    



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
  print("First Logic ---------")
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))

  print("Second Logic -------")
  print("Rearranged string:  " + rearrange_string2("aappp"))
  print("Rearranged string:  " + rearrange_string2("Programming"))
  print("Rearranged string:  " + rearrange_string2("aapa"))


main()


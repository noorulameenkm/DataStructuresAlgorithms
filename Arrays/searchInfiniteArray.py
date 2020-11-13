import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


"""
Time complexity - O(logN + logN) -> logN
Space Complexity - O(1)
"""

def search_in_infinite_array(reader, key):
  start, end = 0, 1
  while reader.get(end) < key:
    newStart = end + 1
    end += (end - start + 1) * 2
    start = newStart
  return binary_search(reader, key, start, end)


"""
Time complexity - O(logN)
"""

def binary_search(reader, key, start, end):
  while start <= end:
    mid = start + (end - start) // 2
    if key > reader.get(mid):
      start = mid + 1
    elif key < reader.get(mid):
      end = mid - 1
    else:
      return mid
  
  return -1

def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()








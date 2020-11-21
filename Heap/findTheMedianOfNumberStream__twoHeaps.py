from heapq import *
class MedianOfAStream:
  minheap = [] # to store the smallest values in the left hand side of the number
  maxheap = [] # to store the largest values in the right hand side of the array

  # Time complexity - O(logN)
  # Space complexity - O(N)
  def insert_num(self, num):
    if not self.maxheap or  num <= -self.maxheap[0]:
      heappush(self.maxheap, -num)
    else:
      heappush(self.minheap, num)

    # either both the heaps will have equal number of elements or max-heap will have one
    # more element than the min-heap
    if len(self.maxheap) > len(self.minheap) + 1:
      heappush(self.minheap, -heappop(self.maxheap))
    elif len(self.minheap) > len(self.maxheap):
      heappush(self.maxheap, -heappop(self.minheap))

  # Time complexity - O(1)
  def find_median(self):
    if len(self.maxheap) == len(self.minheap):
       # we have even number of elements, take the average of middle two elements
      return (-self.maxheap[0] + self.minheap[0]) / 2.0
    
    # because max-heap will have one more element than the min-heap
    return -self.maxheap[0] / 1.0


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()

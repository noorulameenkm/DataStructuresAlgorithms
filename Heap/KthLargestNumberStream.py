from heapq import *

class KthLargestNumberInStream:
  def __init__(self, nums, k):
    # TODO: Write your code here
    self.k = k
    self.minHeap = []

    for num in nums:
      self.add(num)


  def add(self, num):
    # TODO: Write your code here
    heappush(self.minHeap, num)

    if len(self.minHeap) > self.k:
      heappop(self.minHeap)


    return self.minHeap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()


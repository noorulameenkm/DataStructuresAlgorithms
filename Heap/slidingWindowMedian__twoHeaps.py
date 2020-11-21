from heapq import *
class SlidingWindowMedian:

  def __init__(self):
    self.minheap = []
    self.maxheap = []

  """
  Time Complexity - O(N * K)
  Space Complexity - O(K)
  """
  
  def find_sliding_window_median(self, nums, k):
    result = [0.0 for i in range(len(nums) - k + 1)]
    for end in range(len(nums)):
      num = nums[end]
      if not self.maxheap or num <= -self.maxheap[0]:
        heappush(self.maxheap, -num)
      else:
        heappush(self.minheap, num)

      self.rebalance_heap()

      if end - k + 1 >= 0:
        remNumber = nums[end - k + 1]


        if len(self.minheap) == len(self.maxheap):
          result[end - k + 1] = (-self.maxheap[0] + self.minheap[0]) / 2.0
        else:
          result[end - k + 1] = -self.maxheap[0] / 1.0

        if remNumber <= -self.maxheap[0]:
          self.remove(self.maxheap, -remNumber)
        else:
          self.remove(self.minheap, remNumber)
        
        self.rebalance_heap()
      
    return result

  def rebalance_heap(self):
    if len(self.maxheap) > len(self.minheap) + 1:
      heappush(self.minheap, -heappop(self.maxheap))
    elif len(self.minheap) > len(self.maxheap):
      heappush(self.maxheap, -heappop(self.minheap))

  # removes an element from the heap keeping the heap property
  def remove(self, heap, number):
    idx = heap.index(number) # find the element
    # move the element to the end and delete it
    heap[idx] = heap[-1]
    del heap[-1]
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if idx < len(heap):
      heapify(heap)
      """
      # Can do this as well, but before that understand it clearly
      heapq._siftup(heap, ind)
      heapq._siftdown(heap, 0, ind)
      """
      

 
def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

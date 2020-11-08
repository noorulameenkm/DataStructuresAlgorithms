from heapq import *

"""
Time Complexity - O(K * logM) - where N is the total number of elements across all the lists
Space Complexity - O(M) where M is the number of lists available in
"""

def find_Kth_smallest(lists, k):
  number = -1
  minHeap = []
  # put the 1st element of each list in the min heap
  for i in range(len(lists)):
    heappush(minHeap, (lists[i][0], 0, lists[i]))

  numberCount = 1
  while minHeap:
    number, i, list_ = heappop(minHeap)

    # if we have selected 'k' small numbers, bereak out of the loop
    if numberCount == k:
      break
    
    # Increment the counter
    numberCount += 1

    # The array has more elements, then add that number
    if i + 1 < len(list_):
      heappush(minHeap, (list_[i + 1], i + 1, list_))
  
  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()



"""
Problem 1: Given ‘M’ sorted arrays, find the median number among all arrays.

Solution: This problem is similar to our parent problem with K=Median. So if there are ‘N’ total numbers in all the arrays we need to find the K’th minimum number where K=N/2K=N/2.

Problem 2: Given a list of ‘K’ sorted arrays, merge them into one sorted list.

Solution: This problem is similar to Merge K Sorted Lists except that the input is a list of arrays compared to LinkedLists. To handle this, we can use a similar approach as discussed in our parent problem by keeping a track of the array and the element indices.

"""


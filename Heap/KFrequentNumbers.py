from heapq import *

def find_k_frequent_numbers(nums, k):
  topNumbers = []
  # TODO: Write your code here
  frequency = {}
  for num in nums:
    if num not in frequency:
      frequency[num] = 0
    frequency[num] += 1

  minHeap = []
  for num, frequency in frequency.items():
    heappush(minHeap, (frequency, num))
    if len(minHeap) > k:
      heappop(minHeap)

  for i in range(len(minHeap)):
    topNumbers.append(minHeap[i][1])
  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()


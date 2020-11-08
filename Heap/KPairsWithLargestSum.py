from heapq import *


"""
Time Complexity - O(N * M * logK) => O(K^2 logK) if both the array size is K
Space Complexity - O(logK)
"""

def find_k_largest_pairs(nums1, nums2, k):
  result = []
  minheap = []

  for i in range(min(k, len(nums1))):
    for j in range(min(k, len(nums2))):
      if len(minheap) < k:
        heappush(minheap, (nums1[i] + nums2[j], i, j))
      else:
        if nums1[i] + nums2[j] < minheap[0][0]:
          break
        else:
          heappop(minheap)
          heappush(minheap, (nums1[i] + nums2[j], i, j))
  
  for (num, i, j) in minheap:
    result.append([nums1[i], nums2[j]])

  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()

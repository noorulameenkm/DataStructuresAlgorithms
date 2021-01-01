from heapq import *
from queue import PriorityQueue


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


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []
        minheap = []
        A.sort()
        B.sort()
        N = len(A)
        hash_ = {}
        heappush(minheap, (-(A[N-1] + B[N-1]), N-1, N-1)) 
        hash_[str(N-1) + str(N-1)] = 1
        for i in range(N):
            num, j, k = heappop(minheap)
            result.append(-num)
            
            sum1 = -(A[j - 1] + B[k])
            sum2 = -(A[j] + B[k - 1])
            
            pair1 = str(j - 1) + str(k)
            pair2 = str(j) + str(k - 1)
            if j > 0 and not pair1 in hash_:
                heappush(minheap, (sum1, j-1, k))
                hash_[pair1] = 1
            
            if k > 0 and not pair2 in hash_:
                heappush(minheap, (sum2, j, k-1))
                hash_[pair2] = 1
            
        return result
        

"""
You can us these below hashMap also
"""

# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b
        
# class HashMap:
#     def __init__(self):
#         self.bucket = []
    
#     def contains(self,x):
#         for a in self.bucket:
#             if a == x:
#                 return True
        
#         return False
    
#     def add(self,x):
#         self.bucket.append(x)
        

def find_k_largest_pairs_3(A, B):
  A.sort()
  B.sort()
  pq = PriorityQueue()
  s = set()
  n = len(A)
  pq.put((-1* (A[n-1] + B[n-1]), (n-1, n-1)))
  s.add((n-1, n-1))
  res = list()
  for _ in range(n):
    value = pq.get()
    sum_, (i, j) = value
    res.append(-1 * sum_)
    pair1 = (i - 1, j)
    pair2 = (i, j - 1)
    if pair1 not in s:
      s.add(pair1)
      pq.put((-1 * (A[i - 1] + B[j]), (i - 1, j)))
    
    if pair2 not in s:
      s.add(pair2)
      pq.put((-1 * (A[i] + B[j - 1]), (i, j-1)))

  
  return res


def find_k_largest_pairs_4(A, B):
  pq = PriorityQueue()
  n = len(A)
  result = list()
  for i in range(n):
    for j in range(n):
      pq.put(-1 * (A[i] + B[j]))
  
  for k in range(n):
    result.append(-1 * pq.get())

  
  return result



def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))

  print("Pairs with largest sum are: " + str(Solution().solve([9, 8, 2], [6, 3, 1])))

  print("Pairs with largest sum are: " + str(find_k_largest_pairs_3([9, 8, 2], [6, 3, 1])))

  print("Pairs with largest sum are: " + str(find_k_largest_pairs_4([9, 8, 2], [6, 3, 1])))


main()

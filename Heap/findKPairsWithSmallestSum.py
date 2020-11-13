from heapq import *

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        minheap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum_ = nums1[i] + nums2[j]
                if len(minheap) < k:
                    heappush(minheap, (-sum_, i, j))
                else:
                    if -sum_ < minheap[0][0]:
                        break
                    else:
                        heappop(minheap)
                        heappush(minheap, (-sum_, i, j))
                        
        result = []
        while minheap:
            pop = heappop(minheap)
            result.append([nums1[pop[1]], nums2[pop[2]]])
        
        return result
                        
        

def main():
    print(Solution().kSmallestPairs([1,7,11], [2,4,6], 3))


main()
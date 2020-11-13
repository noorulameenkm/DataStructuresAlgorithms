from heapq import *

class Solution:
    def smallestDistancePair(self, nums, k):
        minHeap = []
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                num = abs(nums[i] - nums[j])
                if len(minHeap) < k:
                    heappush(minHeap, -num)
                else:
                    if num < -minHeap[0]:
                        heappop(minHeap)
                        heappush(minHeap, -num)
            
        val = heappop(minHeap)
        return -val
            
        
        
def main():
    print(Solution().smallestDistancePair([1, 3, 1], 1))

main()
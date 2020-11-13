from heapq import *

class Solution:
    def maxSlidingWindow(self, nums, k):
        maxheap, result, start = [], [], 0
        
        for end in range(len(nums)):
            heappush(maxheap, (-nums[end], end))
            
            if end >= k - 1:
                poped = heappop(maxheap)
                while poped[1] < start:
                    poped = heappop(maxheap)
                
                result.append(-poped[0])
                if poped[1] >= start + 1:
                    heappush(maxheap, poped)
                    
                start += 1
                
        
        return result
                
            
def main():
    print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

main()
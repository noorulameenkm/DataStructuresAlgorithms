from heapq import *

class Solution:
    def maxSlidingWindow(self, nums, k):
        result, start, maxHeap = [], 0, []
        
        for end in range(len(nums)):
            heappush(maxHeap, (-nums[end], end))
            
            if end >= k - 1:
                num, index = heappop(maxHeap)
                
                while index < start:
                    num, index = heappop(maxHeap)
                    
                result.append(-num)
                
                if index > start:
                    heappush(maxHeap, (num, index))
                    
                start += 1
                
        return result
            


def main():
    print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

main()
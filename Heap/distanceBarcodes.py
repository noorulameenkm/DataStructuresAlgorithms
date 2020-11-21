from heapq import *
from collections import deque

class Solution:
    def rearrangeBarcodes(self, barcodes):
        maxheap, frequency, result, queue = [], {}, [], deque([])
        
        for i in range(len(barcodes)):
            frequency[barcodes[i]] = frequency.get(barcodes[i], 0) + 1
        
        for barCode, count in frequency.items():
            heappush(maxheap, (-count, barCode))
        
        
        while maxheap:
            count, barCode = heappop(maxheap)
            
            result.append(barCode)
            
            if len(queue) > 0:
                heappush(maxheap, queue.popleft())
            
            if -count > 1:
                queue.append((-(-count - 1), barCode))
                
        return result



print(Solution().rearrangeBarcodes([1,1,1,2,2,2]))
            
            
                
            
        
"""
    Problem Link:- https://leetcode.com/problems/reduce-array-size-to-the-half/submissions/
"""

from heapq import *
from typing import List

class Frequency:
    def __init__(self, num, count):
        self.number = num
        self.count = count
        
    def __lt__(self, other):
        return self.count > other.count

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        max_heap = []
        frequency = {}
        length = len(arr)
        for num in arr:
            if num not in frequency:
                frequency[num] = 0
            
            frequency[num] += 1
        
        for num, count in frequency.items():
            heappush(max_heap, Frequency(num, count))
        
        result = []
        counts = 0
        
        while counts < length // 2:
            freq = heappop(max_heap)
            counts += freq.count
            result.append(freq.number)
        
        return len(result)



print(Solution().minSetSize(arr = [3,3,3,3,5,5,5,2,2,7]))
print(Solution().minSetSize(arr = [7,7,7,7,7,7]))
print(Solution().minSetSize(arr = [1,9]))
print(Solution().minSetSize(arr = [1000,1000,3,7]))
print(Solution().minSetSize(arr = [1,2,3,4,5,6,7,8,9,10]))
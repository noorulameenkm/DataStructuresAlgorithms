from collections import defaultdict
from typing import List, DefaultDict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d: DefaultDict[int,int] = defaultdict(int)
        for i,v in enumerate(nums):
            d[v] = i
            
        for i,v in enumerate(nums):
            t = target - v
            if d[t] != 0:
                if d[t] != i:
                    return [i, d[t]]
        return []
        

sol = Solution()
l = sol.twoSum([1,5,2,8,3], 4)
print(l[0], l[1])
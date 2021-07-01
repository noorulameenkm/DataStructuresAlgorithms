"""
    Problem Link:- https://leetcode.com/problems/gray-code/
"""

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        lst_ = [0]
        
        if n == 0:
            return lst_
        
        lst_.append(1)
        curr = 1
        
        for i in range(2, n + 1):
            curr = curr * 2
            length = len(lst_)
            for j in range(length - 1, -1, -1):
                lst_.append(curr + lst_[j])
            
        
        return lst_



print(Solution().grayCode(n = 3))
print(Solution().grayCode(n = 2))
print(Solution().grayCode(n = 1))



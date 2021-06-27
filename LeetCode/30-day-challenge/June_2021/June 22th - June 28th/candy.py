"""
    Problem Link:- https://leetcode.com/problems/candy/
"""

class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 1:
            return 1
        
        answer = [1 for _ in range(n)]
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                answer[i] = answer[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and answer[i] <= answer[i + 1]:
                answer[i] = answer[i + 1] + 1
        
        return sum(answer)



print(Solution().candy(ratings = [1,0,2]))
print(Solution().candy(ratings = [1,2,2]))
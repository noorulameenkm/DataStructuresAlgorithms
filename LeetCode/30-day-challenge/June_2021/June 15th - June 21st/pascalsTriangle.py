""""
    Problem Link:- https://leetcode.com/problems/pascals-triangle/
"""



class Solution:
    def generate(self, numRows):
        results = [[1]]
        
        i = 0
        for _ in range(numRows - 1):
            ans = [1]
            previous = list(results[i])
            
            for j in range(1, len(previous)):
                sum_ = previous[j] + previous[j - 1]
                ans.append(sum_)
            
            ans.append(1)
            results.append(list(ans))
            i += 1
            
        return results
            


print(Solution().generate(3))
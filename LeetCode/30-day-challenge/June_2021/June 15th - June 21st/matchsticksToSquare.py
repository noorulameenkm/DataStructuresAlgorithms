"""
Leetcode Problem Link:-
https://leetcode.com/problems/matchsticks-to-square/
"""


from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        if sum(matchsticks) % 4 != 0:
            return False
        
        target = sum(matchsticks) // 4
        
        matchsticks.sort(key=lambda x: -x)
        if matchsticks[0] > target:
            return False
        
        results = [0, 0, 0, 0]
        
        length = len(matchsticks)
        
        def dfs(index):
            if index == length:
                return results[0] == target and results[1] == target and results[2] == target and results[3] == target
            
            for i in range(4):
                if results[i] + matchsticks[index] > target:
                    continue
                
                results[i] += matchsticks[index]
                
                if dfs(index + 1):
                    return True
            
                results[i] -= matchsticks[index]
            
            return False
    
        return dfs(0)



def makesquare_optimised(matchsticks: List[int]) -> bool:
    if len(matchsticks) < 4:
        return False
    
    if sum(matchsticks) % 4 != 0:
        return False
    
    target = sum(matchsticks) // 4
    
    matchsticks.sort(key=lambda x: -x)
    if matchsticks[0] > target:
        return False
    
    results = [0, 0, 0, 0]
    
    length = len(matchsticks)
    
    def is_skipped_before(index):
        for i in range(index):
            if results[i] == results[index]:
                return True
        
        return False
    
    def dfs(index):
        if index == length:
            return results[0] == target and results[1] == target and results[2] == target and results[3] == target
        
        for i in range(4):
            if results[i] + matchsticks[index] > target or is_skipped_before(i):
                continue
            
            results[i] += matchsticks[index]
            
            if dfs(index + 1):
                return True
        
            results[i] -= matchsticks[index]
        
        return False

    return dfs(0)




# Test case 1
print(Solution().makesquare(matchsticks = [1,1,2,2,2]))
print(Solution().makesquare(matchsticks = [3,3,3,3,4]))

# Test case 2
print(makesquare_optimised(matchsticks = [1,1,2,2,2]))
print(makesquare_optimised(matchsticks = [3,3,3,3,4]))
        
            
        
        
        
        
    
        
        
        
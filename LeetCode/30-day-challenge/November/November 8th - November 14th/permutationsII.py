from collections import deque
class Solution:
    def permuteUnique(self, nums):
        numLength = len(nums)
        permutations = deque()
        permutations.append([])
        result = []
        
        for num in nums:
            n = len(permutations)
            
            for _ in range(n):
                permutation = permutations.popleft()
                
                for i in range(len(permutation) + 1):
                    if i > 0 and permutation[i - 1] == num:
                        continue
                    
                    newPermutation = list(permutation)
                    newPermutation.insert(i, num)
                    if len(newPermutation) == numLength:
                        if newPermutation not in result:
                            result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
                        
        return result
            
                
                
def main():
    print(Solution().permuteUnique([1,1,2]))
    print(Solution().permuteUnique([1,2,3]))

main()
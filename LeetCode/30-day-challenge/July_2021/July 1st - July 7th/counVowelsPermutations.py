"""
    Problem Link:- https://leetcode.com/problems/count-vowels-permutation/
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        memory = {}
        vowels = ['a', 'e', 'i', 'o', 'u']
        MOD = pow(10, 9) + 7
        total = 0
        
        def traverse(remaining, previous):
            if remaining == 0:
                return 1
            
            key = f"{remaining}-{previous}"
            if key in memory:
                return memory[key]
            
            total = 0
            if previous == 'a':
                total = traverse(remaining - 1, 'e') % MOD
            elif previous == 'e':
                total = (traverse(remaining - 1, 'a') + traverse(remaining - 1, 'i')) % MOD
            elif previous == 'i':
                total = (traverse(remaining - 1, 'a') + traverse(remaining - 1, 'e') + traverse(remaining - 1, 'o') + traverse(remaining - 1, 'u')) % MOD
            elif previous == 'o':
                total = (traverse(remaining - 1, 'i') + traverse(remaining - 1, 'u')) % MOD
            elif previous == 'u':
                total = traverse(remaining - 1, 'a') % MOD
            
            memory[key] = total
            return memory[key]
        
        for vowel in vowels:
            total = (total + traverse(n - 1, vowel)) % MOD
        
        return total




print(Solution().countVowelPermutation(n = 1))
print(Solution().countVowelPermutation(n = 2))
print(Solution().countVowelPermutation(n = 5))
        
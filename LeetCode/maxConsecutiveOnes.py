class Solution:
    def longestOnes(self, A, K):
        start, longest, k_counter = 0, -1, 0
        
        
        for end in range(len(A)):
            num = A[end]
            
            k_counter += 1 if num == 0 else 0

            while k_counter > K:
                if A[start] == 0:
                    k_counter -= 1
                start += 1
            
            longest = max(longest, end - start + 1)
            
        return longest



print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))    
                
                
            
            
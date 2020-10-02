class Solution:
    def longestOnes(self, A, K):
        start, longest, length, k_counter = 0, -1, 0, 0
        
        
        for end in range(len(A)):
            num = A[end]
            
            
            if num == 0:
                k_counter += 1
                length += 1

                while k_counter > K:
                    remNum = A[start]
                    start += 1
                    length -= 1
                    if remNum == 0:
                        k_counter -= 1   
            else:
                length += 1
                    
            longest = max(longest, length)
            
        return longest



print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))    
                
                
            
            
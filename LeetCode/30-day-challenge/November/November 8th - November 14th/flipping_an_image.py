class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for index, value in enumerate(A[i]):
                A[i][index] = 1 if value == 0 else 0
            
        return A
            
    

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

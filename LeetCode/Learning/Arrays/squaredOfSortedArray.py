class Solution:
    def sortedSquares(self, A):
        left, right = 0, len(A) - 1
        result = []
        
        while left < right:
            
            leftSquare = A[left] * A[left]
            rightSquare = A[right] * A[right]
            
            if leftSquare > rightSquare:
                result.insert(0, leftSquare)
                left += 1
            else:
                result.insert(0, rightSquare)
                right -= 1
        
        if left == right:
            result.insert(0, A[left] * A[left])
            
        return result
            
            

print(Solution().sortedSquares([-4,-1,0,3,10]))
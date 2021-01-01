class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        result = []
        A.sort()
        n = len(A)
        if n < 3:
            return []
            
        for i in range(n - 2):
            if i > 0 and A[i] == A[i - 1]:
                continue
            
            isPossibleZero(A, A[i], i, result)
        
        return result
            

def isPossibleZero(A, num1, index, result):
    left = index + 1
    right = len(A) - 1
    target = -num1
    while left < right:
        num2, num3 = A[left], A[right]
        if num2 + num3 == target:
            result.append([num1, num2, num3])
            left += 1
            while left < right and A[left] == A[left - 1]:
                left += 1
            
            right -= 1
            while right > left and A[right] == A[right + 1]:
                right -= 1
                
        elif num2 + num3 > target:
            right -= 1
        else:
            left += 1
        


print(Solution().threeSum([ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]))
print(Solution().threeSum([-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1]))
print(Solution().threeSum([]))
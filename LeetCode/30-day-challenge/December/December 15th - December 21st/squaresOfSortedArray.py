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
            

def sortedSquares2(A):
    neg, pos = [], []
    result = []
    for num in A:
        if num < 0:
            neg.append(num)
        else:
            pos.insert(0, num)
            
    i, j = 0, 0
    while i < len(neg) and j < len(pos):
        if abs(neg[i]) > abs(pos[j]):
            result.insert(0, neg[i] * neg[i])
            i += 1
        else:
            result.insert(0, pos[j] * pos[j])
            j += 1
            
    while i < len(neg):
        result.insert(0, neg[i] * neg[i])
        i += 1
    
    while j < len(pos):
        result.insert(0, pos[j] * pos[j])
        j += 1

    return result
            

def main():
    # Method 1
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))

    # Method 2
    print(sortedSquares2([-4, -1, 0, 3, 10]))

main()
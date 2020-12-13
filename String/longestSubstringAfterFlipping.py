class Solution:
    # @param A : string
    # @return an integer
    # @info:- This question is from interviewbit
    def solve(self, A):
        zeroFound, onesFound = False, False
        zeroLength, onesLength, prevOnes = 0, 0, 0
        
        i, length = 0, len(A)
        maxLength = 0
        
        while i < length:
            num = A[i]
            
            if num == '0':
                if zeroFound:
                    onesLength = prevOnes
                    
                zeroLength = 0
                zeroFound = True
                
                while i < length and A[i] == '0':
                    zeroLength += 1
                    i += 1
                i -= 1
            
            if num == '1':
                onesFound = True
                prevOnes = 0
                while i < length and A[i] == '1':
                    onesLength += 1
                    prevOnes += 1
                    i += 1
                
                i -= 1
            
            maxLength = max(maxLength, zeroLength + onesLength)
            
            i += 1
            
        return maxLength
            

def main():
    print(Solution().solve("10010"))
    print(Solution().solve("1111010001"))

main()
            
        
        
                    
            
            
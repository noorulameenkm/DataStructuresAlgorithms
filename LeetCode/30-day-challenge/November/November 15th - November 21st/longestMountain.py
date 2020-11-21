class Solution:
    def longestMountain(self, A):
        length, maxLength = len(A), 0
        for i in range(length):
            isIncreasing = isDecreasing = False
            length_mountain = 1
            
            j = i + 1
            while j < length:
                if A[j] > A[j - 1]:
                    isIncreasing = True
                    if j > i + 1 and A[j - 1] < A[j - 2]:
                        break
                
                if A[j] < A[j - 1]:
                    isDecreasing = True
                
                if (isDecreasing and not isIncreasing) or (not isIncreasing and not isDecreasing):
                    break
                    
                
                length_mountain += 1
                    
                j += 1
            
            if (not isIncreasing or not isDecreasing) or (isDecreasing and not isIncreasing) or (not isIncreasing and not isDecreasing):
                maxLength = max(maxLength, 0)
            else:
                maxLength = max(maxLength, length_mountain)
                
        return maxLength

    def longestMountain2(self, A):
        start, maxLength = 0, 0
        isIncreasing, isDecreasing = False, False

        for end in range(len(A)):
            if end > start:
                currentIncreasing = False

                if A[end] > A[end - 1]: # check increasing
                    isIncreasing = True
                    currentIncreasing = True
                elif A[end] < A[end - 1]: # check decreasing
                    isDecreasing = True
                else: # check equal
                    if isIncreasing and isDecreasing: # Already a mountain
                        maxLength = max(maxLength, end - start)
                    
                    # set start to end
                    start = end
                    # set increasing, decreasing to false to start from the beginning
                    isIncreasing = False 
                    isDecreasing = False
                    continue  

                if isDecreasing and not isIncreasing:
                    start += 1
                    isIncreasing = False
                    isDecreasing = False
                elif isIncreasing and isDecreasing:
                    if currentIncreasing and end > start + 1 and A[end - 1] < A[end - 2]:
                        maxLength = max(maxLength, end - start)
                        start = end - 1
                        isIncreasing = True
                        isDecreasing = False
                    else:
                        maxLength = max(maxLength, end - start + 1)

        if isIncreasing and isDecreasing:
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength
                   

                





def main():
    # First Solution
    # print(Solution().longestMountain([2,1,4,7,3,2,5]))
    # print(Solution().longestMountain([1,2,3,4]))
    # second Solution
    print(Solution().longestMountain2([2,1,4,7,3,2,5]))
    print(Solution().longestMountain2([1,2,3,4]))
    print(Solution().longestMountain2([1,1,0,0,1,0]))


main()
                
                
                
        
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        mainStr = []
        localStr = ""
        for i in range(n - 1, -1, -1):
            if A[i] == ' ':
                if len(localStr) > 0:
                    mainStr.append(localStr)
                localStr = ""
            else:
                localStr = A[i] + localStr
        
        if len(localStr) > 0 and localStr != ' ':
            mainStr.append(localStr)
        
        return ' '.join(mainStr)



print(Solution().solve("       fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq                 "))
class Solution:
    def findArray(self, pref):
        answer = [pref[0]]
        k = pref[0]
        
        for i in range(1, len(pref)):
            x = k ^ pref[i]
            answer.append(x)
            k = k ^ answer[-1]
        
        return answer


print(Solution().findArray(pref = [5,2,0,3,1]))
print(Solution().findArray(pref = [13]))
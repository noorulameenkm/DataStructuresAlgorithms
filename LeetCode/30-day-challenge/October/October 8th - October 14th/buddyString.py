class Solution:
    def buddyStrings(self, A, B):
        if len(A) == 0 and len(B) == 0:
            return False
        if len(A) != len(B):
            return False
        if sorted(A) != sorted(B):
            return False
        if A == B and len(set(A)) == len(A):
            return False
        
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
            
            if count == 3:
                return False
            
        return True
        

print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))
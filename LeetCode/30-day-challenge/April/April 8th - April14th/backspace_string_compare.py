class Solution:
    def backspaceCompare(self, S, T):
        S = self.getWordAfterDel(S)
        T = self.getWordAfterDel(T)
        
        if S == T:
            return True
        
        return False
    
    
    def getWordAfterDel(self, s):
        s = ''.join(list(reversed(s)))
        result = ''
        hash_count = 0
        for i in range(len(s)):
            if s[i] == '#':
                hash_count += 1
            else:
                if hash_count > 0:
                    hash_count -= 1
                else:
                    result = s[i] + result
        
        return result


print(f'Solution for ab#c and ad#c is {Solution().backspaceCompare("ab#c", "ad#c")}')
print(f'Solution for ab## and c#d# is {Solution().backspaceCompare("ab##", "c#d#")}')
print(f'Solution for a##c and #a#c is {Solution().backspaceCompare("a##c", "#a#c")}')
print(f'Solution for a#c and b is {Solution().backspaceCompare("a#c", "b")}')
            
                
            
        
        
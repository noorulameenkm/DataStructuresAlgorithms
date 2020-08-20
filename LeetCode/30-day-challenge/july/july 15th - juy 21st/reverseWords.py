class Solution:
    def reverseWords(self, s):
        if len(s) <= 0:
            return s
        
        words_array = []
        curr, prv = None, None
        word = ''
        for i in range(len(s)):
            curr = s[i]
            if curr == ' ' and word != '' and word != ' ':
                words_array.insert(0, word)
                word = ''
            else:
                if curr != ' ':
                    word += curr
                
        if word != '' and word != ' ':
            words_array.insert(0, word)
            
        return ' '.join(words_array)     


print(Solution().reverseWords(" Hello World! "));      
                
        
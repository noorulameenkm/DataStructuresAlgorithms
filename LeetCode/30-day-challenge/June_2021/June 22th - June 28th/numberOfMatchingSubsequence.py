

def numMatchingSubseq(s, words):

    def is_matching(original, subs):
        
        if len(subs) == 0:
            return True
        
        if len(original) == 0:
            return False
        
        if original[0] == subs[0]:
            if is_matching(original[1:], subs[1:]):
                return True
            
            return False
        
        return is_matching(original[1:], subs)


    count = 0
    for s_ in words:
        if is_matching(str(s), s_):
            count += 1


    return count


class Solution:
    def numMatchingSubseq(self, s, words):
        d = {}
        count = 0
        
        for letter in s:
            d[letter] = []
        
        for word in words:
            start = word[0]
            if start in d:
                d[start].append(word)
        
        for letter in s:
            words_ = d[letter]
            rest = []
            for index, word in enumerate(words_):
                if len(word) == 1:
                    count += 1
                    continue
                
                if word[1:].startswith(letter):
                    rest.append(word[1:])
                    continue
                
                if word[1] in d:
                    d[word[1]].append(word[1:])
                
            d[letter] = rest
        
        return count



print(numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
print(numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))

# Solution 2
print(Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
print(Solution().numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))

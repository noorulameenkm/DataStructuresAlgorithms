import sys

class Solution:
    def smallestWord(self, string):
        smallest_word = ''
        smallest_word_length = sys.maxsize

        current_word = ''

        for i in range(len(string)):
            if string[i] != ' ':
                current_word += string[i]
            else:
                if len(current_word) < smallest_word_length:
                    smallest_word_length = len(current_word)
                    smallest_word = current_word
                
                current_word = ''
        
        return smallest_word


print(f'Solution for "abc de ghihjk a uvw h j" is {Solution().smallestWord("abc de ghihjk a uvw h j")}')
print(f'Solution for "abc tyde ghihjk yuya uvw ioih poij" is {Solution().smallestWord("abc tyde ghihjk yuya uvw ioih poij")}')
print(f'Solution for "" is {Solution().smallestWord("")}')
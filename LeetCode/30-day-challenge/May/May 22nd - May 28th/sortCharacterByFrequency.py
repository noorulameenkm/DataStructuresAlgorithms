class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        values = []
        result = ""
        for char in s:
            if char not in frequency:
                frequency[char] = ''
            frequency[char] += char

            values = list(frequency.items())
            values = sorted(values, key=lambda x: -len(x[1]))
        for k in values:
            result += k[1]
                
        return result
            
            
        
print(f'Solution for "tree" is {Solution().frequencySort("tree")}')
print(f'Solution for "cccaaa" is {Solution().frequencySort("cccaaa")}')
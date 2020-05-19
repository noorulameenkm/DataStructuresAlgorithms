class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            sortedstring = self.sortedString(s)
            if d.get(sortedstring, -1) is -1:
                d[sortedstring] = [s]
            else:
                d[sortedstring].append(s)
        
        results = []
        for value in d.values():
            results.append(value)
        
        return results
    
    def sortedString(self, string):
        return ''.join(sorted(string))


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(arr))
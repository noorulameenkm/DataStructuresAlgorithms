class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		results = []
		self.find_subsequence(s, 0, [], results)
		subsequences = sorted(results)
		if len(subsequences) == 1:
			return []
		
		return subsequences[1:]
		
	
	def find_subsequence(self, s, index, currLst, results):
		if index == len(s):
			results.append(''.join(currLst))
			return

		currLst.append(s[index])
		self.find_subsequence(s, index + 1, currLst, results)

		currLst.pop()
		self.find_subsequence(s, index + 1, currLst, results)





if __name__ == "__main__":
	print(Solution().AllPossibleStrings("abc"))
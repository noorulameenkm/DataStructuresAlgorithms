"""
Problem Link:- https://practice.geeksforgeeks.org/problems/power-set4302/1
"""

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n = len(s)
		results = []
		for num in range(1, (1 << n)):
		    substr = ""
		    for i in range(n):
		        if (num & (1 << i)) != 0:
		            substr += s[i]
		   
		    results.append(str(substr))
		    
		results.sort()
		return results




print(Solution().AllPossibleStrings(s = "abc"))
print(Solution().AllPossibleStrings(s = "aa"))

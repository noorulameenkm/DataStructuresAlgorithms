"""
    Problem Link:- https://leetcode.com/problems/custom-sort-string/
"""


from collections import Counter
class Solution:
    def customSortString(self, order, str):
        str_count = dict(Counter(str))
        not_there = ""
        for char in str:
            if char not in order:
                not_there += char
        
        result = ""
        for char in order:
            if char in str_count:
                result += (char * str_count[char])
        
        return result + not_there


def customSortString2(order, str):
    frequency_str = dict(Counter(str))

    result = ""
    for char in order:
        if char in frequency_str:
            result += (char * frequency_str[char])
            del frequency_str[char]
    
    for char, val in frequency_str.items():
        result += (char * frequency_str[char])

    return result


# First Approach
print(Solution().customSortString(order = "cba", str = "abcd"))
print(Solution().customSortString(order = "kqep", str = "pekeq"))

# Second Approach
print(customSortString2(order = "cba", str = "abcd"))
print(customSortString2(order = "kqep", str = "pekeq"))
from collections import defaultdict, Counter
from math import inf


"""
    Problem Link:- https://leetcode.com/problems/minimum-window-substring/
"""


def minimum_window_substring(t, s):

    t_frequency = Counter(t)
    required, formed = len(t_frequency), 0
    window = defaultdict(int)

    start, end = 0, 0
    length, ans = 0, inf
    left, right = 0, 0
    for end in range(len(s)):
        char = s[end]
        window[char] += 1
        length += 1
        if char in t_frequency and window[char] == t_frequency[char]:
            formed += 1

        if required == formed:

            while required == formed:
                rem_char = s[start]
                window[rem_char] -= 1
                length -= 1
                start += 1
                if rem_char in t_frequency and window[rem_char] < t_frequency[rem_char]:
                    formed -= 1

            if length + 1 <= ans:
                ans = length + 1
                left, right = start - 1, end

    return "" if ans == inf else s[left:right + 1]


print(minimum_window_substring(s="ADOBECODEBANC", t="ABC"))
print(minimum_window_substring(s="a", t="a"))
print(minimum_window_substring(s="a", t="aa"))

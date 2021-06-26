"""
Problem Link: - https://www.hackerrank.com/challenges/repeated-string/problem
"""

def repeatedString(s, n):
    
    def count_char(s_, n_):
        count = 0
        for i in range(n_):
            if s_[i] == 'a':
                count += 1
        
        return count
    
    if n <= len(s):
        return count_char(s, n)
    
    count_in_string = count_char(s, len(s))
    length = len(s)
    k = n // length
    result = k * count_in_string
    remaining_chars = n - (k * length)
    count = count_char(s, remaining_chars)
    result += count
    
    return result


print(repeatedString(s="aba", n=10))
print(repeatedString(s="a", n=1000000000000))
"""
    Problem Link:- https://leetcode.com/problems/decode-ways-ii/
"""



def decode_ways_2(s):
    length = len(s)
    dp = [0 for _ in range(length + 1)]
    dp[0] = 1
    dp[1] = decode_single_char(s[0])
    MOD = pow(10, 9) + 7
    for i in range(2, length + 1):
        previous_char = s[i - 2]
        current_char = s[i - 1]

        dp[i] += (dp[i - 1] * decode_single_char(current_char))
        dp[i] += (dp[i - 2] * decode_double_char(previous_char, current_char))
        dp[i] = dp[i] % MOD

    return dp[length]



def decode_single_char(char):
    if char == "*":
        return 9
    
    if char == "0":
        return 0
    
    return 1


def decode_double_char(previous_char, current_char):
    if previous_char == "*":
        if current_char == "*":
            return 15
        if current_char >= "0" and current_char <= "6":
            return 2
        
        return 1
    
    if previous_char == "1":
        if current_char == "*":
            return 9
        return 1
    
    if previous_char == "2":
        if current_char == "*":
            return 6
        if current_char >= "0" and current_char <= "6":
            return 1
        return 0

    return 0




print(decode_ways_2(s = "*"))
print(decode_ways_2(s = "1*"))
print(decode_ways_2(s = "2*"))
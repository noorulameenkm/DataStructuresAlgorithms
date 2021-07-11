def decode_ways(digits):
    # use numbers 1 to 26 to represent all alphabet letters
    prefixes = [str(i) for i in range(1, 27)]
    def dfs(index):
        if index == len(digits):
            return 1
            
        ways = 0
        current = digits[index:]
        for prefix in prefixes:
            if current.startswith(prefix):
                ways += dfs(index + len(prefix))
            
        return ways

    return dfs(0)



def decode_string_memoization(digits):
    prefixes = [str(i) for i in range(1, 27)]
    memo = {}
    def dfs(index):
        if index == len(digits):
            return 1

        if index in memo:
            return memo[index]

        ways = 0
        current = digits[index:]
        for prefix in prefixes:
            if current.startswith(prefix):
                ways += dfs(index + len(prefix))

        memo[index] = ways

        return ways 

    return dfs(0)


"""
 Time Complexity - O(N)
 Space Complexity - O(N)
"""
def decode_string_tabulation(digits):
    length = len(digits)

    def decode_two_digit(previous, current):
        if previous == '1':
            return 1
        
        if previous == '2' and (current >= '0' and current <= '6'):
            return 1
        
        return 0

    def decode_single(current):
        if current == '0':
            return 0
        
        return 1

    dp = [0 for _ in range(length + 1)]
    dp[0] = 1
    dp[1] = decode_single(digits[0])
    for i in range(2, length + 1):
        previous = digits[i - 2]
        current = digits[i - 1]

        dp[i] += (dp[i - 1] * decode_single(current))
        dp[i] += (dp[i - 2] * decode_two_digit(previous, current))
    
    return dp[length]


# FIRST FUNCTION
print(decode_ways('18'))
print(decode_ways('123'))
print(decode_ways('11223'))


# SECOND FUNCTION
print(decode_string_memoization('18'))
print(decode_string_memoization('123'))
print(decode_string_memoization('11223'))


# Third Method
print(decode_string_tabulation('18'))
print(decode_string_tabulation('123'))
print(decode_string_tabulation('11223'))




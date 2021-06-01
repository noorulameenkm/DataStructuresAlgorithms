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


# FIRST FUNCTION
print(decode_ways('18'))
print(decode_ways('123'))
print(decode_ways('11223'))


# SECOND FUNCTION
print(decode_string_memoization('18'))
print(decode_string_memoization('123'))
print(decode_string_memoization('11223'))




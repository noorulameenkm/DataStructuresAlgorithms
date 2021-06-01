def word_break(s, words):
    if len(s) == 0:
        return True
    
    if len(words) == 0:
        return False


    def dfs(i):
        if i == len(s):
            return True

        for word in words:
            if s[i:].startswith(word):
                if dfs(i + len(word)):
                    return True

        return False

    return dfs(0)


# Time Complexity - O(N ^ 2)
def word_break_memoization(s, words):
    if len(s) == 0:
        return True
    
    if len(words) == 0:
        return False

   
    memo = {}

    def dfs(i):
        if i == len(s):
            return True
        
        if i in memo:
            return memo[i]

        res = False
        for word in words:
            if s[i:].startswith(word):
                if dfs(i + len(word)):
                    res = True
                    break

        memo[i] = res
        return memo[i]

    
    return dfs(0)
   

    


# Test case 1
print(word_break("educativeio", ["educative", "io"]))
print(word_break("aab", ["a", "c"]))

# Test case 2
print(word_break_memoization("educativeio", ["educative", "io"]))
print(word_break_memoization("aab", ["a", "c"]))
print(word_break_memoization("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']))




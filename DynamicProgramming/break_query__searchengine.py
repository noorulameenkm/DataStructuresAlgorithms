"""
    Time complexity - O(n ^ 3)
    Space complexity - O(n)
"""
def break_query(query, dict):
    n = len(query)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(n):
        if dp[i]:
            for j in dict:
                l = len(j)
                if i + l <= n and query[i: i + l] == j:
                    dp[i + l] = True
    return dp[n]


query = "vegancookbook"
dict = ["i", "cream", "cook", "scream", "ice", "cat", "book", "icecream", "vegan"]
print(break_query(query, dict))

query = "veganicetea"
print(break_query(query, dict))
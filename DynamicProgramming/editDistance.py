"""
Time Complexity - O(3 ^ (m + n))
Space Complexity - O(m + n)
"""
def edit_distance(string1, string2):
    return edit_distance_recursive(string1, string2, 0, 0)


def edit_distance_recursive(string1, string2, index1, index2):
    n1, n2 = len(string1), len(string2)
     # if we have reached the end of s1, then we have to insert all the remaining characters of s2
    if index1 == n1:
        return n2 - index2

    # if we have reached the end of s2, then we have to delete all the remaining characters of s1
    if index2 == n2:
        return n1 - index1

    if string1[index1] == string2[index2]:
        return edit_distance_recursive(string1, string2, index1 + 1, index2 + 1)
    
    
    # replacement
    c1 = 1 + edit_distance_recursive(string1, string2, index1 + 1, index2 + 1)
    # insertion
    c2 = 1 + edit_distance_recursive(string1, string2, index1, index2 + 1)
    # deletions
    c3 = 1 + edit_distance_recursive(string1, string2, index1 + 1, index2)


    return min(c1, c2, c3)


"""
Time complexity - O(m * n)
Space Complexity - O(m * n + (m + n))
"""
def edit_distance_memoization(string1, string2):
    dp = [[-1 for _ in range(len(string2))] for _ in range(len(string1))]
    return edit_distance_memoization_recursive(dp, string1, string2, 0, 0)


def edit_distance_memoization_recursive(dp, str1, str2, index1, index2):
    n1, n2 = len(str1), len(str2)

    if index1 == n1:
        return n2 - index2
    
    if index2 == n2:
        return n1 - index1
    
    if dp[index1][index2] == -1:
        if str1[index1] == str2[index2]:
            dp[index1][index2] = edit_distance_memoization_recursive(dp, str1, str2, index1 + 1, index2 + 1)
            return dp[index1][index2]
        
        c1 = 1 + edit_distance_memoization_recursive(dp, str1, str2, index1 + 1, index2 + 1)
        c2 = 1 + edit_distance_memoization_recursive(dp, str1, str2, index1, index2 + 1)
        c3 = 1 + edit_distance_memoization_recursive(dp, str1, str2, index1 + 1, index2)

        dp[index1][index2] = min(c1, c2, c3)

    return dp[index1][index2]


"""
Time Complexity - O(N * M)
Space Complexity - O(N * M)
"""
def edit_distance_tabulation(string1, string2):
    n1, n2 = len(string1), len(string2)
    dp = [[-1 for i in range(n2 + 1)] for j in range(n1 + 1)]
    
    # if s2 is empty, we have to remove all the characters
    for i1 in range(n1 + 1):
        dp[i1][0] = i1

    for i2 in range(n2 + 1):
        dp[0][i2] = i2
    
    for i1 in range(1, n1 + 1):
        for i2 in range(1, n2 + 1):
            if string1[i1 - 1] == string2[i2 - 1]:
                dp[i1][i2] = dp[i1 - 1][i2 - 1]
            else:
                dp[i1][i2] = 1 + min(
                                    dp[i1 - 1][i2 - 1],
                                    dp[i1 - 1][i2],
                                    dp[i1][i2 - 1]
                                )

    return dp[n1][n2]



def main():
    # Approach 1
    print(edit_distance("bat", "but"))
    print(edit_distance("abdca", "cbda"))
    print(edit_distance("passpot", "ppsspqrt"))

    # Approach 2
    print(edit_distance_memoization("bat", "but"))
    print(edit_distance_memoization("abdca", "cbda"))
    print(edit_distance_memoization("passpot", "ppsspqrt"))

    # Approach 3
    print(edit_distance_tabulation("bat", "but"))
    print(edit_distance_tabulation("abdca", "cbda"))
    print(edit_distance_tabulation("passpot", "ppsspqrt"))


main()
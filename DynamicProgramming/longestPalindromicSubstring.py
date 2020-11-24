"""
Time Complexity - O(3^n)
Space Complexity - O(n)
"""

def find_LPS_length(st):
    return find_LPS_length_recursive(st, 0, len(st) - 1)

def find_LPS_length_recursive(st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    
    if startIndex == endIndex:
        return 1
    
    # case1: elements at the beginning and the end are the same
    if st[startIndex] == st[endIndex]:
        remainingLength = endIndex - startIndex - 1
        if remainingLength == find_LPS_length_recursive(st, startIndex + 1, endIndex - 1):
            return remainingLength + 2
    
    # case2: skip one character either from the beginning or the end
    c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
    c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)

    return max(c1, c2)


"""
Time Complexity - O(n*2)
Space Complexity - O(n*2)
"""

def find_LPS_length_memoization(str_):
    n = len(str_)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LPS_length_memoization_recursive(dp, str_, 0, n - 1)


def find_LPS_length_memoization_recursive(dp, str_, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    if startIndex == endIndex:
        return 1
    
    if dp[startIndex][endIndex] == -1:
        # case 1: elements at the beginning and the end are the same
        if str_[startIndex] == str_[endIndex]:
            remaining = endIndex - startIndex - 1
            if remaining == find_LPS_length_memoization_recursive(dp, str_, startIndex + 1, endIndex - 1):
                dp[startIndex][endIndex] = remaining + 2
                return dp[startIndex][endIndex]
        
        # case 2: skip one character either from the beginning or the end
        c1 = find_LPS_length_memoization_recursive(dp, str_, startIndex, endIndex - 1)
        c2 = find_LPS_length_memoization_recursive(dp, str_, startIndex + 1, endIndex)

        dp[startIndex][endIndex] = max(c1, c2)

    return dp[startIndex][endIndex]


"""
Time Complexity - O(n*2)
Space Complexity - O(n*2)
"""
def find_LPS_tabulation(str_):
    n = len(str_)
    dp = [[False for i in range(len(str_))] for j in range(n)]

    for i in range(n):
        dp[i][i] = True
    
    maxLength = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if str_[startIndex] == str_[endIndex]:
                if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                    dp[startIndex][endIndex] = True
                    maxLength = max(maxLength, endIndex - startIndex + 1)
                
    return maxLength



def main():
    # Recursive
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))

    # Memoization
    print(find_LPS_length_memoization("abdbca"))
    print(find_LPS_length_memoization("cddpd"))
    print(find_LPS_length_memoization("pqr"))

    # Tabulation
    print(find_LPS_tabulation("abdbca"))
    print(find_LPS_tabulation("cddpd"))
    print(find_LPS_tabulation("pqr"))

main()
def longestPalindromicSubstring(str_):
    n = len(str_)

    table = [[False for x in range(n)] for y in range(n)]

    maxLength = 1
    i = 0
    while i < n:
        table[i][i] = True
        i += 1

    start = 0
    i = 0

    while i < n - 1:
        if str_[i] == str_[i + 1]:
            table[i][i + 1] = True
            maxlength = 2
            start = i
        i += 1

    k = 3

    while k <= n:
        i = 0

        while i < (n - k + 1):
            j = i + k - 1

            if str_[i] == str_[j] and table[i + 1][j - 1]:
                table[i][j] = True

                if k > maxLength:
                    maxLength = k
                    start = i
            
            i += 1
        
        k += 1

    return str_[start: start + maxLength]



def longestPalindromicSubstring2(str_):
    maxlength = 1

    start = 0
    n = len(str_)

    low, high = 0, 0

    # One by one consider every character as center point of  
    # even and length palindromes 
    for i in range(1, n):
        # Find the longest even length palindrome with center 
        # points as i-1 and i. 
        low = i - 1
        high = i

        while low >= 0 and high < n and str_[low] == str_[high]:
            if high - low + 1 > maxlength:
                maxlength = high - low + 1
                start = low

            low -= 1
            high += 1
            
        # Find the longest odd length palindrome with center  
        # point as i 
        low = i - 1
        high = i + 1

        while low >= 0 and high < n and str_[low] == str_[high]:
            if high - low + 1 > maxlength:
                maxlength = high - low + 1
                start = low
            
            low -= 1
            high += 1
        
    
    return str_[start: start + maxlength]

def main():
    # First Approach
    print(longestPalindromicSubstring("forgeeksskeegfor"))

    # second approach
    print(longestPalindromicSubstring2("forgeeksskeegfor"))

main()
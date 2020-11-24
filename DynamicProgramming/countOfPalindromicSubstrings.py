def count_palindromic_substring_bruteforce(str_):
    n = len(str_)
    count = n
    for i in range(n):
        count += count_palindromic_substring_(str_, i - 1, i + 1)
        count += count_palindromic_substring_(str_, i, i + 1)
    return count 
     

def count_palindromic_substring_(str_, startIndex, endIndex):
    count = 0
    while startIndex >= 0 and endIndex < len(str_):
        if str_[startIndex] != str_[endIndex]:
            break
            
        count += 1

        startIndex -= 1
        endIndex += 1
        
    return count

def count_palindromic_substring(str):
    n = len(str)
    # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
    dp = [[False for _ in range(n)] for _ in range(n)]

    count = 0

    # every string with one character is a palindrome
    for i in range(n):
        dp[i][i] = True
        count += 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if str[startIndex] == str[endIndex]:
                # if it's a two character string or if the remaining string is a palindrome too
                if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                    dp[startIndex][endIndex] = True
                    count += 1

    return count



def main():
  # Tabulation
  print(count_palindromic_substring("abdbca"))
  print(count_palindromic_substring("cddpd"))
  print(count_palindromic_substring("pqr"))
  print(count_palindromic_substring("qqq"))
  
  # recursive
  print(count_palindromic_substring_bruteforce("abdbca"))
  print(count_palindromic_substring_bruteforce("cddpd"))
  print(count_palindromic_substring_bruteforce("pqr"))
  print(count_palindromic_substring_bruteforce("qqq"))

main()

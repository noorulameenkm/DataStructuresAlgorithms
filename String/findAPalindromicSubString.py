def palindromic_substring(string, length):
    if not string or len(string) == 0:
        return None
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            if (j - i + 1) != length:
                continue

            main_string = string[i: j + 1]
            rev_string = main_string[::-1]
            if main_string == rev_string:
                return main_string
    
    return None





def main():
    print(palindromic_substring("abcbe", 3))


main()
"""
Time Complexity - O(1)
Space Complexity - O(1)
"""
def is_duplicates_exists(str_):
    char_array = [False for _ in range(26)]

    for c in str_:
        index = ord(c) - ord('a')
        if char_array[index] is True:
            return True

        char_array[index] = True
    
    return False



def is_duplicates_exists_2(str_):
    checker = 0
    for char in str_:
        value = ord(char) - ord('a')
        if ((checker & (1 << value)) > 0):
            return True
        
        checker |= (1 << value)
    
    return False



def main():
    # Approach 1
    print(is_duplicates_exists("abcda"))
    print(is_duplicates_exists("abcd"))

    # Approach 2
    print(is_duplicates_exists_2("abcda"))
    print(is_duplicates_exists_2("abcd"))


main()
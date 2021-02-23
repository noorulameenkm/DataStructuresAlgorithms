def is_permutation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    s_1 = [c for c in str_1]
    s_2 = [c for c in str_2]

    s_1.sort()
    s_2.sort()

    return ''.join(s_1) == ''.join(s_2)


def is_permutation_2(str_1, str_2):
    char_set = [0 for i in range(26)]

    if len(str_1) != len(str_2):
        return False

    for c in str_1:
        index = ord(c) - ord('a')
        char_set[index] += 1

    for c in str_2:
        index = ord(c) - ord('a')

        char_set[index] -= 1
        if char_set[index] < 0:
            return False

    return True


def main():
    # Approach 1
    print(is_permutation("abcd", "bcda"))
    print(is_permutation("abcdg", "bcdae"))

    # Approach 1
    print(is_permutation_2("abcd", "bcda"))
    print(is_permutation_2("abcdg", "bcdae"))


main()
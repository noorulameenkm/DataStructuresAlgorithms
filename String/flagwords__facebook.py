"""
    Time Comnplexity - O(max(sl, wl))
    Space Complexity - O(1)
"""

def flag_words(S, W):

    def repeated_count(string, index):
        temp = index
        while temp < len(string) and string[temp] == string[index]:
            temp += 1

        return temp - index


    if not S and not W:
        return False

    i, j = 0, 0
    while i < len(S) and j < len(W):
        if S[i] == W[j]:
            len1 = repeated_count(S, i)
            len2 = repeated_count(W, j)
            if (len1 < 3 and len1 != len2) or (len1 >= 3 and len1 < len2):
                return False
        else:
            return False

        i += len1
        j += len2

    return i == len(S) and j == len(W)


S = "mooooronnn" # modified word
W = "moron" # original word

if flag_words(S, W):
    print("Word Flagged")
    print("The word", '"' + S + '"', "is a possible morph of", '"' + W + '"')
else:
    print("Word Safe")

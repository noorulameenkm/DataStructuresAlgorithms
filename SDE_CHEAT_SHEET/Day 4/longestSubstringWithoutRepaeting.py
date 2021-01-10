def longestSubstringWithoutRepeating1(string):
    n, maxLength = len(string), 0
    for i in range(n):
        str_ = ""
        for j in range(i, n):
            str_ += string[j]
            if singleChar(str_):
                maxLength = max(len(str_), maxLength)

    return maxLength

def singleChar(string):
    frequency = {}
    for c in string:
        if c in frequency:
            return False

        frequency[c] = frequency.get(c, 0) + 1
        
    return True

def longestSubstringWithoutRepeating2(string):
    frequency = {}
    start = 0
    length, maxLength = 0, 0

    for end in range(len(string)):
        char = string[end]

        length += 1

        frequency[char] = frequency.get(char, 0) + 1

        while frequency[char] > 1:
            remChar = string[start]
            frequency[remChar] -= 1
            if frequency[remChar] == 0:
                del frequency[remChar]
            
            length -= 1
            start += 1
        
        maxLength = max(maxLength, length)
    
    return maxLength




def longestSubstringWithoutRepeating3(string):
    frequency = {}

    start, maxLength = 0, 0
    n = len(string)

    for end in range(n):
        char = string[end]

        if char in frequency and frequency[char] >= start:
            start = frequency[char] + 1

        frequency[char] = end
        maxLength = max(maxLength, end - start + 1)

    return maxLength



def main():
    # Method 1
    print(longestSubstringWithoutRepeating1("abcabcbb"))
    print(longestSubstringWithoutRepeating1("bbbbb"))
    print(longestSubstringWithoutRepeating1("pwwkew"))
    print(longestSubstringWithoutRepeating1(""))

    # Method 2
    print(longestSubstringWithoutRepeating2("abcabcbb"))
    print(longestSubstringWithoutRepeating2("bbbbb"))
    print(longestSubstringWithoutRepeating2("pwwkew"))
    print(longestSubstringWithoutRepeating2(""))


    # Method 3
    print(longestSubstringWithoutRepeating3("abcabcbb"))
    print(longestSubstringWithoutRepeating3("bbbbb"))
    print(longestSubstringWithoutRepeating3("pwwkew"))
    print(longestSubstringWithoutRepeating3(""))

main()

            
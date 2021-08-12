from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            sortedstring = self.sortedString(s)
            if d.get(sortedstring, -1) is -1:
                d[sortedstring] = [s]
            else:
                d[sortedstring].append(s)

        results = []
        for value in d.values():
            results.append(value)

        return results

    def sortedString(self, string):
        return ''.join(sorted(string))


"""
Time Complexity - O(n * klogk)
"""


def anagrams(lst):
    """
    Function to find anagram pairs
    :param lst: A lst of strings
    :return: Group of anagrams
    """

    # Write your code here!
    results = []
    dictionary = {}
    for string in lst:
        key = ''.join(sorted(string))

        if key in dictionary:
            dictionary[key].append(string)
        else:
            dictionary[key] = []
            dictionary[key].append(string)

    for _, values in dictionary.items():
        if len(values) >= 2:
            results.append(values)

    results = sorted(results)
    return results


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(arr))
print(anagrams(arr))


def groupAnagrams(strs):

    def construct_char_array(str_):
        array = [0] * 26
        for char in str_:
            index = ord(char) - ord('a')
            array[index] += 1

        return array

    anagrams = []
    dict_ = defaultdict(list)

    for s in strs:
        array = construct_char_array(s)
        dict_[tuple(array)].append(s)

    for value in dict_.values():
        anagrams.append(value)

    return anagrams


print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams(strs=[""]))
print(groupAnagrams(strs=["a"]))

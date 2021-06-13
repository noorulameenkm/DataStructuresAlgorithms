from collections import defaultdict

def palindrome_pairs(words):
    results, n = [], len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if words[i] + words[j] == (words[i] + words[j])[::-1]:
                results.append([i, j])
            
            if words[j] + words[i] == (words[j] + words[i])[::-1]:
                results.append([j, i])
    
    return results


def palindrome_pairs_2(words):
    results, n = [], len(words)
    hash_map = defaultdict(list)
    is_empty, empty_index = False, -1

    for i, word in enumerate(words):
        if word == "":
            is_empty = True
            empty_index = i
            continue

        hash_map[word[-1]].append((word, i))

    for i, word in enumerate(words):

        if word == "":
            continue

        if word == word[::-1] and is_empty:
            results.append([i, empty_index])
            results.append([empty_index, i])

        search_space = hash_map[word[0]]
        for (w, index) in search_space:
            if index == i:
                continue

            if word + w == (word + w)[::-1]:
                results.append([i, index])

    return results
        
        


# Test case 1
print(palindrome_pairs(words = ["abcd","dcba","lls","s","sssll"]))
print(palindrome_pairs(words = ["bat","tab","cat"]))
print(palindrome_pairs(words = ["a",""]))

# Test case 2
print(palindrome_pairs_2(words = ["abcd","dcba","lls","s","sssll"]))
print(palindrome_pairs_2(words = ["bat","tab","cat"]))
print(palindrome_pairs_2(words = ["a",""]))
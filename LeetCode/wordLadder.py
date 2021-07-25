from math import inf
from collections import deque


def diff(word_1, word_2):
    count = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            count += 1
    
    return count

"""
    Time limit exceeded
"""
def word_ladder(beginWord, endWord, wordList):

    def bfs(current_word, count_, visited):
        if current_word == endWord:
            return count_
        
        visited[current_word] = True

        current_min = inf
        for i in range(len(wordList)):
            word = wordList[i]
            if word not in visited and diff(word, current_word) == 1:
                _min = bfs(word, count_ + 1, visited)
                if _min != -1:
                    current_min = min(current_min, _min)
        

        del visited[current_word]
        return -1 if current_min == inf else current_min


    count = bfs(beginWord, 1, {})
    if count == -1:
        return 0
    
    return count


def word_ladder_2(beginWord, endWord, wordList):

    word_set = set()
    is_end_word_present = False
    for word in wordList:
        word_set.add(word)
        if word == endWord:
            is_end_word_present = True
    
    if not is_end_word_present:
        return 0

    queue = deque([])

    depth = 0
    queue.append(beginWord)
    while len(queue) > 0:
        depth += 1

        length = len(queue)
        while length > 0:
            word = queue.popleft()
            for i in range(len(word)):
                temp = list(word)
                for ascii in range(97, 123):
                    temp[i] = chr(ascii)
                    curr_word = ''.join(temp)
                    if curr_word == word:
                       continue

                    if curr_word == endWord:
                        return depth + 1
                    
                    if curr_word in word_set:
                        queue.append(curr_word)
                        word_set.remove(curr_word)

            length -= 1
            
    return 0
                



# First Approach
print(word_ladder(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(word_ladder(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))


# Second Approach
print(word_ladder_2(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(word_ladder_2(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
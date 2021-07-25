from collections import deque


"""
    Problem Link:- https://leetcode.com/problems/word-ladder-ii/
    Time Complexity - O(L * N  + VE)
"""
def dfs(adj_list, beginWord, endWord, path, paths):
    path.append(beginWord)
    if beginWord == endWord:
        paths.append(list(path))
        del path[-1]
        return 
    
    for word in adj_list[beginWord]:
        dfs(adj_list, word, endWord, path, paths)

    del path[-1]

def word_ladder_2(beginWord, endWord, wordList):
    word_set = set()
    visited = {}
    is_end_word_present = False
    for word in wordList:
        word_set.add(word)
        if word == endWord:
            is_end_word_present = True
    
    if not is_end_word_present:
        return []

    queue = deque([])
    visited[beginWord] = 0
    queue.append(beginWord)
    adj_list = {}
    while len(queue) > 0:
        length = len(queue)
        while length > 0:
            word = queue.popleft()
            if word not in adj_list:
                adj_list[word] = []
            for i in range(len(word)):
                temp = list(word)
                for ascii in range(97, 123):
                    temp[i] = chr(ascii)
                    curr_word = ''.join(temp)
                    
                    if curr_word == word:
                        continue

                    if curr_word in word_set:
                        if curr_word not in visited:
                            visited[curr_word] = visited[word] + 1
                            adj_list[word].append(curr_word)
                            queue.append(curr_word)
                        elif visited[curr_word] == visited[word] + 1:
                            adj_list[word].append(curr_word)

            length -= 1

    paths = []
    dfs(adj_list, beginWord, endWord, [], paths)
    return paths



print(word_ladder_2(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(word_ladder_2(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
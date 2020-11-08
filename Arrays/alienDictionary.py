from collections import deque

"""
Time Complexity - O(V + N) where V is the number of distict characters, N is the number of rules.
Space Complexity - O(V + N)
"""

def find_order(words):
  graph = {}
  inDegrees = {}
  for word in words:
    for character in word:
      graph[character] = []
      inDegrees[character] = 0
  
  for i in range(len(words) - 1):
    word1, word2 = words[i], words[i + 1]
    for j in range(min(len(word1), len(word2))):
      parent, child = word1[j], word2[j]
      if parent != child:
        inDegrees[child] += 1
        graph[parent].append(child)
        break

  result = ""
  queue = deque()
  for char, inDegrees_ in inDegrees.items():
    if inDegrees_ == 0:
      queue.append(char)

  while queue:
    char_ = queue.popleft()
    childs = []
    if char_ in graph:
      childs = graph[char_]
    for child in childs:
      inDegrees[child] -= 1
      if inDegrees[child] == 0:
        queue.append(child)
    
    result += char_

  if len(inDegrees) != len(result):
    return ""

  return result


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()

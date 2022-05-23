class Node:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

"""
    # insertWord
      Time Complexity - O(l), l is the length of the word
      Space Complexity - O(l)
    # searchWord
      Time Complexity - O(l)
      Space Complexity - O(l)
    # startsWith
      Time Complexity - O(l)
      Space Complexity - O(l)
"""
class WordDictionary:
    def __init__(self):
        self.root = Node()
    
    def insertWord(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = Node()
            
            root = root.children[char]
        
        root.isEndOfWord = True
    
    def searchWord(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                return False

            root = root.children[char]
        
        return root.isEndOfWord
    
    def startsWith(self, prefix):
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False

            root = root.children[char]
        
        return True


## Driver Code
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
print("Keys to insert: ")
print(keys)

d = WordDictionary()

for i in range(len(keys)):
    d.insertWord(keys[i])

print("Searching 'there' in the dictionary results: " + str(d.searchWord("there")))
print("Searching the prefix 'by' in the dictionary results: " + str(d.startsWith("by")))

    


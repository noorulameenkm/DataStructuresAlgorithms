class TrieNode:
    def __init__(self):
        self.childrens = [None] * 26
        self.isEndOfWord = False




class Trie:
    def __init__(self):
        self.root = TrieNode()

    
    def _char_to_index(self, char):
        return ord(char) - ord('a')

    
    def insert(self, key):
        length = len(key)

        root = self.root
        for i in range(length):
            char_to_index = self._char_to_index(key[i])
            if root.childrens[char_to_index] is None:
                root.childrens[char_to_index] = TrieNode()
            
            root = root.childrens[char_to_index]
        
        root.isEndOfWord = True

    def search(self, key):
        root = self.root
        length = len(key)
        for i in range(length):
            char_to_index = self._char_to_index(key[i])
            if root.childrens[char_to_index] is None:
                return False
            
            root = root.childrens[char_to_index]

        
        return root != None and root.isEndOfWord



def main():
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 

    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))


main() 


            
class Node:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False
        self.rank = 0
        self.data = None


"""
    # constructor
        Time Complexity - O(n * l), n - number of sentence, l - average length of a sentence
        Space Complexity - O(n * l)
    # autoComplete
        Time Complexity - O(q + m + l * (log l))
            where q - the length of the query string at that moment
                  m - total number of nodes and
                  l - averge length
        Space Complexity - O(n * l)
            where n records of average length l are stored in the list to return at the end.
"""
class AutoCompleteSystem:
    def __init__(self, sentences, ranks) -> None:
        self.root = Node()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, ranks[i])
    
    def addRecord(self, sentence, hot):
        root = self.root
        for char in sentence:
            if char not in root.children:
                root.children[char] = Node()
            
            root = root.children[char]
        
        root.isEndOfWord = True
        root.rank -= hot
        root.data = sentence
    
    def dfs(self, root):
        ret = []
        if root.isEndOfWord:
            ret.append((root.rank, root.data))
        
        for char in root.children:
            ret.extend(self.dfs(root.children[char]))
        
        return ret

    def search(self, sentence):
        root = self.root
        for char in sentence:
            if char not in root.children:
                return []
            
            root = root.children[char]
        
        return self.dfs(root)
    
    def autoComplete(self, c):
        results = []
        if c == "#":
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        else:
            self.keyword += c
            results = self.search(self.keyword)
        
        return [item[1] for item in sorted(results)[:3]]
        


# Driver code
sentences = ["beautiful", "best quotes", "best friend", "best birthday wishes", "instagram", "internet"]
times = [30, 14, 21, 10, 10, 15]
auto = AutoCompleteSystem(sentences, times)
print(auto.autoComplete("b"))
print(auto.autoComplete("e"))
print(auto.autoComplete("s"))
print(auto.autoComplete("t"))
print(auto.autoComplete("#"))

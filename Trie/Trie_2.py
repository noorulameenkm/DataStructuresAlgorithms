class TrieNode:
    def __init__(self, char=''):
        self.char = char # To store the value of a particular key
        self.children = [None] * 26 # Total size of the English alphabet
        self.is_end_of_word = False # True if the node represents the end of word

    # Function to mark the currentNode as Leaf
    def mark_as_end_of_word(self):
        self.is_end_of_word = True
    
    # Function to unMark the currentNode as Leaf
    def unmark_as_end_of_word(self):
        self.is_end_of_word = False




class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, char):
        return ord(char) - ord('a')
    
    """
     Time Complexity - O(n) n ->  length of the word that we are inserting 
    """
    def insert(self, key):
        if key is None:
            return
        
        current_node = self.root
        key = key.lower()
        index = 0

        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])
            
            current_node = current_node.children[index]
        
        current_node.mark_as_end_of_word()


    """
        Time complexity - O(h) ->  h is the length of the word we are searching for
    """
    def search(self, key):
        if key is None:
            return False

        current_node = self.root
        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                return False
            
            current_node = current_node.children[index]
        
        return current_node != None and current_node.is_end_of_word

    def has_no_children(self, current_node):
        for i in range(len(current_node.children)):
            if current_node.children[i] is not None:
                return False
        
        return True

    def delete_helper(self, key, current_node, length, level):
        deleted_self = False

        if current_node is None:
            return deleted_self
        
        # Base Case:
        # If we have reached at the node
        # which points to the alphabet at the end of the key.
        if level is length:
            # If there are no nodes ahead of this node in this path
            # Then we can delete this node
            if self.has_no_children(current_node):
                current_node = None
                deleted_self = True
            
            # If there are nodes ahead of current_node in this path
            # Then we cannot delete current_node. We simply unmark this as leaf
            else:
                current_node.unmark_as_end_of_word()
                deleted_self = False
        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(key, child_node, length, level + 1)

            if child_deleted:
                # Making children pointer also None: since child is deleted
                current_node.children[self.get_index(key[level])] = None
                # If current_node is leaf node then
                # current_node is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current_node.is_end_of_word:
                    deleted_self = False
                elif self.has_no_children(current_node) is False:
                    deleted_self = False
                else:
                    current_node = None
                    deleted_self = True
            else:
                deleted_self = False


        return deleted_self 

    """
    Time Complexity - O(h)
    """    
    def delete(self, key):
        if self.root is None or key is None:
            return   
        
        self.delete_helper(key, self.root, len(key), 0)
        



# t = Trie()
# print(t.get_index('a'))

# keys = ["the", "a", "there", "answer", "any",
#         "by", "bye", "their", "abc"]

# output = ["Not present in trie", "Present in trie"]

# for key in keys:
#     t.insert(key)


# # Search for different keys
# if t.search("the") is True:
#     print("the --- " + output[1])
# else:
#     print("the --- " + output[0])

# if t.search("these") is True:
#     print("these --- " + output[1])
# else:
#     print("these --- " + output[0])

# if t.search("abc") is True:
#     print("abc --- " + output[1])
# else:
#     print("abc --- " + output[0])

# if t.search("ther") is True:
#     print("ther --- " + output[1])
# else:
#     print("ther --- " + output[0])


# t.delete("abc")
# print("Deleted key \"abc\"")

# if t.search("abc") is True:
#     print("abc --- " + output[1])
# else:
#     print("abc --- " + output[0])
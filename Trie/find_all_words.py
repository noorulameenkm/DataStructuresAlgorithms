from Trie_2 import Trie

"""
Time Complexity - O(n) where 'n' is the number of nodes in the trie
"""
def find_words(root):
    # Write your code here
    # Return a list of string
    all_words = []
    current_word = []
    find_all_words(root, current_word, all_words)
    return all_words


def find_all_words(current_node, current_word, all_words):
    if current_node is None:
        return 

    
    current_word.append(current_node.char)
    
    if current_node.is_end_of_word:
        all_words.append(''.join(current_word))
    
    
    for i in range(len(current_node.children)):
        if current_node.children[i] is not None:
            find_all_words(current_node.children[i], current_word, all_words)
    
    if len(current_word) > 0:
        current_word.pop()


def get_words(root, result, level, word):

    # Leaf denotes end of a word
    if root.is_end_of_word:
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(str(temp))

    for i in range(26):
        if root.children[i]:
            # Non-None child, so add that index to the character array
            word[level] = chr(i + ord('a'))  # Add character for the level
            get_words(root.children[i], result, level + 1, word)


def find_words_2(root):
    result = []
    word = [None] * 20  # assuming max level is 20
    get_words(root, result, 0, word)
    return result



def main():
    t = Trie()

    keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
    
    for key in keys:
        t.insert(key)
    
    # Approach 1
    all_words = find_words(t.root)
    print(all_words)

    # Approach 2
    all_words = find_words_2(t.root)
    print(all_words)
    
main()
from Trie_2 import Trie

"""
Time Complexity - O(m + n^2)
"""

def is_formation_possible(dictionary, word):
    # write your code here
    t = Trie()
    for w_ in dictionary:
        t.insert(w_)
    
    current_node = t.root
    for level in range(len(word)):
        index = t.get_index(word[level])

        if current_node.children[index] is None:
            return False
        
        if current_node.children[index].is_end_of_word:
            if t.search(word[level + 1:]):
                return True
        
        current_node = current_node.children[index]

    return False


def main():
    print(is_formation_possible(["the", "hello", "there", "answer", "any", "educative", "world", "their", "abc"], "helloworld"))
    print(is_formation_possible(['the', 'hello', 'there', 'answer', 'any', 'educative', 'world', 'their', 'abc'], "educativeinc"))

main()
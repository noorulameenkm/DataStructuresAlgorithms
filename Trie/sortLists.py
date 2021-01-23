from Trie_2 import Trie

"""
 Time Complexity - O(n)
"""
def sort_list(arr):
    t = Trie()
    for st in arr:
        t.insert(st)
    
    result = []
    current_word = []
    find_all_words(t.root, current_word, result)
    return result


def find_all_words(current_node, current_word, result):
    if current_node is None:
        return
    
    current_word.append(current_node.char)
    if current_node.is_end_of_word:
        result.append(''.join(current_word))
    
    for i in range(len(current_node.children)):
        if current_node.children[i] is not None:
            find_all_words(current_node.children[i], current_word, result)
        
    if len(current_word) > 0:
        current_word.pop()
   



def main():
    print(sort_list(["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]))


main()

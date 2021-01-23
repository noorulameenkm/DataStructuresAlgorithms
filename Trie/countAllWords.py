from Trie_2 import Trie



def total_words(root):
    result = [0]
    count_all_words(root, result)
    return result[0]



def count_all_words(current_node, result):
    if current_node is None:
        return
    
    if current_node.is_end_of_word:
        result[0] += 1
    
    for i in range(len(current_node.children)):
        if current_node.children[i] is not None:
            count_all_words(current_node.children[i], result)



"""
 Time Complexity - O(n) n -> is the number of nodes
"""
def count_all_words_2(root):
    result = 0

    if root is None:
        return result
    
    if root.is_end_of_word:
        result += 1
    
    for i in range(len(root.children)):
        if root.children[i] is not None:
            result += count_all_words_2(root.children[i])
    
    return result
    



def main():

    t = Trie()

    keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
    
    for key in keys:
        t.insert(key)
    
    # Approach 1
    words_count = total_words(t.root)
    print(words_count)

    # Approach 2
    words_count = count_all_words_2(t.root)
    print(words_count)


main()
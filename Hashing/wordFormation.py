from HashTable import HashTable

def is_formation_possible(lst, word):
    # Write your code here
    ht = HashTable()
    for w_ in lst:
        ht.insert(w_, True)
    
    for i in range(len(word)):
        if ht.search(word[0: i + 1]) and ht.search(word[i + 1: ]):
            return True

    return False


print(is_formation_possible(['the', 'hello', 'there', 'answer', 'any', 'educative', 'world', 'their', 'abc'],"helloworld"))
print(is_formation_possible(['the', 'hello', 'there', 'answer', 'any', 'educative', 'world', 'their', 'abc'],"educativeinc"))
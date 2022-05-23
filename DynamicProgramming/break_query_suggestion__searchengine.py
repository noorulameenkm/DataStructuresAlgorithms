
"""
    Time complexity - O(n ^ 2 + 2 ^ n + l), where n is the length of query and l is the length of the list containing words of the dictionary.
    Space complexity - O((n * 2 ^ n ) + l), where nn is the length of the query and ll is the length of the list containing the dictionary’s words.
"""
def break_query(query, lisOfWords):
    return helper(query, lisOfWords, {})

def helper(query, listOfWords, result):

    res = []

    if not query:
        return []
    
    if query in result:
        return result[query]

    for word in listOfWords:
        if not query.startswith(word):
            continue

        if len(word) == len(query):
            res.append(word)
        else:
            resultOfRest = helper(query[len(word):], listOfWords, result)
            for res_ in resultOfRest:
                new = word + ' ' + res_
                res.append(new)
    
    result[query] = res
    return res



query = "vegancookbook"
dict = ["an", "book", "car", "cat", "cook", "cookbook", "crash", 
        "cream", "high", "highway", "i", "ice", "icecream", "low", 
        "scream", "veg", "vegan", "way"]
print(break_query(query, dict))
query = "highwaycarcrash"
print(break_query(query, dict))
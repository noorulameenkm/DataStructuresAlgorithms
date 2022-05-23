
"""
    Time Complexity - O(n)
    Space Complexity - O(n)
"""
def search_ranking(page_scores):
    n = len(page_scores)
    rankings = [0] * n

    rankings[0] = 1
    for i in range(1, n):
        rankings[i] = page_scores[i - 1] * rankings[i - 1]
    
    right = 1
    for i in range(n - 1, -1, -1):
        rankings[i] = right * rankings[i]
        right = right * page_scores[i]
    
    return rankings


# Driver code
page_scores = [3, 5, 1, 1, 6, 7, 2, 3, 4, 1, 2]
print(search_ranking(page_scores))
page_scores = [3, 5, 1, 1]
print(search_ranking(page_scores))

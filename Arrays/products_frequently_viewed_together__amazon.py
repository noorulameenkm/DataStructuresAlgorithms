"""
    Time Complexity - O(n + m)
    Space Complexity - O(m)
"""
def findSimilarity(products, candidates):
    candidate_frequency = {}
    for cand in candidates:
        if cand not in candidate_frequency:
            candidate_frequency[cand] = 0
        
        candidate_frequency[cand] += 1
    
    product_frequency = {}
    results = []
    start = 0
    for i in range(len(products)):
        if products[i] not in product_frequency:
            product_frequency[products[i]] = 0

        product_frequency[products[i]] += 1
        while len(product_frequency) == len(candidate_frequency):
            if product_frequency == candidate_frequency:
                results.append(i - len(candidates) + 1)
        
            product_frequency[products[start]] -= 1
            if product_frequency[products[start]] == 0:
                del product_frequency[products[start]]
            
            start += 1
    
    return results



product = [3, 2, 1, 5, 2, 1, 2, 1, 3, 4]
candidate = [1, 2, 3]
print(findSimilarity(product, candidate))
"""
Time Complexity - O(n * m), n -> length of the titles, m -> maximum length of a single title
Space Complexity - O(n * m)
"""

def group_titles(titles):
    hash_map = {}

    for title in titles:
        arr = [0] * 26
        for letter in title:
            index = ord(letter) - ord('a')
            arr[index] += 1

        key = tuple(arr)
        if key not in hash_map:
            hash_map[key] = []
        
        hash_map[key].append(title)
    
    return hash_map.values()


titles = ["duel","dule","speed","spede","deul","cars"]
results = list(group_titles(titles))
query = "spede"

for result in results:
    if query in result:
        print(result)
        break


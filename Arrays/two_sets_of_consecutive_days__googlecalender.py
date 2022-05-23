
"""
Time Complexity - O(n)
Space Complexity - O(n)
"""
def two_sets_of_days(arr, k):
    map = {}
    map[0] = -1

    sum_ = 0
    for i, days in enumerate(arr):
        sum_ += days
        map[sum_] = i
    
    lsize = float('inf')
    result = float('inf')
    sum_ = 0

    for i, days in enumerate(arr):
        sum_ += days

        if sum_ - k in map:
            lsize = min(lsize, i - map[sum_ - k])
        
        if sum_ + k in map and lsize < float('inf'):
            result = min(result, map[sum_ + k] - i + lsize)
        
    if result == float('inf'):
        return -1
    else:
        return result
    

#  Driver code
hours_per_day = [1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8]
k = 5;
print(two_sets_of_days(hours_per_day, k))
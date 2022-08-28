
"""
    Time Complexity - O(log N)
    Space Complexity - O(1)
"""
def milestone_days(days, target):

    def search(n):
        start, end = 0, len(days)

        while start < end:

            mid = start + (end - start) // 2
            if n <= days[mid]:
                end = mid
            else:
                start = mid + 1
        
        return start
    
    first = search(target)
    if target in days[first: first + 1]:
        second = search(target + 1) - 1
        return [first, second]
    else:
        [-1, -1]


## Driver code
milestones = [0, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7]
target = 7
print(milestone_days(milestones, target))

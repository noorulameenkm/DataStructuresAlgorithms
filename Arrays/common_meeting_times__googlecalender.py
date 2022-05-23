
"""
    Time complexity - O(m + n)
    Space complexity - O(max(m, n))
"""
def meetings_intersection(meetings_a, meetings_b):
    i = j = 0
    intersections = []

    while i < len(meetings_a) and j < len(meetings_b):
        start = max(meetings_a[i][0], meetings_b[j][0])
        end = min(meetings_a[i][1], meetings_b[j][1])

        if start < end:
            intersections.append([start, end])
        
        if meetings_a[i][1] < meetings_b[j][1]:
            i += 1
        else:
            j += 1
    
    return intersections



# Driver code
meetings_a = [[1, 3], [5, 6], [7, 9]]
meetings_b = [[2, 3], [5, 7]]
print(meetings_intersection(meetings_a, meetings_b))
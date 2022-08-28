
"""
    Time Complexity - O(n)
    Space Complexity - O(n)
"""
def path_cost(elevation_map):
    n = len(elevation_map)

    left_max = [0] * n
    right_max = [0] * n
    
    left_max[0] = elevation_map[0]
    right_max[n - 1] = elevation_map[n - 1]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], elevation_map[i])
    
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], elevation_map[i])
    
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - elevation_map[i]
    
    return water


# Driver code
elevation_map = [1, 2, 1, 3, 1, 2, 1, 4, 1, 0, 0, 2, 1, 4]
print("Accumulated water:", str(path_cost(elevation_map)) + "cm")
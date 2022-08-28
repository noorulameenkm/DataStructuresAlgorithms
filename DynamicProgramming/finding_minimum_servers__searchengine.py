
"""
    Time Complexity - O(m * n)
    Space Complexity - O(n)
"""
def calculate_minimum_servers(servers, demand, lookup):
    if demand < 0:
        return -1
    
    if demand == 0:
        return 0
    
    if demand in lookup:
        return lookup[demand]
    
    minimum = float('inf')

    for server in servers:
        result = calculate_minimum_servers(servers, demand - server, lookup)
        if result >= 0 and result < minimum:
            minimum = 1 + result

    lookup[demand] = minimum if minimum != float('inf') else -1
    return lookup[demand]


def find_minimum_servers(servers, demand):
    if demand < 1:
        return 0
    return calculate_minimum_servers(servers, demand, {})


capacities = [2,3,4]
demand = 8
print(find_minimum_servers(capacities, demand))
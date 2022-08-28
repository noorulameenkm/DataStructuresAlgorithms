from collections import defaultdict


"""
    Time Complexity - O(m * n)
    Space Complexity - O(m + n)
"""
def get_total_cost(G_map, path_costs, drivers, user):
    city = defaultdict(defaultdict)

    def backtrack_evaluate(city, current_node, target_node, cost, visited):
        visited.add(current_node)
        ret = -1.0
        neighbours = city[current_node]
        if target_node in neighbours:
            ret = cost + neighbours[target_node]
        else:
            for neighbour, value in neighbours.items():
                if neighbour in visited:
                    continue

                ret = backtrack_evaluate(city, neighbour, target_node, cost + value, visited)
                if ret != -1:
                    break

        visited.remove(current_node)
        return ret


    # build city
    for (city1, city2), cost in zip(G_map, path_costs):
        city[city1][city2] = cost
        city[city2][city1] = cost
    
    # traverse the graph
    results = []
    for driver in drivers:
        if driver not in city or user not in city:
            ret = -1
        else:
            visited = set()
            ret = backtrack_evaluate(city, user, driver, 0, visited)

        results.append(ret)

    return results


G_map = [["a","b"],["b","c"],["a","e"],["d","e"]]
path_costs = [12.0,23.0,26.0,18.0]
drivers = ["c", "d", "e", "f"]
user = "a"
all_path_costs = get_total_cost(G_map, path_costs, drivers, user)
print("Total cost of all paths", all_path_costs)
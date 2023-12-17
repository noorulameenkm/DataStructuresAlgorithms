class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        default_value = 10**8
        distance = [default_value for _ in range(V)]
        distance[S] = 0
        for _ in range(V - 1):
            for src, dst, weight in edges:
                if distance[src] != default_value and distance[src] + weight < distance[dst]:
                    distance[dst] = distance[src] + weight
        
        for src, dst, weight in edges:
            if distance[src] != default_value and distance[src] + weight < distance[dst]:
                    return [-1]
        
        return distance
    

if __name__ == "__main__":
    E = [[0,1,9]]
    S = 0
    print(Solution().bellman_ford(2, E, S))
    
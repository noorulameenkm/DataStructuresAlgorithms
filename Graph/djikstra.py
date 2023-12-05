from heapq import *
from math import inf

class Pair:
    def __init__(self, v, weight):
        self.vertex = v
        self.weight = weight
        
    def __lt__(self, other):
        if self.weight == other.weight:
            return self.vertex < other.vertex
        
        return self.weight < other.weight

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        adj_list = [[] for _ in range(V)]
        
        for i, lst in enumerate(adj):
            for j, w in lst:
                adj_list[i].append(Pair(j, w))
                adj_list[j].append(Pair(i, w))
        
        min_heap = []
        results = [inf] * V
        results[S] = 0
        heappush(min_heap, Pair(S, 0))
        
        while min_heap:
            pair = heappop(min_heap)
            distance, vertex = pair.weight, pair.vertex
            for adjacent_pair in adj_list[vertex]:
                weight, adj_vertex = adjacent_pair.weight, adjacent_pair.vertex
                total_distance = weight + distance
                if total_distance < results[adj_vertex]:
                    results[adj_vertex] = total_distance
                    heappush(min_heap, Pair(adj_vertex, total_distance))
        
        return results
    


if __name__ == "__main__":
    vertex = 4
    s = 0
    adj = [
        [[1, 9], [2, 1], [3, 1]],
        [[3, 3]],
        [[3, 2]]
    ]

    print(Solution().dijkstra(vertex, adj, s))

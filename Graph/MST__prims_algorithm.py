from heapq import *
from math import inf

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        min_heap = []
        visited = [False for _ in range(V)]
        # adj_list = [[] for _ in range(V)]
        # for a, b, w in adj:
        #     adj_list[a].append((b, w))
        #     adj_list[b].append((a, w))

        sum_ = 0
        heappush(min_heap, (0, 0))
        while min_heap:
            weight, node = heappop(min_heap)
            
            if visited[node]:
                continue
            
            visited[node] = True
            sum_ += weight
            for adj_node, adj_weight in adj[node]:
                heappush(min_heap, (adj_weight, adj_node))
        
        return sum_
    

if __name__ == "__main__":
    V = 3
    adj = [
        [(1, 5), (2, 1)],
        [(0, 5), (2, 3)],
        [(0, 1), (1, 3)]
    ]

    print(Solution().spanningTree(V, adj))
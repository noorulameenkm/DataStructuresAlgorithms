from heapq import *
from math import inf
from typing import List

"""
    Problem link:- https://leetcode.com/problems/network-delay-time/description
"""

class Pair:
    def __init__(self, vertex, time):
        self.vertex = vertex
        self.time = time
    
    def __lt__(self, other):
        if self.time == other.time:
            return self.vertex < other.vertex
        
        return self.time < other.time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = [[] for _ in range(n + 1)]
        results = [inf for _ in range(n + 1)]

        # Create adjacency list
        for src, dst, time in times:
            adj_list[src].append(Pair(dst, time))

        min_heap = []
        results[k] = 0
        heappush(min_heap, Pair(k, 0))

        while min_heap:
            pair = heappop(min_heap)
            
            vertex, time = pair.vertex, pair.time
            # Get all the adjacent of the current vertex
            for adj_pair in adj_list[vertex]:
                adj_vertex, adj_time = adj_pair.vertex, adj_pair.time
                if time + adj_time < results[adj_vertex]:
                    results[adj_vertex] = time + adj_time
                    heappush(min_heap, Pair(adj_vertex, results[adj_vertex]))
        
        return -1 if inf in results[1:] else max(results[1:])



if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2

    print(Solution().networkDelayTime(times, n, k))

    times = [[1,2,1]]
    n = 2
    k = 2

    print(Solution().networkDelayTime(times, n, k))
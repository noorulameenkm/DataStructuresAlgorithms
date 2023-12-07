from heapq import *
from math import inf
from functools import lru_cache
from typing import List


"""
Problem Link:- https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/description
"""

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n + 1)]

        for src, dst, wgt in edges:
            adj_list[src].append((dst, wgt))
            adj_list[dst].append((src, wgt))
        
        distance = [inf for _ in range(n + 1)]
        distance[n] = 0
        min_heap = []
        heappush(min_heap, (0, n))

        while min_heap:
            d, node = heappop(min_heap)
            for a_node, a_wgt in adj_list[node]:
                if d + a_wgt < distance[a_node]:
                    distance[a_node] = d + a_wgt
                    heappush(min_heap, (distance[a_node], a_node))
        
        @lru_cache(None)
        def dfs(node):
            if node == n:
                return 1
            
            paths = 0
            for adj, _ in adj_list[node]:
                if distance[node] > distance[adj]:
                    paths = (paths + dfs(adj)) % 1000000007

            return paths


        return dfs(1)


if __name__ == "__main__":
    n, edges = 5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
    print(Solution().countRestrictedPaths(n, edges))
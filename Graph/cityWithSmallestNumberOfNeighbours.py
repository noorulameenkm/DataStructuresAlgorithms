from math import inf
from typing import List



"""
Problem link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
"""

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        rows, cols = len(edges), len(edges[0])
        distance = [[inf for _ in range(n)] for _ in range(n)]

        for src, dst, weight in edges:
            distance[src][dst] = weight
            distance[dst][src] = weight
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    distance[i][j] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        
        ans = inf
        city = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    count += 1
            
            if count <= ans:
                ans = count
                city = i
        
        return city



if __name__ == "__main__":
    n, edges, distanceThreshold = 4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4
    print(Solution().findTheCity(n, edges, distanceThreshold))
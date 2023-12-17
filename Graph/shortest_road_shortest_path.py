from heapq import *
from math import inf
class Solution:
    # @param A : integer
    # @param B : tuple of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        adj_list = [{} for _ in range(A + 1)]
        
        for src, dst, wgt in B:
            adj_list[src].update({ dst: wgt })
            adj_list[dst].update({ src: wgt })
        
        distance = [inf for _ in range(A + 1)]
        parent = [-1 for _ in range(A + 1)]
        
        min_heap = [(0, C)]
        distance[C] = 0
        parent[C] = C
        
        while min_heap:
            dist, node = heappop(min_heap)
            
            for adj_node, adj_weight in adj_list[node].items():
                if dist + adj_weight < distance[adj_node]:
                    distance[adj_node] = dist + adj_weight
                    parent[adj_node] = node
                    heappush(min_heap, (distance[adj_node], adj_node))
        
        
        parent_iter = parent[D]
        src = parent_iter
        dst = D
        min_road = inf
        while src != dst:
            min_road = min(min_road, adj_list[src].get(dst))
            src = parent_iter
            parent_iter = parent[parent_iter]
            dst = parent_iter
            
        
        return min_road
            

if __name__ == "__main__":         
    A = 7
    B = [[1, 2, 2],[2, 3, 8],[1, 7, 3],[7, 4, 2],[4, 3, 5],[1, 5, 3],[5, 3, 7],[1, 6, 1]]
    C = 1
    D = 3
    print(Solution().solve(A, B, C, D))
from heapq import *
from math import inf
from typing import List

"""
Problem link: https://leetcode.com/problems/path-with-maximum-probability/description
"""

class Pair:
    def __init__(self, vertex, prob):
        self.vertex = vertex
        self.prob = prob
    
    def __lt__(self, other):
        if self.prob == other.prob:
            return self.vertex < other.vertex

        return self.prob > other.prob

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = [[] for _ in range(n)]
        probability = [-inf for _ in range(n)]

        # Construct adjacency list
        for [src, dst], prob in zip(edges, succProb):
            adj_list[src].append(Pair(dst, prob))
            adj_list[dst].append(Pair(src, prob))
        

        min_heap = []
        probability[start_node] = 1.0
        heappush(min_heap, Pair(start_node, probability[start_node]))

        while min_heap:
            pair = heappop(min_heap)
            vertex, prob = pair.vertex, pair.prob

            for adj_pair in adj_list[vertex]:
                adj_vertex, adj_prob = adj_pair.vertex, adj_pair.prob
                
                if prob * adj_prob > probability[adj_vertex]:
                    probability[adj_vertex] = prob * adj_prob
                    heappush(min_heap, Pair(adj_vertex, probability[adj_vertex]))

        return 0.0 if probability[end_node] == -inf else probability[end_node]
        



if __name__ == "__main__":
    n, edges, succProb, start, end = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2
    print(Solution().maxProbability(n, edges, succProb, start, end))
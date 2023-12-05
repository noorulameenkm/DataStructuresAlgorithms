from math import inf
from heapq import *
from typing import List

"""
Problem link: https://leetcode.com/problems/cheapest-flights-within-k-stops
"""

class Pair:
    def __init__(self, to_city: int, price: int, hops: int = 0) -> None:
        self.to_city = to_city
        self.price = price
        self.hops = hops
    
    def __lt__(self, other):
        if self.hops == other.hops:
            return self.price < other.price
        
        return self.hops < other.hops


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list: List[List[Pair]] = [[] for _ in range(n)]
        for from_, to_, price in flights:
            adj_list[from_].append(Pair(to_, price))
        
        distance: List[int] = [inf for _ in range(n)]
        distance[src] = 0
        min_heap = []
        heappush(min_heap, Pair(src, 0))

        # Do the logic
        while min_heap:
            pair: Pair = heappop(min_heap)
            city, price, hops = pair.to_city, pair.price, pair.hops
            for adj_pair in adj_list[city]:
                to_city, cost = adj_pair.to_city, adj_pair.price
                if hops <= k and price + cost < distance[to_city]:
                    distance[to_city] = price + cost
                    heappush(min_heap, Pair(to_city, distance[to_city], hops + 1))


        return -1 if distance[dst] == inf else distance[dst]




if __name__ == "__main__":
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    print(Solution().findCheapestPrice(n, flights, src, dst, k))

from typing import List
from disjoint_sets import DisjointSet

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        extra_edges = 0
        connected_components = 0
        for src, dst in connections:
            if ds.find_parent(src) != ds.find_parent(dst):
                ds.union_by_rank(src, dst)
            else:
                extra_edges += 1

        for i in range(n):
            if ds.parents[i] == i:
                connected_components += 1
        
        required_edges_to_connect = connected_components - 1
        if required_edges_to_connect < 0:
            return 0
        
        if extra_edges >= required_edges_to_connect:
            return required_edges_to_connect
        
        return -1


if __name__ == "__main__":
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    print(Solution().makeConnected(n, connections))
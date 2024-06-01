from typing import List

from disjoint_sets import DisjointSet

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        ds = DisjointSet(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    ds.union_by_rank(i, j)
        
        count = 0
        for k in range(n):
            if ds.parents[k] == k:
                count += 1

        return count


if __name__ == "__main__":
    graph = [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]

    print(Solution().findCircleNum(graph))
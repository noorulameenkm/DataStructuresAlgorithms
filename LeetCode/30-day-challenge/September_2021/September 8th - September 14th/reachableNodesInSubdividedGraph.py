from heapq import heappop, heappush


"""
    Problem Link:- https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
"""


class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = [[-1 for _ in range(n)] for _ in range(n)]
        for u, v, cost in edges:
            graph[u][v] = cost
            graph[v][u] = cost

        ans = 0
        visited = [False for _ in range(n)]
        max_heap = []
        heappush(max_heap, (-maxMoves, 0))

        while len(max_heap) > 0:
            element = heappop(max_heap)
            node_id = element[1]
            max_moves_available = -element[0]
            if visited[node_id]:
                continue

            visited[node_id] = True
            ans += 1

            for node in range(n):
                if graph[node_id][node] != -1:
                    if not visited[node] and\
                       max_moves_available >= graph[node_id][node] + 1:
                        heappush(max_heap,
                                 (-(max_moves_available - graph[node_id][node] - 1), node))

                    cost = min(max_moves_available, graph[node_id][node])
                    graph[node][node_id] -= cost
                    graph[node_id][node] -= cost
                    ans += cost

        return ans


print(Solution().reachableNodes(
    edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]],
    maxMoves=6, n=3
))
print(Solution().reachableNodes(
    edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]],
    maxMoves=10, n=4
))
print(Solution().reachableNodes(
    edges=[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]],
    maxMoves=17, n=5
))

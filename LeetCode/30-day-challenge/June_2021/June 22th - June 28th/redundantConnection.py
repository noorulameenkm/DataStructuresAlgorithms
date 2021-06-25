"""
    Problem Link:- https://leetcode.com/problems/redundant-connection/
"""
class Solution:
    def findRedundantConnection(self, edges):
        
        def can_form_cycle(visited, src, dest, graph_):
            if src == dest:
                return True
            
            visited.append(src)
            for ed in graph_[src]:
                if ed not in visited:
                    if can_form_cycle(visited, ed, dest, graph_):
                        return True
            
            return False
            
        
        graph = {}
        nodes = len(edges)
        for node in range(1, nodes + 1):
            graph[node] = []
        
        for src, dest in edges:
            if can_form_cycle(list(), src, dest, graph):
                return [src, dest]
        
            graph[src].append(dest)
            graph[dest].append(src)



print(Solution().findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))
print(Solution().findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))
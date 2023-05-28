from collections import deque, defaultdict

class SolutionOne:
    def getAncestors(self, n, edges):
        
        
        # construct graph
        graph = {i: set() for i in range(n)}
        inDegrees = {i: 0 for i in range(n)}
        
        for u,v in edges:
            graph[u].add(v)
            inDegrees[v] += 1
        
        
        queue = deque([k for k in range(n) if inDegrees[k] == 0])
        ancestors = [set() for i in range(n)]
        while queue:
            node = queue.popleft()
            ancestors[node].add(node)
            
            for nxt in graph[node]:
                inDegrees[nxt] -= 1
                
                ancestors[nxt] = ancestors[nxt].union(ancestors[node])
                
                if inDegrees[nxt] == 0:
                    queue.append(nxt)
            
            ancestors[node].remove(node)
        
        answers = [sorted(list(set_)) for set_ in ancestors]
        return answers
            

class SolutionTwo:
    def getAncestors(self, n, edges):
        direct_child = defaultdict(list)
        ans = [[] for _ in range(n)]
        for x, y in edges:
            direct_child[x].append(y)

        def dfs(x, curr):
            for ch in direct_child[curr]:
                if ans[ch] and ans[ch][-1] == x: continue
                ans[ch].append(x)
                dfs(x, ch) 

        for i in range(n): dfs(i, i)
        return ans
        
        
        
        
if __name__ == "__main__":
    print(SolutionOne().getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
    print(SolutionOne().getAncestors(n = 5, edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))

    print(SolutionTwo().getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
    print(SolutionTwo().getAncestors(n = 5, edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))
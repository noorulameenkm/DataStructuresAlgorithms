from collections import deque
import queue

class SolutionOne:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        
        graph = {i: set() for i in range(numCourses)}
        
        # construct graph
        for prerequesite in prerequisites:
            course1, course2 = prerequesite
            graph[course1].add(course2)
        
        results = []
        
        # find answer for all the query
        # find whether u is a prerequisite of of v
        # logic: Do BFS starting from 'u' and see 
        for query in queries:
            u, v = query
            if self.canFind(graph, u, v):
                results.append(True)
            else:
                results.append(False)
        
        return results
        
    

    def canFind(self, graph, u, v):
        visited = set()
        visited.add(u)
        queue = deque([u])
        while queue:
            node = queue.popleft()
            childrens = graph[node]
            for children in childrens:
                if children not in visited:
                    if children == v:
                        return True
                    
                    visited.add(children)
                    queue.append(children)

        return False


class SolutionTwo:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        
        graph = {i: set() for i in range(numCourses)}
        inDegrees = {i: 0 for i in range(numCourses)}
        
        # construct graph
        for prerequesite in prerequisites:
            course1, course2 = prerequesite
            graph[course1].add(course2)
            inDegrees[course2] += 1
        
        results = []
        
        # find the node with zero indegrees (no prerequisite course)
        q = deque([i for i in inDegrees if inDegrees[i] == 0])
        ancestors = [set() for i in range(numCourses)]
        while q:
            node = q.popleft()
            ancestors[node].add(node)
            for nxt in graph[node]:
                inDegrees[nxt] -= 1
                ancestors[nxt] = ancestors[nxt].union(ancestors[node])

                if inDegrees[nxt] == 0:
                    q.append(nxt)
        
        for u, v in queries:
            if u in ancestors[v]:
                results.append(True)
            else:
                results.append(False)
        
        return results
                

class SolutionThree:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        '''
        Problem: All pair reachability problem
        Solution 1: directly use Floyd-Warshall algorithm
        '''
        graph = [[False] * numCourses for _ in range(numCourses)]

        # build graph
        for u, v, in prerequisites:
            graph[u][v] = True
        
        # floyd-warshall algorithm
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
        
        return [graph[u][v] for u, v in queries]

if __name__ == "__main__":
    print(SolutionOne().checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
    print(SolutionOne().checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
    print(SolutionOne().checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))


    print(SolutionTwo().checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
    print(SolutionTwo().checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
    print(SolutionTwo().checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))


    print(SolutionThree().checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
    print(SolutionThree().checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
    print(SolutionThree().checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))
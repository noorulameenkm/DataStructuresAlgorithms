import queue
from collections import defaultdict

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.graph = defaultdict(list)
        
        
    def constructGraph(self,edge_list):
        for edge in edge_list:
            x, y = edge
            self.graph[x].append(y)


    def depthFirstSearch(self):
        visited = [0 for k in range(self.nodes)] 
        q = queue.LifoQueue(maxsize = 0)
        q.put(0)
        while q.empty() != True:
            current_node = q.get()
            if visited[current_node] != 1:
                visited[current_node] = 1
                for node in self.graph[current_node][::-1]: 
                    q.put(node)

                print(current_node, end = ' ')

        print('\n', end = '')
        


def Main():
    t_cases = int(input())
    for t in range(t_cases):
        n,e = [int(num) for num in input().split(" ") if num != '']
        edges = [int(num) for num in input().split(" ") if num != '']
        pairOfEdges = list(zip(edges, edges[1:]))[::2]
        graph = Graph(n,e)
        graph.constructGraph(pairOfEdges)
        graph.depthFirstSearch()




if __name__ == '__main__':
    Main()
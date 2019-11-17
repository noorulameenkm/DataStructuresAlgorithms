import queue

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.graph = [[0  for i in range(self.nodes)]  for j in range(self.nodes)]
        
        
    def constructGraph(self,edge_list):
        for edge in edge_list:
            x, y = edge
            self.graph[x][y] = 1


    def breadthFirstSearch(self):
        visited = [0 for k in range(self.nodes)] 
        q = queue.Queue(maxsize = self.nodes)
        q.put(0)
        visited[0] = 1
        while q.empty() != True:
            edge = q.get()
            for i in range(self.nodes):
                if self.graph[edge][i] == 1 and visited[i] != 1:
                    q.put(i)
                    visited[i] = 1

            print(edge, end = ' ')

        print('\n', end = '')
        


def Main():
    t_cases = int(input())
    for t in range(t_cases):
        n,e = [int(num) for num in input().split(" ") if num != '']
        edges = [int(num) for num in input().split(" ") if num != '']
        pairOfEdges = list(zip(edges, edges[1:]))[::2]
        graph = Graph(n,e)
        graph.constructGraph(pairOfEdges)
        graph.breadthFirstSearch()




if __name__ == '__main__':
    Main()
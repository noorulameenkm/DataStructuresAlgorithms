"""
Given number of edges 'E' and vertices 'V' of a bidirectional graph. 
Your task is to build a graph through adjacency list and print the adjacency list 
for each vertex.

Input:
    The first line of input is T denoting the number of testcases.
    Then first line of each of the T contains two positive integer V and E 
    where 'V' is the number of vertex and 'E' is number of edges in graph. 
    Next, 'E' line contains two positive numbers showing that there is an 
    edge between these two vertex.

Output:
    For each vertex, print their connected nodes in order you are pushing them 
    inside the list . See the  given  example.
"""


"""
    Node Class
"""

class Node:
    def __init__(self, vertice):
        self.v = vertice 
        self.next = None


"""
    Graph Class
"""

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.listOfNodes = [None] * self.vertices

    def addEdge(self, fromNode, toNode):
        node = Node(toNode)
        if self.listOfNodes[fromNode] is None:
            self.listOfNodes[fromNode] = node
        else:
            """
                Iterate through the list and insert at the end
            """
            nodes = self.listOfNodes[fromNode]
            while nodes.next is not None:
                nodes = nodes.next

            nodes.next = node

        # Adding the edge from toNode to fromNode
        node = Node(fromNode)
        if self.listOfNodes[toNode] is None:
            self.listOfNodes[toNode] = node
        else:
            """
                Iterate through the list and insert at the end
            """
            nodes = self.listOfNodes[toNode]
            while nodes.next is not None:
                nodes = nodes.next

            nodes.next = node

    def printGraph(self):
        for v in range(len(self.listOfNodes)):
            nodes = self.listOfNodes[v]
            print(v , end = ' -> ')
            while nodes is not None:
                print(nodes.v, end='')
                if nodes.next is not None:
                    print(' -> ', end = '')
                nodes = nodes.next

            print('\n', end='')


""""
    Main Function
"""

def Main():
    T = int(input())
    for t in range(T):
        vertices, edges = [int(num) for num in input().split(' ') if num != '']
        graph = Graph(vertices, edges)
        for e in range(edges):
            fromNode, toNode = [int(num) for num in input().split(' ') if num != '']
            graph.addEdge(fromNode, toNode)
        
        graph.printGraph()



if __name__ == '__main__':
    Main() 
from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        # total umber of vertices
        self.vertices = vertices

        # initialise the array of lists
        self.array = []

        # intialise the adjacency list
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    
    def add_edge(self, source, destination):
        if source <= self.vertices and destination <= self.vertices:
            self.array[source].insert_at_head(destination)

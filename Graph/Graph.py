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


    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.array[i].head_node
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next_element
            print(" \n")

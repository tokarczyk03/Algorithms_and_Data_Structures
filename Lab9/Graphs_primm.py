#nieskonczone
import graf_mst

class Vertex():
    
    def __init__(self, key, color = None):
        self.key = key
        self._color = color
        self.intree = 0
        self.distance = float('inf') 
        self.parent = None


    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
        

class GraphList():

    def __init__(self):
        self.adjacency_list = {}

    def is_empty(self):
        return self.adjacency_list == 0
    
    def insert_vertex(self,vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=1):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1][vertex2] = edge
            self.adjacency_list[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v, edges in self.adjacency_list.items():
                if vertex in edges:
                    del edges[vertex]


    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            del self.adjacency_list[vertex1][vertex2]
            del self.adjacency_list[vertex2][vertex1]

    def neighbours(self, vertex):
        if vertex in self.adjacency_list:
            return list(self.adjacency_list[vertex].items())  

    def vertices(self):
        return list(self.adjacency_list.keys())  

    def get_vertex(self, vertex):
        if vertex in self.adjacency_list:
            return vertex


def prim(graph):
    
    start_vertex = graph.vertices()[0]
    start_vertex.distance = 0
    v = start_vertex

    mst = GraphList()
    for vertex in graph.adjacency_list:
        mst.insert_vertex(vertex)

    while v.intree == 0:
        v.intree = 1
        for neighbour, weight in graph.adjacency_list[v].items():
            if neighbour.distance > weight and neighbour.intree == 0:
                neighbour.distance = weight
                neighbour.parent = v

        dist = float('inf')
        for vertex in graph.adjacency_list:
            if vertex.intree == 0 and vertex.distance < dist:
                dist = vertex.distance
                v = vertex

    for vertex in graph.adjacency_list:
        if vertex.parent is not None:
            mst.insert_edge(vertex, vertex.parent, graph.adjacency_list[vertex][vertex.parent])

    return mst

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")



def main():
    graph = GraphList()
    for edge in graf_mst.graf:
        vertex1 = Vertex(edge[0])
        vertex2 = Vertex(edge[1])
        graph.insert_vertex(vertex1)
        graph.insert_vertex(vertex2)
        graph.insert_edge(vertex1, vertex2, edge[2])
        graph.insert_edge(vertex2, vertex1, edge[2])

    printGraph(graph)


main()
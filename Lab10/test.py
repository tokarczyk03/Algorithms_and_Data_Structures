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

    def insert_edge(self, vertex1, vertex2, capacity=1):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            edge = Edge(capacity, False)
            residual_edge = Edge(capacity, True)
            self.adjacency_list[vertex1][vertex2] = edge
            self.adjacency_list[vertex2][vertex1] = residual_edge

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
        

    def bfs(self, start_vertex):
        visited = []
        parent = {}
        queue = [start_vertex]

        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            neighbours = self.neighbours(vertex)

            for neighbour, edge in neighbours:
                if neighbour not in visited and edge.residual > 0:
                    visited.add(neighbour)
                    parent[neighbour] = vertex
                    queue.append(neighbour)

        return parent
    
class Edge():
    def __init__(self, capacity, isResuidal : bool):
        self.capacity = capacity
        self.isResuidal = isResuidal
        self.flow = 0
        if isResuidal:
            self.resuidal = 0
        else:
            self.resuidal = capacity

    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.resuidal} {self.isResuidal}"
    

##################

def find_path(graph, start_vertex, end_vertex, parent):
    current_vertex = end_vertex
    min_residual = float('Inf')

    if parent.get(end_vertex) is None:
        return 0

    while current_vertex != start_vertex:
        edge = graph.adjacency_list[parent[current_vertex]][current_vertex]
        min_residual = min(min_residual, edge.residual)
        current_vertex = parent[current_vertex]

    return min_residual






def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")



def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]

main()
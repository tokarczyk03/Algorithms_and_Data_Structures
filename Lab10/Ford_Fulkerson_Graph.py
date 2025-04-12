#nieskonczone

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

    def get_vertex(self, key):
        for vertex in self.vertices():
            if vertex.key == key:
                return vertex
        

    def bfs(self, start_vertex):
        visited = []
        parent = {}
        queue = [start_vertex]

        visited.append(start_vertex)

        while queue:
            vertex = queue.pop(0)
            neighbours = self.neighbours(vertex)

            for neighbour, edge in neighbours:
                if neighbour not in visited and edge.residual > 0:
                    visited.append(neighbour)
                    parent[neighbour] = vertex
                    queue.append(neighbour)

        return parent
    

        

class Edge():
    def __init__(self, capacity, isResidual : bool):
        self.capacity = capacity
        self.isResidual = isResidual
        self.flow = 0
        if isResidual:
            self.residual = 0
        else:
            self.residual = capacity

    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual} {self.isResidual}"
    

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

def augment_path(graph, start_vertex, end_vertex, parent, min_capacity):
    current_vertex = end_vertex

    while current_vertex != start_vertex:
        parent_vertex = parent[current_vertex]
        edge = graph.adjacency_list[parent_vertex][current_vertex]
        reverse_edge = graph.adjacency_list[current_vertex][parent_vertex]

        if not edge.isResidual:
            edge.flow += min_capacity
            edge.residual -= min_capacity
            reverse_edge.residual += min_capacity
        else:
            reverse_edge.flow -= min_capacity
            reverse_edge.residual -= min_capacity
            edge.residual += min_capacity

        current_vertex = parent_vertex

    
def ford_fulkerson_edmonds_karp(graph):
    total_flow = 0
    start_vertex = graph.get_vertex('s')
    end_vertex = graph.get_vertex('t')

    while True:
        if start_vertex in graph.vertices():
            parent = graph.bfs(start_vertex)
        min_capacity = find_path(graph, start_vertex, end_vertex, parent)
        if min_capacity == 0:
            break
        augment_path(graph, start_vertex, end_vertex, parent, min_capacity)
        total_flow += min_capacity

    return total_flow




def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")



def main():

    # Graf 1
    graph1 = GraphList()

    edges1 = [('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    vertices1 = []
    for edge in edges1:
        for v in edge[:2]:
            if v not in vertices1:
                vertices1.append(v)
    for vertex in vertices1:
        graph1.insert_vertex(Vertex(vertex))
    for vertex1, vertex2, capacity in edges1:
        graph1.insert_edge(graph1.get_vertex(vertex1), graph1.get_vertex(vertex2), capacity)

    max_flow = ford_fulkerson_edmonds_karp(graph1)
    print(f"# Wynik {max_flow}")
    printGraph(graph1)

    # Graf 2
    graph2 = GraphList()

    edges2 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    vertices2 = []
    for edge in edges2:
        for v in edge[:2]:
            if v not in vertices2:
                vertices2.append(v)
    for vertex in vertices2:
        graph2.insert_vertex(Vertex(vertex))
    for vertex1, vertex2, capacity in edges2:
        graph2.insert_edge(graph2.get_vertex(vertex1), graph2.get_vertex(vertex2), capacity)

    max_flow = ford_fulkerson_edmonds_karp(graph2)
    print(f"# Wynik {max_flow}")
    printGraph(graph2)

    # Graf 3
    graph3 = GraphList()

    edges3 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    vertices3 = []
    for edge in edges3:
        for v in edge[:2]:
            if v not in vertices3:
                vertices3.append(v)
    for vertex in vertices3:
        graph3.insert_vertex(Vertex(vertex))
    for vertex1, vertex2, capacity in edges3:
        graph3.insert_edge(graph3.get_vertex(vertex1), graph3.get_vertex(vertex2), capacity)

    max_flow = ford_fulkerson_edmonds_karp(graph3)
    print(f"# Wynik {max_flow}")
    printGraph(graph3)


main()

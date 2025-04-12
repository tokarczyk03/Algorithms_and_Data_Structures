#skonczone

class Vertex():
    
    def __init__(self,key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

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


class GraphMatrix():

    def __init__(self):
        self.adjaceny_matrix = []
        self.vertex_list = []


    def is_empty(self):
        return len(self.vertex_list) == 0
    
    def insert_vertex(self,vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            for i in range(len(self.adjaceny_matrix)):
                self.adjaceny_matrix[i].append(0)
            self.adjaceny_matrix.append([0] * (len(self.adjaceny_matrix) + 1))

    def insert_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            index1 = self.vertex_list.index(vertex1)
            index2 = self.vertex_list.index(vertex2)
            self.adjaceny_matrix[index1][index2] = 1
            self.adjaceny_matrix[index2][index1] = 1

    def delete_vertex(self, vertex):
        if vertex in self.vertex_list:
            index = self.vertex_list.index(vertex)
            self.vertex_list.remove(vertex)
            del self.adjaceny_matrix[index]
            for i in range(len(self.adjaceny_matrix)):
                del self.adjaceny_matrix[i][index]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            index1 = self.vertex_list.index(vertex1)
            index2 = self.vertex_list.index(vertex2)
            self.adjaceny_matrix[index1][index2] = 0
            self.adjaceny_matrix[index2][index1] = 0

    def neighbours(self, vertex_id):
        if 0 <= vertex_id < len(self.vertex_list):
            neighbours = []
            for j in range(len(self.adjaceny_matrix[vertex_id])):
                if self.adjaceny_matrix[vertex_id][j] != 0:
                    neighbours.append((j, self.adjaceny_matrix[vertex_id][j]))
            return iter(neighbours)

    def vertices(self):
            return list(range(len(self.vertex_list)))

    def get_vertex(self, vertex_id):
        return self.vertex_list[vertex_id]



def main():
    import polska

    adjacency_list_graph = GraphList()
    for edge in polska.graf:
        vertex1 = Vertex(edge[0])
        vertex2 = Vertex(edge[1])

        adjacency_list_graph.insert_vertex(vertex1)
        adjacency_list_graph.insert_vertex(vertex2)
        adjacency_list_graph.insert_edge(vertex1, vertex2)

    malopolskie = Vertex('K')
    mazowieckie = Vertex('W')
    lodzkie = Vertex('E')

    adjacency_list_graph.delete_vertex(malopolskie)
    adjacency_list_graph.delete_edge(mazowieckie, lodzkie)

    polska.draw_map(adjacency_list_graph)


    adjacency_matrix_graph = GraphMatrix()
    for edge in polska.graf:
        vertex1 = Vertex(edge[0])
        vertex2 = Vertex(edge[1])

        adjacency_matrix_graph.insert_vertex(vertex1)
        adjacency_matrix_graph.insert_vertex(vertex2)
        adjacency_matrix_graph.insert_edge(vertex1, vertex2)


    malopolskie = Vertex('K')
    mazowieckie = Vertex('W')
    lodzkie = Vertex('E')


    adjacency_matrix_graph.delete_vertex(malopolskie)
    adjacency_matrix_graph.delete_edge(mazowieckie, lodzkie)

    polska.draw_map(adjacency_matrix_graph)

main()
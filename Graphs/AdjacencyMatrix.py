"""
In the graph,  V = {0, 1, 2, 3},  E = {(0,1), (0,2), (0,3), (1,2)} , G = {V, E}

An adjacency matrix is a way of representing a graph G = {V, E} as a matrix of booleans.
The size of the matrix is VxV where V is the number of vertices in the graph and the value of an entry Aij is either 1 or 0
depending on whether there is an edge from vertex i to vertex j.

"""

class Adjacency_Matrix:
    def __init__(self, size, vertices):
        self.matrix = size*[0]
        for i in range(size):
            self.matrix[i] = size*[0]

        self.size = size
        self.vertices = vertices

    def add_edge(self, v1, v2, direct=None):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
        else:
            print("Vertex/edge is invalid")
            return

        self.matrix[i][j] = 1
        if not direct:
            if i == j:
                print("Given vertices are similar for undirected graph")
                return
            self.matrix[j][i] = 1
        return

    def remove_edge(self, v1, v2, direct = None):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
        else:
            print("Vertex/edge is invalid")
            return

        self.matrix[i][j] = 0
        if not direct:
            self.matrix[j][i] = 0

    def print_matrix(self):
        for i in range(0, self.size):
            print("\t" + str(self.vertices[i]), end="")
        print("\n")

        for i in range(0, self.size):
            print(self.vertices[i], end="")
            for j in range(0, self.size):
                print("\t" + str(self.matrix[i][j]), end="")
            print("\n")


if __name__ ==  "__main__":
    vertices = ['a', 'b', 'c', 'd']
    a = Adjacency_Matrix(len(vertices), vertices)
    a.add_edge('a', 'b')
    a.add_edge('a', 'c')
    a.add_edge('a', 'a')
    a.remove_edge('a', 'b')
    a.print_matrix()

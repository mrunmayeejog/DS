"""
An adjacency list represents a graph as an array of linked lists.
The index of the array represents a vertex and each element in its linked list represents the other vertices that form an edge with the vertex.
"""
import pprint

class AdjacencyList:
    def __init__(self, vertices):
        self.adj_list = {}
        for each in vertices:
            self.adj_list[each] = set([])

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            print("Invalid vertices")
            return
        self.adj_list[v1].add(v2)
        self.adj_list[v2].add(v1)

    def remove_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            print("Invalid vertices")
            return
        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)

    def print_adj_list(self):
        pprint.pprint(self.adj_list)


if __name__ == "__main__":
    ver = [0, 1, 2, 3]
    al = AdjacencyList(ver)
    al.add_edge(0, 1)
    al.add_edge(0, 3)
    al.add_edge(0, 6)
    al.add_edge(2, 3)
    al.remove_edge(0, 1)
    al.print_adj_list()

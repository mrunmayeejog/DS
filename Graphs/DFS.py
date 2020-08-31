"""
DFS traversal - Traversal means visiting all the nodes of a graph. Depth first traversal or
Depth first Search is a recursive algorithm for searching all the vertices of a graph or tree data structure.

DFS traversal works using Stack.
-Start with one node and add it to visited list.
-Push all its children nodes on to stack.
-Pop-top element, if not visited take its children and add to stack.
-Repeat till the stack is empty.
"""
from DS.Graphs.AdjacencyList import *
from DS.Stack.Stack_using_Array import *

c = 0

class dfs_traversal:
    def __init__(self):
        self.visited = []
        self.stack = Array_stack()

    def dfs(self, node):
        self.stack.push(node)
        return self.find_dfs()

    def find_dfs(self):
        while not self.stack.is_empty():
            top = self.stack.pop()
            if top not in self.visited:
                self.visited.append(top)
                c_node = list(al.adj_list[top])
                for each in c_node:
                    self.stack.push(each)
        return self.visited


if __name__ == "__main__":
    ver = [0, 1, 2, 3, 4]
    al = AdjacencyList(ver)
    al.add_edge(0, 1)
    al.add_edge(0, 2)
    al.add_edge(0, 4)
    al.add_edge(1, 0)
    al.add_edge(1, 2)
    al.add_edge(1, 3)
    al.add_edge(2, 0)
    al.add_edge(2, 1)
    al.add_edge(2, 3)
    al.add_edge(2, 4)
    al.print_adj_list()
    d = dfs_traversal()
    v = d.dfs(ver[0])
    print(v)






class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for i in self.adj_list:
            print(i, ":", self.adj_list[i])

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def reove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
            return False
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for i in self.adj_list[vertex]:
                self.adj_list[i].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False




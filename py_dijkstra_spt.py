import sys


class Dijkstra_Shortest_Path:
    def __init__(self):
        self.__spt_set = []
        self.__dist = []
        self.__graph = []
        self.__spt_src = 0
        self.__vertices = 0
        self.__active_vertex = 0

    def set_vertices_graph(self, g):
        self.__graph = g
        self.__vertices = len(self.__graph)

        for i in range(self.__vertices):
            self.__spt_set.append(False)
            self.__dist.append(sys.maxsize)

    def dijkstra(self, src):
        if src >= self.__vertices:
            return

        self.__dist[src] = 0
        self.__active_vertex = src
        self.__spt_src = src

        for vertex in range(self.__vertices):
            self.__update_distance_table()
            self.__pick_next_minimum_non_processed_vertex()

        self.__print_source_to_vertex_distance_table()

    def __update_distance_table(self):
        for vertex in range(self.__vertices):
            if vertex == self.__active_vertex:
                continue
            if self.__graph[self.__active_vertex][vertex] == 0:
                continue

            new_vertex_distance = self.__graph[self.__active_vertex][vertex] + self.__dist[self.__active_vertex]
            if self.__dist[vertex] < new_vertex_distance:
                continue

            self.__dist[vertex] = new_vertex_distance

        self.__spt_set[self.__active_vertex] = True

    def __pick_next_minimum_non_processed_vertex(self):
        minimum = sys.maxsize
        next_minimum_vertex = 0
        for vertex in range(self.__vertices):
            if self.__spt_set[vertex] is True:
                continue
            if self.__dist[vertex] > minimum:
                continue

            minimum = self.__dist[vertex]
            next_minimum_vertex = vertex

        self.__active_vertex = next_minimum_vertex

    def __print_source_to_vertex_distance_table(self):
        vertex_id = 0
        for distance in self.__dist:
            if vertex_id == self.__spt_src:
                vertex_msg = " src "
            else:
                vertex_msg = ""
            print("[",vertex_id,distance,"]", vertex_msg)
            vertex_id = vertex_id + 1

dsp = Dijkstra_Shortest_Path()
#graph = [[0, 0, 3], [0, 0, 4], [3, 4, 0]]
graph = [[0,6,4,0],[6,0,0,0],[4,0,0,5],[0,0,5,0]]
dsp.set_vertices_graph(graph)
dsp.dijkstra(0)

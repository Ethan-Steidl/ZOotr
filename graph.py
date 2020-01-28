'''
Standard graph class taken from online resources with additions
to the constructors 

Online resources provided the nodes as a Vertex class.  Adjustments
made to constructor
'''

import re

class Vertex:
    def __init__(self, node, size = 0):
        self.id = node
        self.checks = size
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self, node_file = None, edge_file = None):
        self.vert_dict = {}
        self.num_vertices = 0
        
        if node_file != None:
            self.generate_from_file(node_file, edge_file)


    def __iter__(self):
        return iter(self.vert_dict.values())


    '''
    Added functionality to generate from a file,  This should be made
    into a constructor.  Currently reads lines in from the nodes.txt
    and edges.txt and adds them as nodes and edges
    '''
    def generate_from_file(self, node_file, edge_file):
        fin_nodes = open(node_file, 'r')
        lines = fin_nodes.readlines()
        fin_nodes.close()
        for line in lines:
            pair = line.split(", ")
            self.add_vertex(pair[0], pair[1])

        fin_edges = open(edge_file, 'r')
        lines = fin_edges.readlines()
        fin_edges.close()
        for line in lines:
            trip = line.split(", ")
            self.add_edge(trip[0], trip[1], trip[2])


    def add_vertex(self, node, size):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, size)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

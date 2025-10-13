# graph_builder.py
import networkx as nx
from scipy.spatial import Delaunay

def build_graph(coords):
    tri = Delaunay(coords)
    edges = set()
    for simplex in tri.simplices:
        for i in range(3):
            for j in range(i+1, 3):
                edges.add(tuple(sorted([simplex[i], simplex[j]])))
    G = nx.Graph(list(edges))
    for i, (x, y) in enumerate(coords):
        G.nodes[i]['x'] = x
        G.nodes[i]['y'] = y
    return G

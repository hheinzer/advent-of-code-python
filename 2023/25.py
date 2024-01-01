import networkx as nx

lines = open("input/25.txt").read().splitlines()

graph = nx.Graph()
for line in lines:
    key, nodes = line.split(":")
    for node in nodes.split():
        graph.add_edge(key, node)

# part one (pffffffff)
graph.remove_edges_from(nx.minimum_edge_cut(graph))
a, b = nx.connected_components(graph)
print(len(a) * len(b))

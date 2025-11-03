import networkx as nx
import random

def generate_graph(n_nodes, directed=True, negative=False):
    g = nx.DiGraph() if directed else nx.Graph()
    node_labels = [f"N{i}" for i in range(1, n_nodes + 1)]
    g.add_nodes_from(node_labels)

    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            if i == j:
                continue
            if g.has_edge(i, j) == False and random.random() < 0.7:
                w = random.randint(1, 10) if not negative else random.randint(-10, 10)
                g.add_edge(node_labels[i], node_labels[j], weight=w)

    return g


g = generate_graph(5)
print(g.nodes)
print(g.edges(data=True))

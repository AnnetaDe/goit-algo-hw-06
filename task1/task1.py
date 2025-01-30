import networkx as nx
import matplotlib.pyplot as plt
import pprint as pp


def create_graph(edges):
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)
    return G


def draw_graph(G):
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        edge_color="gray",
        node_size=3000,
        font_size=10,
    )
    edge_labels = {(u, v): w for u, v, w in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Company departments and connections")
    plt.show()


company_departments = {
    "CEO": ["HR", "Engineering", "Finance", "Marketing"],
    "HR": ["Recruitment", "Employee Relations"],
    "Engineering": ["Software", "Hardware", "R&D"],
    "Finance": ["Accounting", "Budgeting"],
    "Marketing": ["SEO", "Advertising", "Public Relations"],
    "Software": ["Frontend", "Backend"],
}
edges = []
for department, connection in company_departments.items():
    for connect in connection:
        if connect in company_departments["CEO"]:
            weight = 1
        else:
            weight = 2
        edges.append((department, connect, weight))

pp.pprint(edges)

Graph_my = create_graph(edges)
draw_graph(Graph_my)

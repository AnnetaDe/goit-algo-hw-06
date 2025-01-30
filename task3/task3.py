import networkx as nx
import matplotlib.pyplot as plt


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


def shortest_path_di(graph, start, end):
    shortest_path = nx.dijkstra_path(graph, start, end)
    shortest_distance = nx.dijkstra_path_length(graph, start, end)
    return shortest_path, shortest_distance


company_departments = {
    "CEO": ["HR", "Engineering", "Finance", "Marketing"],
    "HR": ["Recruitment", "Employee Relations"],
    "Engineering": ["Software", "Hardware", "R&D"],
    "Finance": ["Accounting", "Budgeting"],
    "Marketing": ["SEO", "Advertising", "Public Relations"],
    "Software": ["Frontend", "Backend"],
}
all_departments = set()
edges = []

for department, connection in company_departments.items():
    all_departments.add(department)
    all_departments.update(connection)
    for connect in connection:
        if connect in company_departments["CEO"]:
            weight = 1
        else:
            weight = 2
        edges.append((department, connect, weight))


Graph_my = create_graph(edges)


for target in all_departments:
    source = "CEO"
    print("*" * 50)
    print(f"Target: {target}")
    print(
        f"Way from {source} to {target}", shortest_path_di(Graph_my, source, target)[0]
    )
    print(f"Total distance steps: {shortest_path_di(Graph_my, source, target)[1]}")

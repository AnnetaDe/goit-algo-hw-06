import networkx as nx
import matplotlib.pyplot as plt

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
        edges.append((department, connect))

print(edges)
G = nx.Graph()
G.add_edges_from(edges)
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
plt.title("Company departments and connections")
plt.show()

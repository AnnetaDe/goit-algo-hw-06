from collections import deque


def depth():
    pass


def width():
    pass


class Graph:
    def __init__(self):
        self.graph = {}
        self.levels = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            self.levels[vertex] = None

    def add_edge(self, u, v, directed_both=False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        if directed_both:
            self.graph[v].append(u)

    def add_level(self, level):
        if level not in self.levels:
            return "no level"
        queue = deque([level])
        self.levels[level] = 0
        while queue:
            current = queue.popleft()
            for vertex in self.graph[current]:
                if self.levels[vertex] is None:
                    self.levels[vertex] = self.levels[current] + 1
                    queue.append(vertex)

    def dfs(self, start, target, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()
        path.append(start)
        visited.add(start)

        if start == target:
            print(f"DFS-Path to {target}: {path}")
            print(f"Visited: {visited}")
            print("*" * 50)
            return path
        for vertex in self.graph.get(start, []):
            if vertex not in visited:
                new_path = self.dfs(vertex, target, path, visited)
                if new_path:
                    return new_path
        return None

    def bfs(self, start, target):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()
            if node == target:
                print(f"BFS-Path from {start} to {target}: {path}")
                print(f"Visited: {visited}")
                print(f"Queue: {queue}")
                print("*" * 50)
                return path

            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)

        return None

    def show(self):
        for vertex, edges in self.graph.items():
            print(f"Vertex: {vertex}: Level:{self.levels[vertex]}---> {edges}")


g = Graph()
g.add_edge(1, 2, directed_both=True)
g.add_edge(2, 22)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(1, 3)
g.add_edge(1, 13)

g.add_edge(2, 4, directed_both=True)
g.add_edge(4, 5)
g.add_edge(4, 8)
g.add_edge(8, 9)
g.add_edge(9, 10)
g.add_edge(10, 11)
g.add_edge(11, 12)

g.add_level(1)

g.bfs(1, 7)
g.dfs(1, 7)
g.bfs(1, 22)
g.dfs(1, 22)
print(
    " DFS проходить глибоко всередину графа перед поверненням назад.\nВ даному випадку він спочатку пішов через вершину 2 → 22, що є непрямим шляхом до 7.\nDFS відвідав менше вузлів, ніж BFS, оскільки він знайшов шлях раніше без перевірки всіх можливих варіантів."
)
g.show()

import heapq


def dijkstra(graph, start):
    priority_line = [(0, start, [])]
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    while priority_line:
        (current_distance, current_node, path) = heapq.heappop(priority_line)
        path.append(current_node)

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node].items():

            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_line, (distance, neighbor, path))

    return distances

import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, start):
        distance = [float('inf')] * self.V
        distance[start] = 0
        heap = [(0, start)]  # (distance, vertex)

        while heap:
            dist_u, u = heapq.heappop(heap)

            if dist_u > distance[u]:
                continue

            for v, edge_weight in self.graph[u]:
                alt = dist_u + edge_weight

                if alt < distance[v]:
                    distance[v] = alt
                    heapq.heappush(heap, (alt, v))

        return distance


g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 3)
g.add_edge(2, 4, 4)
g.add_edge(3, 4, 1)
g.add_edge(3, 5, 2)
g.add_edge(4, 5, 3)

start_vertex = 0
shortest_distances = g.dijkstra(start_vertex)

print(f"Shortest distances from vertex {start_vertex}:")
for i, dist in enumerate(shortest_distances):
    print(f"To vertex {i}: {dist}")

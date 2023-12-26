import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def addEdge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w  # Assuming the graph is undirected

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [-1] * self.V
        mstSet = [False] * self.V

        key[0] = 0  # Start with the first vertex
        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1  # Initialize min_index before the loop

        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def printMST(self, parent):
        print("Edges with minimum spanning tree:")
        minCost = 0
        for i in range(1, self.V):
            print(parent[i], "--", i, "=", self.graph[i][parent[i]])
            minCost += self.graph[i][parent[i]]

        print("Minimum Spanning Tree Cost:", minCost)

# Example usage:
graph = Graph(5)
graph.addEdge(0, 1, 2)
graph.addEdge(0, 2, 4)
graph.addEdge(1, 2, 1)
graph.addEdge(1, 3, 3)
graph.addEdge(2, 3, 5)

graph.primMST()

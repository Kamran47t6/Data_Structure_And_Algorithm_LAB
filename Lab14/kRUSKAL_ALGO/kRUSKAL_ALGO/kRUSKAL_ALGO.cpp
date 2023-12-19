#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Structure to represent an edge in the graph
struct Edge {
    int src, dest, weight;
};

// Structure to represent a disjoint-set for Union-Find
struct DisjointSet {
    int* parent, * rank;

    DisjointSet(int n) {
        parent = new int[n];
        rank = new int[n];

        // Initialize each subset as a single element set
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    // Find the set to which an element belongs (with path compression)
    int find(int u) {
        if (u != parent[u])
            parent[u] = find(parent[u]);
        return parent[u];
    }

    // Perform union of two sets (with union by rank)
    void unionSets(int u, int v) {
        int rootU = find(u);
        int rootV = find(v);

        if (rank[rootU] < rank[rootV])
            parent[rootU] = rootV;
        else if (rank[rootU] > rank[rootV])
            parent[rootV] = rootU;
        else {
            parent[rootV] = rootU;
            rank[rootU]++;
        }
    }
};
// Function to compare edges based on their weights
bool compareEdges(const Edge& a, const Edge& b) {
    return a.weight < b.weight;
}

// Function to perform Kruskal's algorithm
void kruskalMST(vector<Edge>& edges, int numVertices) {
    // Sort the edges in non-decreasing order of weights
    sort(edges.begin(), edges.end(), compareEdges);

    // Initialize a disjoint set for Union-Find
    DisjointSet disjointSet(numVertices);

    // Vector to store the edges of the MST
    vector<Edge> mst;

    for (const Edge& edge : edges) {
        int rootSrc = disjointSet.find(edge.src);
        int rootDest = disjointSet.find(edge.dest);

        // If including this edge does not create a cycle, add it to the MST
        if (rootSrc != rootDest) {
            mst.push_back(edge);
            disjointSet.unionSets(rootSrc, rootDest);
        }
    }

    // Display the edges of the Minimum Spanning Tree
    cout << "Edges of the Minimum Spanning Tree:\n";
    for (const Edge& edge : mst)
        cout << edge.src << " -- " << edge.dest << " : " << edge.weight << "\n";
}

int main() {
    // Example usage
    int numVertices = 4;
    vector<Edge> edges = { {0, 1, 10}, {0, 2, 6}, {0, 3, 5},
                           {1, 3, 15}, {2, 3, 4} };

    kruskalMST(edges, numVertices);

    return 0;
}
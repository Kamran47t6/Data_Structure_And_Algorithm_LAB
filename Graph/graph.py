class Graph:
    def __init__(self,nodes):
        self.nodes=nodes
        self.adj_list={node: [] for node in nodes}

    def add_edge(self,u,v):
        self.adj_list[u].append(v)

    def is_edge(self,u,v):
        return v in self.adj_list[u]
    def in_neighbors(self,node):
        in_neighbors=[]
        for u, neighbors in self.adj_list.items():
            if node in neighbors:
                in_neighbors.append(u)
        return in_neighbors
    
    def degree(self,node):
        return len(self.adj_list[node])
    
    def out_neighbors(self,node):
        return self.adj_list[node]
    def print_graph(self):
        for node, neighbors in self.adj_list.items():
            print({node},"-->",neighbors)

nodes=["A","B","C","D","E"]
graph=Graph(nodes)
graph.add_edge("A","B")

graph.add_edge("A","C")

graph.add_edge("B","D")

graph.add_edge("C","E")

graph.add_edge("D","E")
print("Graph")
graph.print_graph()
print("In Neighbors:",graph.in_neighbors("C"))
print("Out Neighbors:",graph.out_neighbors("C"))
print("\n Is there any edge between A and B?",graph.is_edge("A","B"))

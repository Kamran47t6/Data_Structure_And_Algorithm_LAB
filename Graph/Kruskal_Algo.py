class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,i):
        if parent[i]!=i:
            parent[i]=self.find(parent,parent[i])
        return parent[i]
    
    def union(self,parent,rank,x,y):
        if rank[x]<rank[y]:
            parent[x]=y
        elif rank[x]>rank[y]:
            parent[y]=x

        else:
            parent[y]=x
            rank[x]+=1
        
    def KruskalMST(self):
        result=[]
        parent=[]
        rank=[]
        i=0
        e=0
        self.graph=sorted(self.graph, key=lambda item:item[2])

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V -1:
            u,v,w=self.graph[i]
            i=i+1
            x=self.find(parent,u)
            y=self.find(parent,v)

            if x!=y:
                e=e+1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
        
        minCost=0
        print("Edges with minimum spanning tree:")
        for u,v,w in result:
            minCost+=w
            print(u,"--",v,"=",w)
            
        print("Minimum Spanning Tree:",minCost)

graph=Graph(4)
graph.addEdge(0,1,10)
graph.addEdge(0,2,6)
graph.addEdge(0,3,5)
graph.addEdge(1,3,15)
graph.addEdge(2,3,4)
graph.KruskalMST()


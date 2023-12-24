from collections import defaultdict
# backtracking is only in DFS
# time complexity O(V+E)
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,s):
        visited=[False]*self.V
        stack=[]
        stack.append(s)
        visited[s]=True

        while stack:
            s=stack.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    stack.append(i)
                    visited[i]=True
    
g=Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)
g.DFS(2)
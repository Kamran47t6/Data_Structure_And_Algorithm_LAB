// BFS implementation for adjacency list
#include<iostream>
#include<conio.h>
#include<list>
#include<queue>
using namespace std;
class Graph {
private:
	int vertices;
	list<int>* adjacencylist;
public:
	Graph(int v) :vertices(v) {
		adjacencylist = new list<int>[v];
	}
	void addEdge(int u,int v) {
		adjacencylist[u].push_back(v);
	}
	void BFS(int s) {
		bool* visited = new bool[vertices];
		for (int i = 0; i < vertices; ++i) {
			visited[i] = false;
		}
		queue<int> q;
		visited[s] = true;
		q.push(s);
		cout << "Breadth First Search (Starting from vertex " << s << " ):";
		while (!q.empty()) {
			s = q.front();
			cout << s << " ";
			q.pop();
			for (auto i = adjacencylist[s].begin(); i != adjacencylist[s].end(); ++i) {
				if (!visited[*i]) {
					visited[*i] = true;
					q.push(*i);
				}
			}
		}
		delete[] visited;
	}
};
int main() {
	Graph g(4);
	g.addEdge(0, 1);
	g.addEdge(0, 2);
	g.addEdge(1, 2);
	g.addEdge(2, 0);
	g.addEdge(2, 3);
	g.addEdge(3, 3);
	g.BFS(2);
	return 0;

}

// DFS

//#include<iostream>
//#include<list>
//#include<stack>
//using namespace std;
//class Graph {
//private:
//	int vertices;
//	list<int>* adjacencylist;
//public:
//	Graph(int v) :vertices(v) {
//		adjacencylist = new list<int>[v];
//	}
//	void addEdge(int u,int v) {
//		adjacencylist[u].push_back(v);
//	}
//	void DFS(int s) {
//		bool* visited = new bool[vertices];
//		for (int i = 0; i < vertices; i++) {
//			visited[i] = false;
//		}
//		stack<int> stk;
//		visited[s] = true;
//		stk.push(s);
//
//		cout << "Depth first search (start from vertex " << s << " ):";
//		while (!stk.empty()) {
//			s = stk.top();
//			cout << s << "  ";
//			stk.pop();
//			for (auto i = adjacencylist[s].begin(); i != adjacencylist[s].end(); i++) {
//				if (!visited[*i]) {
//					visited[*i] = true;
//					stk.push(*i);
//				}
//			}
//		}
//		delete[] visited;
//	}
//};
//int main() {
//	Graph g(5);
//	g.addEdge(0, 1);
//	g.addEdge(1, 2);
//	g.addEdge(2, 2);
//	g.addEdge(2, 3);
//	g.addEdge(3, 4);
//	g.addEdge(4, 5);
//	g.DFS(3);
//	return 0;
//
//}
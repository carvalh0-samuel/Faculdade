#include <iostream>
#include <vector>

using namespace std;

void dfs(int v, vector<vector<int>>& adj, vector<bool>& visited) {
	visited[v] = true;
	cout << v << " ";

	for (int vizinho : adj[v]) {
		if (!visited[vizinho]){
			dfs(vizinho, adj, visited);
		}
	}
}

int main (){
	int n = 5;
	vector<vector<int>> adj(n);

	adj[0] = {1, 2};
	adj[1] = {0, 3, 4};
	adj[2] = {0};
	adj[3] = {1};
	adj[4] = {1};

	vector<bool> visited(n, false);
	
	dfs(0, adj, visited);
	return 0;
}
from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.inf = float('inf')
        
        self.dist = [[self.inf]*n for _ in range(n)]
        
        for i in range(n):
            self.dist[i][i] = 0
        
        for u,v,w in edges:
            self.dist[u][v] = min(self.dist[u][v], w)
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]


    def addEdge(self, edge: List[int]) -> None:
        u,v,w = edge
        
        if w < self.dist[u][v]:
            self.dist[u][v] = w
        
        for i in range(self.n):
            for j in range(self.n):
                if self.dist[i][u] + w + self.dist[v][j] < self.dist[i][j]:
                    self.dist[i][j] = self.dist[i][u] + w + self.dist[v][j]


    def shortestPath(self, node1: int, node2: int) -> int:
        d = self.dist[node1][node2]
        return -1 if d == float('inf') else d
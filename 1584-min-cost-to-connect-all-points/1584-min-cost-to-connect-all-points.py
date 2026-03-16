class Solution:
    def minCostConnectPoints(self, points):
        
        n = len(points)
        visited = [False] * n
        minDist = [float('inf')] * n
        
        minDist[0] = 0
        res = 0
        
        for _ in range(n):
            
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or minDist[i] < minDist[u]):
                    u = i
            
            visited[u] = True
            res += minDist[u]
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    minDist[v] = min(minDist[v], dist)
        
        return res
from typing import List
import heapq

class Solution:

    def dijkstra(self, graph, start, n):
        dist = [float('inf')] * n
        dist[start] = 0

        pq = [(0, start)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nei, w in graph[node]:
                nd = d + w
                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(pq, (nd, nei))

        return dist


    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        graph = [[] for _ in range(n)]
        rev_graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))

        d1 = self.dijkstra(graph, src1, n)
        d2 = self.dijkstra(graph, src2, n)
        d3 = self.dijkstra(rev_graph, dest, n)

        ans = float('inf')

        for i in range(n):
            if d1[i] == float('inf') or d2[i] == float('inf') or d3[i] == float('inf'):
                continue

            ans = min(ans, d1[i] + d2[i] + d3[i])

        return ans if ans != float('inf') else -1
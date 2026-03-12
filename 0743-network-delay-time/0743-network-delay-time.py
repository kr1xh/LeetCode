from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i: [] for i in range(1, n + 1)}
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        
        pq = [(0, k)]
        
        while pq:
            time, node = heapq.heappop(pq)
            
            if time > dist[node]:
                continue
            
            for nei, w in graph[node]:
                new_time = time + w
                
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))
        
        ans = max(dist.values())
        
        return ans if ans != float('inf') else -1
from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads):
        graph = defaultdict(list)

        for a,b,d in roads:
            graph[a].append((b,d))
            graph[b].append((a,d))

        visited = set([1])
        q = deque([1])
        ans = float('inf')

        while q:
            node = q.popleft()

            for nei, dist in graph[node]:
                ans = min(ans, dist)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans
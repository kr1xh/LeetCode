from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        graph = defaultdict(list)

        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        visited = [0] * len(values)
        ans = 0

        def dfs(node, time, score):
            nonlocal ans

            if time > maxTime:
                return

            if visited[node] == 0:
                score += values[node]

            visited[node] += 1

            if node == 0:
                ans = max(ans, score)

            for nxt, t in graph[node]:
                dfs(nxt, time + t, score)

            visited[node] -= 1

        dfs(0, 0, 0)

        return ans
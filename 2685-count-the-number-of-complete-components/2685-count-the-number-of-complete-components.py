from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:

                stack = [i]
                nodes = 0
                degree_sum = 0

                while stack:
                    node = stack.pop()

                    if visited[node]:
                        continue

                    visited[node] = True
                    nodes += 1
                    degree_sum += len(graph[node])

                    for nei in graph[node]:
                        if not visited[nei]:
                            stack.append(nei)

                edges_in_component = degree_sum // 2

                if edges_in_component == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        q = deque([source])

        while q:
            node = q.popleft()

            if node == destination:
                return True

            if node in visited:
                continue

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)

        return False
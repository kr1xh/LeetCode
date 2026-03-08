class Solution:
    def friendRequests(self, n, restrictions, requests):
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        result = []

        for u, v in requests:
            ru, rv = find(u), find(v)
            can = True

            for x, y in restrictions:
                rx, ry = find(x), find(y)

                if (ru == rx and rv == ry) or (ru == ry and rv == rx):
                    can = False
                    break

            if can:
                union(ru, rv)
                result.append(True)
            else:
                result.append(False)

        return result
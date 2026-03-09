from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        graph = defaultdict(set)
        deg = [0]*(n+1)

        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            deg[u]+=1
            deg[v]+=1

        odd = [i for i in range(1,n+1) if deg[i]%2]

        if len(odd)==0:
            return True

        if len(odd)==2:
            a,b = odd
            if b not in graph[a]:
                return True

            for x in range(1,n+1):
                if x!=a and x!=b and x not in graph[a] and x not in graph[b]:
                    return True
            return False

        if len(odd)==4:
            a,b,c,d = odd

            if b not in graph[a] and d not in graph[c]:
                return True
            if c not in graph[a] and d not in graph[b]:
                return True
            if d not in graph[a] and c not in graph[b]:
                return True

        return False
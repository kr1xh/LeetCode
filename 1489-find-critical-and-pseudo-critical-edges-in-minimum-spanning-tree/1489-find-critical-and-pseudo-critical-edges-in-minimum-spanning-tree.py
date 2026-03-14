class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        
        for i,e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda x: x[2])
        
        
        def mst(skip=-1, pick=-1):
            uf = UnionFind(n)
            weight = 0
            
            if pick != -1:
                u,v,w,_ = edges[pick]
                if uf.union(u,v):
                    weight += w
            
            for i,(u,v,w,idx) in enumerate(edges):
                if i == skip:
                    continue
                
                if uf.union(u,v):
                    weight += w
            
            root = uf.find(0)
            for i in range(n):
                if uf.find(i) != root:
                    return float('inf')
            
            return weight
        
        
        base = mst()
        
        critical = []
        pseudo = []
        
        for i in range(len(edges)):
            
            if mst(skip=i) > base:
                critical.append(edges[i][3])
            
            elif mst(pick=i) == base:
                pseudo.append(edges[i][3])
        
        return [critical, pseudo]
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        has_incoming = set()
        
        for u, v in edges:
            has_incoming.add(v)
        
        result = []
        for i in range(n):
            if i not in has_incoming:
                result.append(i)
        
        return result
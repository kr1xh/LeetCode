from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        if zeros == 0:
            return 0
        
        sz = n // 2 + 2
        par = [list(range(sz + 2)), list(range(sz + 2))]
        
        def find2(p, v):
            i = v >> 1
            root = i
            while par[p][root] != root:
                root = par[p][root]
            while par[p][i] != root:
                par[p][i], i = root, par[p][i]
            return (root << 1) | p
        
        def remove2(p, v):
            par[p][v >> 1] = (v >> 1) + 1
        
        dist = [-1] * (n + 1)
        dist[zeros] = 0
        remove2(zeros % 2, zeros)
        q = deque([zeros])
        
        while q:
            z = q.popleft()
            d = dist[z]
            
            a_min = max(0, k - (n - z))
            a_max = min(z, k)
            if a_min > a_max:
                continue
            
            nz_max = z + k - 2 * a_min
            nz_min = z + k - 2 * a_max
            parity = nz_min & 1
            
            cur = find2(parity, nz_min)
            while cur <= min(nz_max, n):
                next_cur = find2(parity, cur + 2)
                remove2(parity, cur)
                dist[cur] = d + 1
                if cur == 0:
                    return d + 1
                q.append(cur)
                cur = next_cur
        
        return -1
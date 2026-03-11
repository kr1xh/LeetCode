from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        
        red = defaultdict(list)
        blue = defaultdict(list)
        
        for u,v in redEdges:
            red[u].append(v)
            
        for u,v in blueEdges:
            blue[u].append(v)
        
        res = [-1]*n
        visited = set()
        
        q = deque()
        q.append((0,0,'red'))
        q.append((0,0,'blue'))
        
        visited.add((0,'red'))
        visited.add((0,'blue'))
        
        while q:
            node,dist,color = q.popleft()
            
            if res[node] == -1:
                res[node] = dist
            
            if color == 'red':
                for nxt in blue[node]:
                    if (nxt,'blue') not in visited:
                        visited.add((nxt,'blue'))
                        q.append((nxt,dist+1,'blue'))
            else:
                for nxt in red[node]:
                    if (nxt,'red') not in visited:
                        visited.add((nxt,'red'))
                        q.append((nxt,dist+1,'red'))
        
        return res
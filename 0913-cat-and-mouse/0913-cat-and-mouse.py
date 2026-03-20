from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        

        dp = [[[0]*2 for _ in range(n)] for _ in range(n)]
        degree = [[[0]*2 for _ in range(n)] for _ in range(n)]
        
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len(graph[c]) 
                if 0 in graph[c]:
                    degree[m][c][1] -= 1 
        
        queue = deque()
        
        for i in range(n):
            for t in range(2):
                if i != 0:
                    dp[0][i][t] = 1
                    queue.append((0, i, t, 1))
                    
                    dp[i][i][t] = 2
                    queue.append((i, i, t, 2))
        
        while queue:
            m, c, turn, result = queue.popleft()
            
            for pm, pc, pturn in self.parents(graph, m, c, turn):
                if dp[pm][pc][pturn] != 0:
                    continue
                
                if (pturn == 0 and result == 1) or (pturn == 1 and result == 2):
                    dp[pm][pc][pturn] = result
                    queue.append((pm, pc, pturn, result))
                else:
                    degree[pm][pc][pturn] -= 1
                    if degree[pm][pc][pturn] == 0:
                        dp[pm][pc][pturn] = 2 if pturn == 0 else 1
                        queue.append((pm, pc, pturn, dp[pm][pc][pturn]))
        
        return dp[1][2][0]
    
    def parents(self, graph, m, c, turn):
        if turn == 0:
            for pc in graph[c]:
                if pc != 0:
                    yield m, pc, 1
        else:
            for pm in graph[m]:
                yield pm, c, 0
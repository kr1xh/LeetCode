from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        px = [[0]*n for _ in range(m)]
        py = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    px[i][j] = 1
                elif grid[i][j] == 'Y':
                    py[i][j] = 1
                
                if i > 0:
                    px[i][j] += px[i-1][j]
                    py[i][j] += py[i-1][j]
                if j > 0:
                    px[i][j] += px[i][j-1]
                    py[i][j] += py[i][j-1]
                if i > 0 and j > 0:
                    px[i][j] -= px[i-1][j-1]
                    py[i][j] -= py[i-1][j-1]
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                x = px[i][j]
                y = py[i][j]
                
                if x == y and x > 0:
                    res += 1
        
        return res
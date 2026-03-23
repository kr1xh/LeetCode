class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        dp_max = [[0]*n for _ in range(m)]
        dp_min = [[0]*n for _ in range(m)]
        
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        for i in range(1, m):
            val = grid[i][0]
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * val
        
        for j in range(1, n):
            val = grid[0][j]
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * val
        
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                candidates = [
                    dp_max[i-1][j] * val,
                    dp_min[i-1][j] * val,
                    dp_max[i][j-1] * val,
                    dp_min[i][j-1] * val
                ]
                
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)
        
        result = dp_max[m-1][n-1]
        
        if result < 0:
            return -1
        return result % MOD
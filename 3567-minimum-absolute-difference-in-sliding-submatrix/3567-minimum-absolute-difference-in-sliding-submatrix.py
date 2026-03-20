class Solution:
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                
                values = set()
                
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.add(grid[x][y])
                
                if len(values) <= 1:
                    ans[i][j] = 0
                    continue
                
                vals = sorted(values)
                
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    min_diff = min(min_diff, vals[t] - vals[t - 1])
                
                ans[i][j] = min_diff
        
        return ans
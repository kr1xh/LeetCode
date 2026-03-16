class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):

                res.add(grid[r][c])

                k = 1
                while True:

                    if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
                        break

                    total = 0

                    i, j = r-k, c
                    for d in range(k):
                        total += grid[i+d][j+d]

                    i, j = r, c+k
                    for d in range(k):
                        total += grid[i+d][j-d]

                    i, j = r+k, c
                    for d in range(k):
                        total += grid[i-d][j-d]

                    i, j = r, c-k
                    for d in range(k):
                        total += grid[i-d][j+d]

                    res.add(total)
                    k += 1

        return sorted(res, reverse=True)[:3]
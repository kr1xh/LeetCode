from collections import deque

class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        res = [[-1]*n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy

                if 0 <= nx < m and 0 <= ny < n and res[nx][ny] == -1:
                    res[nx][ny] = res[x][y] + 1
                    q.append((nx, ny))

        return res
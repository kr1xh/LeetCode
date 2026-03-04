class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        row = [0] * m
        col = [0] * n
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    count += 1
        
        return count
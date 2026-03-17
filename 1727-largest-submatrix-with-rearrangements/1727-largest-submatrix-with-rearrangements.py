class Solution:
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        height = [0] * n
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            
            sorted_h = sorted(height, reverse=True)
            
            for k in range(n):
                res = max(res, sorted_h[k] * (k + 1))
        
        return res
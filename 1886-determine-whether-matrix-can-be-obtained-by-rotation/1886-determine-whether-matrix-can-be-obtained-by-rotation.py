class Solution:
    def findRotation(self, mat, target):
        for _ in range(4):
            if mat == target:
                return True
            
            mat = [list(row) for row in zip(*mat[::-1])]
        
        return False
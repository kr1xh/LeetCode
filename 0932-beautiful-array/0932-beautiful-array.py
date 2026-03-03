class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        res = [1]
        
        while len(res) < n:
            temp = []
            
            for x in res:
                if 2 * x - 1 <= n:
                    temp.append(2 * x - 1)
            
            for x in res:
                if 2 * x <= n:
                    temp.append(2 * x)
            
            res = temp
        
        return res
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.isqrt(c))
        
        while left <= right:
            total = left * left + right * right
            
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1
        
        return False
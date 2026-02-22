class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        max_dist = 0
        pos = 0
        
        while n > 0:
            if n & 1:
                if last != -1:
                    max_dist = max(max_dist, pos - last)
                last = pos
            n >>= 1
            pos += 1
        
        return max_dist
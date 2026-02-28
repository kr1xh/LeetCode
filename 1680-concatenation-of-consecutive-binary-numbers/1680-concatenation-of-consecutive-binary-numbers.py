class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0
        bit_length = 0
        
        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                bit_length += 1
            
            res = ((res << bit_length) | i) % MOD
        
        return res
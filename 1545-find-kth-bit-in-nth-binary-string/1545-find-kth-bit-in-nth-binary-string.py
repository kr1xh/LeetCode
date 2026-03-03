class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k):
            if n == 1:
                return "0"
            
            mid = 1 << (n - 1)
            
            if k == mid:
                return "1"
            elif k < mid:
                return helper(n - 1, k)
            else:
                mirror = (1 << n) - k
                bit = helper(n - 1, mirror)
                return "1" if bit == "0" else "0"
        
        return helper(n, k)
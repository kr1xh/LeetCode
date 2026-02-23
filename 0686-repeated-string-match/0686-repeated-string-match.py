import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        k = math.ceil(len(b) / len(a))
        
        if b in a * k:
            return k
        if b in a * (k + 1):
            return k + 1
        
        return -1
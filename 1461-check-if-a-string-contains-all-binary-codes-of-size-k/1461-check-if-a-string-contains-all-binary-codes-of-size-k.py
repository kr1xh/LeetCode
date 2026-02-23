class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k
        
        if len(s) - k + 1 < needed:
            return False
        
        seen = set()
        mask = 0
        
        for i in range(len(s)):
            mask = ((mask << 1) & ((1 << k) - 1)) | int(s[i])
            
            if i >= k - 1:
                seen.add(mask)
                if len(seen) == needed:
                    return True
        
        return False
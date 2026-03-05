class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        new = s + "#" + rev
        
        lps = [0] * len(new)
        
        for i in range(1, len(new)):
            j = lps[i - 1]
            
            while j > 0 and new[i] != new[j]:
                j = lps[j - 1]
                
            if new[i] == new[j]:
                j += 1
                
            lps[i] = j
        
        add = rev[:len(s) - lps[-1]]
        return add + s
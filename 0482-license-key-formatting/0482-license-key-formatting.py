class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = s.replace('-', '').upper()
        
        n = len(cleaned)
        if n == 0:
            return ""
        
        first_group_size = n % k
        
        result = []
        

        if first_group_size > 0:
            result.append(cleaned[:first_group_size])
        for i in range(first_group_size, n, k):
            result.append(cleaned[i:i+k])
        
        return "-".join(result)
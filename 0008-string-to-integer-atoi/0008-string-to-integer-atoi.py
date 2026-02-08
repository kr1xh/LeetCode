class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        return sign * result
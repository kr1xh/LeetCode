class Solution:
    def selfDividingNumbers(self, left, right):
        def is_valid(num):
            x = num
            
            while x > 0:
                digit = x % 10
                
                if digit == 0 or num % digit != 0:
                    return False
                
                x //= 10
            
            return True
        
        res = []
        
        for num in range(left, right + 1):
            if is_valid(num):
                res.append(num)
        
        return res
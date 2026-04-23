class Solution:
    def singleNumber(self, nums):
        result = 0
        
        for i in range(32):
            bit_sum = 0
            
            for num in nums:
                if (num >> i) & 1:
                    bit_sum += 1
            
            if bit_sum % 3:
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= (1 << i)
        
        return result
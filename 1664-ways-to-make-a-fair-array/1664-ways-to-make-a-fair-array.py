class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        
        total_even = 0
        total_odd = 0
        
        for i in range(n):
            if i % 2 == 0:
                total_even += nums[i]
            else:
                total_odd += nums[i]
        
        left_even = 0
        left_odd = 0
        result = 0
        
        for i in range(n):
            if i % 2 == 0:
                total_even -= nums[i]
            else:
                total_odd -= nums[i]
            
            new_even = left_even + total_odd
            new_odd = left_odd + total_even
            
            if new_even == new_odd:
                result += 1
            
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]
        
        return result
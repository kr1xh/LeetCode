from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        def kadane(nums):
            max_sum = 0
            curr = 0
            for x in nums:
                curr = max(0, curr + x)
                max_sum = max(max_sum, curr)
            return max_sum
        
        total_sum = sum(arr)
        
        if k == 1:
            return kadane(arr) % MOD
        
        max_twice = kadane(arr * 2)
        
        if total_sum > 0:
            return (max_twice + (k - 2) * total_sum) % MOD
        else:
            return max_twice % MOD
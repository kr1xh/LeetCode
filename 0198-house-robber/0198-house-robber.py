from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0 
        
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        
        return prev1
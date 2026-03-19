class Solution:
    def maximumPrimeDifference(self, nums):
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        first = -1
        last = -1
        
        for i in range(len(nums)):
            if is_prime(nums[i]):
                if first == -1:
                    first = i
                last = i
        
        return last - first
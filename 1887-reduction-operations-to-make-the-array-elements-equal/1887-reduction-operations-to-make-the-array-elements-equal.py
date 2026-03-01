class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        operations = 0
        
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                operations += n - i
        
        return operations
class Solution:
    def findMissingElements(self, nums):
        low = min(nums)
        high = max(nums)

        seen = set(nums)
        ans = []

        for num in range(low, high + 1):
            if num not in seen:
                ans.append(num)

        return ans
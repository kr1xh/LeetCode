import math

class Solution:
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)
        return math.gcd(smallest, largest)
class Solution:
    def sortByBits(self, arr):
        def countBits(x):
            count = 0
            while x:
                x &= x - 1
                count += 1
            return count
        
        return sorted(arr, key=lambda x: (countBits(x), x))
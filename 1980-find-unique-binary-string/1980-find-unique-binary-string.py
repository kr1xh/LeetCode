class Solution:
    def findDifferentBinaryString(self, nums):
        res = []
        
        for i in range(len(nums)):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
                
        return "".join(res)
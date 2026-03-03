class Solution:
    def reversePairs(self, nums):
        self.count = 0
        
        def merge_sort(left, right):
            if left >= right:
                return
            
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                self.count += j - (mid + 1)
            
            temp = []
            i, j = left, mid + 1
            
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            
            while j <= right:
                temp.append(nums[j])
                j += 1
            
            nums[left:right+1] = temp
        
        merge_sort(0, len(nums) - 1)
        return self.count
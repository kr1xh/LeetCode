from collections import defaultdict

class Solution:
    def distance(self, nums):
        groups = defaultdict(list)
        
        for i, num in enumerate(nums):
            groups[num].append(i)
        
        res = [0] * len(nums)
        
        for indices in groups.values():
            prefix_sum = [0]
            
            for idx in indices:
                prefix_sum.append(prefix_sum[-1] + idx)
            
            total = prefix_sum[-1]
            k = len(indices)
            
            for i in range(k):
                idx = indices[i]
                
                left_sum = prefix_sum[i]
                right_sum = total - prefix_sum[i+1]
                
                left_count = i
                right_count = k - i - 1
                
                left = idx * left_count - left_sum
                right = right_sum - idx * right_count
                
                res[idx] = left + right
        
        return res
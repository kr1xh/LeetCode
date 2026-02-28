class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        n = len(arr)
        
        min_diff = float('inf')
        
        for i in range(1, n):
            min_diff = min(min_diff, arr[i] - arr[i - 1])
        
        result = []
        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
        
        return result
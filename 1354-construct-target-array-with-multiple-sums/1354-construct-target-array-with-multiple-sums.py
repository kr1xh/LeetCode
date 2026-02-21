import heapq
class Solution:
    def isPossible(self, target):
        total = sum(target)
        
        heap = [-x for x in target]
        heapq.heapify(heap)
        
        while True:
            maxVal = -heapq.heappop(heap)
            rest = total - maxVal

            if maxVal == 1 or rest == 1:
                return True
            
            if rest == 0 or maxVal <= rest:
                return False
            
            newVal = maxVal % rest
            
            if newVal == 0:
                return False
            
            total = rest + newVal
            heapq.heappush(heap, -newVal)
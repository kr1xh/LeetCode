from typing import List

class Solution:

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        n = len(heights)

        size = 1
        while size < n:
            size *= 2

        seg = [0]*(2*size)

        for i in range(n):
            seg[size+i] = heights[i]

        for i in range(size-1,0,-1):
            seg[i] = max(seg[i*2],seg[i*2+1])

        def query(node,l,r,start,threshold):

            if r < start or seg[node] <= threshold:
                return -1

            if l == r:
                return l

            mid = (l+r)//2

            res = query(node*2,l,mid,start,threshold)
            if res != -1:
                return res

            return query(node*2+1,mid+1,r,start,threshold)

        ans = [-1]*len(queries)

        for i,(a,b) in enumerate(queries):

            if a > b:
                a,b = b,a

            if a == b:
                ans[i] = a

            elif heights[a] < heights[b]:
                ans[i] = b

            else:
                ans[i] = query(1,0,size-1,b+1,heights[a])

        return ans
from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        class DSU:
            def __init__(self,n):
                self.p=list(range(n))
                self.r=[0]*n

            def find(self,x):
                if self.p[x]!=x:
                    self.p[x]=self.find(self.p[x])
                return self.p[x]

            def union(self,a,b):
                pa,pb=self.find(a),self.find(b)
                if pa==pb:
                    return False

                if self.r[pa]<self.r[pb]:
                    pa,pb=pb,pa

                self.p[pb]=pa

                if self.r[pa]==self.r[pb]:
                    self.r[pa]+=1

                return True

        def can(x):
            dsu=DSU(n)
            used=0
            upgrades=0
            optional=[]

            for u,v,s,m in edges:
                if m==1:
                    if s<x:
                        return False
                    if not dsu.union(u,v):
                        return False
                    used+=1
                else:
                    optional.append((u,v,s))

            upgrade_candidates=[]

            for u,v,s in optional:
                if s>=x:
                    if dsu.union(u,v):
                        used+=1
                elif s*2>=x:
                    upgrade_candidates.append((u,v))

            for u,v in upgrade_candidates:
                if upgrades==k:
                    break
                if dsu.union(u,v):
                    upgrades+=1
                    used+=1

            return used==n-1

        lo,hi=0,2*10**5
        ans=-1

        while lo<=hi:
            mid=(lo+hi)//2

            if can(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1

        return ans
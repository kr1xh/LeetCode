class Solution:
    def largestComponentSize(self, nums):
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for num in nums:
            x = num
            f = 2
            while f * f <= x:
                if x % f == 0:
                    union(num, f)
                    union(num, x // f)
                f += 1

        count = {}
        ans = 0

        for num in nums:
            root = find(num)
            count[root] = count.get(root, 0) + 1
            ans = max(ans, count[root])

        return ans
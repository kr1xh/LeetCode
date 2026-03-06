class Solution:
    def combine(self, n: int, k: int):
        res = []
        path = []

        def backtrack(start):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res
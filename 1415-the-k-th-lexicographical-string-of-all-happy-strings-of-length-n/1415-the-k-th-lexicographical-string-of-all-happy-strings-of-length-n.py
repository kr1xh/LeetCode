class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        chars = ['a', 'b', 'c']

        def backtrack(path):
            if len(path) == n:
                res.append("".join(path))
                return

            for c in chars:
                if not path or path[-1] != c:
                    path.append(c)
                    backtrack(path)
                    path.pop()

        backtrack([])
        
        return res[k-1] if k <= len(res) else ""
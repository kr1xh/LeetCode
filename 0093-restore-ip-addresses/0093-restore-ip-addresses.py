class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for i in range(start, min(start + 3, len(s))):
                segment = s[start:i+1]

                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue

                path.append(segment)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
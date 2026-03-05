class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        ans = 0

        for i, ch in enumerate(s):
            last[ch] = i
            ans += min(last.values()) + 1

        return ans
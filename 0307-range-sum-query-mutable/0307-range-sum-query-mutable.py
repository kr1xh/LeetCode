from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def _prefix(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix(right + 1) - self._prefix(left)
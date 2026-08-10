class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for stones in range(1, n + 1):
            square = 1
            while square * square <= stones:
                if not dp[stones - square * square]:
                    dp[stones] = True
                    break
                square += 1

        return dp[n]
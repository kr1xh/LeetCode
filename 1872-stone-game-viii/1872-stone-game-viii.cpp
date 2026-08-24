class Solution {
public:
    long long stoneGameVIII(vector<int>& stones) {
        int n = stones.size();

        for (int i = 1; i < n; ++i)
            stones[i] += stones[i - 1];

        long long dp = stones[n - 1];

        for (int i = n - 2; i >= 1; --i)
            dp = max(dp, (long long)stones[i] - dp);

        return dp;
    }
};
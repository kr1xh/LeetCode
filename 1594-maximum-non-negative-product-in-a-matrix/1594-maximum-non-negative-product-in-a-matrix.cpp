class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        const long long INF = 4e18;
        const int MOD = 1e9 + 7;

        int m = grid.size();
        int n = grid[0].size();

        vector<vector<long long>> mx(m, vector<long long>(n, -INF));
        vector<vector<long long>> mn(m, vector<long long>(n, INF));

        mx[0][0] = mn[0][0] = grid[0][0];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (i == 0 && j == 0)
                    continue;

                long long maxVal = -INF;
                long long minVal = INF;

                auto relax = [&](long long a, long long b) {
                    if (a == -INF || b == INF)
                        return;

                    long long x = a * grid[i][j];
                    long long y = b * grid[i][j];

                    maxVal = max(maxVal, max(x, y));
                    minVal = min(minVal, min(x, y));
                };

                if (i)
                    relax(mx[i - 1][j], mn[i - 1][j]);

                if (j)
                    relax(mx[i][j - 1], mn[i][j - 1]);

                mx[i][j] = maxVal;
                mn[i][j] = minVal;
            }
        }

        if (mx[m - 1][n - 1] < 0)
            return -1;

        return mx[m - 1][n - 1] % MOD;
    }
};
class Solution {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        if (m > n) return 0;
        vector<unsigned int> dp(m + 1, 0);
        dp[0] = 1;

        for (int i = 1; i <= n; i++) {
            char sc = s[i - 1];
            for (int j = m; j >= 1; j--) {
                if (sc == t[j - 1]) {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return (int)dp[m];
    }
};
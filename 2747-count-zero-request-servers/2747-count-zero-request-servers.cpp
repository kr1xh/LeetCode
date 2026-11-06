class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        int q = queries.size();

        vector<int> order(q);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b) { return queries[a] < queries[b]; });

        sort(logs.begin(), logs.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        vector<int> cnt(n + 1, 0);
        int active = 0;
        int add = 0, remove = 0;
        int m = logs.size();

        vector<int> ans(q);
        for (int idx : order) {
            int hi = queries[idx], lo = hi - x;

            while (add < m && logs[add][1] <= hi) {
                if (cnt[logs[add][0]]++ == 0) active++;
                add++;
            }
            while (remove < add && logs[remove][1] < lo) {
                if (--cnt[logs[remove][0]] == 0) active--;
                remove++;
            }

            ans[idx] = n - active;
        }

        return ans;
    }
};
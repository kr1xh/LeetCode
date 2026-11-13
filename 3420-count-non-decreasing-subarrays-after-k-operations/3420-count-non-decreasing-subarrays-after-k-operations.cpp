class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> P(n + 1, 0);
        for (int i = 0; i < n; i++) P[i + 1] = P[i] + nums[i];

        vector<long long> S(n + 1, 0);
        vector<int> st;
        auto cost = [&](int l, int r) -> long long {
            int lo = 0, hi = (int)st.size() - 1;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (st[mid] <= r) hi = mid;
                else lo = mid + 1;
            }
            int m = st[lo];
            long long sumPrefixMax = (S[l] - S[m]) + 1LL * nums[m] * (r - m + 1);
            return sumPrefixMax - (P[r + 1] - P[l]);
        };

        long long ans = 0;
        int r = n - 1;
        for (int l = n - 1; l >= 0; l--) {
            while (!st.empty() && nums[st.back()] <= nums[l]) st.pop_back();
            int ng = st.empty() ? n : st.back();
            S[l] = 1LL * nums[l] * (ng - l) + S[ng];
            st.push_back(l);

            while (cost(l, r) > k) r--;
            ans += r - l + 1;
        }
        return ans;
    }
};
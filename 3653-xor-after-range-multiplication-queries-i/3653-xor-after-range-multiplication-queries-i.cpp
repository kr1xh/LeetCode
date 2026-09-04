class Solution {
public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        const long long MOD = 1000000007LL;

        for (auto& q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            for (int idx = l; idx <= r; idx += k) {
                nums[idx] = (int)((long long)nums[idx] * v % MOD);
            }
        }

        int result = 0;
        for (int x : nums) result ^= x;
        return result;
    }
};
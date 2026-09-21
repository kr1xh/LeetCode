class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> result(k, 0);
        vector<long long> cur(k, 0);

        for (int i = n - 1; i >= 0; i--) {
            int a = nums[i] % k;
            vector<long long> next(k, 0);

            for (int r = 0; r < k; r++) {
                if (cur[r] > 0) {
                    int newr = (int)((long long)a * r % k);
                    next[newr] += cur[r];
                }
            }
            next[a] += 1;

            cur.swap(next);

            for (int r = 0; r < k; r++) result[r] += cur[r];
        }

        return result;
    }
};
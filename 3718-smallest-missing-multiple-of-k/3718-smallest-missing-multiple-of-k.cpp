class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        vector<bool> present(101 * k + 1, false);

        for (int x : nums) {
            if (x % k == 0 && x <= 101 * k)
                present[x] = true;
        }

        for (int m = k; ; m += k) {
            if (m >= (int)present.size() || !present[m])
                return m;
        }
    }
};
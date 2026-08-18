class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        vector<int> cnt(51, 0);
        int n = nums.size();

        for (int i = 0; i + k <= n; i++) {
            unordered_set<int> seen;

            for (int j = i; j < i + k; j++)
                seen.insert(nums[j]);

            for (int x : seen)
                cnt[x]++;
        }

        for (int x = 50; x >= 0; x--) {
            if (cnt[x] == 1)
                return x;
        }

        return -1;
    }
};
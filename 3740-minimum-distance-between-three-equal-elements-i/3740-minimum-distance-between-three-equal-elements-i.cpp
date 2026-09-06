class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, vector<int>> positions;
        for (int i = 0; i < n; i++) {
            positions[nums[i]].push_back(i);
        }

        int best = INT_MAX;

        for (auto& [val, idxs] : positions) {
            int m = idxs.size();
            if (m < 3) continue;
            for (int p = 0; p + 2 < m; p++) {
                int span = idxs[p + 2] - idxs[p];
                best = min(best, 2 * span);
            }
        }

        return (best == INT_MAX) ? -1 : best;
    }
};
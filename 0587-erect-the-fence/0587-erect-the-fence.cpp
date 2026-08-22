class Solution {
public:
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        int n = trees.size();
        if (n < 4) return trees;

        sort(trees.begin(), trees.end());
        auto cross = [](const vector<int>& O, const vector<int>& A, const vector<int>& B) -> long long {
            return (long long)(A[0] - O[0]) * (B[1] - O[1]) -
                   (long long)(A[1] - O[1]) * (B[0] - O[0]);
        };

        vector<vector<int>> hull;
        for (int i = 0; i < n; i++) {
            while (hull.size() >= 2 &&
                   cross(hull[hull.size() - 2], hull[hull.size() - 1], trees[i]) < 0) {
                hull.pop_back();
            }
            hull.push_back(trees[i]);
        }
        size_t lower_size = hull.size() + 1;
        for (int i = n - 2; i >= 0; i--) {
            while (hull.size() >= lower_size &&
                   cross(hull[hull.size() - 2], hull[hull.size() - 1], trees[i]) < 0) {
                hull.pop_back();
            }
            hull.push_back(trees[i]);
        }

        hull.pop_back();
        set<vector<int>> unique_pts(hull.begin(), hull.end());
        return vector<vector<int>>(unique_pts.begin(), unique_pts.end());
    }
};
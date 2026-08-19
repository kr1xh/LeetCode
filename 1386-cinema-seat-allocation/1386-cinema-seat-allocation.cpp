class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        unordered_map<int, int> rows;

        for (auto &seat : reservedSeats) {
            rows[seat[0]] |= 1 << seat[1];
        }

        int ans = (n - rows.size()) * 2;

        for (auto &[row, mask] : rows) {

            bool left =
                !(mask & (1 << 2)) &&
                !(mask & (1 << 3)) &&
                !(mask & (1 << 4)) &&
                !(mask & (1 << 5));

            bool middle =
                !(mask & (1 << 4)) &&
                !(mask & (1 << 5)) &&
                !(mask & (1 << 6)) &&
                !(mask & (1 << 7));

            bool right =
                !(mask & (1 << 6)) &&
                !(mask & (1 << 7)) &&
                !(mask & (1 << 8)) &&
                !(mask & (1 << 9));

            if (left && right)
                ans += 2;
            else if (left || middle || right)
                ans += 1;
        }

        return ans;
    }
};
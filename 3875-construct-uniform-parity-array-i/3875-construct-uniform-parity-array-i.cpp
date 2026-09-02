class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int oddCount = 0;
        for (int x : nums1) {
            if (x % 2 != 0) oddCount++;
        }
        if (oddCount >= 1) return true;
        return true;
    }
};
class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int minVal = nums1[0];
        int oddCount = 0;

        for (int x : nums1) {
            minVal = min(minVal, x);
            if (x % 2 != 0) oddCount++;
        }
        if (minVal % 2 == 1) return true;
        if (oddCount == 0) return true;

        return false;
    }
};
class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        for (int i = 0; i < (int)nums.size(); i++) {
            int sum = 0;
            for (int x = nums[i]; x > 0; x /= 10) {
                sum += x % 10;
            }
            if (sum == i) return i;
        }
        return -1;
    }
};
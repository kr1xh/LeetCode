class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int totalXor = 0;

        for (int x : nums)
            totalXor ^= x;

        if (totalXor != 0)
            return nums.size();

        for (int x : nums)
            if (x != 0)
                return nums.size() - 1;

        return 0;
    }
};
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int n = nums.size();
        long long total = 0;
        for (int v : nums) total += v;

        long long target = total - x;
        if (target < 0) return -1;
        int left = 0;
        long long windowSum = 0;
        int bestLen = -1;

        for (int right = 0; right < n; right++) {
            windowSum += nums[right];
            while (windowSum > target) {
                windowSum -= nums[left];
                left++;
            }

            if (windowSum == target) {
                bestLen = max(bestLen, right - left + 1);
            }
        }

        return (bestLen == -1) ? -1 : (n - bestLen);
    }
};
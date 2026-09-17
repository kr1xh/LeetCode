class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        vector<int> bestEndingAt(n, INT_MAX);

        int left = 0;
        long long sum = 0;
        int result = INT_MAX;
        int bestSoFar = INT_MAX;

        for (int right = 0; right < n; right++) {
            sum += arr[right];
            while (sum > target) {
                sum -= arr[left];
                left++;
            }

            if (sum == target) {
                int curLen = right - left + 1;
                if (left > 0 && bestEndingAt[left - 1] != INT_MAX) {
                    result = min(result, bestEndingAt[left - 1] + curLen);
                }

                bestSoFar = min(bestSoFar, curLen);
            }

            bestEndingAt[right] = bestSoFar;
        }

        return (result == INT_MAX) ? -1 : result;
    }
};
class Solution {
public:
    long long countCommas(long long n) {
        long long total = 0;
        long long lower = 1;

        for (int d = 1; d <= 18; d++) {
            long long upper = lower * 10 - 1;
            if (lower > n) break;

            long long rangeHigh = min(upper, n);
            long long count = rangeHigh - lower + 1;
            long long commasPerNumber = (d - 1) / 3;

            total += count * commasPerNumber;

            lower = upper + 1;
        }

        return total;
    }
};
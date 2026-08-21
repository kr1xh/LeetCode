class Solution {
public:
    using ll = long long;
    ll count(ll x, vector<int>& coins, vector<ll>& lcmArr) {
        int n = coins.size();
        int full = 1 << n;
        lcmArr[0] = 1;
        ll total = 0;

        for (int mask = 1; mask < full; mask++) {
            int lowBit = mask & (-mask);
            int i = __builtin_ctz(mask);
            int prev = mask ^ lowBit;

            ll prevLcm = lcmArr[prev];
            if (prevLcm > x) {
                lcmArr[mask] = prevLcm;
                continue;
            }

            ll c = coins[i];
            ll g = std::gcd(prevLcm, c);
            ll multiplier = c / g;

            if (multiplier != 0 && prevLcm > x / multiplier) {
                lcmArr[mask] = x + 1;
                continue;
            }

            ll cur = prevLcm * multiplier;
            lcmArr[mask] = cur;

            if (cur > x) continue;

            ll ways = x / cur;
            if (__builtin_popcount(mask) & 1)
                total += ways;
            else
                total -= ways;
        }
        return total;
    }

    long long findKthSmallest(vector<int>& coins, int k) {
        int n = coins.size();
        vector<ll> lcmArr(1 << n);

        ll low = 1;
        ll high = 1LL * *min_element(coins.begin(), coins.end()) * k;

        while (low < high) {
            ll mid = low + (high - low) / 2;
            if (count(mid, coins, lcmArr) >= k)
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }
};
class Solution {
public:
    const long long MOD = 1000000007LL;

    long long modpow(long long base, long long exp, long long mod) {
        long long result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) result = result * base % mod;
            base = base * base % mod;
            exp >>= 1;
        }
        return result;
    }

    int numberOfSets(int n, int k) {
        int N = n + k;

        vector<long long> fact(N + 1), invFact(N + 1);
        fact[0] = 1;
        for (int i = 1; i <= N; i++)
            fact[i] = fact[i - 1] * i % MOD;
        invFact[N] = modpow(fact[N], MOD - 2, MOD);
        for (int i = N - 1; i >= 0; i--)
            invFact[i] = invFact[i + 1] * (i + 1) % MOD;

        auto comb = [&](int a, int b) -> long long {
            if (b < 0 || b > a) return 0;
            return fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
        };

        return (int)comb(n + k - 1, 2 * k);
    }
};
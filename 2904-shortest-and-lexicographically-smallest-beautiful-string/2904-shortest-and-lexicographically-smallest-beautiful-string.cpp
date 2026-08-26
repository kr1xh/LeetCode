class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.size();
        string best = "";
        int bestLen = INT_MAX;
        int left = 0, ones = 0;

        for (int right = 0; right < n; right++) {
            if (s[right] == '1') ones++;

            while (ones == k) {
                int len = right - left + 1;

                if (len < bestLen) {
                    bestLen = len;
                    best = s.substr(left, len);
                } else if (len == bestLen) {
                    string candidate = s.substr(left, len);
                    if (candidate < best) best = candidate;
                }
                if (s[left] == '1') ones--;
                left++;
            }
        }

        return best;
    }
};
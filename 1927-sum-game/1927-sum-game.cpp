class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();
        int half = n / 2;

        int sumA = 0, sumB = 0;
        int cntA = 0, cntB = 0;

        for (int i = 0; i < half; i++) {
            if (num[i] == '?')
                cntA++;
            else
                sumA += num[i] - '0';
        }

        for (int i = half; i < n; i++) {
            if (num[i] == '?')
                cntB++;
            else
                sumB += num[i] - '0';
        }

        if ((cntA + cntB) % 2 == 1)
            return true;

        int forced = 2 * (sumA - sumB)
                   + 9 * (cntA - cntB);

        return forced != 0;
    }
};
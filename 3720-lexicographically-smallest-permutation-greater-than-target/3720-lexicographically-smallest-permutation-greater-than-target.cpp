class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();

        array<int, 26> cnt0 = {};
        for (char c : s) cnt0[c - 'a']++;

        vector<array<int, 26>> states;
        states.push_back(cnt0);

        int matchLen = 0;
        for (int i = 0; i < n; i++) {
            array<int, 26> cur = states.back();
            int c = target[i] - 'a';
            if (cur[c] == 0) break;
            cur[c]--;
            states.push_back(cur);
            matchLen++;
        }

        int hi = min(matchLen, n - 1);

        for (int i = hi; i >= 0; i--) {
            array<int, 26>& avail = states[i];
            int tChar = target[i] - 'a';

            int chosen = -1;
            for (int c = tChar + 1; c < 26; c++) {
                if (avail[c] > 0) { chosen = c; break; }
            }
            if (chosen == -1) continue;

            string result = target.substr(0, i);
            result += char('a' + chosen);

            array<int, 26> rest = avail;
            rest[chosen]--;

            for (int c = 0; c < 26; c++) {
                result.append(rest[c], char('a' + c));
            }

            return result;
        }

        return "";
    }
};
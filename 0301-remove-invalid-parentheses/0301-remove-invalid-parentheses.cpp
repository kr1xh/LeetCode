class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> result;
        unordered_set<string> visited;
        queue<string> q;

        visited.insert(s);
        q.push(s);

        bool found = false;

        while (!q.empty()) {
            int levelSize = q.size();

            for (int i = 0; i < levelSize; i++) {
                string cur = q.front();
                q.pop();

                if (isValid(cur)) {
                    result.push_back(cur);
                    found = true;
                }

                if (found) continue;

                for (int j = 0; j < (int)cur.size(); j++) {
                    if (cur[j] != '(' && cur[j] != ')') continue;
                    string next = cur.substr(0, j) + cur.substr(j + 1);
                    if (visited.insert(next).second) {
                        q.push(next);
                    }
                }
            }

            if (found) break;
        }

        return result;
    }

private:
    bool isValid(const string& str) {
        int balance = 0;
        for (char c : str) {
            if (c == '(') balance++;
            else if (c == ')') {
                balance--;
                if (balance < 0) return false;
            }
        }
        return balance == 0;
    }
};
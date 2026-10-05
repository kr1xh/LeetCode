class Solution {
public:
    int scoreOfParentheses(string s) {
        vector<int> stack;
        stack.push_back(0);

        for (char c : s) {
            if (c == '(') {
                stack.push_back(0);
            } else {
                int top = stack.back();
                stack.pop_back();
                int score = (top == 0) ? 1 : 2 * top;
                stack.back() += score;
            }
        }

        return stack.back();
    }
};
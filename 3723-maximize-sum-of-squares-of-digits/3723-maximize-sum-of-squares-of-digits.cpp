class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        if (sum > 9LL * num) return "";

        int nines = sum / 9;
        int rem = sum % 9;

        string result;
        result.reserve(num);

        result.append(nines, '9');
        if (rem > 0) result.push_back('0' + rem);
        result.append(num - result.size(), '0');

        return result;
    }
};
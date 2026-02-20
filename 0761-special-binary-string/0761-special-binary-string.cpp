class Solution 
{
public:
    string makeLargestSpecial(string s) 
    {
        vector<string> blocks;
        int balance = 0;
        int start = 0;

        for (int i = 0; i < s.size(); i++) 
        {
            if (s[i] == '1') balance++;
            else balance--;

            if (balance == 0) 
            {
                string inner = s.substr(start + 1, i - start - 1);
                string processed = "1" + makeLargestSpecial(inner) + "0";
                blocks.push_back(processed);
                start = i + 1;
            }
        }
        sort(blocks.begin(), blocks.end(), greater<string>());

        string result;
        for (auto& b : blocks)
            result += b;

        return result;
    }
};
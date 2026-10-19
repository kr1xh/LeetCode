class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int less = 0, equal = 0;
        for (int x : nums) {
            if (x < target) less++;
            else if (x == target) equal++;
        }
        
        vector<int> result;
        for (int i = 0; i < equal; i++)
            result.push_back(less + i);

        return result;
    }
};
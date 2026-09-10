class Solution {
public:
    int count = 0;

    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return count;
    }

private:
    pair<int, int> dfs(TreeNode* node) {
        if (!node) return {0, 0};

        auto [leftSum, leftCount] = dfs(node->left);
        auto [rightSum, rightCount] = dfs(node->right);

        int sum = leftSum + rightSum + node->val;
        int cnt = leftCount + rightCount + 1;

        if (sum / cnt == node->val) {
            count++;
        }

        return {sum, cnt};
    }
};
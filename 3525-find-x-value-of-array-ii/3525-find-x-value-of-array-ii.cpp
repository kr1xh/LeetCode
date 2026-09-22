struct Node {
    int prod;
    int cnt[5][5];
};

class Solution {
public:
    int n, K;
    vector<int> arr;
    vector<Node> tree;

    void pull(int node) {
        int lc = node * 2, rc = node * 2 + 1;
        tree[node].prod = (tree[lc].prod * tree[rc].prod) % K;
        for (int s = 0; s < K; s++) {
            int midS = (s * tree[lc].prod) % K;
            for (int r = 0; r < K; r++) {
                tree[node].cnt[s][r] = tree[lc].cnt[s][r] + tree[rc].cnt[midS][r];
            }
        }
    }

    void setLeaf(int node, int v) {
        int vm = v % K;
        tree[node].prod = vm;
        for (int s = 0; s < K; s++) {
            for (int r = 0; r < K; r++) tree[node].cnt[s][r] = 0;
            int r = (s * vm) % K;
            tree[node].cnt[s][r] = 1;
        }
    }

    void build(int node, int l, int r) {
        if (l == r) { setLeaf(node, arr[l]); return; }
        int mid = (l + r) / 2;
        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);
        pull(node);
    }

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) { setLeaf(node, val); return; }
        int mid = (l + r) / 2;
        if (idx <= mid) update(node * 2, l, mid, idx, val);
        else update(node * 2 + 1, mid + 1, r, idx, val);
        pull(node);
    }

    void query(int node, int l, int r, int ql, int qr, int& s, vector<int>& result) {
        if (r < ql || qr < l) return;
        if (ql <= l && r <= qr) {
            for (int rr = 0; rr < K; rr++) result[rr] += tree[node].cnt[s][rr];
            s = (s * tree[node].prod) % K;
            return;
        }
        int mid = (l + r) / 2;
        query(node * 2, l, mid, ql, qr, s, result);
        query(node * 2 + 1, mid + 1, r, ql, qr, s, result);
    }

    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        n = nums.size();
        K = k;
        arr = nums;
        tree.assign(4 * n, Node());
        build(1, 0, n - 1);

        vector<int> ans;
        ans.reserve(queries.size());

        for (auto& q : queries) {
            int idx = q[0], val = q[1], start = q[2], x = q[3];

            update(1, 0, n - 1, idx, val);
            arr[idx] = val;

            vector<int> result(K, 0);
            int s = 1 % K;
            query(1, 0, n - 1, start, n - 1, s, result);
            ans.push_back(result[x]);
        }

        return ans;
    }
};
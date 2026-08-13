class Solution {
    struct Node {
        int len;
        int pref;
        int suff;
        int best;
        char first;
        char last;
    };

    vector<Node> tree;
    string s;

    inline Node merge(const Node& L, const Node& R) {
        Node res;

        res.len = L.len + R.len;
        res.first = L.first;
        res.last = R.last;

        res.pref = L.pref;
        if (L.pref == L.len && L.last == R.first)
            res.pref += R.pref;

        res.suff = R.suff;
        if (R.suff == R.len && L.last == R.first)
            res.suff += L.suff;

        res.best = max(L.best, R.best);
        if (L.last == R.first)
            res.best = max(res.best, L.suff + R.pref);

        return res;
    }

    void build(int node, int l, int r) {
        if (l == r) {
            tree[node] = {1, 1, 1, 1, s[l], s[l]};
            return;
        }

        int mid = (l + r) >> 1;

        build(node << 1, l, mid);
        build(node << 1 | 1, mid + 1, r);

        tree[node] = merge(tree[node << 1], tree[node << 1 | 1]);
    }

    void update(int node, int l, int r, int idx, char c) {
        if (l == r) {
            tree[node] = {1, 1, 1, 1, c, c};
            return;
        }

        int mid = (l + r) >> 1;

        if (idx <= mid)
            update(node << 1, l, mid, idx, c);
        else
            update(node << 1 | 1, mid + 1, r, idx, c);

        tree[node] = merge(tree[node << 1], tree[node << 1 | 1]);
    }

public:
    vector<int> longestRepeating(string str, string queryCharacters, vector<int>& queryIndices) {
        s = move(str);

        int n = s.size();
        tree.resize(n << 2);

        build(1, 0, n - 1);

        int q = queryIndices.size();
        vector<int> ans;
        ans.reserve(q);

        for (int i = 0; i < q; ++i) {
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i]);
            ans.push_back(tree[1].best);
        }

        return ans;
    }
};
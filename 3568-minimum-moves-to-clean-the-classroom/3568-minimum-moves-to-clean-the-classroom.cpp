class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size(), n = classroom[0].size();
        int sr = -1, sc = -1;
        vector<pair<int,int>> litterPos;
        vector<vector<int>> litterIdx(m, vector<int>(n, -1));
        vector<vector<bool>> obstacle(m, vector<bool>(n, false));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = classroom[i][j];
                if (c == 'S') { sr = i; sc = j; }
                else if (c == 'L') {
                    litterIdx[i][j] = litterPos.size();
                    litterPos.push_back({i, j});
                }
                else if (c == 'X') {
                    obstacle[i][j] = true;
                }
            }
        }

        int k = litterPos.size();
        if (k == 0) return 0;
        int fullMask = (1 << k) - 1;

        int E = energy + 1;
        int M = 1 << k;
        long long totalStates = (long long)m * n * E * M;
        vector<int> dist(totalStates, -1);

        auto encode = [&](int r, int c, int e, int mask) -> long long {
            return (((long long)(r * n + c) * E + e) * M + mask);
        };

        long long startIdx = encode(sr, sc, energy, 0);
        dist[startIdx] = 0;
        queue<long long> q;
        q.push(startIdx);

        int dr[4] = {-1, 1, 0, 0};
        int dc[4] = {0, 0, -1, 1};

        int answer = -1;

        while (!q.empty()) {
            long long cur = q.front(); q.pop();
            int d = dist[cur];
            int mask = cur % M;
            long long tmp = cur / M;
            int e = tmp % E;
            long long rc = tmp / E;
            int c = rc % n;
            int r = rc / n;

            if (mask == fullMask) {
                answer = d;
                break;
            }

            if (e == 0) continue;

            for (int dir = 0; dir < 4; dir++) {
                int nr = r + dr[dir], nc = c + dc[dir];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (obstacle[nr][nc]) continue;

                int ne = e - 1;
                int nmask = mask;
                char ch = classroom[nr][nc];

                if (ch == 'L') {
                    int idx = litterIdx[nr][nc];
                    if (idx >= 0) nmask |= (1 << idx);
                }
                if (ch == 'R') {
                    ne = energy;
                }

                long long nstate = encode(nr, nc, ne, nmask);
                if (dist[nstate] == -1) {
                    dist[nstate] = d + 1;
                    q.push(nstate);
                }
            }
        }

        return answer;
    }
};
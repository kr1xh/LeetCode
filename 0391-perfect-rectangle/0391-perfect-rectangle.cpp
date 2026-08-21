class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        long long area = 0;
        long long minX = LLONG_MAX, minY = LLONG_MAX;
        long long maxX = LLONG_MIN, maxY = LLONG_MIN;
        auto encode = [](long long x, long long y) -> long long {
            return (x + 200000LL) * 500000LL + (y + 200000LL);
        };

        unordered_set<long long> corners;
        corners.reserve(rectangles.size() * 4 * 2);

        for (auto& r : rectangles) {
            int x1 = r[0], y1 = r[1], x2 = r[2], y2 = r[3];

            minX = min(minX, (long long)x1);
            minY = min(minY, (long long)y1);
            maxX = max(maxX, (long long)x2);
            maxY = max(maxY, (long long)y2);

            area += (long long)(x2 - x1) * (long long)(y2 - y1);

            long long pts[4] = {
                encode(x1, y1), encode(x1, y2),
                encode(x2, y1), encode(x2, y2)
            };
            for (long long p : pts) {
                if (corners.count(p))
                    corners.erase(p);
                else
                    corners.insert(p);
            }
        }
        if (corners.size() != 4)
            return false;

        long long need[4] = {
            encode(minX, minY), encode(minX, maxY),
            encode(maxX, minY), encode(maxX, maxY)
        };

        for (long long p : need) {
            if (!corners.count(p))
                return false;
        }
        long long boundingArea = (maxX - minX) * (maxY - minY);
        return area == boundingArea;
    }
};
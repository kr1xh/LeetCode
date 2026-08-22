class Solution {
public:
    double r, xc, yc;

    Solution(double radius, double x_center, double y_center) {
        r = radius;
        xc = x_center;
        yc = y_center;
    }

    vector<double> randPoint() {
        while (true) {
            double x = xc - r + (2 * r) * ((double)rand() / RAND_MAX);
            double y = yc - r + (2 * r) * ((double)rand() / RAND_MAX);

            double dx = x - xc;
            double dy = y - yc;

            if (dx * dx + dy * dy <= r * r) {
                return {x, y};
            }
        }
    }
};
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int firstIdx = -1, lastIdx = -1, prevCritIdx = -1;
        int minDist = INT_MAX;

        ListNode* prev = head;
        ListNode* cur = head->next;
        int idx = 1;

        while (cur->next != nullptr) {
            bool isCritical = (cur->val > prev->val && cur->val > cur->next->val) ||
                               (cur->val < prev->val && cur->val < cur->next->val);

            if (isCritical) {
                if (firstIdx == -1) {
                    firstIdx = idx;
                } else {
                    minDist = min(minDist, idx - prevCritIdx);
                }
                prevCritIdx = idx;
                lastIdx = idx;
            }
            prev = cur;
            cur = cur->next;
            idx++;
        }

        if (firstIdx == -1 || firstIdx == lastIdx) {
            return {-1, -1};
        }

        int maxDist = lastIdx - firstIdx;
        return {minDist, maxDist};
    }
};
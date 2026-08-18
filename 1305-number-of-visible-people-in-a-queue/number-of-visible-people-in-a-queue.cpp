class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        int sz = heights.size();
        vector<int> heightStack;
        vector<int> ans(sz, 0);

        for (int idx = sz - 1; idx >= 0; idx--) {
            while (!heightStack.empty() && heights[idx] > heights[heightStack.back()]) {
                ans[idx] += 1;
                heightStack.pop_back();
            }

            if (!heightStack.empty()) {
                ans[idx] += 1;
            }

            heightStack.push_back(idx);
        }

        return ans;
    }
};
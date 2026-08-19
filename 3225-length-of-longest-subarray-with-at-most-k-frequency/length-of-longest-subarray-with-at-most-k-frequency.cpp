class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int sz = nums.size();
        unordered_map<int, int> freqMap;
        int left = 0, right = 0, maxLen = 0;

        while (right < sz) {
            freqMap[nums[right]]++;

            if (freqMap[nums[right]] > k) {
                while (freqMap[nums[right]] > k) {
                    freqMap[nums[left]]--;
                    if (freqMap[nums[left]] == 0) freqMap.erase(nums[left]);
                    left++;
                }
            }

            maxLen = max(maxLen, right - left + 1);
            right++;
        }

        return maxLen;
    }
};
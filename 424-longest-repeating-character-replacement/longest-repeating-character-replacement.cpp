class Solution {
public:
    int characterReplacement(string s, int k) {
        int sLen = s.size();
        int maxFreq = 0;
        int maxWindowLen = 0;
        int left = 0;
        vector<int> freq(26, 0);

        for (int right = 0; right < sLen; right++) {
            freq[s[right] - 'A']++;
            maxFreq = max(maxFreq, freq[s[right] - 'A']);
            
            while ((right - left + 1) - maxFreq > k) {
                freq[s[left] - 'A']--;
                left++;
            }

            maxWindowLen = max(maxWindowLen, right - left + 1);
        }

        return maxWindowLen;
    }
};
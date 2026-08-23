from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqMap = defaultdict(int)
        longestLen = 0
        i , j = 0, 0

        while j < len(s):
            freqMap[s[j]] += 1

            while freqMap[s[j]] > 1:
                freqMap[s[i]] -= 1
                i += 1

            longestLen = max(longestLen, j - i + 1)
            j += 1

        return longestLen 
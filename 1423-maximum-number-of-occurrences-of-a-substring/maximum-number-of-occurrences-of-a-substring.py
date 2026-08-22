from collections import defaultdict

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        freqMap = defaultdict(int)
        strFreqMap = defaultdict(int)
        i , j = 0, 0

        while j < len(s):
            freqMap[s[j]] += 1

            while len(freqMap) > maxLetters or (j - i + 1) > minSize:
                freqMap[s[i]] -= 1
                if freqMap[s[i]] == 0:
                    freqMap.pop(s[i])
                i += 1

            if len(freqMap) <= maxLetters and (j - i + 1) >= minSize:
                strFreqMap[s[i:j + 1]] += 1

            j += 1

        return max(strFreqMap.values()) if strFreqMap else 0


              
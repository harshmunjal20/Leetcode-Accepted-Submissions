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
        freqIdxMap = defaultdict(int)
        strOccurences = defaultdict(int)

        i , j = 0, 0

        while j < len(s):
            freqIdxMap[s[j]] += 1

            while (j - i + 1) > minSize or len(freqIdxMap) > maxLetters:
                freqIdxMap[s[i]] -= 1
                if (freqIdxMap[s[i]] == 0):
                    freqIdxMap.pop(s[i])
                i += 1
            
            if (j - i + 1) == minSize and len(freqIdxMap) <= maxLetters:
                strOccurences[s[i : j + 1]] += 1
            
            j += 1
        
        return max(strOccurences.values()) if strOccurences else 0
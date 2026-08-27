class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        freqCharsMap = defaultdict(int)
        strFreqMap = defaultdict(int)
        i, j = 0, 0
        strLen = len(s)

        while j < strLen:
            freqCharsMap[s[j]] += 1   

            while len(freqCharsMap) > maxLetters or j - i + 1 > minSize:
                freqCharsMap[s[i]] -= 1
                if freqCharsMap[s[i]] == 0:
                    freqCharsMap.pop(s[i])
                i += 1

            if len(freqCharsMap) <= maxLetters and j - i + 1 == minSize:
                strFreqMap[s[i: j + 1]] += 1

            j += 1

        return max(strFreqMap.values()) if strFreqMap else 0
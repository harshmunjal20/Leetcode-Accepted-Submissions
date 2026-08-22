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

        maxFreq = 0

        # for key, value in strFreqMap.items():
        #     index = 0

        #     while index <= len(key) - minSize:
        #         strFreqMap[key[index : index + minSize + 1]] += value 
        #         index += 1
        
        for key , value in strFreqMap.items():
            print(key)
            if (value > maxFreq):
                maxFreq = value

        return maxFreq


              
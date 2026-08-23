from collections import defaultdict

class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqMap = [0] * 26

        for char in s:
            idx = ord(char) - ord('a')
            freqMap[idx] += 1
        
        def getMinChar(freqMap):
            for idx in range(26):
                if (freqMap[idx] > 0):
                    return idx
            
            return 26
        
        t = []
        ans = []

        for i in range(len(s)):
            currChar = ord(s[i]) - ord('a')
            t.append(s[i])
            freqMap[currChar] -= 1

            while t and (ord(t[-1]) - ord('a')) <= getMinChar(freqMap):
                ans.append(t[-1])
                t.pop()

        return "".join(ans)
            
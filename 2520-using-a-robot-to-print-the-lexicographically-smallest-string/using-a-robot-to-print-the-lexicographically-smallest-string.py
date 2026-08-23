class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqMap = [0] * 26

        for char in s:
            freqMap[ord(char) - ord('a')] += 1

        t = []
        ans = []

        def getMinChar(freqMap):
            for idx in range(26):
                if freqMap[idx] > 0:
                    return idx

            return 26

        for i in range(len(s)):
            currChar = ord(s[i]) - ord('a')
            t.append(s[i])
            freqMap[currChar] -= 1

            while t and (ord(t[-1]) - ord('a')) <= getMinChar(freqMap):
                ans.append(t.pop())

        return "".join(ans)

